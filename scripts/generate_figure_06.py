"""Figure 6: verified data scales, with light-filled, log-area-scaled bubbles.

The y coordinate is logarithmic in reported hours. Circle area is affine in
log10(hours), between radii of 4 and 22 points for the smallest and largest
reported values/thresholds. Circle areas are NOT proportional to raw hours.
"""
from pathlib import Path
import argparse,json,math,subprocess,shutil
from reportlab.graphics.shapes import Drawing,String,Line,Circle,Group
from reportlab.graphics import renderPDF,renderSVG
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import reportlab

HERE=Path(__file__).resolve().parent
INK='#30383D';GREY='#697176';GRID='#E2E5E6'
WIDTH=7.16*72
# Each plotted record has a distinct pale fill and a darker matching outline.
PALETTE={
    'cosmos_raw':('#DCEAF7','#567BA1'),
    'vjepa2_pretrain':('#D6EEE9','#4F8276'),
    'dreamer4_video':('#E7DFF2','#837094'),
    'pi0_pretrain':('#F6E0CB','#B18155'),
    'droid_full':('#F2ECC6','#998A43'),
    'dreamer4_actions':('#F1DCE2','#AA7381'),
    'vjepa2_ac':('#E2EACF','#788953'),
}
STEM='figure_06_data_scale_bubbles'
CAPTION=r'''Source-reported data scales shown as light-filled bubbles on a logarithmic hours axis~\cite{cosmos,vjepa2,pi0,dreamer4,droid}. Colors distinguish the plotted records. Bubble area increases linearly with the logarithm of the reported value or bound threshold; areas are not proportional to raw hours. The numerical labels retain approximate values and lower or upper bounds. Cosmos denotes the raw candidate collection, $\pi_0$ a robot pretraining mixture, and DROID its reported demonstration corpus. Dreamer~4's 100-hour action-label generation ablation is nested within its 2,541-hour gameplay pool (90/10 training/evaluation split), not the full agent-training budget. V-JEPA~2-AC denotes robot-video post-training with states and derived actions, excluding earlier video pretraining. Different tasks, supervision, and populations prevent a sample-efficiency ranking.'''

def fonts():
    bundled=Path(reportlab.__file__).parent/'fonts'
    pairs=[(Path('C:/Windows/Fonts/arial.ttf'),Path('C:/Windows/Fonts/arialbd.ttf')),
           (Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')),
           (bundled/'Vera.ttf',bundled/'VeraBd.ttf')]
    for normal,bold in pairs:
        if normal.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont('Chart',str(normal)))
            pdfmetrics.registerFont(TTFont('Chart-Bold',str(bold)))
            return
    raise RuntimeError('No suitable TrueType font found. Configure fonts() for this platform.')

def text(d,x,y,s,size=9,bold=False,anchor='start',color=INK):
    d.add(String(x,y,s,fontName='Chart-Bold' if bold else 'Chart',fontSize=size,textAnchor=anchor,fillColor=HexColor(color)))

def line(d,x1,y1,x2,y2,color=GRID,width=.55):
    d.add(Line(x1,y1,x2,y2,strokeColor=HexColor(color),strokeWidth=width))

def radius(value,smallest,largest):
    if not (0<smallest<=value<=largest):raise ValueError('Bubble value outside the positive input range.')
    t=math.log10(value/smallest)/math.log10(largest/smallest)
    return math.sqrt(4**2+(22**2-4**2)*t)

def value_label(row):
    v=row['value_hours']
    label=f'{v/1e6:g}M' if v>=1e6 else (f'{v/1000:g}k' if v>=10000 else f'{v:,g}')
    return {'approximate':'≈','reported_point':'','lower_bound':'>','upper_bound':'<'}[row['bound_type']]+label

def draw(data,out):
    rows={r['id']:r for r in data['figure6']['records']}
    order=['cosmos_raw','vjepa2_pretrain','dreamer4_video','pi0_pretrain','droid_full','dreamer4_actions','vjepa2_ac']
    names=[('Cosmos','raw collection'),('V-JEPA 2','pretraining'),('Dreamer 4','video pool'),('π','pretraining'),
           ('DROID','corpus'),('Dreamer 4','label ablation'),('V-JEPA 2-AC','post-training')]
    smallest=min(r['value_hours'] for r in rows.values());largest=max(r['value_hours'] for r in rows.values())
    d=Drawing(WIDTH,3.25*72)
    left,right,bottom,top=60,503,35,193
    xmap=lambda x:left+(x+.55)/7.1*(right-left)
    ymap=lambda h:bottom+(math.log10(h)-1)/7*(top-bottom)
    for k in range(1,9):
        y=ymap(10**k);line(d,left,y,right,y)
        line(d,left-3,y,left,y,color=GREY)
        text(d,left-8,y-3,'10'+str(k).translate(str.maketrans('12345678','¹²³⁴⁵⁶⁷⁸')),size=8.5,anchor='end')
    line(d,left,bottom,left,top,color='#9DA4A7',width=.6)
    g=Group();g.add(String(0,0,'Source-reported hours (log scale)',fontName='Chart',fontSize=9,textAnchor='middle',fillColor=HexColor(INK)))
    g.translate(17,(bottom+top)/2);g.rotate(90);d.add(g)
    for x in [2.5,4.5]:line(d,xmap(x),bottom,xmap(x),top,color='#C6CBCF',width=.6)
    for x,heading in [(1,'Video sources'),(3.5,'Robot data'),(5.5,'Adaptation / ablation')]:
        text(d,xmap(x),219,heading,size=9,bold=True,anchor='middle')
    plotted=[]
    for i,rid in enumerate(order):
        row=rows[rid];value=row['value_hours'];r=radius(value,smallest,largest)
        x,y=xmap(i),ymap(value)
        fill,edge=PALETTE[rid]
        d.add(Circle(x,y,r,fillColor=HexColor(fill),strokeColor=HexColor(edge),strokeWidth=.85))
        text(d,x,y+r+6,value_label(row),size=9,bold=True,anchor='middle')
        if rid=='pi0_pretrain':
            text(d,x-2,18,'π',size=9,anchor='middle');text(d,x+2.2,16,'0',size=6.3,anchor='middle')
        else:text(d,x,18,names[i][0],size=8.1,anchor='middle')
        text(d,x,6,names[i][1],size=7.9,color=GREY,anchor='middle')
        plotted.append({'record_id':rid,'hours':value,'bound_type':row['bound_type'],'label':value_label(row),
                        'x_pt':x,'y_pt':y,'radius_pt':r,'area_pt2':math.pi*r*r,
                        'fill_color':fill,'outline_color':edge})
    out.mkdir(parents=True,exist_ok=True)
    renderPDF.drawToFile(d,str(out/f'{STEM}.pdf'))
    renderSVG.drawToFile(d,str(out/f'{STEM}.svg'))
    if shutil.which('pdftoppm'):
        subprocess.run(['pdftoppm','-singlefile','-r','400','-png',str(out/f'{STEM}.pdf'),str(out/STEM)],
            check=True,capture_output=True,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    else:print('PDF/SVG saved. Install Poppler (pdftoppm) for a PNG preview.')
    return {'minimum_threshold_hours':smallest,'maximum_threshold_hours':largest,
            'radius_range_pt':[4,22], 'area_formula':'pi*(4^2 + (22^2-4^2)*log10(h/62)/log10(20000000/62))',
            'raw_area_proportional':False,'points':plotted}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data',type=Path,default=HERE.parent/'data/verified_plot_inputs.json')
    ap.add_argument('--out',type=Path,default=HERE.parent/'figures')
    ap.add_argument('--manifest',type=Path)
    args=ap.parse_args();fonts();data=json.loads(args.data.read_text(encoding='utf-8'))
    spec=draw(data,args.out)
    if args.manifest:args.manifest.write_text(json.dumps(spec,indent=2),encoding='utf-8')
    print('Saved bubble chart to '+str(args.out))

if __name__=='__main__':main()
