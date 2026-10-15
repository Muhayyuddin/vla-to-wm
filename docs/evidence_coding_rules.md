# Evidence coding rules for the limitation-to-mechanism map (Table 3)

The unit of coding is a claim and its experimental contrast, linked to one
source version and one report. A report can contribute several contrasts and
several limitations; no paper-wide label is assigned.

## Eligibility of a comparison

A comparison enters the evidence ledger when

1. the evaluated task is robotic manipulation or, for latent-dynamics systems,
   a continuous-control domain recorded as other-domain;
2. the report identifies the baseline against which the change is measured;
3. the measured outcome maps to one of L1–L6; and
4. the compared package is described in enough detail to label the claim as
   direct, indirect, or prospective.

All comparisons that meet these criteria are retained, including mixed and
adverse outcomes. Table 3 presents, for each limitation, the entries that
measure the stated outcome most directly under a reported protocol; the
remaining entries are cited in the corresponding subsections of the paper.

## What counts as the stated outcome

| Limitation | Outcome required for a direct label |
| --- | --- |
| L1 Execution monitoring and recovery | Detection or correction after an imposed execution error: failure type, detection delay, recovery success conditional on failure, repeated ineffective actions. Aggregate task completion alone is indirect. |
| L2 Distribution shift | Performance under an explicitly declared change in layout, viewpoint, instruction, object, or embodiment. Physical transfer is recorded separately from evaluation inside a learned environment. |
| L3 Data requirements | A defined data question. A pipeline that needs no new task-specific teleoperation answers that narrow question; it does not estimate hours saved at matched performance. Passive, synthetic, and action-grounded data are recorded separately. |
| L4 Physical grounding | A physical-property or contact intervention that connects prediction to behavior. Video realism or geometry alone is indirect. |
| L5 Evaluation validity | Agreement between the proposed evaluation proxy and the intended physical reference, including ranking transfer. A direct validation can return an adverse result. |
| L6 Safety and uncertainty | Constraint violations, calibration for the relevant hazard, abstention or fallback behavior, or a stated assurance property. Task value or completion alone is not such an outcome. |
| Cost (prediction and search) | Observation-to-command latency, chunk duration, hardware, and candidate counts for the reported implementation. Recorded as a cost of predictive mechanisms, not as a seventh VLA limitation. |

## Labels

- **Direct** — the contrast or reference measures the stated outcome in the
  declared domain. It may support a package-level conclusion while leaving
  component attribution unresolved.
- **Indirect** — the argument requires transfer from another outcome, domain,
  or an untested attribution; the missing link is stated in the ledger.
- **Prospective** — the mechanism–outcome link is not tested in the cited
  experiment.
- **Outcome direction** — favorable, adverse, mixed, inconclusive, or not
  measured; recorded separately from directness. Adverse tasks and
  non-significant results are preserved as reported.
- **Baseline** — matched, partially matched, unmatched, or none, with the
  reason. A shared benchmark name does not make two results a matched
  comparison.
- **Evaluation domain** — physical robot, conventional simulation, learned
  environment, passive video, or mixed.
- **Attribution level** — component ablation, package comparison,
  observational association, reference validation, or untested hypothesis.

The ledger is `data/evidence_ledger.csv` (also `.json`). Each row carries the
source version, locator, and URL used for the label.
