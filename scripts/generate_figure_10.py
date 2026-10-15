"""Reproduce the current Figure 10 from the verified task means."""
from pathlib import Path
import argparse,json,subprocess,shutil
from reportlab.graphics.shapes import Drawing,Rect
from reportlab.graphics import renderPDF,renderSVG
from reportlab.lib.colors import HexColor
from generate_figure_06 import fonts,text,line,INK,GREY,GRID

def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser();ap.add_argument('--data',type=Path,default=root/'data/verified_plot_inputs.json')
    ap.add_argument('--out',type=Path,default=root/'figures');args=ap.parse_args()
    data=json.loads(args.data.read_text(encoding='utf-8'));fonts();args.out.mkdir(parents=True,exist_ok=True)
    d=Drawing(7.16*72,2.95*72)
    left,right,bottom,top=161,497,51,174
    xm=lambda x:left+(x+50)/100*(right-left)
    for x in [-40,-20,0,20,40]:
        line(d,xm(x),bottom,xm(x),top);line(d,xm(x),bottom-3,xm(x),bottom,color=GREY)
        text(d,xm(x),bottom-15,f'{x:+d}' if x else '0',size=8.5,anchor='middle')
    line(d,left,bottom,right,bottom,color='#A6ADB0',width=.6)
    text(d,(left+right)/2,13,'World-Gymnast − SIMPLER (percentage points)',size=9,anchor='middle')
    names=['Open drawer','Close drawer','Eggplant to blue sink','Eggplant to yellow basket']
    for i,row in enumerate(data['world_gymnast']['records']):
        y=159-i*29;delta=row['world_gymnast_mean_pct']-row['simpler_mean_pct']
        assert delta==row['difference_pp']
        d.add(Rect(min(xm(0),xm(delta)),y-6,abs(xm(delta)-xm(0)),12,fillColor=HexColor('#59666E'),strokeColor=None))
        text(d,left-12,y-3,names[i],size=9,anchor='end')
        text(d,xm(delta)+(5 if delta>0 else -5),y-3,f'{delta:+d}',size=9.7,bold=True,anchor='start' if delta>0 else 'end')
    line(d,xm(0),bottom,xm(0),top,color='#52595D',width=1)
    text(d,xm(-25),190,'Favors SIMPLER',size=8.5,color=GREY,anchor='middle')
    text(d,xm(25),190,'Favors World-Gymnast',size=8.5,color=GREY,anchor='middle')
    stem='figure_10_task_differences'
    renderPDF.drawToFile(d,str(args.out/f'{stem}.pdf'));renderSVG.drawToFile(d,str(args.out/f'{stem}.svg'))
    if shutil.which('pdftoppm'):
        subprocess.run(['pdftoppm','-singlefile','-r','400','-png',str(args.out/f'{stem}.pdf'),str(args.out/stem)],
                      check=True,capture_output=True,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    print('Saved Figure 10 to '+str(args.out))

if __name__=='__main__':main()
