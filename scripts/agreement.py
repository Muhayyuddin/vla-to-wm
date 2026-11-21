"""Agreement between the second coder and the register on the double-coding subsample.
Prints raw agreement and Cohen's kappa for the decision and for the primary category."""
import csv
from collections import Counter
from pathlib import Path
D = Path(__file__).resolve().parent.parent / "data"
reg = {r["record_id"]: r for r in csv.DictReader(open(D / "literature_register.csv", encoding="utf-8-sig"))}
sub = list(csv.DictReader(open(D / "double_coding_subsample.csv", encoding="utf-8-sig")))

def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")

for label, col, regcol in (("decision", "second_coder_decision", "decision"),
                           ("primary category", "second_coder_primary_category", "primary_category")):
    pairs = [(reg[r["record_id"]][regcol].strip(), r[col].strip()) for r in sub if r[col].strip()]
    if not pairs:
        print(f"{label}: no second-coder entries yet"); continue
    po, k = kappa(pairs)
    print(f"{label}: n = {len(pairs)}, agreement = {100 * po:.1f}%, Cohen's kappa = {k:.2f}")
    for a, b in pairs:
        if a != b: print("   disagreement:", a, "vs", b)
