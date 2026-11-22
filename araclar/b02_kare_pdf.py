#!/usr/bin/env python3
"""SB20 karesi için ChatGPT'ye gönderilecek tek PDF: talimat + prompt + tek referans (özgün JPEG).
Çalıştır: python3 araclar/b02_kare_pdf.py"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from PIL import Image
B="diziler/sifir-sehir/bolumler/B02"; OUT=f"{B}/B02_SB20_chatgpt.pdf"
pdfmetrics.registerFont(TTFont("D","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
REFIMG=f"{B}/kareler/SB20/01_V8_plaka_koy_girisi.jpg"
p20=open(f"{B}/kareler/SB20/SB20_prompt.txt",encoding="utf-8").read().strip()
T=[("h","SB20 — tek görsel: gündüz yanan sokak lambaları"),
("p","Bu PDF'i okuyan ChatGPT için talimat. Üretilecek TEK görsel var: SB20. Bu bir manzara karesidir: boş bir köy sokağı ve yanan dört sokak lambası. Görselde İNSAN YOK. Önceki mesajlarda ya da başka dosyalarda gördüğün yaşlı adamı, tabureyi, çay bardağını bu görsele koyma; önceki görsellerle ilgisi yok."),
("h","Nasıl üretilecek"),
("p","1. Tek referans görsel bu PDF'in SON sayfasında (sayfa 2), özgün JPEG olarak gömülü: boş köy sokağı. Görsel üretim aracını bu görseli DÜZENLEME modunda kullan: görsel aynı kalır, yalnızca iki değişiklik yapılır (tabela kalkar, dört yanan lamba eklenir)."),
("p","2. Sayfayı doğrudan düzenleyemiyorsan önce kod aracıyla PDF'in 2. sayfasındaki görseli çıkar ve onu düzenle. Onu da yapamıyorsan üretme; kullanıcıya 'köy sokağı görselini ayrıca yükle' de."),
("p","3. Oran dikey 9:16, referansla aynı kadraj. Yazı, altyazı, logo, çerçeve yok."),
("p","4. Promptu İngilizce ve kelimesi kelimesine kullan."),
("h","Prompt"),("c",p20),
("h","Kontrol (kullanıcıya vermeden önce kendin bak)"),
("p","Görselde insan var mı? Varsa YANLIŞ. · Dört lamba var mı ve dördü de yanıyor mu? · Tabela ve yazı kalktı mı? · Hayvan, araç yok mu? · Sokak, evler, ışık referansla aynı mı? · Dikey 9:16 mı?"),
("p","Geçmiyorsa aynı promptla bir kez daha üret. İkincide de geçmezse dur ve neyin yanlış çıktığını yaz."),
("h","Teslim"),("p","Görseli tam çözünürlükte, SB20 adıyla ver.")]
c=canvas.Canvas(OUT,pagesize=A4); W,H=A4; M=50; y=H-M
for k,t in T:
    f,s,l=("DB",13,18) if k=="h" else ("D",8.6,12) if k=="c" else ("D",10,14.5)
    if k=="h": y-=8
    for par in t.split("\n"):
        for line in (simpleSplit(par,f,s,W-2*M) or [""]):
            assert y>M, "taştı"
            c.setFont(f,s); c.drawString(M,y,line); y-=l
    y-=5
c.showPage()
w,h=Image.open(REFIMG).size
c.setPageSize((w,h)); c.drawImage(REFIMG,0,0,w,h); c.showPage()
c.save(); print(OUT)
