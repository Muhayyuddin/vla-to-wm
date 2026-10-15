"""Figure 12 of the paper: World-Gymnast versus SIMPLER real-robot task success.

Four side-by-side panels, one per task, on a shared 0-100% success axis.
Each panel shows the source-reported mean +/- standard error for the policy
trained in SIMPLER (open square) and in the World-Gymnast learned environment
(filled circle); the segment joins the two means only. Values come from
data/figure_inputs.json (World-Gymnast, arXiv:2602.02454v1, Table 1).
"""
from pathlib import Path
import argparse, json, subprocess, shutil
from reportlab.graphics.shapes import Drawing, Rect, Circle
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib.colors import HexColor
from generate_figure07 import fonts, text, line, INK, GREY, GRID

HERE = Path(__file__).resolve().parent
STEM = 'figure12_world_gymnast_tasks'
TEAL = '#2A7F7F'; SLATE = '#59666E'
WIDTH = 7.16 * 72; HEIGHT = 3.0 * 72

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', type=Path, default=HERE.parent / 'data/figure_inputs.json')
    ap.add_argument('--out', type=Path, default=HERE.parent / 'figures')
    args = ap.parse_args(); fonts()
    recs = json.loads(args.data.read_text(encoding='utf-8'))['figure12']['records']
    titles = ['Open drawer', 'Close drawer', 'Eggplant to\nblue sink', 'Eggplant to\nyellow basket']
    d = Drawing(WIDTH, HEIGHT)
    left, right, bottom, top = 58, 500, 44, 170
    pw = (right - left) / 4
    ymap = lambda v: bottom + v / 100 * (top - bottom)
    text(d, 8, HEIGHT - 16, 'Real-robot task success (%)', size=9, bold=True)
    text(d, WIDTH - 8, HEIGHT - 16, 'Point labels: mean ± SE', size=8, color=GREY, anchor='end')
    for v in (0, 50, 100):
        line(d, left, ymap(v), right, ymap(v)); text(d, left - 6, ymap(v) - 3, str(v), size=8.5, anchor='end')
    for i, r in enumerate(recs):
        x0 = left + i * pw; xs, xw = x0 + pw * 0.3, x0 + pw * 0.7
        assert r['world_gymnast_mean_pct'] - r['simpler_mean_pct'] == r['difference_pp']
        tl = titles[i].split('\n')
        for j, t in enumerate(tl):
            text(d, x0 + pw / 2, HEIGHT - 38 - j * 10, (f'({"abcd"[i]})  ' if j == 0 else '') + t, size=8.5, bold=True, anchor='middle')
        sm, se = r['simpler_mean_pct'], r['simpler_se_pct']; wm, we = r['world_gymnast_mean_pct'], r['world_gymnast_se_pct']
        line(d, xs, ymap(sm), xw, ymap(wm), color='#9DB7B7', width=1.2)
        for x, m, e in ((xs, sm, se), (xw, wm, we)):
            line(d, x, ymap(m - e), x, ymap(m + e), color=INK, width=0.8)
            line(d, x - 3, ymap(m - e), x + 3, ymap(m - e), color=INK, width=0.8)
            line(d, x - 3, ymap(m + e), x + 3, ymap(m + e), color=INK, width=0.8)
        d.add(Rect(xs - 3.5, ymap(sm) - 3.5, 7, 7, fillColor=HexColor('#FFFFFF'), strokeColor=HexColor(SLATE), strokeWidth=1))
        d.add(Circle(xw, ymap(wm), 3.8, fillColor=HexColor(TEAL), strokeColor=HexColor(TEAL)))
        text(d, xs, ymap(sm - se) - 11, f'{sm} ± {se}', size=8, bold=True, color=SLATE, anchor='middle')
        text(d, xw, ymap(wm + we) + 5, f'{wm} ± {we}', size=8, bold=True, color=TEAL, anchor='middle')
        text(d, xs, bottom - 14, 'SIMPLER', size=7.8, color=GREY, anchor='middle')
        text(d, xw, bottom - 14, 'World-', size=7.8, color=GREY, anchor='middle')
        text(d, xw, bottom - 23, 'Gymnast', size=7.8, color=GREY, anchor='middle')
        if i: line(d, x0, bottom - 26, x0, top + 4, color='#D5D9DB', width=0.6)
    args.out.mkdir(parents=True, exist_ok=True)
    renderPDF.drawToFile(d, str(args.out / f'{STEM}.pdf')); renderSVG.drawToFile(d, str(args.out / f'{STEM}.svg'))
    if shutil.which('pdftoppm'):
        subprocess.run(['pdftoppm', '-singlefile', '-r', '400', '-png', str(args.out / f'{STEM}.pdf'), str(args.out / STEM)], check=True, capture_output=True)
    print('Saved Figure 12 to ' + str(args.out))

if __name__ == '__main__':
    main()
