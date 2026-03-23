"""
QC pipeline: generates QA reports, contact sheets, auto-flags exclusions
for all 24 images across 8 samples.
"""
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
import math

import AxonDeepSeg
from AxonDeepSeg.qa.metrics_qa import MetricsQA
from AxonDeepSeg.morphometrics.compute_morphometrics import (
    get_axon_morphometrics, save_axon_morphometrics
)

DATA_DIR = Path("data/macaque/data")
RESULTS_DIR = Path("results")

SAMPLE_SLICES = {
    "sample1": ["01", "03", "07"],
    "sample2": ["01", "03", "05"],
    "sample3": ["01", "03", "05"],
    "sample4": ["01", "05", "07"],
    "sample5": ["01", "03", "05"],
    "sample6": ["01", "03", "05"],
    "sample7": ["01", "03", "05"],
    "sample8": ["01", "03", "05"],
}

AD = "axon_diam (um)"
MT = "myelin_thickness (um)"
AA = "axon_area (um^2)"
MA = "myelin_area (um^2)"
IBT = "image_border_touching"


def image_to_base64(img_array):
    if img_array.dtype != np.uint8:
        img_array = img_array.astype(np.uint8)
    pil_img = Image.fromarray(img_array)
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode('utf-8')


def auto_flag(df):
    """Auto-flag axons for exclusion. Returns list of dicts."""
    flags = []
    for i, row in df.iterrows():
        reasons = []
        cats = []

        if row[IBT] == True:
            reasons.append("border-touching")
            cats.append("border")

        if row['gratio'] >= 1.0:
            reasons.append(f"gratio={row['gratio']:.3f}")
            cats.append("invalid")
        elif row['gratio'] <= 0:
            reasons.append(f"gratio={row['gratio']:.3f}")
            cats.append("invalid")

        if row[MA] <= 0 or row[MT] <= 0:
            reasons.append("no myelin")
            cats.append("unmyelinated")

        if row[AD] < 0.05:
            reasons.append(f"tiny axon ({row[AD]:.4f} um)")
            cats.append("artifact")

        if 0 < row['gratio'] < 0.3:
            reasons.append(f"very low gratio ({row['gratio']:.3f})")
            cats.append("myelin_dominant")

        if row['solidity'] < 0.75:
            reasons.append(f"low solidity ({row['solidity']:.3f})")
            cats.append("merge_error")

        if row[MT] > 0 and row[AD] > 0 and row[MT] / row[AD] > 1.0:
            reasons.append(f"myelin>>axon (mt/ad={row[MT]/row[AD]:.2f})")
            if "myelin_dominant" not in cats:
                cats.append("myelin_dominant")

        if reasons:
            primary_cat = cats[0] if cats else "other"
            flags.append({
                'axon_id': i,
                'reasons': '; '.join(reasons),
                'category': primary_cat,
                'gratio': row['gratio'],
                'axon_diam': row[AD],
                'myelin_thickness': row[MT],
                'solidity': row['solidity'],
                'eccentricity': row['eccentricity'],
            })
    return flags


def generate_contact_sheets(qa_folder, df, flags, batch_size=50):
    """Generate batch contact sheets with flagged axons in red."""
    n_axons = len(df)
    flagged_ids = {f['axon_id'] for f in flags}

    for batch_start in range(0, n_axons, batch_size):
        batch_end = min(batch_start + batch_size, n_axons)
        n = batch_end - batch_start
        cols = 10
        rows = (n + cols - 1) // cols
        fig, axes = plt.subplots(rows, cols, figsize=(30, rows * 3))
        if rows == 1:
            axes = axes.reshape(1, -1)
        for j in range(n):
            idx = batch_start + j
            ax = axes[j // cols, j % cols]
            img_path = qa_folder / f"axon_{idx}_labeled.png"
            if img_path.exists():
                ax.imshow(np.array(Image.open(img_path)))
            color = 'red' if idx in flagged_ids else 'black'
            r = df.iloc[idx]
            ax.set_title(f"#{idx} g={r['gratio']:.2f} d={r[AD]:.2f}", fontsize=7, color=color)
            ax.axis('off')
        for j in range(n, rows * cols):
            axes[j // cols, j % cols].axis('off')
        plt.tight_layout()
        plt.savefig(qa_folder / f"batch_{batch_start:03d}_{batch_end:03d}.png",
                    dpi=150, bbox_inches='tight')
        plt.close()


def generate_suspects_zoom(qa_folder, df, flags):
    """Generate a zoom grid of all flagged axons."""
    if not flags:
        return
    suspect_ids = [f['axon_id'] for f in flags]
    cols = min(8, len(suspect_ids))
    rows = (len(suspect_ids) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    if rows == 1 and cols == 1:
        axes = np.array([[axes]])
    elif rows == 1:
        axes = axes.reshape(1, -1)
    elif cols == 1:
        axes = axes.reshape(-1, 1)

    for j, idx in enumerate(suspect_ids):
        ax = axes[j // cols, j % cols]
        img_path = qa_folder / f"axon_{idx}_labeled.png"
        if img_path.exists():
            ax.imshow(np.array(Image.open(img_path)))
        r = df.iloc[idx]
        ax.set_title(f"#{idx} g={r['gratio']:.3f} d={r[AD]:.3f}\n"
                     f"mt={r[MT]:.3f} sol={r['solidity']:.2f}", fontsize=7)
        ax.axis('off')
    for j in range(len(suspect_ids), rows * cols):
        axes[j // cols, j % cols].axis('off')
    plt.tight_layout()
    plt.savefig(qa_folder / "suspects_zoom.png", dpi=150, bbox_inches='tight')
    plt.close()


def process_image(sample, slice_id):
    """Full QC pipeline for one image."""
    sample_dir = DATA_DIR / sample
    qa_folder = RESULTS_DIR / f"qa_{sample}_{slice_id}"
    qa_folder.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Processing {sample}/{slice_id}")
    print(f"{'='*60}")

    # Load
    image = np.array(Image.open(sample_dir / f"{slice_id}.png"))
    axon_mask = np.array(Image.open(sample_dir / f"{slice_id}_seg-axon.png"))
    myelin_mask = np.array(Image.open(sample_dir / f"{slice_id}_seg-myelin.png"))
    axon_label = (axon_mask > 0).astype(np.uint8)
    myelin_label = (myelin_mask > 0).astype(np.uint8)

    # Morphometrics with instance map
    print("  Computing morphometrics...")
    morph_output = get_axon_morphometrics(
        im_axon=axon_mask, im_myelin=myelin_mask,
        pixel_size=0.009144, axon_shape="circle",
        return_index_image=True, return_border_info=True,
        return_instance_seg=True, return_im_axonmyelin_label=True,
    )
    stats_df, index_image, instance_seg, im_axonmyelin_label = morph_output

    # Save morphometrics
    morph_xlsx = qa_folder / "morphometrics.xlsx"
    save_axon_morphometrics(morph_xlsx, stats_df)
    df = pd.read_excel(morph_xlsx)
    df.to_csv(qa_folder / "morphometrics.csv", index=False)

    print(f"  Total axons: {len(df)}")

    # QA plots and overlay
    print("  Generating QA plots...")
    qa = MetricsQA(str(qa_folder / "morphometrics.csv"))
    qa.plot_all(str(qa_folder), quiet=True)
    qa.save_seg_overlay(image, axon_label, myelin_label, qa_folder)

    # Axon closeups
    print("  Generating axon closeups...")
    axon_data = qa.generate_axon_closeups(
        qa_folder, image, axon_label, myelin_label,
        im_axonmyelin_label, buffer_pixels=20
    )

    # QA HTML report
    print("  Generating HTML report...")
    axon_stats = qa.plot("axon_diam (um)", quiet=True)
    myelin_stats = qa.plot("myelin_thickness (um)", quiet=True)
    gratio_stats = qa.plot("gratio", quiet=True)

    sections = {
        "Summary": [
            {"type": "stats", "stats": [
                {"label": "Axon Diameter (um)", "value": f"{axon_stats[0]} +/- {axon_stats[1]}"},
                {"label": "Myelin Thickness (um)", "value": f"{myelin_stats[0]} +/- {myelin_stats[1]}"},
                {"label": "g-ratio", "value": f"{gratio_stats[0]} +/- {gratio_stats[1]}"},
            ]},
            {"type": "segmented",
             "labeled_src": str(qa_folder / "segmentation_overlay.png"),
             "original_src": str(qa_folder / "base_image.png")}
        ],
        "Histograms": [{"type": "histogram_viewer", "histograms": [
            {"name": "Axon Diameter", "src": str(qa_folder / "axon_diam (um).png")},
            {"name": "Myelin Thickness", "src": str(qa_folder / "myelin_thickness (um).png")},
            {"name": "g-ratio", "src": str(qa_folder / "gratio.png")},
        ]}],
    }

    package_dir = Path(AxonDeepSeg.__file__).parent
    env = Environment(loader=FileSystemLoader((package_dir / "qa").resolve()))
    template = env.get_template("report_template.html")
    html_out = template.render(
        sections=sections, axon_data=axon_data,
        sample_id=f"{sample}_{slice_id}",
        report_date=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
        software_version=AxonDeepSeg.__version__,
        axon_mask_data=image_to_base64(axon_label * 255),
        myelin_mask_data=image_to_base64(myelin_label * 255),
        index_mask_data=image_to_base64(im_axonmyelin_label),
    )
    with open(qa_folder / "AxonDeepSeg_QA_Report.html", "w") as f:
        f.write(html_out)

    # Auto-flag
    print("  Auto-flagging exclusions...")
    flags = auto_flag(df)
    print(f"  Flagged: {len(flags)} / {len(df)}")

    # Save flags to CSV
    if flags:
        flags_df = pd.DataFrame(flags)
        flags_df['sample'] = sample
        flags_df['slice_id'] = slice_id
        flags_df.to_csv(qa_folder / "exclusions.csv", index=False)
    else:
        pd.DataFrame(columns=['axon_id', 'reasons', 'category', 'sample', 'slice_id']).to_csv(
            qa_folder / "exclusions.csv", index=False)

    # Contact sheets
    print("  Generating contact sheets...")
    generate_contact_sheets(qa_folder, df, flags)

    # Suspects zoom
    print("  Generating suspects zoom...")
    generate_suspects_zoom(qa_folder, df, flags)

    print(f"  Done: {qa_folder}")
    return len(df), len(flags)


if __name__ == "__main__":
    total_axons = 0
    total_flagged = 0

    for sample in sorted(SAMPLE_SLICES.keys()):
        for slice_id in SAMPLE_SLICES[sample]:
            n_axons, n_flagged = process_image(sample, slice_id)
            total_axons += n_axons
            total_flagged += n_flagged

    print(f"\n{'='*60}")
    print(f"ALL DONE: {total_axons} total axons, {total_flagged} flagged ({100*total_flagged/total_axons:.1f}%)")
    print(f"{'='*60}")
