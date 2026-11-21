"""Fig. 7 of the paper: source-reported data scales as labelled points on a
logarithmic hours axis. Every record uses the same marker; the value is encoded
once, by vertical position. Input: data/figure07_data_scale.csv."""
import csv, sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def label(v, bound):
    txt = f"{v/1e6:g}M" if v >= 1e6 else (f"{v/1000:g}k" if v >= 10000 else f"{v:,g}")
    return {"approximate": "≈", "reported_point": "", "lower_bound": ">", "upper_bound": "<"}[bound] + txt + " h"

def main(csv_path, out_stem):
    rows = {r["record_id"]: r for r in csv.DictReader(open(csv_path, encoding="utf-8-sig"))}
    order = ["cosmos_raw", "vjepa2_pretrain", "dreamer4_video", "pi0_pretrain", "droid_full", "dreamer4_actions", "vjepa2_ac"]
    names = ["Cosmos\nraw collection", "V-JEPA 2\npretraining", "Dreamer 4\nvideo pool", "$\\pi_0$\npretraining",
             "DROID\ncorpus", "Dreamer 4\nlabel ablation", "V-JEPA 2-AC\npost-training"]
    plt.rcParams.update({"font.family": "serif", "font.size": 8, "mathtext.fontset": "cm"})
    fig, ax = plt.subplots(figsize=(7.16, 2.7))
    for i, rid in enumerate(order):
        v = float(rows[rid]["reported_hours"])
        ax.plot(i, v, "o", ms=5.5, color="#30383D")
        ax.annotate(label(v, rows[rid]["bound_type"]), (i, v), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8)
    ax.set_yscale("log"); ax.set_ylim(10, 3e8); ax.set_xlim(-0.6, 6.6)
    ax.set_xticks(range(7)); ax.set_xticklabels(names, fontsize=7.5)
    ax.set_ylabel("Source-reported hours (log scale)")
    ax.grid(axis="y", color="#E2E5E6", lw=0.6); ax.set_axisbelow(True)
    for x in (2.5, 4.5): ax.axvline(x, color="#C6CBCF", lw=0.6)
    for x, h in ((1, "Video sources"), (3.5, "Robot data"), (5.5, "Adaptation / ablation")):
        ax.text(x, 1.2e8, h, ha="center", va="center", fontsize=8, fontweight="bold")
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(out_stem + ".pdf"); fig.savefig(out_stem + ".png", dpi=300)

if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    main(sys.argv[1] if len(sys.argv) > 1 else str(here.parent / "data" / "figure07_data_scale.csv"),
         sys.argv[2] if len(sys.argv) > 2 else str(here.parent / "figures" / "figure07_data_scale"))
