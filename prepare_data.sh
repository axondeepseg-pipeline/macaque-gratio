#!/bin/bash
set -euo pipefail

# ============================================================================
# Prepare data and run ADS morphometrics for macaque CC analysis
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ADS_DIR="$SCRIPT_DIR/axondeepseg"
DATA_DIR="$SCRIPT_DIR/data/macaque/data"
PIXEL_SIZE="0.009144"

# Activate ADS venv
source "$ADS_DIR/ads_conda/bin/activate" "$ADS_DIR/ads_conda/envs/venv_ads/"

# Sample-to-slice mapping
declare -A SAMPLE_SLICES
SAMPLE_SLICES[sample1]="01 03 07"
SAMPLE_SLICES[sample2]="01 03 05"
SAMPLE_SLICES[sample3]="01 03 05"
SAMPLE_SLICES[sample4]="01 05 07"
SAMPLE_SLICES[sample5]="01 03 05"
SAMPLE_SLICES[sample6]="01 03 05"
SAMPLE_SLICES[sample7]="01 03 05"
SAMPLE_SLICES[sample8]="01 03 05"

# --- Step 1: Fix misspelled corrections directory for sample2/05 ---
MISSPELLED="$DATA_DIR/sample2/05_correctioins"
CORRECT="$DATA_DIR/sample2/05_corrections"
if [ -d "$MISSPELLED" ] && [ ! -d "$CORRECT" ]; then
    echo "Renaming misspelled directory: 05_correctioins -> 05_corrections"
    mv "$MISSPELLED" "$CORRECT"
fi

# --- Step 2: Copy & rename corrected segmentations ---
echo ""
echo "=== Copying corrected segmentations ==="
for sample in $(echo "${!SAMPLE_SLICES[@]}" | tr ' ' '\n' | sort); do
    for slice in ${SAMPLE_SLICES[$sample]}; do
        corrections_dir="$DATA_DIR/$sample/${slice}_corrections"
        target_dir="$DATA_DIR/$sample"

        if [ ! -d "$corrections_dir" ]; then
            echo "WARNING: $corrections_dir does not exist, skipping"
            continue
        fi

        echo "  $sample/$slice: copying corrected segmentations"
        cp "$corrections_dir/ADS_seg-axon.png"  "$target_dir/${slice}_seg-axon.png"
        cp "$corrections_dir/ADS_seg-myelin.png" "$target_dir/${slice}_seg-myelin.png"
        cp "$corrections_dir/ADS_seg.png"        "$target_dir/${slice}_seg-axonmyelin.png"
    done
done

# --- Step 3: Create pixel_size_in_micrometer.txt ---
echo ""
echo "=== Creating pixel_size_in_micrometer.txt files ==="
for sample in $(echo "${!SAMPLE_SLICES[@]}" | tr ' ' '\n' | sort); do
    echo "$PIXEL_SIZE" > "$DATA_DIR/$sample/pixel_size_in_micrometer.txt"
    echo "  $sample: pixel_size_in_micrometer.txt created ($PIXEL_SIZE um)"
done

# --- Step 4: Run ADS morphometrics per image ---
echo ""
echo "=== Running ADS morphometrics ==="
for sample in $(echo "${!SAMPLE_SLICES[@]}" | tr ' ' '\n' | sort); do
    for slice in ${SAMPLE_SLICES[$sample]}; do
        img_path="$DATA_DIR/$sample/${slice}.png"
        if [ ! -f "$img_path" ]; then
            echo "WARNING: $img_path does not exist, skipping"
            continue
        fi
        echo "  Processing $sample/$slice.png ..."
        axondeepseg_morphometrics -i "$img_path" -s "$PIXEL_SIZE"
    done
done

echo ""
echo "=== Done ==="
echo "Morphometrics files generated. Run analyze_morphometrics.py next."
