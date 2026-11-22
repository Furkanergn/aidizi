#!/usr/bin/env python3
"""B02'nin iki yeni karesi için Claude sohbete gönderilecek tek PDF: talimat + promptlar + referans görseller (özgün JPEG).
Çalıştır: python3 araclar/b02_kare_pdf.py"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from PIL import Image
B="diziler/sifir-sehir/bolumler/B02"; OUT=f"{B}/B02_kare_uretim_paketi.pdf"
pdfmetrics.registerFont(TTFont("D","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
IMG=[("SB21","01_SB10_onayli.jpg"),("SB21","02_Naci_sayfasi.jpg"),("SB21","03_Naci_ifade_sayfasi.jpg"),("SB20","01_V8_plaka_koy_girisi.jpg"),("SB20","02_SB09_onayli.jpg")]
p21=open(f"{B}/kareler/SB21/SB21_prompt.txt",encoding="utf-8").read().strip()
p20=open(f"{B}/kareler/SB20/SB20_prompt.txt",encoding="utf-8").read().strip()
T=[("h","B02 kare üretim paketi — talimat"),
("p","Bu PDF'i okuyan Claude için: aşağıdaki iki görseli Higgsfield ile üret."),
("p","Model: Nano Banana Pro · oran 9:16 · çözünürlük 2K · sınırsız üretim hakkıyla (use_unlim). Kredi harcama; sınırsız hak kullanılamıyorsa üretme, kullanıcıya söyle."),
("p","Referans görseller bu PDF'in 3.–7. sayfalarında, her sayfada bir tane, özgün JPEG olarak gömülü. Sayfa görüntüsünü değil gömülü görseli kullan: kod ortamında `pdfimages -all dosya.pdf ref` (ya da PyMuPDF/pypdf) ile çıkar; sırasıyla ref-000 … ref-004 = sayfa 3 … 7. Çıkardığın dosyaları Higgsfield'a yükle (media_upload, PUT, media_confirm)."),
("p","Her görsel için yalnızca kendi referanslarını bağla ve promptu kelimesi kelimesine kullan; değiştirme, kısaltma, çevirme."),
("h","GÖRSEL 1: SB21 — referanslar: sayfa 3, 4, 5"),("c",p21),
("h","GÖRSEL 2: SB20 — referanslar: sayfa 6, 7"),("c",p20),
("h","Kontrol (kullanıcıya göstermeden önce)"),
("p","SB21: taş rafta zarf YOK; sol el dizde; sağ elde çay bardağı; adam, tabure, duvar ve kapı sayfa 3'teki kareyle aynı; oran 9:16."),
("p","SB20: dört lamba da yanıyor; insan, hayvan, tabela, yazı yok; oran 9:16."),
("p","Bir görsel kontrolü geçmezse aynı promptla bir kez daha üret. İkincide de geçmezse dur ve neyin yanlış çıktığını yaz."),
("h","Teslim"),
("p","İki görseli özgün çözünürlükte, yeniden sıkıştırmadan SB21.jpg ve SB20.jpg adlarıyla ver; mümkünse ikisini B02_kareler.zip içinde de indirilebilir yap."),
("h","Referans sayfaları"),
("p","Sayfa 3: 01_SB10_onayli.jpg (SB21) · Sayfa 4: 02_Naci_sayfasi.jpg (SB21) · Sayfa 5: 03_Naci_ifade_sayfasi.jpg (SB21) · Sayfa 6: 01_V8_plaka_koy_girisi.jpg (SB20) · Sayfa 7: 02_SB09_onayli.jpg (SB20)")]
c=canvas.Canvas(OUT,pagesize=A4); W,H=A4; M=50; y=H-M
for k,t in T:
    f,s,l=("DB",13,18) if k=="h" else ("D",8.6,12) if k=="c" else ("D",10,14.5)
    if k=="h": y-=8
    for par in t.split("\n"):
        for line in (simpleSplit(par,f,s,W-2*M) or [""]):
            if y<M+l: c.showPage(); y=H-M
            c.setFont(f,s); c.drawString(M,y,line); y-=l
    y-=5
c.showPage()
assert c.getPageNumber()==3, c.getPageNumber()
for d,n in IMG:
    path=f"{B}/kareler/{d}/{n}"; w,h=Image.open(path).size
    c.setPageSize((w,h)); c.drawImage(path,0,0,w,h); c.showPage()
c.save(); print(OUT)
