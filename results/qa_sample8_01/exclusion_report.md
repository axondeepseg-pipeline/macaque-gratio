# Axon Exclusion Report — Sample 8, Slice 01 (Corrected)

Total axons reviewed: 195
Axons excluded: 69
Axons retained: 126

Note: Sample 8 has significantly more segmentation artifacts than Sample 1. The tissue in this region (near the splenium) has larger, more irregularly shaped axons and lower axon density, which appears to cause more segmentation failures.

## Exclusion criteria applied

All 195 axon closeups were visually inspected alongside their morphometric values.

### Category 1: Border-touching (29 axons)

Truncated fiber masks at image edges. All visually confirmed.

**Excluded axon IDs:** 0, 1, 2, 3, 4, 5, 6, 8, 15, 18, 28, 35, 38, 45, 56, 62, 69, 73, 102, 120, 132, 133, 143, 175, 184, 190, 192, 193, 194

### Category 2: Unmyelinated / no myelin (4 axons)

Detections with g-ratio = 1.0 and zero myelin area.

| Axon ID | g-ratio | axon_diam (um) | Justification |
|---------|---------|----------------|---------------|
| 22 | 1.000 | 0.156 | Small detection with no myelin ring visible. |
| 23 | 1.000 | 0.046 | Tiny artifact, no discernible axon structure. |
| 39 | 1.000 | 0.070 | Small dark region, no myelin. |
| 96 | 1.000 | 0.029 | Sub-pixel artifact, no structure. |

### Category 3: Invalid segmentation — g-ratio > 1.0 (1 axon)

| Axon ID | g-ratio | axon_diam (um) | myelin_thickness (um) | Justification |
|---------|---------|----------------|----------------------|---------------|
| 36 | 1.540 | 1.580 | -0.277 | Negative myelin thickness, solidity=0.461. Visually this is a large red blob (myelin only) with no coherent axon-myelin structure. Completely invalid detection. |

### Category 4: Myelin-dominant artifacts (22 axons)

Detections with very low g-ratio (< 0.35) where myelin area greatly exceeds axon area. Visual inspection confirms these are not real myelinated axon cross-sections — they are tiny axon seeds inside large myelin fragments, or elongated slivers of tissue incorrectly labeled.

| Axon ID | g-ratio | axon_diam (um) | mt/ad ratio | Visual description |
|---------|---------|----------------|-------------|-------------------|
| 20 | 0.059 | 0.025 | 7.95 | Tiny dot inside large myelin wedge. Not an axon. |
| 34 | 0.314 | 0.025 | 1.09 | Sub-pixel axon with small myelin. Artifact. |
| 43 | 0.065 | 0.015 | 7.17 | Single pixel "axon" in myelin region. |
| 48 | 0.150 | 0.161 | 2.84 | Large red triangle — myelin fragment, not an axon. |
| 51 | 0.296 | 0.117 | 1.19 | Elongated sliver, not circular axon cross-section. |
| 54 | 0.262 | 0.134 | 1.41 | Elongated fragment between fibers. |
| 55 | 0.148 | 0.015 | 2.87 | Single pixel in myelin strip. |
| 91 | 0.085 | 0.044 | 5.39 | Vertical red bar — myelin fragment, no axon. |
| 92 | 0.179 | 0.064 | 2.29 | Red rectangle — pure myelin artifact. |
| 98 | 0.247 | 0.077 | 1.52 | Elongated red sliver. |
| 99 | 0.183 | 0.036 | 2.23 | Tiny axon in myelin patch. |
| 105 | 0.325 | 0.057 | 1.04 | Small ambiguous detection. |
| 108 | 0.157 | 0.021 | 2.68 | Red rectangle — myelin only. |
| 131 | 0.129 | 0.044 | 3.38 | Myelin strip with no visible axon. |
| 145 | 0.296 | 0.209 | 1.19 | Large red triangle — myelin fragment. |
| 146 | 0.054 | 0.010 | 8.77 | Single pixel in large myelin. Lowest g-ratio. |
| 149 | 0.157 | 0.021 | 2.68 | Red bar — myelin strip. |
| 150 | 0.152 | 0.015 | 2.78 | Single pixel in myelin. |
| 151 | 0.211 | 0.023 | 1.87 | Tiny fragment. |
| 152 | 0.106 | 0.023 | 4.22 | Tiny fragment with disproportionate myelin. |
| 154 | 0.023 | 0.010 | 21.56 | Lowest g-ratio in dataset. Pure artifact — single pixel with massive myelin assignment. |
| 160 | 0.059 | 0.036 | 8.04 | Red triangle — myelin fragment. |

### Category 5: Merge errors / irregular shape (8 axons)

Detections where segmentation merged multiple structures or captured non-axonal tissue. Identified by low solidity and/or high eccentricity, confirmed visually.

| Axon ID | g-ratio | axon_diam (um) | solidity | eccentricity | Justification |
|---------|---------|----------------|----------|--------------|---------------|
| 25 | 0.716 | 0.538 | 0.803 | 0.958 | Irregular elongated shape — appears to be two fibers merged. |
| 37 | 0.564 | 0.387 | 0.720 | 0.964 | Crescent-shaped detection wrapping around another fiber. Not a single axon. |
| 65 | 0.688 | 0.386 | 0.519 | 0.687 | Lowest solidity in dataset. Highly fragmented, irregular shape — not a coherent axon. |
| 68 | 0.384 | 0.074 | 0.912 | 0.964 | Very small elongated detection, no clear axon structure. |
| 95 | 0.577 | 0.036 | 0.750 | 0.977 | Tiny elongated sliver between fibers. |
| 130 | 0.447 | 0.015 | 1.000 | 1.000 | Sub-pixel elongated artifact. |
| 140 | 0.328 | 0.103 | 0.769 | 0.934 | Irregular shape, myelin bleeds into neighbor. |
| 159 | 0.388 | 0.195 | 0.730 | 0.984 | Elongated irregular detection — not a single axon cross-section. |

### Category 6: Additional artifacts (5 axons)

Detections that don't fit neatly into the above categories but are visually not valid myelinated axons.

| Axon ID | g-ratio | axon_diam (um) | Justification |
|---------|---------|----------------|---------------|
| 40 | 1.000* | 0.046 | ADS warned about unexpected measures. Visually ambiguous tiny detection. |
| 41 | 0.707 | 0.021 | ~2 pixel axon. Too small to be a reliable measurement. |
| 97 | 1.000* | 0.018 | ADS warned about unexpected measures. Sub-pixel. |
| 181 | 0.576 | 0.546 | solidity=0.714. Irregular concave shape — myelin from neighboring fiber incorrectly assigned. |
| 189 | 0.063 | 0.021 | Tiny pixel in large red wedge. Border artifact (not flagged as border-touching but visually at edge). |

\* These had ADS warnings about unexpected equivalent_diameter values.

## Summary

| Category | Count | Axon IDs |
|----------|-------|----------|
| Border-touching | 29 | 0-6, 8, 15, 18, 28, 35, 38, 45, 56, 62, 69, 73, 102, 120, 132, 133, 143, 175, 184, 190, 192-194 |
| Unmyelinated | 4 | 22, 23, 39, 96 |
| Invalid (g>1) | 1 | 36 |
| Myelin-dominant artifact | 22 | 20, 34, 43, 48, 51, 54, 55, 91, 92, 98, 99, 105, 108, 131, 145, 146, 149, 150, 151, 152, 154, 160 |
| Merge error / irregular | 8 | 25, 37, 65, 68, 95, 130, 140, 159 |
| Additional artifacts | 5 | 40, 41, 97, 181, 189 |
| **Total excluded** | **69** | |
| **Total retained** | **126** | |

## Comparison with Sample 1

| Metric | Sample 1 (01) | Sample 8 (01) |
|--------|---------------|---------------|
| Total axons | 496 | 195 |
| Excluded | 64 (12.9%) | 69 (35.4%) |
| Retained | 432 (87.1%) | 126 (64.6%) |
| Border-touching | 54 | 29 |
| Non-border exclusions | 10 | 40 |
| Myelin-dominant artifacts | 4 | 22 |

Sample 8 has a much higher exclusion rate (35% vs 13%), driven primarily by myelin-dominant artifacts (22 vs 4). This suggests the segmentation model performs less reliably in this CC region, possibly due to larger inter-axonal spaces and more irregular myelin morphology near the splenium.

## Recommendation

The existing notebook filters (`gratio > 0`, `gratio < 1.0`, `myelin_area > 0`, `myelin_thickness > 0`, `image_border_touching != True`) already catch most of these. Adding a **solidity > 0.75** filter would catch the merge errors. The myelin-dominant artifacts (g < 0.3) are already removed by implicit quality since they have extreme g-ratios that are clear outliers, but an explicit **g-ratio > 0.3** filter or **axon_diam > 0.05 um** filter would catch them cleanly.
