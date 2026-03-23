# Macaque Corpus Callosum G-Ratio Analysis

Morphometric analysis of axon diameter, fiber diameter, myelin thickness, and g-ratio across 8 regions of the macaque corpus callosum, using segmentations from [AxonDeepSeg](https://github.com/axondeepseg/axondeepseg).

The analysis is published as an interactive MyST book with Plotly figures and per-axon quality control reports.

## Book chapters

| Chapter | Description |
|---------|-------------|
| **ADS2026_minorQC** | Corrected ADS segmentations with basic filters (border-touching, unmyelinated, invalid) |
| **ADS2015_noQC** | Original pre-correction morphometrics from 2015, no quality filters |
| **ADS2026_fullQC** | Corrected segmentations with full per-axon exclusion database from visual QC |
| **Quality Control** | Per-sample, per-image visual review of all flagged axons with exclusion justifications |

## Data

Source data consists of 24 histology images (8 CC regions x 3 slices each) with corresponding axon and myelin segmentation masks at 0.009144 um/pixel resolution.

- `data/macaque/data/sample{1-8}/` — raw images, masks, and morphometrics xlsx files
- `build_data/` — lightweight CSVs (morphometrics, flags, exclusion database) for reproducibility
- QC closeup images are hosted on S3

## Local development

### Prerequisites

- [Node.js](https://nodejs.org/) >= 18
- [mystmd](https://mystmd.org/): `npm install -g mystmd`

### Preview the book

```bash
myst start
```

### Re-execute notebooks (requires Python environment)

Install AxonDeepSeg and dependencies:

```bash
git clone https://github.com/axondeepseg/axondeepseg.git
cd axondeepseg && ./install_ads
source axondeepseg/ads_conda/bin/activate axondeepseg/ads_conda/envs/venv_ads/
```

Then execute:

```bash
jupyter nbconvert --to notebook --execute --inplace ADS2026_minorQC.ipynb
jupyter nbconvert --to notebook --execute --inplace ADS2015_noQC.ipynb
jupyter nbconvert --to notebook --execute --inplace ADS2026_fullQC.ipynb
```

### Re-run QC pipeline

```bash
python run_qc.py
```

This regenerates morphometrics, flags, closeup images, and the exclusion database for all 24 images.

## Deployment

The book is deployed to GitHub Pages via GitHub Actions on push to `main`. Notebooks are committed pre-executed, so CI only needs Node.js to build the static site.

## References

- Stikov, N. et al. (2015). In vivo histology of the myelin g-ratio with magnetic resonance imaging. *NeuroImage*, 118, 397-405.
- Zaimi, A. et al. (2018). AxonDeepSeg: automatic axon and myelin segmentation from microscopy data using convolutional neural networks. *Scientific Reports*, 8, 3816.
