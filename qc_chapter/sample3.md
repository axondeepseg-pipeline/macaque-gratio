# Region 3

## Slice 01

### Segmentation overlay

![Segmentation overlay](../results/qa_sample3_01/segmentation_overlay.png)

### Summary

- **Total axons:** 276
- **Excluded:** 57 (20.7%)
- **Retained:** 219

### Exclusions by category

- **artifact:** 11
- **border:** 32
- **invalid:** 5
- **merge_error:** 3
- **myelin_dominant:** 6

### Flagged axons (visual review)

![Flagged axons](../results/qa_sample3_01/suspects_zoom.png)

### Exclusion details

| Axon ID | Category | G-ratio | Axon diam (um) | Myelin thickness (um) | Solidity | Reasons | Closeup |
|---------|----------|---------|----------------|----------------------|----------|---------|---------|
| 0 | border | 0.519 | 1.1808 | 0.5461 | 0.709 | border-touching; low solidity (0.709) | [view](../results/qa_sample3_01/axon_0_labeled.png) |
| 1 | border | 0.905 | 1.8355 | 0.0959 | 0.977 | border-touching | [view](../results/qa_sample3_01/axon_1_labeled.png) |
| 2 | border | 0.763 | 0.2889 | 0.0450 | 0.958 | border-touching | [view](../results/qa_sample3_01/axon_2_labeled.png) |
| 3 | border | 0.179 | 0.0744 | 0.1710 | 0.897 | border-touching; very low gratio (0.179); myelin>>axon (mt/ad=2.30) | [view](../results/qa_sample3_01/axon_3_labeled.png) |
| 4 | border | 0.637 | 0.2502 | 0.0713 | 0.932 | border-touching | [view](../results/qa_sample3_01/axon_4_labeled.png) |
| 5 | border | 0.738 | 0.1664 | 0.0295 | 0.825 | border-touching | [view](../results/qa_sample3_01/axon_5_labeled.png) |
| 6 | border | 0.338 | 0.1149 | 0.1126 | 0.642 | border-touching; low solidity (0.642) | [view](../results/qa_sample3_01/axon_6_labeled.png) |
| 7 | border | 0.763 | 1.2506 | 0.1945 | 0.890 | border-touching | [view](../results/qa_sample3_01/axon_7_labeled.png) |
| 9 | artifact | 0.549 | 0.0413 | 0.0169 | 1.000 | tiny axon (0.0413 um) | [view](../results/qa_sample3_01/axon_9_labeled.png) |
| 17 | artifact | 0.171 | 0.0206 | 0.0501 | 1.000 | tiny axon (0.0206 um); very low gratio (0.171); myelin>>axon (mt/ad=2.43) | [view](../results/qa_sample3_01/axon_17_labeled.png) |
| 23 | artifact | 0.263 | 0.0206 | 0.0290 | 1.000 | tiny axon (0.0206 um); very low gratio (0.263); myelin>>axon (mt/ad=1.40) | [view](../results/qa_sample3_01/axon_23_labeled.png) |
| 24 | myelin_dominant | 0.263 | 0.0692 | 0.0970 | 0.692 | very low gratio (0.263); low solidity (0.692); myelin>>axon (mt/ad=1.40) | [view](../results/qa_sample3_01/axon_24_labeled.png) |
| 28 | artifact | 0.094 | 0.0103 | 0.0494 | 1.000 | tiny axon (0.0103 um); very low gratio (0.094); myelin>>axon (mt/ad=4.79) | [view](../results/qa_sample3_01/axon_28_labeled.png) |
| 31 | myelin_dominant | 0.173 | 0.0565 | 0.1349 | 0.667 | very low gratio (0.173); low solidity (0.667); myelin>>axon (mt/ad=2.39) | [view](../results/qa_sample3_01/axon_31_labeled.png) |
| 38 | border | 0.579 | 0.3378 | 0.1229 | 0.752 | border-touching | [view](../results/qa_sample3_01/axon_38_labeled.png) |
| 45 | border | 0.617 | 0.0584 | 0.0181 | 1.000 | border-touching | [view](../results/qa_sample3_01/axon_45_labeled.png) |
| 56 | border | 0.817 | 0.7512 | 0.0841 | 0.959 | border-touching | [view](../results/qa_sample3_01/axon_56_labeled.png) |
| 58 | artifact | 0.289 | 0.0461 | 0.0567 | 0.952 | tiny axon (0.0461 um); very low gratio (0.289); myelin>>axon (mt/ad=1.23) | [view](../results/qa_sample3_01/axon_58_labeled.png) |
| 62 | myelin_dominant | 0.275 | 0.0505 | 0.0667 | 1.000 | very low gratio (0.275); myelin>>axon (mt/ad=1.32) | [view](../results/qa_sample3_01/axon_62_labeled.png) |
| 63 | border | 0.802 | 0.4204 | 0.0520 | 0.946 | border-touching | [view](../results/qa_sample3_01/axon_63_labeled.png) |
| 73 | border | 0.860 | 1.5258 | 0.1242 | 0.959 | border-touching | [view](../results/qa_sample3_01/axon_73_labeled.png) |
| 77 | border | 0.850 | 0.7773 | 0.0686 | 0.972 | border-touching | [view](../results/qa_sample3_01/axon_77_labeled.png) |
| 81 | merge_error | 0.841 | 1.6129 | 0.1527 | 0.688 | low solidity (0.688) | [view](../results/qa_sample3_01/axon_81_labeled.png) |
| 85 | artifact | 0.124 | 0.0206 | 0.0732 | 1.000 | tiny axon (0.0206 um); very low gratio (0.124); myelin>>axon (mt/ad=3.55) | [view](../results/qa_sample3_01/axon_85_labeled.png) |
| 101 | border | 0.660 | 0.2053 | 0.0528 | 0.961 | border-touching | [view](../results/qa_sample3_01/axon_101_labeled.png) |
| 104 | artifact | 0.192 | 0.0292 | 0.0614 | 1.000 | tiny axon (0.0292 um); very low gratio (0.192); myelin>>axon (mt/ad=2.10) | [view](../results/qa_sample3_01/axon_104_labeled.png) |
| 113 | border | 0.802 | 1.4929 | 0.1845 | 0.961 | border-touching | [view](../results/qa_sample3_01/axon_113_labeled.png) |
| 114 | border | 0.405 | 0.1130 | 0.0829 | 0.889 | border-touching | [view](../results/qa_sample3_01/axon_114_labeled.png) |
| 116 | invalid | 1.000 | 0.0231 | 0.0000 | 0.833 | gratio=1.000; no myelin; tiny axon (0.0231 um) | [view](../results/qa_sample3_01/axon_116_labeled.png) |
| 118 | invalid | 1.000 | 0.0292 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0292 um) | [view](../results/qa_sample3_01/axon_118_labeled.png) |
| 122 | invalid | 1.000 | 0.0292 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0292 um) | [view](../results/qa_sample3_01/axon_122_labeled.png) |
| 123 | invalid | 1.000 | 0.0206 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0206 um) | [view](../results/qa_sample3_01/axon_123_labeled.png) |
| 137 | artifact | 0.157 | 0.0253 | 0.0676 | 1.000 | tiny axon (0.0253 um); very low gratio (0.157); myelin>>axon (mt/ad=2.68) | [view](../results/qa_sample3_01/axon_137_labeled.png) |
| 141 | border | 0.762 | 0.4168 | 0.0649 | 0.937 | border-touching | [view](../results/qa_sample3_01/axon_141_labeled.png) |
| 146 | invalid | 1.000 | 0.0206 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0206 um) | [view](../results/qa_sample3_01/axon_146_labeled.png) |
| 149 | artifact | 0.179 | 0.0413 | 0.0947 | 1.000 | tiny axon (0.0413 um); very low gratio (0.179); myelin>>axon (mt/ad=2.30) | [view](../results/qa_sample3_01/axon_149_labeled.png) |
| 167 | border | 0.890 | 2.6773 | 0.1658 | 0.890 | border-touching | [view](../results/qa_sample3_01/axon_167_labeled.png) |
| 170 | merge_error | 0.743 | 1.2248 | 0.2114 | 0.642 | low solidity (0.642) | [view](../results/qa_sample3_01/axon_170_labeled.png) |
| 175 | artifact | 0.074 | 0.0206 | 0.1296 | 1.000 | tiny axon (0.0206 um); very low gratio (0.074); myelin>>axon (mt/ad=6.28) | [view](../results/qa_sample3_01/axon_175_labeled.png) |
| 195 | artifact | 0.164 | 0.0206 | 0.0527 | 1.000 | tiny axon (0.0206 um); very low gratio (0.164); myelin>>axon (mt/ad=2.55) | [view](../results/qa_sample3_01/axon_195_labeled.png) |
| 200 | border | 0.474 | 0.1544 | 0.0858 | 0.858 | border-touching | [view](../results/qa_sample3_01/axon_200_labeled.png) |
| 205 | border | 0.811 | 1.2638 | 0.1471 | 0.973 | border-touching | [view](../results/qa_sample3_01/axon_205_labeled.png) |
| 216 | border | 0.337 | 0.2761 | 0.2712 | 0.941 | border-touching | [view](../results/qa_sample3_01/axon_216_labeled.png) |
| 218 | merge_error | nan | 0.2485 | nan | 0.546 | low solidity (0.546) | [view](../results/qa_sample3_01/axon_218_labeled.png) |
| 224 | border | 0.584 | 0.2947 | 0.1048 | 0.948 | border-touching | [view](../results/qa_sample3_01/axon_224_labeled.png) |
| 227 | myelin_dominant | 0.315 | 0.0990 | 0.1075 | 0.844 | myelin>>axon (mt/ad=1.09) | [view](../results/qa_sample3_01/axon_227_labeled.png) |
| 229 | myelin_dominant | 0.273 | 0.0876 | 0.1163 | 0.720 | very low gratio (0.273); low solidity (0.720); myelin>>axon (mt/ad=1.33) | [view](../results/qa_sample3_01/axon_229_labeled.png) |
| 233 | border | 0.652 | 0.4060 | 0.1082 | 0.944 | border-touching | [view](../results/qa_sample3_01/axon_233_labeled.png) |
| 246 | border | 0.568 | 0.3116 | 0.1186 | 0.805 | border-touching | [view](../results/qa_sample3_01/axon_246_labeled.png) |
| 259 | border | 0.901 | 3.3111 | 0.1829 | 0.964 | border-touching | [view](../results/qa_sample3_01/axon_259_labeled.png) |
| 269 | myelin_dominant | 0.297 | 0.0968 | 0.1144 | 0.721 | very low gratio (0.297); low solidity (0.721); myelin>>axon (mt/ad=1.18) | [view](../results/qa_sample3_01/axon_269_labeled.png) |
| 270 | border | 0.709 | 0.4857 | 0.0995 | 0.889 | border-touching | [view](../results/qa_sample3_01/axon_270_labeled.png) |
| 271 | border | 0.653 | 0.2643 | 0.0703 | 0.937 | border-touching | [view](../results/qa_sample3_01/axon_271_labeled.png) |
| 272 | border | 0.667 | 0.3526 | 0.0881 | 0.947 | border-touching | [view](../results/qa_sample3_01/axon_272_labeled.png) |
| 273 | border | 0.420 | 0.2874 | 0.1985 | 0.747 | border-touching; low solidity (0.747) | [view](../results/qa_sample3_01/axon_273_labeled.png) |
| 274 | border | 0.298 | 0.1903 | 0.2244 | 0.808 | border-touching; very low gratio (0.298); myelin>>axon (mt/ad=1.18) | [view](../results/qa_sample3_01/axon_274_labeled.png) |
| 275 | border | 0.464 | 0.1958 | 0.1129 | 0.870 | border-touching | [view](../results/qa_sample3_01/axon_275_labeled.png) |

---

## Slice 03

### Segmentation overlay

![Segmentation overlay](../results/qa_sample3_03/segmentation_overlay.png)

### Summary

- **Total axons:** 166
- **Excluded:** 66 (39.8%)
- **Retained:** 100

### Exclusions by category

- **artifact:** 17
- **border:** 33
- **invalid:** 10
- **merge_error:** 4
- **myelin_dominant:** 2

### Flagged axons (visual review)

![Flagged axons](../results/qa_sample3_03/suspects_zoom.png)

### Exclusion details

| Axon ID | Category | G-ratio | Axon diam (um) | Myelin thickness (um) | Solidity | Reasons | Closeup |
|---------|----------|---------|----------------|----------------------|----------|---------|---------|
| 0 | border | 0.631 | 0.3334 | 0.0973 | 0.936 | border-touching | [view](../results/qa_sample3_03/axon_0_labeled.png) |
| 1 | border | 0.852 | 3.4280 | 0.2986 | 0.966 | border-touching | [view](../results/qa_sample3_03/axon_1_labeled.png) |
| 2 | border | 0.312 | 0.0413 | 0.0454 | 1.000 | border-touching; tiny axon (0.0413 um); myelin>>axon (mt/ad=1.10) | [view](../results/qa_sample3_03/axon_2_labeled.png) |
| 3 | border | 0.694 | 0.5752 | 0.1268 | 0.969 | border-touching | [view](../results/qa_sample3_03/axon_3_labeled.png) |
| 4 | border | 0.840 | 0.8398 | 0.0797 | 0.931 | border-touching | [view](../results/qa_sample3_03/axon_4_labeled.png) |
| 5 | border | 0.746 | 0.2691 | 0.0459 | 0.963 | border-touching | [view](../results/qa_sample3_03/axon_5_labeled.png) |
| 6 | border | 0.835 | 1.1368 | 0.1120 | 0.924 | border-touching | [view](../results/qa_sample3_03/axon_6_labeled.png) |
| 7 | border | 0.716 | 0.4060 | 0.0805 | 0.947 | border-touching | [view](../results/qa_sample3_03/axon_7_labeled.png) |
| 8 | border | 0.849 | 2.0711 | 0.1840 | 0.951 | border-touching | [view](../results/qa_sample3_03/axon_8_labeled.png) |
| 9 | border | 0.716 | 0.9873 | 0.1961 | 0.966 | border-touching | [view](../results/qa_sample3_03/axon_9_labeled.png) |
| 10 | artifact | 0.065 | 0.0206 | 0.1480 | 1.000 | tiny axon (0.0206 um); very low gratio (0.065); myelin>>axon (mt/ad=7.17) | [view](../results/qa_sample3_03/axon_10_labeled.png) |
| 13 | merge_error | 0.396 | 0.2154 | 0.1644 | 0.721 | low solidity (0.721) | [view](../results/qa_sample3_03/axon_13_labeled.png) |
| 14 | artifact | 0.213 | 0.0357 | 0.0660 | 1.000 | tiny axon (0.0357 um); very low gratio (0.213); myelin>>axon (mt/ad=1.85) | [view](../results/qa_sample3_03/axon_14_labeled.png) |
| 18 | border | 0.842 | 0.4786 | 0.0450 | 0.941 | border-touching | [view](../results/qa_sample3_03/axon_18_labeled.png) |
| 33 | artifact | 0.359 | 0.0292 | 0.0260 | 0.800 | tiny axon (0.0292 um) | [view](../results/qa_sample3_03/axon_33_labeled.png) |
| 34 | artifact | 0.250 | 0.0206 | 0.0310 | 1.000 | tiny axon (0.0206 um); very low gratio (0.250); myelin>>axon (mt/ad=1.50) | [view](../results/qa_sample3_03/axon_34_labeled.png) |
| 36 | invalid | 1.000 | 0.0461 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0461 um) | [view](../results/qa_sample3_03/axon_36_labeled.png) |
| 37 | invalid | 1.000 | 0.0146 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0146 um) | [view](../results/qa_sample3_03/axon_37_labeled.png) |
| 38 | invalid | 1.000 | 0.0146 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0146 um) | [view](../results/qa_sample3_03/axon_38_labeled.png) |
| 40 | border | 0.722 | 0.7784 | 0.1501 | 0.957 | border-touching | [view](../results/qa_sample3_03/axon_40_labeled.png) |
| 43 | border | 0.874 | 1.3635 | 0.0983 | 0.963 | border-touching | [view](../results/qa_sample3_03/axon_43_labeled.png) |
| 44 | border | 0.823 | 2.8197 | 0.3035 | 0.960 | border-touching | [view](../results/qa_sample3_03/axon_44_labeled.png) |
| 46 | artifact | 0.057 | 0.0206 | 0.1712 | 1.000 | tiny axon (0.0206 um); very low gratio (0.057); myelin>>axon (mt/ad=8.30) | [view](../results/qa_sample3_03/axon_46_labeled.png) |
| 47 | artifact | 0.471 | 0.0484 | 0.0271 | 0.815 | tiny axon (0.0484 um) | [view](../results/qa_sample3_03/axon_47_labeled.png) |
| 53 | border | 0.271 | 0.0684 | 0.0921 | 0.898 | border-touching; very low gratio (0.271); myelin>>axon (mt/ad=1.35) | [view](../results/qa_sample3_03/axon_53_labeled.png) |
| 55 | border | 0.119 | 0.0357 | 0.1318 | 1.000 | border-touching; tiny axon (0.0357 um); very low gratio (0.119); myelin>>axon (mt/ad=3.69) | [view](../results/qa_sample3_03/axon_55_labeled.png) |
| 57 | border | 0.795 | 2.1076 | 0.2709 | 0.945 | border-touching | [view](../results/qa_sample3_03/axon_57_labeled.png) |
| 80 | border | 0.830 | 1.4914 | 0.1528 | 0.936 | border-touching | [view](../results/qa_sample3_03/axon_80_labeled.png) |
| 82 | border | 0.790 | 0.9445 | 0.1252 | 0.958 | border-touching | [view](../results/qa_sample3_03/axon_82_labeled.png) |
| 84 | invalid | 1.000 | 0.0103 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0103 um) | [view](../results/qa_sample3_03/axon_84_labeled.png) |
| 87 | invalid | 1.000 | 0.0206 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0206 um) | [view](../results/qa_sample3_03/axon_87_labeled.png) |
| 88 | invalid | 1.000 | 0.0253 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0253 um) | [view](../results/qa_sample3_03/axon_88_labeled.png) |
| 89 | border | 0.759 | 0.3627 | 0.0574 | 0.819 | border-touching | [view](../results/qa_sample3_03/axon_89_labeled.png) |
| 90 | invalid | 1.000 | 0.0310 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0310 um) | [view](../results/qa_sample3_03/axon_90_labeled.png) |
| 92 | invalid | 1.000 | 0.0292 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0292 um) | [view](../results/qa_sample3_03/axon_92_labeled.png) |
| 93 | invalid | 1.000 | 0.0146 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0146 um) | [view](../results/qa_sample3_03/axon_93_labeled.png) |
| 94 | merge_error | 0.840 | 1.7808 | 0.1695 | 0.683 | low solidity (0.683) | [view](../results/qa_sample3_03/axon_94_labeled.png) |
| 98 | merge_error | 0.701 | 0.3680 | 0.0787 | 0.725 | low solidity (0.725) | [view](../results/qa_sample3_03/axon_98_labeled.png) |
| 99 | border | 0.717 | 1.3048 | 0.2574 | 0.970 | border-touching | [view](../results/qa_sample3_03/axon_99_labeled.png) |
| 100 | artifact | 0.202 | 0.0206 | 0.0408 | 1.000 | tiny axon (0.0206 um); very low gratio (0.202); myelin>>axon (mt/ad=1.97) | [view](../results/qa_sample3_03/axon_100_labeled.png) |
| 101 | merge_error | 0.523 | 0.1221 | 0.0556 | 0.745 | low solidity (0.745) | [view](../results/qa_sample3_03/axon_101_labeled.png) |
| 103 | artifact | 0.316 | 0.0292 | 0.0316 | 1.000 | tiny axon (0.0292 um); myelin>>axon (mt/ad=1.08) | [view](../results/qa_sample3_03/axon_103_labeled.png) |
| 104 | myelin_dominant | 0.330 | 0.2389 | 0.2429 | 0.926 | myelin>>axon (mt/ad=1.02) | [view](../results/qa_sample3_03/axon_104_labeled.png) |
| 111 | invalid | 1.000 | 0.0146 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0146 um) | [view](../results/qa_sample3_03/axon_111_labeled.png) |
| 114 | border | 0.828 | 1.4600 | 0.1517 | 0.966 | border-touching | [view](../results/qa_sample3_03/axon_114_labeled.png) |
| 126 | border | 0.593 | 0.5927 | 0.2036 | 0.943 | border-touching | [view](../results/qa_sample3_03/axon_126_labeled.png) |
| 128 | artifact | 0.209 | 0.0386 | 0.0733 | 1.000 | tiny axon (0.0386 um); very low gratio (0.209); myelin>>axon (mt/ad=1.90) | [view](../results/qa_sample3_03/axon_128_labeled.png) |
| 130 | artifact | 0.152 | 0.0146 | 0.0408 | 1.000 | tiny axon (0.0146 um); very low gratio (0.152); myelin>>axon (mt/ad=2.80) | [view](../results/qa_sample3_03/axon_130_labeled.png) |
| 131 | artifact | 0.056 | 0.0103 | 0.0874 | 1.000 | tiny axon (0.0103 um); very low gratio (0.056); myelin>>axon (mt/ad=8.47) | [view](../results/qa_sample3_03/axon_131_labeled.png) |
| 133 | border | 0.326 | 0.0799 | 0.0827 | 0.882 | border-touching; myelin>>axon (mt/ad=1.03) | [view](../results/qa_sample3_03/axon_133_labeled.png) |
| 135 | border | 0.799 | 0.8295 | 0.1046 | 0.964 | border-touching | [view](../results/qa_sample3_03/axon_135_labeled.png) |
| 138 | artifact | 0.070 | 0.0357 | 0.2363 | 1.000 | tiny axon (0.0357 um); very low gratio (0.070); myelin>>axon (mt/ad=6.61) | [view](../results/qa_sample3_03/axon_138_labeled.png) |
| 139 | artifact | 0.089 | 0.0103 | 0.0530 | 1.000 | tiny axon (0.0103 um); very low gratio (0.089); myelin>>axon (mt/ad=5.13) | [view](../results/qa_sample3_03/axon_139_labeled.png) |
| 140 | artifact | 0.095 | 0.0179 | 0.0848 | 1.000 | tiny axon (0.0179 um); very low gratio (0.095); myelin>>axon (mt/ad=4.74) | [view](../results/qa_sample3_03/axon_140_labeled.png) |
| 141 | border | 0.449 | 0.2307 | 0.1414 | 0.667 | border-touching; low solidity (0.667) | [view](../results/qa_sample3_03/axon_141_labeled.png) |
| 144 | artifact | 0.088 | 0.0206 | 0.1063 | 1.000 | tiny axon (0.0206 um); very low gratio (0.088); myelin>>axon (mt/ad=5.15) | [view](../results/qa_sample3_03/axon_144_labeled.png) |
| 145 | artifact | 0.085 | 0.0206 | 0.1111 | 1.000 | tiny axon (0.0206 um); very low gratio (0.085); myelin>>axon (mt/ad=5.38) | [view](../results/qa_sample3_03/axon_145_labeled.png) |
| 147 | artifact | 0.046 | 0.0146 | 0.1510 | 1.000 | tiny axon (0.0146 um); very low gratio (0.046); myelin>>axon (mt/ad=10.35) | [view](../results/qa_sample3_03/axon_147_labeled.png) |
| 148 | myelin_dominant | 0.117 | 0.0505 | 0.1910 | 0.727 | very low gratio (0.117); low solidity (0.727); myelin>>axon (mt/ad=3.78) | [view](../results/qa_sample3_03/axon_148_labeled.png) |
| 152 | border | 0.717 | 0.7885 | 0.1559 | 0.972 | border-touching | [view](../results/qa_sample3_03/axon_152_labeled.png) |
| 158 | border | 0.863 | 1.2375 | 0.0982 | 0.967 | border-touching | [view](../results/qa_sample3_03/axon_158_labeled.png) |
| 161 | border | 0.775 | 0.6725 | 0.0978 | 0.881 | border-touching | [view](../results/qa_sample3_03/axon_161_labeled.png) |
| 162 | border | 0.683 | 0.8093 | 0.1879 | 0.967 | border-touching | [view](../results/qa_sample3_03/axon_162_labeled.png) |
| 163 | border | 0.777 | 0.4710 | 0.0675 | 0.938 | border-touching | [view](../results/qa_sample3_03/axon_163_labeled.png) |
| 164 | border | 0.485 | 0.1572 | 0.0833 | 0.928 | border-touching | [view](../results/qa_sample3_03/axon_164_labeled.png) |
| 165 | border | 0.408 | 0.0206 | 0.0150 | 1.000 | border-touching; tiny axon (0.0206 um) | [view](../results/qa_sample3_03/axon_165_labeled.png) |

---

## Slice 05

### Segmentation overlay

![Segmentation overlay](../results/qa_sample3_05/segmentation_overlay.png)

### Summary

- **Total axons:** 276
- **Excluded:** 59 (21.4%)
- **Retained:** 217

### Exclusions by category

- **artifact:** 5
- **border:** 48
- **invalid:** 2
- **merge_error:** 2
- **myelin_dominant:** 2

### Flagged axons (visual review)

![Flagged axons](../results/qa_sample3_05/suspects_zoom.png)

### Exclusion details

| Axon ID | Category | G-ratio | Axon diam (um) | Myelin thickness (um) | Solidity | Reasons | Closeup |
|---------|----------|---------|----------------|----------------------|----------|---------|---------|
| 0 | border | 0.827 | 0.8249 | 0.0862 | 0.955 | border-touching | [view](../results/qa_sample3_05/axon_0_labeled.png) |
| 1 | border | 0.820 | 0.5598 | 0.0614 | 0.954 | border-touching | [view](../results/qa_sample3_05/axon_1_labeled.png) |
| 2 | border | 0.596 | 0.1384 | 0.0469 | 0.947 | border-touching | [view](../results/qa_sample3_05/axon_2_labeled.png) |
| 3 | border | 0.872 | 1.1639 | 0.0852 | 0.977 | border-touching | [view](../results/qa_sample3_05/axon_3_labeled.png) |
| 4 | border | 0.890 | 1.2020 | 0.0741 | 0.956 | border-touching | [view](../results/qa_sample3_05/axon_4_labeled.png) |
| 5 | border | 0.878 | 1.7566 | 0.1222 | 0.945 | border-touching | [view](../results/qa_sample3_05/axon_5_labeled.png) |
| 6 | border | 0.838 | 0.9108 | 0.0879 | 0.971 | border-touching | [view](../results/qa_sample3_05/axon_6_labeled.png) |
| 7 | border | 0.738 | 0.5726 | 0.1016 | 0.919 | border-touching | [view](../results/qa_sample3_05/axon_7_labeled.png) |
| 8 | border | 0.883 | 1.3699 | 0.0907 | 0.941 | border-touching | [view](../results/qa_sample3_05/axon_8_labeled.png) |
| 9 | border | 0.654 | 0.2675 | 0.0707 | 0.957 | border-touching | [view](../results/qa_sample3_05/axon_9_labeled.png) |
| 10 | border | 0.873 | 0.9117 | 0.0665 | 0.926 | border-touching | [view](../results/qa_sample3_05/axon_10_labeled.png) |
| 11 | border | 0.572 | 0.4605 | 0.1725 | 0.845 | border-touching | [view](../results/qa_sample3_05/axon_11_labeled.png) |
| 12 | border | 0.481 | 0.2213 | 0.1194 | 0.948 | border-touching | [view](../results/qa_sample3_05/axon_12_labeled.png) |
| 18 | merge_error | 0.546 | 0.1936 | 0.0805 | 0.730 | low solidity (0.730) | [view](../results/qa_sample3_05/axon_18_labeled.png) |
| 19 | myelin_dominant | 0.235 | 0.0707 | 0.1150 | 0.887 | very low gratio (0.235); myelin>>axon (mt/ad=1.63) | [view](../results/qa_sample3_05/axon_19_labeled.png) |
| 49 | invalid | 1.000 | 0.0253 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0253 um) | [view](../results/qa_sample3_05/axon_49_labeled.png) |
| 52 | artifact | 0.285 | 0.0413 | 0.0518 | 1.000 | tiny axon (0.0413 um); very low gratio (0.285); myelin>>axon (mt/ad=1.25) | [view](../results/qa_sample3_05/axon_52_labeled.png) |
| 54 | border | 0.776 | 0.6407 | 0.0926 | 0.974 | border-touching | [view](../results/qa_sample3_05/axon_54_labeled.png) |
| 60 | border | 0.788 | 1.5413 | 0.2075 | 0.968 | border-touching | [view](../results/qa_sample3_05/axon_60_labeled.png) |
| 62 | border | 0.846 | 0.6875 | 0.0626 | 0.965 | border-touching | [view](../results/qa_sample3_05/axon_62_labeled.png) |
| 67 | border | 0.840 | 0.7187 | 0.0682 | 0.967 | border-touching | [view](../results/qa_sample3_05/axon_67_labeled.png) |
| 70 | invalid | 1.000 | 0.0206 | 0.0000 | 1.000 | gratio=1.000; no myelin; tiny axon (0.0206 um) | [view](../results/qa_sample3_05/axon_70_labeled.png) |
| 74 | artifact | 0.147 | 0.0206 | 0.0599 | 1.000 | tiny axon (0.0206 um); very low gratio (0.147); myelin>>axon (mt/ad=2.90) | [view](../results/qa_sample3_05/axon_74_labeled.png) |
| 82 | artifact | 0.142 | 0.0292 | 0.0885 | 1.000 | tiny axon (0.0292 um); very low gratio (0.142); myelin>>axon (mt/ad=3.03) | [view](../results/qa_sample3_05/axon_82_labeled.png) |
| 89 | border | 0.716 | 0.3490 | 0.0693 | 0.957 | border-touching | [view](../results/qa_sample3_05/axon_89_labeled.png) |
| 97 | border | 0.284 | 0.1321 | 0.1664 | 0.828 | border-touching; very low gratio (0.284); myelin>>axon (mt/ad=1.26) | [view](../results/qa_sample3_05/axon_97_labeled.png) |
| 103 | border | 0.902 | 1.0369 | 0.0564 | 0.971 | border-touching | [view](../results/qa_sample3_05/axon_103_labeled.png) |
| 104 | border | 0.530 | 0.1638 | 0.0725 | 0.887 | border-touching | [view](../results/qa_sample3_05/axon_104_labeled.png) |
| 106 | border | 0.901 | 1.4270 | 0.0783 | 0.928 | border-touching | [view](../results/qa_sample3_05/axon_106_labeled.png) |
| 114 | border | 0.698 | 0.3150 | 0.0680 | 0.948 | border-touching | [view](../results/qa_sample3_05/axon_114_labeled.png) |
| 121 | border | 0.835 | 0.7116 | 0.0704 | 0.944 | border-touching | [view](../results/qa_sample3_05/axon_121_labeled.png) |
| 126 | border | 0.804 | 0.5088 | 0.0620 | 0.969 | border-touching | [view](../results/qa_sample3_05/axon_126_labeled.png) |
| 135 | border | 0.810 | 0.5518 | 0.0647 | 0.967 | border-touching | [view](../results/qa_sample3_05/axon_135_labeled.png) |
| 147 | border | 0.807 | 0.4343 | 0.0518 | 0.893 | border-touching | [view](../results/qa_sample3_05/axon_147_labeled.png) |
| 164 | border | 0.654 | 0.4001 | 0.1057 | 0.953 | border-touching | [view](../results/qa_sample3_05/axon_164_labeled.png) |
| 177 | border | 0.846 | 0.6111 | 0.0554 | 0.966 | border-touching | [view](../results/qa_sample3_05/axon_177_labeled.png) |
| 180 | artifact | 0.064 | 0.0461 | 0.3372 | 0.769 | tiny axon (0.0461 um); very low gratio (0.064); myelin>>axon (mt/ad=7.31) | [view](../results/qa_sample3_05/axon_180_labeled.png) |
| 185 | border | 0.767 | 0.7842 | 0.1192 | 0.965 | border-touching | [view](../results/qa_sample3_05/axon_185_labeled.png) |
| 189 | myelin_dominant | 0.105 | 0.0653 | 0.2787 | 0.800 | very low gratio (0.105); myelin>>axon (mt/ad=4.27) | [view](../results/qa_sample3_05/axon_189_labeled.png) |
| 192 | merge_error | 0.706 | 0.1914 | 0.0399 | 0.616 | low solidity (0.616) | [view](../results/qa_sample3_05/axon_192_labeled.png) |
| 203 | border | 0.923 | 1.5466 | 0.0645 | 0.937 | border-touching | [view](../results/qa_sample3_05/axon_203_labeled.png) |
| 207 | border | 0.787 | 0.6139 | 0.0829 | 0.960 | border-touching | [view](../results/qa_sample3_05/axon_207_labeled.png) |
| 223 | border | 0.912 | 1.6479 | 0.0792 | 0.912 | border-touching | [view](../results/qa_sample3_05/axon_223_labeled.png) |
| 237 | border | 0.873 | 1.1661 | 0.0848 | 0.978 | border-touching | [view](../results/qa_sample3_05/axon_237_labeled.png) |
| 243 | artifact | 0.408 | 0.0206 | 0.0150 | 1.000 | tiny axon (0.0206 um) | [view](../results/qa_sample3_05/axon_243_labeled.png) |
| 253 | border | 0.683 | 0.4269 | 0.0992 | 0.923 | border-touching | [view](../results/qa_sample3_05/axon_253_labeled.png) |
| 258 | border | 0.888 | 1.4816 | 0.0938 | 0.957 | border-touching | [view](../results/qa_sample3_05/axon_258_labeled.png) |
| 263 | border | 0.830 | 1.3823 | 0.1412 | 0.965 | border-touching | [view](../results/qa_sample3_05/axon_263_labeled.png) |
| 265 | border | 0.883 | 1.5390 | 0.1018 | 0.868 | border-touching | [view](../results/qa_sample3_05/axon_265_labeled.png) |
| 266 | border | 0.741 | 0.4614 | 0.0807 | 0.939 | border-touching | [view](../results/qa_sample3_05/axon_266_labeled.png) |
| 267 | border | 0.815 | 0.8938 | 0.1018 | 0.911 | border-touching | [view](../results/qa_sample3_05/axon_267_labeled.png) |
| 268 | border | 0.875 | 0.8835 | 0.0634 | 0.958 | border-touching | [view](../results/qa_sample3_05/axon_268_labeled.png) |
| 269 | border | 0.886 | 1.0241 | 0.0657 | 0.885 | border-touching | [view](../results/qa_sample3_05/axon_269_labeled.png) |
| 270 | border | 0.857 | 0.8546 | 0.0710 | 0.968 | border-touching | [view](../results/qa_sample3_05/axon_270_labeled.png) |
| 271 | border | 0.831 | 0.5192 | 0.0529 | 0.729 | border-touching; low solidity (0.729) | [view](../results/qa_sample3_05/axon_271_labeled.png) |
| 272 | border | 0.714 | 0.2874 | 0.0576 | 0.923 | border-touching | [view](../results/qa_sample3_05/axon_272_labeled.png) |
| 273 | border | 0.611 | 0.3610 | 0.1152 | 0.877 | border-touching | [view](../results/qa_sample3_05/axon_273_labeled.png) |
| 274 | border | 0.665 | 0.1321 | 0.0333 | 0.872 | border-touching | [view](../results/qa_sample3_05/axon_274_labeled.png) |
| 275 | border | 0.766 | 0.0968 | 0.0148 | 0.815 | border-touching | [view](../results/qa_sample3_05/axon_275_labeled.png) |

---
