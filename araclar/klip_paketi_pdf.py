"""Resim–prompt çiftleri sırayla tek PDF: python3 araclar/klip_paketi_pdf.py <klipler_klasoru> <cikti.pdf> P01 P02 ..."""
import sys, glob, os
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
F='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('D',F+'DejaVuSans.ttf')); pdfmetrics.registerFont(TTFont('DB',F+'DejaVuSans-Bold.ttf')); pdfmetrics.registerFont(TTFont('M',F+'DejaVuSansMono.ttf'))
H=ParagraphStyle('h',fontName='DB',fontSize=15,leading=19,spaceAfter=4)
N=ParagraphStyle('n',fontName='D',fontSize=9.5,leading=13,spaceAfter=6)
P=ParagraphStyle('p',fontName='M',fontSize=7.2,leading=9.2,backColor='#f3f1ec',borderPadding=6)
kl, out, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
s=[]
for i,pid in enumerate(ids,1):
    d=os.path.join(kl,pid); img=sorted(glob.glob(d+'/*baslangic_karesi*.jpg')); txt=glob.glob(d+'/*_prompt_8sn.txt')[0]
    s.append(Paragraph(f'{i}) B06_{pid}',H))
    if img:
        s.append(Paragraph('<b>RESİM</b> — Flow\'da “Frames to Video” başlangıç karesi yuvasına: '+escape(os.path.basename(img[0])),N))
        s.append(Image(img[0],width=6.4*cm,height=9.6*cm)); s.append(Spacer(1,6))
    s.append(Paragraph('<b>PROMPT</b> — bu resmin altına yapıştır (8 sn, 1080p indir):',N))
    s.append(Paragraph(escape(open(txt).read()).replace('\n','<br/>'),P))
    s.append(PageBreak())
SimpleDocTemplate(out,pagesize=A4,leftMargin=1.6*cm,rightMargin=1.6*cm,topMargin=1.4*cm,bottomMargin=1.4*cm).build(s)
print(out)
