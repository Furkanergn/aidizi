#!/usr/bin/env python3
"""B02'nin iki yeni karesi için Claude sohbete gönderilecek tek PDF: talimat + promptlar + referans görseller (özgün JPEG).
Çalıştır: python3 araclar/b02_kare_pdf.py"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from PIL import Image
B="diziler/sifir-sehir/bolumler/B02"; OUT=f"{B}/B02_gorsel_paketi_chatgpt.pdf"
pdfmetrics.registerFont(TTFont("D","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
IMG=[("SB21","01_SB10_onayli.jpg"),("SB21","02_Naci_sayfasi.jpg"),("SB21","03_Naci_ifade_sayfasi.jpg"),("SB20","01_V8_plaka_koy_girisi.jpg"),("SB20","02_SB09_onayli.jpg")]
p21=open(f"{B}/kareler/SB21/SB21_prompt.txt",encoding="utf-8").read().strip()
p20=open(f"{B}/kareler/SB20/SB20_prompt.txt",encoding="utf-8").read().strip()
T=[("h","Sıfır Şehir · Bölüm 2 — görsel üretim paketi (ChatGPT için)"),
("p","Bu PDF'i okuyan ChatGPT için talimat. Bu bölüm için üretilecek görsellerin TAMAMI aşağıdaki iki karedir (SB21 ve SB20). Bölümün diğer 12 planı önceki bölümün onaylı karelerinden başlıyor; onlar yeniden üretilmeyecek. Başka görsel üretme."),
("h","Nasıl üretilecek"),
("p","1. Görsel üretim aracını kullan. Her kare ayrı bir görsel: önce SB21'i, hemen ardından soru sormadan SB20'yi üret. İkisini tek görselde birleştirme, kolaj yapma."),
("p","2. Oran dikey 9:16 (örnek 1024×1792 ya da daha yüksek). Yatay ya da kare görsel kabul edilmez."),
("p","3. Referans görseller bu PDF'in 3.–7. sayfalarında, her sayfada bir tane, özgün JPEG olarak gömülü. Bunları görsel referansı olarak kullan (düzenleme / referanslı üretim). Sayfaları doğrudan referans alamıyorsan önce kod aracıyla PDF'ten çıkar (pypdf ya da PyMuPDF; sırayla sayfa 3…7) ve çıkan dosyaları referans olarak ver. Referansları hiç kullanamıyorsan üretme; kullanıcıya 'referans görselleri ayrıca yükle' de."),
("p","4. Promptları İngilizce ve kelimesi kelimesine kullan; kısaltma, yeniden yazma, çevirme. Stil: stilize 3D animasyon filmi karesi; fotogerçekçi değil."),
("p","5. Görsellerin üzerine yazı, altyazı, logo, çerçeve, filigran koyma."),
("h","GÖRSEL 1: SB21 — Naci taburede, zarf yok · referanslar: sayfa 3 (ana kare), 4, 5"),
("p","Bu bir DÜZENLEME işidir: sayfa 3'teki kare birebir korunur, yalnızca iki şey değişir (raftaki zarf kalkar, sol el dize konur). Sayfa 4 ve 5 karakterin yüzünü ve kıyafetini sabitlemek içindir."),
("c",p21),
("h","GÖRSEL 2: SB20 — gündüz yanan sokak lambaları · referanslar: sayfa 6, 7"),
("p","Sayfa 6 ve 7 köyün görünüşünü, taş dokusunu, ışığı ve stili sabitlemek içindir. Kamera aynı sokağın biraz daha içinde durur; tabela ve keçi bu karede YOKTUR."),
("c",p20),
("h","Kontrol (kullanıcıya vermeden önce kendin bak)"),
("p","SB21: taş rafta zarf YOK, görselin hiçbir yerinde zarf yok · sol el sol dizde · sağ elde ince belli çay bardağı, göğüs hizasında · adam, tabure, taş duvar, mavi kapı, asma sayfa 3 ile aynı · kameraya bakmıyor · dikey 9:16 · yazı yok."),
("p","SB20: dört lamba var ve dördü de YANIYOR · insan, hayvan, araç, tabela, yazı yok · ışık ikindi sonrası altın ışık, güneş solda · stil sayfa 6–7 ile aynı · dikey 9:16."),
("p","Bir görsel bu listeden geçmiyorsa aynı promptla bir kez daha üret. İkinci denemede de geçmezse dur ve neyin yanlış çıktığını yaz; üçüncü kez üretme."),
("h","Teslim"),
("p","İki görseli tam çözünürlükte ver ve hangisinin SB21, hangisinin SB20 olduğunu yaz. Dosya adları: SB21 ve SB20."),
("h","Referans sayfaları"),
("p","Sayfa 3: SB10 onaylı kare — Naci taburede (SB21'in ana karesi) · Sayfa 4: Naci karakter sayfası (SB21) · Sayfa 5: Naci ifade sayfası (SB21) · Sayfa 6: köy girişi plakası (SB20) · Sayfa 7: SB09 onaylı kare — köy sokağı, yerde tabela ve keçi (SB20; yalnızca mekân ve stil için)")]
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
