"""Source-linked selected-evidence heatmap; vector PDF/SVG with embedded fonts.

Uses ReportLab, the same vector chart stack as companion Figures 6 and 10.
Run from any directory. Reads the original ledger without modifying it.
"""
from pathlib import Path
import csv
import json
import shutil
import subprocess
from collections import defaultdict
from reportlab.graphics.shapes import Drawing, Rect, String, Line, STATE_DEFAULTS
from reportlab.graphics import renderPDF, renderSVG
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import reportlab

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT/'data'
OUT = ROOT/'figures'
INK = '#242424'
MUTED = '#616161'
GRID = '#D7D7D7'
COLORS = {0: '#FAFAFA', 1: '#EAE6EF', 2: '#CFC1DF'}

def register_fonts():
    bundled = Path(reportlab.__file__).parent/'fonts'
    choices = [(Path('C:/Windows/Fonts/arial.ttf'),Path('C:/Windows/Fonts/arialbd.ttf')),
               (Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')),
               (bundled/'Vera.ttf',bundled/'VeraBd.ttf')]
    for plain,bold in choices:
        if plain.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont('Evidence',str(plain)))
            pdfmetrics.registerFont(TTFont('Evidence-Bold',str(bold)))
            return
    raise RuntimeError('Configure a TrueType font pair in register_fonts().')

def text(d,x,y,value,size=8.5,bold=False,anchor='start',color=INK):
    d.add(String(x,y,value,fontName='Evidence-Bold' if bold else 'Evidence',fontSize=size,
                 textAnchor=anchor,fillColor=HexColor(color)))

def write_csv(path,rows,fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    rows=list(csv.DictReader((HERE/'selected_evidence_ledger.csv').open(encoding='utf-8-sig')))
    selected=[r for r in rows if r['author_decision_in_register']=='Include' and r['limitation'] in {f'L{i}' for i in range(1,7)}]
    assert {r['ledger_id'] for r in selected}=={'E01','E02','E03','E04','E05','E07','E09','E10'}
    study_ids={r['study_id'] for r in selected}
    assert len(study_ids)==6

    # New explicit design codes are attached only to the filtered plotting copy.
    # "Matched" does not mean every direct result is a component ablation.
    designs={
        'E01':('Matched component ablation','Yes','No'),
        'E02':('Partially matched package comparison','No','No'),
        'E03':('Partially matched package comparison','No','No'),
        'E04':('Training augmentation comparison in learned environment','No','No'),
        'E05':('Task-data pipeline comparison','No','No'),
        'E07':('No matched data-budget comparator','No','No'),
        'E09':('Paired evaluator validation against physical reference','No','Yes'),
        'E10':('No safety-specific comparator','No','No'),
    }
    for r in selected:
        design,component,reference=designs[r['ledger_id']]
        r.update(comparison_design=design,matched_component_ablation=component,paired_physical_reference=reference)
    write_csv(HERE/'selected_evidence_plotted_rows.csv',selected,list(selected[0]))

    matrices={}
    cell_records=[]
    for panel in ['Direct','Indirect','Prospective']:
        for limitation in [f'L{i}' for i in range(1,7)]:
            for family in [f'WM{i}' for i in range(1,7)]:
                rs=[r for r in selected if r['directness_for_limitation']==panel and r['limitation']==limitation and family in r['wm_family'].split(';')]
                ids=sorted({r['study_id'] for r in rs})
                key=(panel,limitation,family)
                matrices[key]=len(ids)
                cell_records.append({'panel':panel,'limitation':limitation,'wm_family':family,'unique_source_count':len(ids),
                                     'study_ids':';'.join(ids),'ledger_ids':';'.join(r['ledger_id'] for r in rs),
                                     'adverse':any(r['outcome_direction'].startswith('Adverse') for r in rs),
                                     'mixed':any(r['outcome_direction']=='Mixed' for r in rs)})
    write_csv(HERE/'selected_evidence_heatmap_cells.csv',cell_records,list(cell_records[0]))

    empirical=[r for r in selected if r['directness_for_limitation']!='Prospective']
    physical={r['study_id'] for r in empirical if r['physical_robot_evaluation']=='Yes'}
    ablations={r['study_id'] for r in empirical if r['matched_component_ablation']=='Yes'}
    references={r['study_id'] for r in empirical if r['paired_physical_reference']=='Yes'}
    stats={'audit_date':'2026-10-02','selected_claim_rows':len(selected),'selected_unique_included_papers':len(study_ids),
           'empirical_selected_sources_with_physical_robot_evaluation':len(physical),
           'matched_component_ablation_sources':len(ablations),'paired_physical_reference_validation_sources':len(references),
           'physical_robot_study_ids':sorted(physical),'matched_component_ablation_study_ids':sorted(ablations),
           'paired_physical_reference_study_ids':sorted(references),
           'panel_unique_sources':{p:len({r['study_id'] for r in selected if r['directness_for_limitation']==p}) for p in ['Direct','Indirect','Prospective']},
           'denominator':'Six selected included sources; not the144-paper corpus',
           'zero_interpretation':'No source coded in this selected subset; not absence of evidence',
           'overlap':'A source may contribute to several cells and panels; counts must not be summed as independent papers',
           'noncomponent_designs':'Package/data comparisons and evaluator validation are not labeled matched component ablations'}
    (HERE/'selected_evidence_heatmap_summary.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
    assert len(physical)==5 and len(ablations)==1 and len(references)==1

    register_fonts()
    STATE_DEFAULTS['fontName']='Evidence'
    d=Drawing(7.16*72,4.56*72)
    text(d,8,310,'Selected source-linked evidence',size=11.5,bold=True)
    text(d,8,295,'6 included papers · 8 claim records · revision audit: 2 October 2026',size=8.5,color=MUTED)
    left,top,cw,ch,gap=128,250,19,24,9
    labels=[('L1','Execution monitoring','and recovery'),('L2','Distribution shift',''),('L3','Data requirements',''),
            ('L4','Physical grounding',''),('L5','Evaluation validity',''),('L6','Safety and uncertainty','')]
    for i,(key,a,b) in enumerate(labels):
        cy=top-(i+.5)*ch
        text(d,8,cy-3,key,size=8.5,bold=True)
        if b:
            text(d,29,cy+2,a,size=8.1);text(d,29,cy-8,b,size=8.1)
        else:text(d,29,cy-3,a,size=8.1)

    for p,panel in enumerate(['Direct','Indirect','Prospective']):
        x0=left+p*(6*cw+gap)
        np=stats['panel_unique_sources'][panel]
        noun='paper' if np==1 else 'papers'
        text(d,x0+3*cw,273,f'{panel} ({np} {noun})',size=9,bold=True,anchor='middle')
        for j in range(6):text(d,x0+(j+.5)*cw,258,f'WM{j+1}',size=7,anchor='middle',color=MUTED)
        for i in range(6):
            for j in range(6):
                x,y=x0+j*cw,top-(i+1)*ch
                n=matrices[(panel,f'L{i+1}',f'WM{j+1}')]
                d.add(Rect(x,y,cw,ch,fillColor=HexColor(COLORS[n]),strokeColor=HexColor(GRID),strokeWidth=.4))
                adverse=(panel=='Direct' and i==4 and j==4)
                mixed=(panel=='Direct' and i==1 and j==4)
                if adverse:
                    # Short diagonal corner strokes signal adverse direction without obscuring the count.
                    for k in range(4):
                        xx=x+1+k*4
                        d.add(Line(xx,y+1,min(xx+7,x+cw-1),y+min(8,cw-xx+x-1),strokeColor=HexColor('#7B648D'),strokeWidth=.45))
                text(d,x+cw/2,y+ch/2-3,str(n),size=9 if n else 7.7,bold=bool(n),anchor='middle',color=INK if n else '#A6A6A6')
                if mixed:text(d,x+cw-2,y+ch-6,'m',size=5.2,anchor='end',color=MUTED)

    text(d,8,89,'Cells count distinct papers; papers can appear in several cells or panels.',size=8,color=MUTED)
    text(d,8,76,'0 = no source coded in this subset. Hatched cell: adverse; m: mixed task outcomes.',size=8,color=MUTED)
    text(d,8,60,'Selected sources: 5/6 include physical evaluation; 1 component ablation; 1 paired rank validation.',size=8)
    text(d,8,41,'WM1 latent dynamics · WM2 generative video · WM3 latent prediction',size=7.8,color=MUTED)
    text(d,8,28,'WM4 physical state · WM5 learned environments · WM6 world–action models',size=7.8,color=MUTED)
    text(d,8,10,'This selected audit does not estimate evidence prevalence across the 144-paper corpus.',size=8,bold=True)
    stem=OUT/'selected-evidence-heatmap'
    renderPDF.drawToFile(d,str(stem.with_suffix('.pdf')),initialFontName='Evidence')
    renderSVG.drawToFile(d,str(stem.with_suffix('.svg')))
    shutil.copy2(stem.with_suffix('.pdf'),ROOT/'paper/figures/selected-evidence-heatmap.pdf')
    tool=shutil.which('pdftoppm')
    if not tool:raise RuntimeError('PDF saved; pdftoppm is required for PNG verification.')
    subprocess.run([tool,'-singlefile','-r','300','-png',str(stem.with_suffix('.pdf')),str(stem)],check=True,capture_output=True,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    print(json.dumps(stats,indent=2))

if __name__=='__main__':main()
