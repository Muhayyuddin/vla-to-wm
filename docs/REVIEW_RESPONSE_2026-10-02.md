# Revision response — 2 October 2026

The editable manuscript incorporates the author's review comments and the subsequent approval to include Seer, Video Prediction Policy, and Unified World Models. Revised prose is marked purple. The PRISMA diagram and its caption retain black revision text. The main manuscript PDF is a **previous render**, not a verified render of this revision; see [BUILD.md](BUILD.md).

## Review population and selection flow

The authoritative [literature register](../data/VLA_WM_Literature_Register.xlsx) contains **144 included reports: 69 VLA, 42 world-model, and 33 dataset/benchmark/evaluation papers**. Each report has one primary counting category. Seer and VPP were added as VLA reports and UWM as a world-model report. Four additional methodological/contextual references support recovery and learned planning; they are recorded as background and do not increase the included total.

| Stage | Revised number | Basis |
| --- | ---: | --- |
| Database records | 2,455 | Existing author-reported discovery count |
| Other discovery | 100 | Original 97 assisted-search/citation-chasing records plus three author-supplied reports |
| Total identified | 2,555 | 2,455 + 100 |
| Duplicate records removed | 704 | Existing author-reported count |
| Screened | 1,851 | 2,555 − 704 |
| Title/abstract exclusions | 1,525 | Existing author-reported count |
| Reports assessed | 326 | 1,851 − 1,525 |
| Full-text exclusions | 182 | Author-confirmed 62 + 49 + 44 + 27 |
| Included | 144 | 326 − 182 |

The exclusion reasons are driving/navigation only (62), no action/control component (49), insufficient technical detail (44), and superseded version (27). The three additions were not retroactively described as LLM-search results. [Machine-readable counts](../data/prisma_counts.json) accompany the revised PRISMA asset.

## Changes addressing the review

| Comment | Revision and scope |
| --- | --- |
| Missing study-selection/extraction method | Added subsections describing divided reviewer responsibilities, recorded extraction fields, report deduplication, and limitations of the retained audit materials. No independent dual screening or agreement statistic is claimed. |
| Derivation of limitation categories | Described six analytical questions organized during narrative synthesis. An undocumented prespecified or independently reproduced coding process is not asserted. |
| Evidence rubric and counts | Defined direct, indirect, and prospective relationships at claim level. Adverse/mixed are outcome directions. The source-linked ledger contains 12 claim records from nine sources. The heatmap filters this to eight claims from six included papers, excluding contextual/vendor sources and deployment-cost rows. Neither is exhaustive corpus coding. |
| Physical and matched evidence | Within that selected subset, five sources contain physical-robot evaluation, one contains a matched auxiliary-prediction component ablation, and one validates rankings against a paired physical reference. Package comparisons remain distinct from component ablations. |
| Circular L1 and overlap with L2 | L1 now asks about execution monitoring and recovery after controlled failures. L2 concerns performance under declared distribution shifts. Explicit prediction is not made a prerequisite for recovery. |
| L7 deliberation cost | Removed the seventh VLA limitation and corresponding matrix row. Prediction/search cost is discussed under limitations of world models, with policy inference, action execution, and planning latency distinguished. |
| Repeated small-study caveats | Centralized the scope of WorldVLA, Cosmos Policy, World-Gymnast, and DreamGen comparisons in the evidence-map section and shortened the conclusion. |
| DreamGen attribution | Replaced the bundled GR00T N1-to-N1.5 comparison with DreamGen Table 1's task scores: 11.2 to 43.2 for novel behaviors, and 0 to 28.5 for new environments. These permit partial credit and do not quantify robot-hours replacement. The source's nearby prose/table discrepancy is retained in the ledger. |
| Selection-framework claim / Wang comparison | Softened the contribution to evaluation and deployment considerations. Table 1's marks are explicitly author-assessed scope descriptions, not quality scores; cross-family synthesis remains partial. |
| LLM-assisted discovery | Distinguished original 97 combined discovery records from the three later author-supplied inclusions. Missing model versions, query dates, separate yields, and discard logs are explicitly acknowledged. No new Scopus, Web of Science, or reproducible Google Scholar search is claimed. |
| D10 novelty | Explicitly discusses learned operators, neural/symbolic transitions, learned predicates, and Video Language Planning. The open question concerns validated interfaces and conditional assurance, not first use of learned models in planning. |
| Missing predictive policies | Added Seer and VPP to the VLA discussion and table; UWM to the world-model discussion and table; all three to the workbook and README catalogue. Their first reports predate WorldVLA. |
| Prior Information Fusion review | States the distinction between prior fusion-focused VLA organization and the present predictive-mechanism/evidence synthesis. A limited local lexical comparison is documented below. |
| Intro's LIBERO citation | Replaced the robustness-paper citation for the >97% statement with the relevant configuration-specific policy sources. |
| OpenVLA-OFT | Moved it to continuous actions in the text, tables, and diagrams; continuous L1 regression is explicitly distinguished from token generation. |
| Names and citations | Expanded Gemini Robotics 1.5, harmonized A–G labels, added Ctrl-World's missing citation, and corrected reference identities, full author metadata, URLs, and release records where primary verification supported changes. |
| Figures | Removed ancestry-implying timeline connectors; dated Cosmos 2025; aligned the paper roadmap and D1–D10 roadmap with the text; enlarged figure labels and corrected overlapping connectors. Replaced raster architecture/map assets with editable vector sources where relevant. |
| New detailed architecture request | Added representative VLA and action-conditioned world-model diagrams and explanations, including equations, training objectives, optional components, execution feedback, and alternative uses of prediction. |
| Abstract and affiliation | Abstract is approximately 201 words. Corrected Ibrar Yaqoob's name and added the supplied Charles Sturt University affiliation and a brief biography using only the supplied role/affiliation. |

## Figure numbering

The two newly requested architecture figures change downstream numbers. Stable filenames and LaTeX labels identify the assets; all manuscript references use labels.

| Current source order | Figure |
| ---: | --- |
| 1 | Timeline |
| 2 | Paper roadmap |
| 3 | PRISMA |
| 4 | VLA interface overview |
| 5 | VLA taxonomy |
| 6 | Detailed representative VLA architecture — new |
| 7 | Data-scale bubbles — previously Figure 6 |
| 8 | Control-interface comparison |
| 9 | Detailed representative world-model architecture — new |
| 10 | World-model taxonomy |
| 11 | Task-level transfer comparison — previously Figure 9 |
| 12 | Task differences — previously Figure 10 |
| 13 | Selected-evidence heatmap |
| 14 | World-model family architecture panels |
| 15 | D1–D10 research roadmap |

The previously verified numerical plot data were retained. Final placement and numbering in a complete rebuilt manuscript remain to be confirmed when the editor compiler is available.

## Similarity check and its limits

The comparison used the publicly accessible [43-page author-hosted prior review](https://iocnet.upc.edu/usuaris/jan.rosell/PDFs/2026_Information_Fusion_Multimodal_Fusion_with_Vision-Language-Action_Models_for_Robotic_Manipulation-A_Systematic_Review.pdf). Its identity was checked, but it was not verified as byte-identical to the publisher's final version. Poppler extracted its reading-order text. The check compared normalized, case-insensitive exact sequences of eight or more words, excluding current-draft figures, tables, equations, citation keys, and bibliography.

No exact eight-word sequence matches were found in Section IV or the checked main narrative. This is a limited lexical result, **not a plagiarism score or an IEEE similarity clearance**. It does not assess close paraphrase, conceptual overlap, table/figure reuse, or other publications; PDF extraction can also miss matches. The method and results are in [similarity_check.json](similarity_check.json). A publisher or institutional similarity service remains a separate check.

## IEEE Access format and remaining work

[IEEE Access's official APC guidance](https://ieeeaccess.ieee.org/about/article-processing-charges/) states no overlength charge and recommends a manuscript below 20 pages for readability. The [submission guidelines](https://ieeeaccess.ieee.org/authors/submission-guidelines/) describe the requirements for longer manuscripts and the Topical Review/Survey exception to the pre-inquiry condition. The previous 28-page render is not the length of this uncompiled revision.

The source is substantially improved but should not yet be labeled submission-ready. The following remain explicit limitations or author tasks:

- Recover historical LLM-search details and screening/coding records if available. No values or agreement statistics were invented.
- An exhaustive 144-report limitation/mechanism extraction and independent reliability check have not been completed. The new heatmap is deliberately a selected-example audit.
- Add the public repository URL; confirm the conflict-of-interest statement and all author contribution statements, including Ibrar Yaqoob's contribution.
- Obtain a successful full-manuscript build and inspect final pagination, float placement, reference formatting, and source/PDF agreement. The built-in compiler currently fails before source diagnostics with “Unable to find standard directories for platform.” Individual figure assets were compiled and visually inspected separately.
- Run the intended institutional/publisher similarity check if required; the local comparison is not a substitute for that service.

See [release_validation.json](release_validation.json) for machine-readable checks and [BUILD.md](BUILD.md) for the distinction between current sources and the previous manuscript render.
