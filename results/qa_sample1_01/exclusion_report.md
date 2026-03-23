# Axon Exclusion Report — Sample 1, Slice 01 (Corrected)

Total axons reviewed: 496
Axons excluded: 65
Axons retained: 431

## Exclusion criteria applied

All 496 axon closeups were visually inspected alongside their morphometric values (g-ratio, axon diameter, myelin thickness, solidity, eccentricity). Exclusions fall into the following categories:

### Category 1: Border-touching (54 axons)

Axons whose fiber (axon+myelin) mask touches the image border. These are excluded because the axon and/or myelin is truncated, leading to unreliable diameter, area, and g-ratio measurements.

**Excluded axon IDs:** 0, 1, 2, 3, 4, 5, 6, 18, 31, 37, 51, 60, 79, 95, 98, 110, 114, 122, 131, 132, 134, 153, 160, 170, 197, 219, 232, 253, 262, 273, 309, 319, 321, 343, 350, 362, 383, 389, 397, 403, 420, 430, 442, 474, 481, 483, 484, 489, 490, 491, 492, 493, 494, 495

**Visual confirmation:** All 54 axons were visually verified to have truncated masks at image edges. Many show partial myelin rings or clipped axon bodies. Some (e.g., #494, #495) are severely truncated with highly elongated apparent shapes (eccentricity > 0.98).

### Category 2: No myelin / unmyelinated (1 axon)

Axons detected with zero myelin area and g-ratio = 1.0. These represent either unmyelinated axons or segmentation failures where the myelin was not captured.

| Axon ID | g-ratio | axon_diam (um) | myelin_thickness (um) | Justification |
|---------|---------|----------------|----------------------|---------------|
| 66 | 1.000 | 0.023 | 0.000 | Tiny detection with no myelin. Visual inspection shows a single-pixel artifact with no discernible axon or myelin structure. |

### Category 3: Myelin-dominant detections (4 axons)

Axons with extremely low g-ratio (< 0.3) where myelin thickness greatly exceeds axon diameter. These represent segmentation errors where a tiny axon seed was placed inside a large myelin ring, or where neighboring myelin was incorrectly assigned.

| Axon ID | g-ratio | axon_diam (um) | myelin_thickness (um) | mt/ad ratio | Justification |
|---------|---------|----------------|----------------------|-------------|---------------|
| 146 | 0.199 | 0.029 | 0.059 | 2.02 | Tiny axon seed (~3 pixels) inside a disproportionately large myelin region. Visual inspection confirms the "axon" is a speck, not a real axon cross-section. |
| 210 | 0.228 | 0.051 | 0.085 | 1.69 | Very small axon with thick myelin. Visually appears to be a small dark region incorrectly labeled as axon inside a myelin sheath that likely belongs to a neighboring fiber. |
| 326 | 0.196 | 0.029 | 0.060 | 2.06 | Same pattern as #146 — sub-pixel axon seed with disproportionate myelin. Not a real myelinated axon. |
| 448 | 0.137 | 0.029 | 0.092 | 3.16 | Lowest g-ratio in the dataset. Tiny axon (~3 pixels) with very thick myelin. Visual inspection confirms this is a segmentation artifact — the "axon" is not a real axon cross-section. |

### Category 4: Segmentation merge errors (4 axons)

Axons where the segmentation has merged two or more adjacent axons into a single detection, or where the myelin boundary includes tissue from a neighboring fiber. These are identified by very low solidity (< 0.85) combined with high eccentricity (> 0.8), and confirmed visually.

| Axon ID | g-ratio | axon_diam (um) | solidity | eccentricity | Justification |
|---------|---------|----------------|----------|--------------|---------------|
| 133 | 0.840 | 1.422 | 0.824 | 0.953 | Very elongated shape with low solidity. Visual inspection shows two axons merged into one detection — the blue mask clearly covers two distinct axon bodies connected by a thin bridge. |
| 200 | 0.787 | 0.773 | 0.809 | 0.874 | Irregular axon shape with concavity. Visual inspection shows the axon mask extends into a neighboring fiber's territory. The myelin ring is asymmetric and incomplete on one side. |
| 241 | 0.809 | 0.328 | 0.683 | 0.944 | Lowest solidity in the dataset. The axon mask is highly irregular with large concavities. Visually this is not a single well-defined axon — it appears to be a fragment or noise. |
| 291 | 0.586 | 0.463 | 0.825 | 0.958 | Irregular dumbbell-shaped axon. Visual inspection shows two small axons merged into a single detection with a shared myelin boundary. |

### Category 5: Confirmed valid — not excluded

The following axons were flagged by automated criteria but confirmed valid upon visual inspection:

- **High eccentricity only (not border-touching):** Axon #393 (ecc=0.953, sol=0.794) — visually a small but real axon with an elongated shape. The shape is unusual but the segmentation is correct. **Excluded** — upon closer inspection, this is a very small elongated detection (d=0.107 um, ~12 pixels) that does not show a clear myelinated axon structure. **Reclassified to exclude.**
- **Large axons #82 and #175** (d=1.884 and 2.287 um) — visually confirmed as genuine large myelinated axons. The segmentation boundaries are accurate and the myelin rings are well-defined. **Retained.**
- **Axon #162** (sol=0.838, ecc=0.870) — visually the axon shape is somewhat irregular but represents a real myelinated axon. The myelin ring is complete. **Retained.**
- **Axon #203** (sol=0.846, ecc=0.839) — similar to #162, slightly irregular but a real axon. **Retained.**

### Updated Category 4 (adding #393):

| Axon ID | g-ratio | axon_diam (um) | solidity | eccentricity | Justification |
|---------|---------|----------------|----------|--------------|---------------|
| 393 | 0.399 | 0.107 | 0.794 | 0.953 | Very small elongated detection. Visual inspection shows no clear myelinated axon structure — appears to be a dark region between fibers incorrectly labeled as axon+myelin. |

## Summary

| Category | Count | Axon IDs |
|----------|-------|----------|
| Border-touching | 54 | 0-6, 18, 31, 37, 51, 60, 79, 95, 98, 110, 114, 122, 131, 132, 134, 153, 160, 170, 197, 219, 232, 253, 262, 273, 309, 319, 321, 343, 350, 362, 383, 389, 397, 403, 420, 430, 442, 474, 481, 483, 484, 489-495 |
| Unmyelinated / artifact | 1 | 66 |
| Myelin-dominant (bad seg) | 4 | 146, 210, 326, 448 |
| Merge error / irregular | 5 | 133, 200, 241, 291, 393 |
| **Total excluded** | **64** | |
| **Total retained** | **432** | |

## Notes

- The vast majority of axons (432/496 = 87%) have clean segmentation with well-defined axon and myelin boundaries.
- Border-touching axons are the dominant exclusion category (54/64 = 84% of exclusions). This is expected given the image has many axons near the edges.
- Only 10 non-border axons were excluded, all for clear segmentation artifacts visible in the closeup images.
- The two largest axons (#82 and #175, d > 1.8 um) were visually confirmed as valid despite their unusual size.
