# Macaque Corpus Callosum G-Ratio Analysis

This book presents a morphometric analysis of myelinated axons across 8 regions of the macaque corpus callosum (CC). The goal is to characterize the relationship between axon diameter, fiber diameter, and g-ratio across CC regions, and to determine whether the g-ratio is constant or regionally variable.

## Data

- **Species:** Macaque
- **Structure:** Corpus callosum, 8 regions (Region 1 = genu through Region 8 = splenium)
- **Images per region:** 3 histology image fields of view
- **Pixel size:** 0.009144 um
- **Image dimensions:** 2300 x 3040 pixels

## Pipeline

1. **Segmentation:** Axon and myelin masks were generated using [AxonDeepSeg](https://axondeepseg.readthedocs.io/) (v5.4.0), then manually corrected.
2. **Morphometrics:** Per-axon measurements (diameter, area, g-ratio, myelin thickness, etc.) were computed using `axondeepseg_morphometrics`.
3. **Filtering:** Axons touching the image border, unmyelinated axons, and invalid segmentations were removed.
4. **Analysis:** Linear regression of axon diameter vs fiber diameter and g-ratio vs fiber diameter.

## Contents

```{tableofcontents}
```
