# Companion package — 2 October 2026

This revision supplies updated manuscript source and bibliography, the author-confirmed 144-report register, revised vector diagrams and a source-linked reading guide. **The bundled `paper/manuscript.pdf` is still the PREVIOUS RENDER from 1 October 2026 at 13:51. It does not contain this revision.** A current complete PDF has not yet passed compilation and visual verification; the last reported built-in editor failure was “Unable to find standard directories for platform”. See [BUILD.md](BUILD.md).

See the [review-response record](REVIEW_RESPONSE_2026-10-02.md) for the detailed revision account. The [selected-evidence script](../scripts/generate_selected_evidence_heatmap.py), [ledger](../data/selected_evidence_ledger.csv) and [scope notes](../data/selected_evidence_scope.json) make the heatmap reproducible. The ten compiled diagrams are additional to PRISMA and this selected-example display.

## Current corpus and screening flow

- **144 included reports:** 69 VLA, 42 world-model and 33 dataset/benchmark/evaluation. The register has 214 source records: 144 `Include`, 60 `Background`, 10 `Exclude` and zero pending author decisions.
- Four additional contextual citations are recorded as `Background`, bringing that category to 60 without changing the included-report numerator. The [latest cited-reference export](../data/current_cited_references_2026-10-02.csv) records current citations separately from the historical 179-source snapshot.
- **Three author-supplied additions:** [Seer (2024)](https://arxiv.org/abs/2412.15109) and [Video Prediction Policy (2024)](https://arxiv.org/abs/2412.14803) are counted under VLA; [Unified World Models (2025)](https://arxiv.org/abs/2504.02792) is counted under world models. They are reports, not extra counts for each role a model can serve.
- **Reconciled author-confirmed flow:** 2,455 database/indexed-proceedings records plus 100 supplementary records, less 704 duplicates, gives 1,851 screened. The supplementary 100 comprises the original 97 assisted/citation-discovery records and 3 author-supplied papers. Excluding 1,525 at title/abstract leaves 326 sought and assessed; full-text reasons total 62 + 49 + 44 + 27 = 182; 326 − 182 = 144.
- The earlier **21-exclusion discrepancy is resolved** by the confirmed reason totals. Arithmetic reconciliation does not reconstruct the original per-record screening log or establish independent dual screening. The removed non-retrieval and temporary pending boxes are not reinstated.

## Scientific and presentation changes

- Six VLA limitations are used. L1 concerns execution monitoring and recovery, rather than treating the lack of a world model as a failure outcome. Prediction/search cost is discussed under predictive-system limitations in Sec. VI-I and direction D8, not as L7.
- Evidence directness, outcome direction and component attribution are distinguished. Adverse findings can be direct; package-level completion gains do not by themselves demonstrate a specific recovery mechanism. The evidence figure summarizes selected source-linked examples and does not claim corpus-wide prevalence.
- The README retains seven VLA taxonomy groups A–G, six predictive-system families and the ten numbered research directions. Its catalogue has 74 policy, 55 world-model/predictive-system and 31 related-method rows. These overlap and are not counts of included reports.
- Bibliographic corrections and new primary references are supplied in `paper/references.bib`; historical citation snapshots remain preserved separately.

## Figure changes

Diagram titles and asset names are used below because the two added architectures change the automatically assigned figure numbers.

- **Chronology (`timeline`):** independently dated chronological landmarks without ancestry arrows; Cosmos is 2025. Dates consistently denote the first public report, which can precede a venue publication.
- **Paper organization (`paper-roadmap`):** native five-chevron paper roadmap in `paper-roadmap.tex` / `paper-roadmap.pdf`, replacing the raster input. It shows L1–L6, the correct section roles and D1–D10 without T/R/K/P shorthand.
- **VLA interface and taxonomy (`vla-anatomy`, `vla-taxonomy`):** larger readable labels, full Gemini Robotics 1.5 name, continuous regression included in B, and OpenVLA-OFT moved from A to B. The taxonomy uses exact A–G group names, separated connectors, and labels FAST as a tokenizer. SayCan and navigation-only Mobility-VLA are no longer VLA exemplars in that diagram.
- **Detailed representative architectures:** `vla-detailed-architecture` separates demonstration training from the observation-to-action loop and shows token, regression and diffusion/flow heads as alternatives. `world-model-detailed-architecture` distinguishes transition training, action-conditioned prediction and goal-based candidate scoring, with optional output heads. Both are editable TikZ/PDF diagrams with 8 pt body text.
- **Control interfaces (`contrast`):** non-overlapping labels and candidate-action feedback, with architecture-dependent optional outputs and qualified deployment-cost wording.
- **World-model taxonomy (`wm-taxonomy`):** readable vector family cards with functional descriptions; no L7 or unsupported limitation-remedy implication.
- **Selected-example evidence heatmap:** selected-example evidence display; it must not be read as an exhaustive coding of all 144 reports or as proof of absent evidence in unfilled cells.
- **World-model-family architectures (`wm-architectures`):** native four-panel `wm-architectures.tex` / `wm-architectures.pdf` replaces `image (27).png`. It uses consistent fonts, correct Cosmos Policy spelling and model-specific conditioning instead of a universal tokenizer compression claim.
- **Research roadmap (`roadmap`):** exact D1–D10 numbering and five requested thematic groups, without unsupported maturity/dependency arrows.
- **Data-scale and task-comparison plots:** plotting values, bounds and uncertainty conventions are unchanged. The data-scale plot (`figure_06_data_scale_bubbles`) retains distinct pale circles and no bottom size-key row.

The ten revised or added diagrams compiled independently without errors or font/overfull warnings and were visually checked. Body fonts are 8 pt Times (8.5–9 pt in the paper-organization diagram), with a 7.5 pt candidate-action annotation in the control-interface diagram. This is standalone-asset validation, not verification of the complete manuscript PDF. Original raster files remain unchanged as historical assets.

## Historical records and release status

The 12 earlier workbook sheets remain preserved. `Current References` retains its 179-source snapshot and `Cited Papers` its earlier 175-row snapshot, including historical Pending values. These do not override finalized decisions in `Literature Register`. `Table Coverage` retains the earlier citation-mapping audit, including 23 then-uncited included reports; it is historical rather than a claim of current omissions.

The [historical workbook validation](workbook_validation.json), [dated register notes](workbook_release_notes.md) and [quantitative audit](Plot_Data_Validation.md) document prior states. Their earlier totals, hashes or PDF status should not be interpreted as this revision’s current verification. The [current release-validation record](release_validation.json) is maintained separately for the latest package checks. Current corpus membership is given by the register; current source/PDF status is stated above and in [BUILD.md](BUILD.md).

Rebuild the main paper, check all updated figures and references, and replace `paper/manuscript.pdf` only after that validation. Add the real repository URL and final publication metadata when available. This package does not claim final publication or that a repository has already been made public.
