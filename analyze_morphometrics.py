"""
Macaque corpus callosum morphometrics analysis and plotting.

Loads ADS morphometrics outputs, filters, combines per sample,
and generates publication-quality plots of:
  A) Axon diameter vs Fiber diameter
  B) G-ratio vs Fiber diameter

Usage:
  source axondeepseg/ads_conda/bin/activate axondeepseg/ads_conda/envs/venv_ads/
  python analyze_morphometrics.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy import stats as scipy_stats
from pathlib import Path

# ============================================================================
# Configuration
# ============================================================================

DATA_DIR = Path(__file__).parent / "data" / "macaque" / "data"
OUTPUT_DIR = Path(__file__).parent / "results"

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

REGION_LABELS = {
    "sample1": "Region 1",
    "sample2": "Region 2",
    "sample3": "Region 3",
    "sample4": "Region 4",
    "sample5": "Region 5",
    "sample6": "Region 6",
    "sample7": "Region 7",
    "sample8": "Region 8",
}

# ADS saves columns with display names including units.
# Map them back to short names for easier use.
COLUMN_RENAME = {
    "x0 (px)": "x0",
    "y0 (px)": "y0",
    "axon_area (um^2)": "axon_area",
    "axon_perimeter (um)": "axon_perimeter",
    "myelin_area (um^2)": "myelin_area",
    "axon_diam (um)": "axon_diam",
    "myelin_thickness (um)": "myelin_thickness",
    "axonmyelin_area (um^2)": "axonmyelin_area",
    "axonmyelin_perimeter (um)": "axonmyelin_perimeter",
}


# ============================================================================
# Functions
# ============================================================================

def setup_publication_style():
    rcParams.update({
        "font.size": 14,
        "axes.titlesize": 16,
        "axes.labelsize": 16,
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "axes.linewidth": 2,
        "xtick.major.width": 2,
        "ytick.major.width": 2,
        "xtick.major.size": 6,
        "ytick.major.size": 6,
        "xtick.minor.width": 1,
        "ytick.minor.width": 1,
        "lines.linewidth": 2,
        "lines.markersize": 3,
        "legend.fontsize": 10,
        "mathtext.fontset": "stix",
        "font.family": "STIXGeneral",
        "figure.dpi": 300,
    })


def load_morphometrics(sample, slice_id):
    """Load a single morphometrics xlsx file."""
    path = DATA_DIR / sample / f"{slice_id}_axon_morphometrics.xlsx"
    df = pd.read_excel(path)
    df = df.rename(columns=COLUMN_RENAME)
    df["sample"] = sample
    df["slice_id"] = slice_id
    return df


def filter_morphometrics(df, sample, slice_id):
    """Filter out invalid axons. Returns filtered DataFrame."""
    n_before = len(df)

    # Remove border-touching axons
    if "image_border_touching" in df.columns:
        df = df[df["image_border_touching"] != True]

    # Remove axons with no myelin
    df = df[df["myelin_area"] > 0]
    df = df[df["myelin_thickness"] > 0]
    df = df[df["gratio"] < 1.0]

    # Remove myelin with no axons
    df = df[df["axon_area"] > 0]
    df = df[df["axon_diam"] > 0]

    # Remove invalid g-ratios
    df = df[df["gratio"] > 0]

    # Drop NaN rows in key columns
    df = df.dropna(subset=["gratio", "axon_diam", "myelin_thickness", "myelin_area"])

    n_after = len(df)
    print(f"    {sample}/{slice_id}: {n_before} -> {n_after} axons ({n_before - n_after} removed)")
    return df


def combine_sample_morphometrics(sample):
    """Load, filter, and combine all slices for one sample."""
    dfs = []
    for slice_id in SAMPLE_SLICES[sample]:
        df = load_morphometrics(sample, slice_id)
        df = filter_morphometrics(df, sample, slice_id)
        dfs.append(df)
    combined = pd.concat(dfs, ignore_index=True)
    return combined


def compute_fiber_diameter(df):
    """Add fiber_diam column."""
    df = df.copy()
    df["fiber_diam"] = df["axon_diam"] + 2 * df["myelin_thickness"]
    return df


def plot_axon_vs_fiber_diameter(all_data, fixed_range, output_dir):
    """Plot axon diameter vs fiber diameter for all 8 regions."""
    fig, axes = plt.subplots(2, 4, figsize=(24, 12))

    if fixed_range:
        all_df = pd.concat(all_data.values())
        x_max = all_df["axon_diam"].max() * 1.05
        y_max = all_df["fiber_diam"].max() * 1.05

    for idx, sample in enumerate(sorted(all_data.keys())):
        df = all_data[sample]
        ax = axes[idx // 4, idx % 4]

        x = df["axon_diam"].values
        y = df["fiber_diam"].values

        ax.scatter(x, y, alpha=0.3, s=8, color="steelblue", edgecolors="none")

        # Linear regression
        slope, intercept, r_value, p_value, std_err = scipy_stats.linregress(x, y)
        x_line = np.linspace(0, x.max() * 1.05, 100)
        y_line = slope * x_line + intercept
        ax.plot(x_line, y_line, "r-", linewidth=2,
                label=f"y = {slope:.2f}x + {intercept:.4f}\n$R^2$ = {r_value**2:.3f}")

        ax.set_xlabel("Axon diameter (\u03bcm)")
        ax.set_ylabel("Fiber diameter (\u03bcm)")
        ax.set_title(REGION_LABELS[sample])
        ax.legend(loc="upper left", fontsize=9)
        ax.text(0.95, 0.05, f"n = {len(df)}", transform=ax.transAxes,
                ha="right", va="bottom", fontsize=11)

        if fixed_range:
            ax.set_xlim(0, x_max)
            ax.set_ylim(0, y_max)
        else:
            ax.set_xlim(0, x.max() * 1.05)
            ax.set_ylim(0, y.max() * 1.05)

    plt.tight_layout()
    suffix = "fixed_range" if fixed_range else "optimal_range"
    fig.savefig(output_dir / f"axon_vs_fiber_diameter_{suffix}.pdf", bbox_inches="tight")
    fig.savefig(output_dir / f"axon_vs_fiber_diameter_{suffix}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved axon_vs_fiber_diameter_{suffix}.{{pdf,png}}")


def plot_gratio_vs_fiber_diameter(all_data, fixed_range, output_dir):
    """Plot g-ratio vs fiber diameter for all 8 regions."""
    fig, axes = plt.subplots(2, 4, figsize=(24, 12))

    if fixed_range:
        all_df = pd.concat(all_data.values())
        x_max = all_df["fiber_diam"].max() * 1.05
        y_min = max(all_df["gratio"].min() * 0.95, 0)
        y_max = min(all_df["gratio"].max() * 1.05, 1.0)

    for idx, sample in enumerate(sorted(all_data.keys())):
        df = all_data[sample]
        ax = axes[idx // 4, idx % 4]

        x = df["fiber_diam"].values
        y = df["gratio"].values

        ax.scatter(x, y, alpha=0.3, s=8, color="darkorange", edgecolors="none")

        # Linear fit
        slope, intercept, r_value, p_value, std_err = scipy_stats.linregress(x, y)
        x_line = np.linspace(0, x.max() * 1.05, 100)
        y_line = slope * x_line + intercept
        ax.plot(x_line, y_line, "r-", linewidth=2,
                label=f"y = {slope:.4f}x + {intercept:.3f}\n$R^2$ = {r_value**2:.3f}")

        ax.set_xlabel("Fiber diameter (\u03bcm)")
        ax.set_ylabel("G-ratio")
        ax.set_title(REGION_LABELS[sample])
        ax.legend(loc="lower right", fontsize=9)
        ax.text(0.95, 0.95, f"n = {len(df)}", transform=ax.transAxes,
                ha="right", va="top", fontsize=11)

        if fixed_range:
            ax.set_xlim(0, x_max)
            ax.set_ylim(y_min, y_max)
        else:
            ax.set_xlim(0, x.max() * 1.05)
            ax.set_ylim(max(y.min() * 0.95, 0), min(y.max() * 1.05, 1.0))

    plt.tight_layout()
    suffix = "fixed_range" if fixed_range else "optimal_range"
    fig.savefig(output_dir / f"gratio_vs_fiber_diameter_{suffix}.pdf", bbox_inches="tight")
    fig.savefig(output_dir / f"gratio_vs_fiber_diameter_{suffix}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved gratio_vs_fiber_diameter_{suffix}.{{pdf,png}}")


# ============================================================================
# Main
# ============================================================================

def main():
    setup_publication_style()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load, filter, combine morphometrics for each sample
    print("=== Loading and filtering morphometrics ===")
    all_data = {}
    for sample in sorted(SAMPLE_SLICES.keys()):
        print(f"  {sample} ({REGION_LABELS[sample]}):")
        df = combine_sample_morphometrics(sample)
        df = compute_fiber_diameter(df)
        all_data[sample] = df

        # Save combined filtered data
        df.to_csv(OUTPUT_DIR / f"{sample}_filtered_morphometrics.csv", index=False)

    # Print summary statistics
    print("\n=== Summary Statistics ===")
    for sample in sorted(all_data.keys()):
        df = all_data[sample]
        print(f"\n{REGION_LABELS[sample]} ({sample}):")
        print(f"  Total axons: {len(df)}")
        print(f"  Axon diameter:  {df['axon_diam'].mean():.4f} \u00b1 {df['axon_diam'].std():.4f} \u03bcm")
        print(f"  Fiber diameter: {df['fiber_diam'].mean():.4f} \u00b1 {df['fiber_diam'].std():.4f} \u03bcm")
        print(f"  G-ratio:        {df['gratio'].mean():.4f} \u00b1 {df['gratio'].std():.4f}")
        print(f"  Myelin thickness: {df['myelin_thickness'].mean():.4f} \u00b1 {df['myelin_thickness'].std():.4f} \u03bcm")

    # Generate plots
    print("\n=== Generating plots ===")
    for fixed in [True, False]:
        plot_axon_vs_fiber_diameter(all_data, fixed_range=fixed, output_dir=OUTPUT_DIR)
        plot_gratio_vs_fiber_diameter(all_data, fixed_range=fixed, output_dir=OUTPUT_DIR)

    print(f"\nAll outputs saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
