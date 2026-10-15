# From Reactive Vision-Language-Action Policies to Predictive World Models: A Review for Robotic Manipulation

Supplementary materials for the review article of the same title (Muhayy Ud
Din, Ahsan B. Bakht, Ibrar Yaqoob, and Irfan Hussain; submitted to IEEE
Access). The repository holds the data that the paper's methodology section,
evidence map, and quantitative figures are built from.

## Contents

| Path | What it is | Where the paper uses it |
| --- | --- | --- |
| `data/literature_register.csv` / `.xlsx` | The included-report register: 214 source records with the author decision (Include / Background / Exclude), primary category, canonical identifier, primary URL, citation keys, and decision reason. The 144 `Include` rows are the corpus: 69 VLA, 42 world-model, and 33 dataset/benchmark/evaluation reports. | Sec. III-C, Fig. 3 |
| `data/screening_counts.json` | The identification, screening, and eligibility counts of the PRISMA-style flow. | Fig. 3 |
| `data/search_log.csv` | Search sources with their discovery route (database search, curated list, citation chasing, language-model-assisted discovery, targeted search), the records retrieved by each route before deduplication (2,455 from databases and indexed proceedings; 100 from other discovery), and the targeted supplementary searches with the primary records they led to. | Sec. III-B |
| `data/evidence_ledger.csv` / `.json` | The claim-level evidence ledger: one row per limitation-to-mechanism comparison with directness, outcome direction, baseline, evaluation domain, attribution level, source version, and locator. | Table 3, Sec. VI-H |
| `data/companion_workbook.xlsx` | One workbook with the corpus, the evidence ledger, the benchmark landscape (Table 6), the LIBERO results (Table 7), the training corpora with source versions (Table 9), the screening counts, and the data behind Figs. 7 and 12. Built by `scripts/build_workbook.py`. | Tables 6, 7, 9; Figs. 3, 7, 12 |
| `data/figure07_data_scale.csv`, `data/figure12_world_gymnast.csv`, `data/figure_inputs.json`, `data/figure07_bubble_encoding.json` | Source-linked values and encodings for the two data figures. | Figs. 7, 12 |
| `figures/` | The two data figures as PDF, SVG, and PNG, regenerated from the files above. | Figs. 7, 12 |
| `scripts/` | `generate_figure07.py`, `generate_figure12.py`, and `build_workbook.py`. | — |
| `docs/evidence_coding_rules.md` | The eligibility criteria and label definitions used for the evidence ledger. | Sec. III-E, VI-H |

## Corpus

The register counts one report per source: versions of the same work are
consolidated under a canonical identifier, and hybrid contributions are
assigned one primary category with secondary roles retained. Background
rows are references cited for context (historical precursors, surveys,
methods outside the manipulation scope) and are not part of the 144 included
reports. Exclude rows are records assessed at full text and excluded.

Screening flow: 2,455 database and indexed-proceedings records plus 100
records from other discovery; 704 duplicates removed; 1,851 screened at title
and abstract; 326 assessed at full text; 182 excluded (62 driving or
navigation only, 49 without an action or control component, 44 with
insufficient technical detail, 27 superseded versions); 144 included.

## Data figures

**Fig. 7 — source-reported data scales.** Seven records on a logarithmic hours
axis. Bound types (`approximate`, `lower_bound`, `upper_bound`,
`reported_point`) and the reporting scope of each value are kept with the
number; the records describe different populations and stages of learning and
are not comparable as supervision budgets. Bubble area increases linearly with
the logarithm of the value or bound (radius 4–22 pt); areas are not
proportional to raw hours.

**Fig. 12 — World-Gymnast versus SIMPLER.** Real-robot task success (mean ±
standard error, 10 trials per evaluation repeated five times) for four tasks,
from World-Gymnast Table 1. Differences in percentage points: +24 (open
drawer), −12 (close drawer), +40 (eggplant to blue sink), +38 (eggplant to
yellow basket). No confidence interval or significance test is inferred.

## Reproduce

```bash
python -m pip install -r requirements.txt
python scripts/generate_figure07.py      # figures/figure07_data_scale_bubbles.{pdf,svg,png}
python scripts/generate_figure12.py      # figures/figure12_world_gymnast_tasks.{pdf,svg,png}
python scripts/build_workbook.py         # data/companion_workbook.xlsx
```

PNG previews require Poppler (`pdftoppm`); the PDF and SVG are written without it.

## License

The register, ledger, workbook, figure data, scripts, and documentation in this repository are released under the Creative Commons Attribution 4.0 International license (`LICENSE`). The papers, datasets, and models they describe remain under their own terms.

## Citing

Please cite the primary papers for any model, dataset, or result taken from
these files; each row carries its primary URL. For the synthesis, cite the
review article; the bibliographic record will be added here on publication
(see `CITATION.cff`).
