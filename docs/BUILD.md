# Build and reproduce the companion materials

## Source and PDF status

The bundled [paper/manuscript.pdf](../paper/manuscript.pdf) is the **PREVIOUS RENDER**, built on 1 October 2026 at 13:51. It does **not** contain the 2 October revision. Use the [latest LaTeX source](../paper/manuscript.tex), [bibliography](../paper/references.bib) and current standalone figure assets for the revision. Do not describe the old PDF as the current or final manuscript.

The source revision uses the author-confirmed **144-report corpus: 69 VLA, 42 world-model and 33 dataset/benchmark/evaluation reports**. It distinguishes six VLA limitations, treats execution monitoring and recovery as L1, and discusses prediction/search cost under predictive-system limitations in Sec. VI-I. Evidence directness, outcome direction and component attribution are separate dimensions. The selected-example evidence heatmap concerns selected examples rather than an exhaustive corpus-wide evidence count.

The last reported built-in editor compilation failed with **“Unable to find standard directories for platform”**. A successful current main-manuscript build has not yet been verified. The ten revised or added standalone diagrams compiled successfully and were visually checked; this does not establish that the full manuscript has passed compilation or final page-layout review.

## Compile the manuscript

Use an existing TeX Live or MiKTeX installation with `latexmk`, the supplied IEEE class, TikZ/PGF and the packages imported by the manuscript.

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
```

The result is `paper/build/manuscript.pdf`. Inspect the full PDF for figure placement, legible text, resolved citations/references and the current 144-report flow before copying it to `paper/manuscript.pdf`. Without `latexmk`, run `pdflatex`, `bibtex`, `pdflatex` and `pdflatex` from `paper/`. An earlier build reported inherited font-map and layout warnings; historical checks do not validate the revised source.

## Editable diagram assets

| Diagram | Editable source under `paper/tkz/` | Manuscript PDF input under `paper/figures/` |
| --- | --- | --- |
| Chronology | `timeline.tex` | `timeline.pdf` |
| Paper organization | `paper-roadmap.tex` | `paper-roadmap.pdf` |
| Screening flow | `prisma.tex` | `prisma.pdf` |
| VLA interface | `vla-anatomy.tex` | `vla-anatomy.pdf` |
| VLA taxonomy | `vla-taxonomy.tex` | `vla-taxonomy.pdf` |
| Detailed VLA architecture | `vla-detailed-architecture.tex` | `vla-detailed-architecture.pdf` |
| Control interfaces | `contrast.tex` | `contrast.pdf` |
| Detailed world-model architecture | `world-model-detailed-architecture.tex` | `world-model-detailed-architecture.pdf` |
| World-model taxonomy | `wm-taxonomy.tex` | `wm-taxonomy.pdf` |
| World-model architectures | `wm-architectures.tex` | `wm-architectures.pdf` |
| Research directions | `roadmap.tex` | `roadmap.pdf` |

From the repository root, `bash paper/tkz/build.sh` rebuilds the standalone TikZ sources and copies their PDFs into the manuscript asset folder. This also rebuilds PRISMA, so inspect its current count labels after any source change. On systems without Bash, compile a source with `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=<build-directory> paper/tkz/<name>.tex`, then inspect and copy the PDF to `paper/figures/`.

The ten revised or added diagrams retain the restrained palette and use embedded vector text. The paper-organization diagram uses 8.5–9 pt Times and the other diagrams use 8 pt body text, with a 7.5 pt candidate-action annotation in the control-interface diagram. The two new detailed architecture diagrams are 171.4 mm wide and use 8 pt body text; their heights are 97.4 mm (VLA) and 119.4 mm (world model). They preserve separate training and deployment/prediction panels. Avoid unnecessary downscaling. The chronology diagram uses first-public-report years, including preprints, and has no ancestry arrows. The paper-organization and world-model-family architecture diagrams replace raster inputs with native PDF diagrams; the old `structure.png` and `image (27).png` are preserved historical assets. The research-roadmap numbers and headings match D1–D10 in Section VIII. The selected-example evidence display must retain its selection and coding qualifications; it is not a full-corpus prevalence plot.

## Selected-example evidence heatmap

The [heatmap script](../scripts/generate_selected_evidence_heatmap.py) reads the [claim-level CSV ledger](../data/selected_evidence_ledger.csv) and writes vector PDF/SVG output using ReportLab. Run `python scripts/generate_selected_evidence_heatmap.py` from the repository root after installing `requirements.txt`; PNG rendering requires Poppler. Inspect the generated figure and synchronized manuscript copy before rebuilding the paper.

The [JSON ledger](../data/selected_evidence_ledger.json), [scope notes](../data/selected_evidence_scope.json), [plotted rows](../data/selected_evidence_plotted_rows.csv) and [cell values](../data/selected_evidence_heatmap_cells.csv) preserve the extraction and plotting interpretation. The scope notes retain the initial 207-record/141-included extraction snapshot explicitly as history. The current register has 214 records and 144 included reports; neither count is a denominator for this selected-example plot. Repeated claims from a paper must not be treated as independent studies. The [review response](REVIEW_RESPONSE_2026-10-02.md) explains the revision.

These heatmap and PRISMA assets are additional to the ten independently compiled architecture/taxonomy/roadmap diagrams.

## Screening-flow reconciliation

The author-confirmed revised arithmetic is:

```text
2,455 database/indexed-proceedings + 100 supplementary = 2,555 identified
100 supplementary = 97 original assisted/citation records + 3 author-supplied papers
2,555 - 704 duplicates = 1,851 screened
1,851 - 1,525 title/abstract exclusions = 326 sought and assessed
62 + 49 + 44 + 27 = 182 full-text exclusions
326 - 182 = 144 included = 69 VLA + 42 world-model + 33 dataset/benchmark/evaluation
```

The four full-text reasons are navigation-only, lack of action/control relevance, insufficient technical detail and superseded reports, respectively. The earlier 21-exclusion discrepancy is resolved in these confirmed totals. The six-not-retrieved and temporary search-flow boxes remain absent. These are author-confirmed totals; arithmetic alone does not recover a record-level exclusion log or establish independent screening.

After rebuilding Figure 3, keep `paper/figures/prisma.pdf`, `figures/figure_03_selection.pdf` and `figures/figure_03_selection.png` synchronized. Render a PNG with Poppler, inspect it, and then compile the main paper. The older embedded Figure 3 remains in the previous main PDF until that PDF is replaced after a verified build.

## Reproduce the data-scale and task-comparison plots

From the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/generate_figure_06.py
python scripts/generate_figure_10.py
```

Both scripts read [verified_plot_inputs.json](../data/verified_plot_inputs.json) and write vector PDF/SVG files to `figures/`. PNG export also requires Poppler’s `pdftoppm` on `PATH`. Fonts are selected from Windows Arial, Linux DejaVu Sans or ReportLab’s bundled Vera. Inspect regenerated output before copying the corresponding PDF into `paper/figures/`. The task-comparison plot (`figure_09_task_slopes`) is supplied as editable SVG and vector PDF; its means and standard errors are also in the JSON/CSV and workbook.

The data-scale plot (`figure_06_data_scale_bubbles`) retains a distinct light-colored circle for each plotted record, with no bottom row of size-key circles. Its y coordinate is logarithmic in reported hours. For the current range, bubble area is:

```text
A(h) = pi * [4^2 + (22^2 - 4^2) * log10(h/62) / log10(20000000/62)]
```

Radii range from 4 to 22 points. Area ratios are not raw-hour ratios. Approximation and bound symbols remain in the value labels; a bound is plotted and sized at its reported threshold. The script derives the range from the inputs, so inspect sizes and update the explanation if records change. The current mapping is recorded in [bubble_encoding.json](../data/bubble_encoding.json).

The task-difference plot (`figure_10_task_differences`) subtracts SIMPLER’s reported mean from World-Gymnast’s mean. It does not calculate a confidence interval or standard error for the difference. The task-comparison plot presents the original marginal standard errors. These are complementary views of one experiment, not independent replications.

## Data and provenance

- [Original plotting workbook](../data/VLA_WM_verified_data_and_plots.xlsx): quantitative tabs and preserved historical citation registers.
- [Finalized literature register](../data/VLA_WM_Literature_Register.xlsx) and [CSV](../data/literature_register.csv): 214 source records with 144 `Include`, 60 `Background`, 10 `Exclude` and no pending author decisions. Included primary categories are 69 VLA, 42 world-model and 33 dataset/benchmark/evaluation. The 12 historical sheets are preserved. Seer, VPP and UWM were added as included reports; four additional contextual citations are Background records.
- [Latest cited-reference CSV](../data/current_cited_references_2026-10-02.csv): the current manuscript citation inventory; distinct from corpus membership.
- [Historical current-references CSV](../data/current_references.csv): the preserved 179-source citation snapshot, not a current inclusion ledger.
- [Scale records](../data/verified_data_scale.csv) and [World-Gymnast records](../data/verified_world_gymnast_real_robot.csv): plotted quantities, bounds, uncertainty interpretation and source locators.
- [Historical numeric audit](Plot_Data_Validation.md), [historical register notes](workbook_release_notes.md) and [historical workbook validation](workbook_validation.json): provenance records, whose earlier corpus totals and build statuses do not override the current register or this revision’s source/PDF status.

The workbook’s historical labels, formulas, charts and metadata are preserved for provenance. They are not all revalidated by this revision. Reading-guide rows can denote families, variants and components and can overlap; they must not be counted as included reports. The table-coverage sheet preserves an earlier 23-report citation gap as a historical audit, not a timeless claim about the current manuscript.

The current [release-validation record](release_validation.json) records the latest package checks; the separately dated historical workbook records retain earlier states.

## Release metadata

Add the actual public repository URL and final publication metadata when available. Retain the previous-PDF label until a successful current build has passed visual review. Maintain source versions, stable identifiers and explicit author decisions when adding later reports, and update the flow arithmetic and figures together. Original papers, code, datasets and model weights retain their own terms; this package does not assign a license to them.
