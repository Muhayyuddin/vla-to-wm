> Historical audit, 23 September 2026. The numerical checks remain relevant. Statements below about restored/original figure designs refer to that earlier draft; the current designs and reproduction instructions are documented in [the repository README](../README.md) and [BUILD.md](BUILD.md).

# Plot data validation

Checked 23 September 2026 against the version-specific primary papers, the supplied Excel workbook, and the revised manuscript figures.

**Result:** all seven reported scale values/bounds and all eight World-Gymnast means and eight standard errors are supported by the cited primary sources. The paper's plotted values, uncertainty bars, and four percentage-point differences agree with the workbook. No numerical replacement is required. Following the author's restoration request, the final surgical draft retains the original graphics unchanged and adds the two necessary scope qualifications in its purple caption text.

## Workbook identity and coverage

Input: `VLA_WM_verified_data_and_plots.xlsx`. SHA-256: `fa1112ca7a7cdd4bd2e16acb32db462cfb4068ab983db18794d548474b795775`.

This file is byte-for-byte identical to the workbook in the supplied verified-data package used for the plots. The original workbook was inspected without changing or re-exporting it. The checks covered the seven scale records, four task comparisons, their source/version fields, derived logarithms and differences, formula caches, native chart source ranges, and quantitative figure outputs. Source-paper checks are independent of the workbook's pre-existing `verified_primary_source` labels. The final surgical manuscript uses the two original quantitative figure PDFs, copied byte-for-byte; the earlier redesigned figures have been superseded.

The workbook's **147 rows** describe an earlier CSV audit: 106 corpus rows, 34 evidence rows, and 7 scale rows. They are not the manuscript's **156 included reports**. The historical exclusion decisions reconcile internally, but the full original review ledger is not supplied or independently validated by this plotting audit.

## Data-scale values

All workbook locations below refer to `Verified Data Scale`. Column E contains the numeric plotting coordinate, F its bound type, G the source version, and H/I the locator/URL.

| Record and cells | Source-supported value | Correct population and interpretation | Primary source |
| --- | --- | --- | --- |
| Cosmos, E2:F2 | Approximately 20,000,000 hours | Raw candidate-video collection before curation; not retained training hours. | [Cosmos v3](https://arxiv.org/html/2501.03575v3), Section 3.1; version dated 9 July 2025. |
| V-JEPA 2, E3:F3 | More than 1,000,000 hours | Action-free video pretraining pool. Images are also used but are not converted into video-hours. | [V-JEPA 2 v1](https://arxiv.org/html/2506.09985v1), Sections 1–2; 11 June 2025. |
| π0, E4:F4 | More than 10,000 hours | Robot pretraining mixture, including the contributed demonstrations and existing robot datasets; not the visual-language backbone's entire pretraining exposure. | [π0 v4](https://arxiv.org/html/2410.24164v4), Sections I, II and VII; 8 January 2026. |
| Dreamer 4 video, E5:F5 | 2,541 reported hours | Combined VPT contractor gameplay pool, with a 90/10 training/evaluation split. The source also uses rounded 2.5K/2,500 descriptions. | [Dreamer 4 v1 PDF](https://arxiv.org/pdf/2509.24527v1), Section 4, p.9; Appendix A, p.25; 29 September 2025. |
| DROID, E6:F6 | 350 reported hours | Reported demonstration-corpus scale. The source additionally releases unsuccessful trajectories excluded from its reported dataset size; 350 is not established as the duration of every released file. | [DROID v2](https://arxiv.org/html/2403.12945v2), abstract and Section III-C; 22 April 2025. |
| Dreamer 4 action labels, E7:F7 | 100 reported hours | A nested action-label ablation condition within the video pool, not an additional 100 hours and not the full successful agent's training budget. | [Dreamer 4 v1 PDF](https://arxiv.org/pdf/2509.24527v1), Section 4.3/Figure 7, p.14. |
| V-JEPA 2-AC, E8:F8 | Less than 62 hours | Filtered robot video used for action-conditioned post-training, with end-effector states and actions derived from consecutive states. It is not action-free and excludes earlier pretraining. | [V-JEPA 2 v1](https://arxiv.org/html/2506.09985v1), Section 3.1 and Appendix B.1. |

The workbook's `exact` category means a **reported point value**, not independently measured duration at unlimited precision. The final figure legend accordingly says “Reported value.” Heterogeneous populations on a common hours axis do not establish a sample-efficiency ranking.

Two source inconsistencies do not invalidate these retained values: V-JEPA 2 v1's Table 1 and Section 2.3 give different totals for one constituent video source (1.6M versus 1.4M hours), so the conservative >1M headline is retained. DROID's arXiv abstract metadata and PDF disagree on task count (84 versus 86), while agreeing on 350 hours. Neither inconsistent count was used to calculate the plotted hours.

## World-Gymnast real-robot results

The following cells are on `World-Gymnast`. Source: [World-Gymnast v1](https://arxiv.org/html/2602.02454v1), Section 4.1 and Table 1; [PDF](https://arxiv.org/pdf/2602.02454v1), pp.4–5. The arXiv submission date is 2 February 2026; the PDF's internal date is 3 February.

| Row/task | SIMPLER mean ± SE, C:D | World-Gymnast mean ± SE, F:G | Derived difference, P | Verification |
| --- | ---: | ---: | ---: | --- |
| 2: Open drawer | 34 ± 7% | 58 ± 4% | +24 percentage points | Exact match |
| 3: Close drawer | 74 ± 5% | 62 ± 6% | −12 percentage points | Exact match |
| 4: Eggplant into blue sink | 32 ± 10% | 72 ± 10% | +40 percentage points | Exact match |
| 5: Eggplant into yellow basket | 40 ± 10% | 78 ± 2% | +38 percentage points | Exact match |

The metric is real-robot task success on AutoEval after policy training. Columns H:I correctly state **10 trials per policy–task evaluation, repeated five times**. The five repeats are evaluations, not five independently trained seeds. The error entries are **standard errors**, not standard deviations or confidence intervals. The figure preserves the unfavorable close-drawer result; no new significance test or isolated causal effect is inferred.

## Paper-to-workbook matching

| Paper figure | Checks performed | Result |
| --- | --- | --- |
| Restored Figure 6, data scale | All seven labels; logarithmic scale; approximate/lower/upper-bound symbols and arrow direction; mapping by record ID despite row reordering. | All numerical values match. Original artwork is unchanged; the purple caption clarifies the DROID scope and the nested Dreamer condition/split. |
| Restored Figures 9 and 10, World-Gymnast | Eight means and eight SE entries in the plotting data; four delta labels, 0–100% axis, task identities, trial/repeat wording, and rendered plots. | All match. Both occurrences use the same unchanged original quantitative PDF; means and SE are not reinterpreted as another uncertainty measure. |
| Original draft Figure 6, p.10 | Visible numeric labels, bounds, and units compared with the workbook. | Numerical labels agree; the DROID scope was overly broad and is refined in the revision. |
| Original draft Figures 9 and 10, pp.14–15 | Both visual copies compared with the task table and protocol. | They reproduce the same comparison. Both are retained in the final surgical draft to honor the request to restore all original figures; their LaTeX labels are distinct. |

The other revised figures are conceptual diagrams or the inherited selection flow; they are not calculated from this plotting workbook. In particular, this workbook does not independently establish the PRISMA intermediate counts or a full report-level evidence map.

The workbook's stored logarithms, percentage-point differences, direction labels, and audit arithmetic are consistent with independent calculations. No cached formula errors or missing formula caches were found. The two native chart series point to the intended formula-linked ranges on `Figures`. Native Excel recalculation behavior after future edits was not tested; this is an audit of the supplied saved state and independent calculations.

## Workbook preview limitations and recommended metadata edits

The `Figures` worksheet contains **preview** bar charts. Its scale chart plots log10 thresholds without drawing bound symbols; its task chart omits SE bars. Long chart labels are crowded. These previews are numerically consistent but should not replace the publication PDF figures, which preserve bounds and uncertainty.

Recommended metadata edits for a future workbook revision:

1. Change `Verified Data Scale!C6` from “full robot-interaction dataset” to “reported DROID demonstration-corpus scale.” Its linked label on `Figures!A9` will then follow. Keep E6 = 350.
2. Record that `Verified Data Scale!E7` is a nested action-label condition within E5's pool, and that the latter has a 90/10 train/evaluation split. Do not sum 100 and 2,541.
3. Pin Cosmos, V-JEPA and Dreamer URLs to the versions recorded in column G; the version-specific links in this report provide these targets. Keep the historical 26 August 2026 audit dates and record this fresh 23 September check separately.
4. Interpret `exact` as “reported point value,” or rename that category consistently in the extraction/plotting pipeline. The numeric points require no change.

The original workbook and inherited CSV package were preserved. The manuscript's corrected wording and this dated report document the scope qualifications without altering historical records.
