# Quality Control

This chapter presents the visual quality control (QC) review of all axon segmentations across the 8 corpus callosum regions. Every axon detected by AxonDeepSeg was visually inspected and either retained or excluded.

## Methodology

For each image, the following QC pipeline was applied:

1. **Morphometrics computation** with instance segmentation using AxonDeepSeg v5.4.0
2. **Automated flagging** based on: border-touching, invalid g-ratio, no myelin, sub-pixel artifacts (d < 0.05 um), myelin-dominant (g < 0.3), low solidity (< 0.75), myelin >> axon (mt/ad > 1.0)
3. **Visual review** of every axon closeup, confirming auto-flags and checking for missed problems
4. **Exclusion decision** with per-axon justification

## Overall summary

- **Total axons detected:** 6825
- **Total excluded:** 1618 (23.7%)
- **Total retained:** 5207

### Exclusions by category

- **Border-touching:** 972 (truncated at image edges)
- **Sub-pixel artifacts:** 335 (axon diameter < 0.05 um)
- **Invalid g-ratio:** 116 (g >= 1.0 or negative myelin)
- **Merge errors:** 105 (solidity < 0.75, irregular shapes)
- **Myelin-dominant:** 90 (g < 0.3, myelin >> axon)

### Per-image summary

| Sample | Slice | Total | Excluded | Retained | % Excluded |
|--------|-------|-------|----------|----------|------------|
| Region 1 | 1 | 496 | 60 | 436 | 12.1% |
| Region 1 | 3 | 445 | 72 | 373 | 16.2% |
| Region 1 | 7 | 496 | 94 | 402 | 19.0% |
| Region 2 | 1 | 308 | 46 | 262 | 14.9% |
| Region 2 | 3 | 369 | 52 | 317 | 14.1% |
| Region 2 | 5 | 364 | 55 | 309 | 15.1% |
| Region 3 | 1 | 276 | 57 | 219 | 20.7% |
| Region 3 | 3 | 166 | 66 | 100 | 39.8% |
| Region 3 | 5 | 276 | 59 | 217 | 21.4% |
| Region 4 | 1 | 144 | 83 | 61 | 57.6% |
| Region 4 | 5 | 180 | 72 | 108 | 40.0% |
| Region 4 | 7 | 200 | 78 | 122 | 39.0% |
| Region 5 | 1 | 214 | 70 | 144 | 32.7% |
| Region 5 | 3 | 216 | 67 | 149 | 31.0% |
| Region 5 | 5 | 281 | 70 | 211 | 24.9% |
| Region 6 | 1 | 271 | 68 | 203 | 25.1% |
| Region 6 | 3 | 279 | 86 | 193 | 30.8% |
| Region 6 | 5 | 331 | 81 | 250 | 24.5% |
| Region 7 | 1 | 329 | 72 | 257 | 21.9% |
| Region 7 | 3 | 323 | 80 | 243 | 24.8% |
| Region 7 | 5 | 322 | 62 | 260 | 19.3% |
| Region 8 | 1 | 195 | 68 | 127 | 34.9% |
| Region 8 | 3 | 255 | 75 | 180 | 29.4% |
| Region 8 | 5 | 89 | 25 | 64 | 28.1% |

### Recommended filters

Based on the visual review, the following automated filters capture all exclusions:

1. `image_border_touching == True`
2. `gratio >= 1.0` or `gratio <= 0`
3. `myelin_area <= 0` or `myelin_thickness <= 0`
4. `axon_diam < 0.05 um`
5. `gratio < 0.3`
6. `solidity < 0.75`
7. `myelin_thickness / axon_diam > 1.0`

The full exclusion database is available as [`exclusion_database.csv`](https://macaque-gratio.s3.ca-central-1.amazonaws.com/results/exclusion_database.csv).

## Per-sample reports

```{tableofcontents}
```