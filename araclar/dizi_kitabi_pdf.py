#!/usr/bin/env python3
"""Sıfır Şehir dizi kitabı (PDF): dünya, karakterler, yayınlanan bölümlerin senaryosu, sonraki bölümler için plan önerisi.
Çalıştır: python3 araclar/dizi_kitabi_pdf.py  →  diziler/sifir-sehir/Sifir_Sehir_dizi_kitabi.pdf"""
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
                                Image as RLImage, KeepTogether)
from PIL import Image

D = "diziler/sifir-sehir"
V = f"{D}/varliklar/onayli"
OUT = f"{D}/Sifir_Sehir_dizi_kitabi.pdf"
pdfmetrics.registerFont(TTFont("D", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DI", "/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf"))
pdfmetrics.registerFontFamily("D", normal="D", bold="DB", italic="DI", boldItalic="DB")

HARDAL = colors.HexColor("#F2B33D")
KOYU = colors.HexColor("#1E1B18")
GRI = colors.HexColor("#6B655E")
ACIK = colors.HexColor("#FAF3E3")

S = dict(
    h1=ParagraphStyle("h1", fontName="DB", fontSize=20, leading=25, textColor=KOYU, spaceAfter=8),
    h2=ParagraphStyle("h2", fontName="DB", fontSize=13.5, leading=18, textColor=KOYU, spaceBefore=12, spaceAfter=5, keepWithNext=1),
    h3=ParagraphStyle("h3", fontName="DB", fontSize=10.5, leading=14, textColor=KOYU, spaceBefore=8, spaceAfter=2, keepWithNext=1),
    p=ParagraphStyle("p", fontName="D", fontSize=9.6, leading=14, textColor=KOYU, spaceAfter=4),
    k=ParagraphStyle("k", fontName="D", fontSize=8.6, leading=12, textColor=GRI, spaceAfter=4),
    m=ParagraphStyle("m", fontName="D", fontSize=9.6, leading=14, textColor=KOYU, leftIndent=10, bulletIndent=0, spaceAfter=2),
    r=ParagraphStyle("r", fontName="D", fontSize=9.8, leading=14.5, textColor=KOYU, leftIndent=16, spaceAfter=1),
    e=ParagraphStyle("e", fontName="DI", fontSize=9.2, leading=13.5, textColor=GRI, spaceBefore=4, spaceAfter=2),
    t=ParagraphStyle("t", fontName="D", fontSize=8.8, leading=12.5, textColor=KOYU),
    tb=ParagraphStyle("tb", fontName="DB", fontSize=8.8, leading=12.5, textColor=KOYU),
)
A = []
W = A4[0] - 36 * mm


def h1(x): A.append(Paragraph(x, S["h1"])); A.append(cizgi())
def h2(x): A.append(Paragraph(x, S["h2"]))
def h3(x): A.append(Paragraph(x, S["h3"]))
def p(x): A.append(Paragraph(x, S["p"]))
def k(x): A.append(Paragraph(x, S["k"]))
def m(*xs):
    for x in xs: A.append(Paragraph(x, S["m"], bulletText="•"))
def e(x): A.append(Paragraph(x, S["e"]))
def r(kim, soz, oyun=""):
    o = f' <font name="DI" color="#6B655E">({oyun})</font>' if oyun else ""
    A.append(Paragraph(f"<b>{kim}</b>{o}: {soz}", S["r"]))


def cizgi():
    t = Table([[""]], colWidths=[W], rowHeights=[3])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), HARDAL)]))
    return KeepTogether([t, Spacer(1, 8)])


def tablo(rows, widths, baslik=True):
    data = [[Paragraph(c, S["tb"] if (baslik and i == 0) else S["t"]) for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=[W * w for w in widths], repeatRows=1 if baslik else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D9CFBB")),
          ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if baslik: st.append(("BACKGROUND", (0, 0), (-1, 0), ACIK))
    t.setStyle(TableStyle(st)); A.append(t); A.append(Spacer(1, 6))


def gorsel(yol, gen_mm, kutu=None):
    im = Image.open(yol).convert("RGB")
    if kutu: im = im.crop(kutu)
    im.thumbnail((1500, 1500))
    b = io.BytesIO(); im.save(b, "JPEG", quality=85); b.seek(0)
    w = gen_mm * mm
    return RLImage(b, width=w, height=w * im.size[1] / im.size[0])


def yan_yana(yollar, gen_mm, alt=None):
    hucre = [gorsel(y, gen_mm) for y in yollar]
    rows = [hucre]
    if alt: rows.append([Paragraph(a, S["k"]) for a in alt])
    t = Table(rows, colWidths=[(gen_mm + 4) * mm] * len(yollar))
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    A.append(t); A.append(Spacer(1, 6))


# ───────────────────────── KAPAK
A.append(Spacer(1, 30 * mm))
A.append(Paragraph("SIFIR ŞEHİR", ParagraphStyle("kp", fontName="DB", fontSize=40, leading=46, textColor=KOYU)))
A.append(Paragraph("Dizi kitabı", ParagraphStyle("kp2", fontName="D", fontSize=18, leading=26, textColor=GRI)))
A.append(Spacer(1, 4 * mm)); A.append(cizgi())
p("Dünya, karakterler, yayınlanan üç bölümün senaryosu ve sonraki bölümler için plan.")
k("24 Kasım 2026 · Bölüm 1–3 tamamlandı · Bölüm 4 ve sonrası öneridir, onay bekliyor")
A.append(Spacer(1, 6 * mm))
yan_yana([f"{D}/bolumler/B01/cikti/B01_kapak.jpg", f"{D}/bolumler/B02/cikti/B02_kapak.jpg", f"{D}/bolumler/B03/cikti/B03_kapak.jpg"], 52,
         ["Bölüm 1: Koca Bir Şehir", "Bölüm 2: Muhtar", "Bölüm 3: Toplantı"])
h3("İçindekiler")
m("1. Dizi tek bakışta", "2. Dünya: köy, mekânlar, arka plan bilgisi", "3. Karakterler", "4. Tekrar eden şakalar",
  "5. Buraya kadar olan hikâye: Bölüm 1, 2, 3 (replikleriyle)", "6. Şu an kim nerede, ne kimin elinde",
  "7. Sonraki bölümler: plan önerisi", "8. Açık sorular ve kararlar")
A.append(PageBreak())

# ───────────────────────── 1
h1("1. Dizi tek bakışta")
tablo([
    ["Tür", "Dikey kısa komedi dizisi (Instagram Reels), bölüm başına 60–80 saniye"],
    ["Tek cümle", "Rıza, karısıyla ev almak için biriktirdikleri parayla internetten bir “şehir” satın alır. Şehir, üç nüfuslu, borçlu bir köy çıkar ve muhtarı bir keçidir."],
    ["Komedinin motoru", "Şehirli çiftin köye beceriksiz uyumu. Köylüler akıllı taraftır; izleyici köylüye değil, Rıza'nın plaza diliyle köyü yönetmeye çalışmasına güler."],
    ["Kalp", "Evlilik. Rıza hata yapmadığını kanıtlamak ister; Selin paranın peşindedir ama köyü gizlice sevmeye başlar."],
    ["Görsel dil", "Stilize 3D animasyon filmi görünümü (hafif büyük gözler, sade cilt, gerçekçi kumaş ve saç). İkindi sonrası altın ışık. Vurgu rengi hardal."],
    ["Bölüm kalıbı", "İlk 2 saniyede kanca ve ekran yazısı; bölüm başına bir tanışma; soruyla biter; son kare donar, müzik girer, “tahminini yoruma yaz” ve “takip et”."],
    ["Zaman", "İlk üç bölüm aynı günün aynı yarım saatinde geçer: çiftin köye geldiği ikindi."],
], [0.22, 0.78], baslik=False)

# ───────────────────────── 2
h1("2. Dünya")
h2("Köy")
m("Satış ilanında “şehir” olarak geçti. Tapuda: <b>on iki ev, bir depo, bir değirmen. Nüfus: üç.</b>",
  "Köyün adı henüz hiç söylenmedi. (Fatura görselinde “Boğaztepe” yazıyor ama o görsel hatalı; isim karar bekliyor.)",
  "Evlerin çoğu boş, kepenkler kapalı, taş duvarlar, kiremit çatılar. Çevre kuru tepeler.",
  "Köyün <b>333.333,33 TL elektrik borcu</b> var ve tapuyla birlikte yeni sahibe geçti.",
  "Borcun sebebi: meydandaki sokak lambaları <b>on iki senedir gece gündüz yanıyor</b>. “Gerisi faiz.”",
  "Şalter muhtardadır. Muhtar bir keçidir; <b>üç oyla</b> seçilmiştir. Şalterin anahtarı Emine'nin boynundaki ipte asılıdır.",
  "<b>“Öncekiler”:</b> köyü daha önce de satın alanlar oldu. Heyecanlıydılar, slayt getirdiler, <b>üç gün dayandılar</b>.")
h2("Mekânlar")
tablo([
    ["Mekân", "Ne var", "İlk görüldüğü yer"],
    ["Çakıl yol ve araba", "Çiftin arabası köyün dışında, girişin on metre gerisinde durur. Arka planda uzakta görünür.", "B01"],
    ["Köy girişi", "Yere devrilmiş paslı “ŞEHİR MERKEZİ” tabelası. Keçinin yeri burasıdır.", "B01"],
    ["Giriş sokağı", "Taş sokak, iki yanında boş evler. Selin ve Rıza burada durur. Burada sokak lambası yoktur.", "B01"],
    ["Naci'nin duvarı", "Sokağın sağ yanı: taş duvar, mavi kapı, alçak tabure, taş raf. Naci hep buradadır.", "B01"],
    ["Köy meydanı", "Sokağın sonunda. Kuru çeşme, yaşlı çınar, gündüz yanan dört paslı sokak lambası. Emine'nin alanı.", "B02"],
    ["Henüz görülmeyenler", "Depo, değirmen, şalterin durduğu yer (trafo kulübesi), çiftin kalacağı ev, Emine ile Hüseyin'in evi ve ağılı.", "—"],
], [0.22, 0.63, 0.15])
yan_yana([f"{V}/V8_plaka_koy_girisi.jpg", f"{V}/V9_plaka_naci_duvari.jpg", f"{D}/bolumler/B02/kareler/onayli/SB20.jpg"], 50,
         ["Köy girişi ve sokak", "Naci'nin duvarı", "Köy meydanı"])
h2("Önemli nesneler")
tablo([
    ["Nesne", "Tarif", "Hikâyedeki işi"],
    ["Tapu dosyası", "Bordo deri dosya, ince lastik bantlı, A4", "Selin “Nüfus: üç”ü buradan okur. B03'te Rıza'ya geçer, kovalamacada girişte yere düşer."],
    ["Sarı zarf", "Kalın, sarı, el büyüklüğünde", "Elektrik borcu bununla gelir. Naci verir, Rıza açar."],
    ["Fatura", "Buruşuk A4, mavi başlıklı", "Rıza keçiye gösterir, keçi kapıp kaçar, Emine ağzından alır."],
    ["Anahtar", "Eski demir anahtar, Emine'nin boynunda ipte", "Şaltere giden tek yol. Emine “bir şartla” verir."],
    ["Çay bardağı", "İnce belli bardak ve tabağı", "Naci'nin elinden hiç düşmez."],
    ["Tabela", "Paslı “ŞEHİR MERKEZİ”", "Keçi köşesini yer, B01'de devrilir, o günden beri yerde."],
], [0.18, 0.32, 0.50])
A.append(PageBreak())

# ───────────────────────── 3
h1("3. Karakterler")


def karakter(ad, alt, gor, satirlar, kutu=None):
    blok = [Paragraph(ad, S["h2"]), Paragraph(alt, S["k"])]
    if gor: blok.append(gorsel(gor, 120, kutu)); blok.append(Spacer(1, 4))
    A.append(KeepTogether(blok))
    tablo(satirlar, [0.2, 0.8], baslik=False)


karakter("Rıza", "Başrol · otuzlarının ortası · satış yöneticisi", f"{V}/V1_riza_ifade.jpg", [
    ["Görünüş", "Dağınık koyu bukleler, uzun burun, kalın koyu kaşlar, hafif sakal. Lacivert blazer, kırmızı cep mendili, krem gömlek (yaka açık), kahverengi pantolon ve kemer, bordo makosen. Selin'den yarım baş uzun."],
    ["Kişilik", "Aceleci, ikna edici, komik. Büyük kararları hızlı alır. Her felakette bir “potansiyel” görür."],
    ["İsteği", "Hata yapmadığını kanıtlamak."],
    ["Kusuru", "Kötü haberi küçülterek söyler (“biraz da birikim”, “Üç…”), saçmalığı normalleştirir (“Demokratik bir süreç olmuştur”)."],
    ["Konuşması", "Plaza dili: potansiyel, konum, yatırım, toplantı, ortak, kazan kazan, “Sayın Muhtar”. Selin'e “aşkım”, “hayatım” der. Sıkışınca sesi küçülür."],
    ["Sesi", "Sıcak, parlak, hafif genizden tenor; hızlı konuşur."],
    ["Arka plan", "Para: dedesinden kalan miras ve çiftin ev için ayırdığı birikim. Köyü Selin'e sormadan aldı. Şehirde bir satış işi var (henüz gösterilmedi)."],
])
karakter("Selin", "Başrol · otuzlarının başı · finans kökenli", f"{V}/V2_selin_ifade.jpg", [
    ["Görünüş", "Çeneye kadar altın sarısı bukleler, çiller, gamzeler, kahverengi gözler, küçük altın halka küpe. Kalp yaka pembe fitilli üst, kısa iki katlı fırfırlı bordo etek, çıplak bacak, kahverengi bantlı babet."],
    ["Kişilik", "Hesabı iyi yapar. Sıcak ama kuru mizahlı. Sinirlenince iğneler, sitem eder, sesini yükseltir; komik bulduğunda kahkahayla güler."],
    ["İsteği", "Paranın nereye gittiğini tam öğrenmek ve geri almak. Gizli çizgisi: köyü sevmeye başlar."],
    ["İşlevi", "Her bölümde kararı o verir: tapuyu o okur, hesabı o sorar, Rıza'yı keçiyle konuşmaya o yollar."],
    ["Konuşması", "Kısa, net, gündelik karı koca ağzı: “Kaç para?”, “Kim yaktı ya?”, “Hadi git konuş.” Elleriyle konuşur."],
    ["Sesi", "Sıcak, hafif boğuk alçak ses; geniş duygu aralığı."],
    ["Arka plan", "Ev alma hayali vardı; para ona aitti de. Şehirdeki işi henüz gösterilmedi."],
])
karakter("Naci", "Köylü · altmışlarının sonu · eski sulama görevlisi · bekâr", f"{V}/V3_naci_ifade.jpg", [
    ["Görünüş", "İnce yapılı, geriye taranmış gri saç, kalın gri bıyık, gür gri kaşlar. Soluk mavi iş ceketi, kareli gömlek, gri pantolon, kahverengi bot. Elinde hep çay."],
    ["Kişilik", "Her şeyi bilir, hiçbirini acele etmeden söyler. Kötü haberi önemsizmiş gibi verir. Hafifçe eğlenir."],
    ["İşlevi", "Bilgi veren ve tek cümleyle bitiren adam: “Üç gün dayandılar.” “Otuz üç de kuruşu var.” “Yetişemez.”"],
    ["Sesi", "Yavaş, kuru, çakıllı alçak ses."],
    ["Arka plan", "Köyün üç sakininden biri. Taburesinden kalktığı henüz görülmedi. Öncekilerin hepsini görmüş."],
])
karakter("Emine", "Köylü · altmışlarının ortası · hayvancılık · köyün gerçek patronu", f"{V}/V19_emine_ifade.jpg", [
    ["Görünüş", "Sağlam yapılı; örgülü gri topuz, arkadan bağlı bordo çiçekli yazma, kalın koyu gri kaşlar, küçük altın küpe. Kiremit rengi örgü yelek, lacivert çiçekli elbise (kolları sıvalı), siyah lastik çizme. Boynunda ipte demir anahtar."],
    ["Kişilik", "Buyurgan, pazarlıkçı, gür kahkahalı; altında sıcaklık var. Kimseden çekinmez."],
    ["İşlevi", "Köyde söz onundur. Muhtar (keçi) onundur, anahtar ondadır. Çiftin her istediği onun şartından geçer."],
    ["Sesi", "Güçlü, hafif kısık, yüksek; içten kahkaha."],
    ["Arka plan", "Hüseyin'le birlikte yaşar. B03'te tanıştık."],
])
karakter("Muhtar (keçi)", "Köyün muhtarı · üç oyla seçildi", f"{V}/V7_keci.jpg", [
    ["Görünüş", "Krem beyazı köy keçisi, tek kulağı kahverengi, kıvrık boynuz, küçük sakal, yarı kapalı bıkkın gözler. Boynunda yıpranmış kırmızı ip ve küçük pirinç çan."],
    ["Kişilik", "Hiçbir şeyi umursamaz. Her şeyi çiğner ya da kapar: tabela, fatura."],
    ["İşlevi", "Köyün dördüncü sakini. Şalter “onda”. Emine'nin sözünden çıkmaz."],
])
h2("Hüseyin")
k("Köylü · hayvancılık · Emine'yle yaşar · henüz görünmedi")
tablo([
    ["Tasarım", "İlk karakter dosyasında sayfası var; bu üretim sistemi için ifade ve jest sayfaları henüz yapılmadı."],
    ["Planlanan işlev", "Her işe “olur” deyip hiçbirini yapmayan adam. Emine konuşur, o onaylar."],
], [0.2, 0.8], baslik=False)
h3("Boy ilişkileri")
A.append(gorsel(f"{V}/V4_boy_sayfasi.jpg", 120))
A.append(PageBreak())

# ───────────────────────── 4
h1("4. Tekrar eden şakalar")
tablo([
    ["Şaka", "Şimdiye kadar", "Nasıl büyür"],
    ["“Üç”", "Nüfus üç. “Üç bin mi? / Üç.” Öncekiler üç gün dayandı. Borç 333.333,33. Muhtar üç oyla seçildi.", "Her sayı bir şekilde üçe çıkar. Çiftin üçüncü günü bir dönüm noktası olur."],
    ["Rıza'nın plaza dili", "Potansiyel, kafe, ortak çalışma alanı, toplantı, yeni ortağınız, kazan kazan.", "Her köy işine kurumsal bir ad takar; köylüler düz anlamıyla cevap verir."],
    ["Keçi her şeyi kapar", "Tabelayı yedi, faturayı kapıp kaçtı.", "Rıza'nın önemli saydığı her kâğıt keçinin ağzında biter."],
    ["“Öncekiler”", "Heyecanlıydılar, üç gün dayandılar, slayt getirmişlerdi.", "Rıza ne yapsa öncekiler de yapmıştır. Köyde izleri çıkar."],
    ["Naci'nin son sözü", "“Otuz üç de kuruşu var.” “Yetişemez.”", "Her sahneyi çayından başını kaldırmadan tek cümleyle kapatır."],
    ["Henüz kullanılmayanlar", "Telefonun köyde tek bir noktada çekmesi. Hüseyin'in “olur”u. “Navigasyon bile emin konuştu.”", "B05 ve sonrası."],
], [0.2, 0.42, 0.38])

# ───────────────────────── 5
h1("5. Buraya kadar olan hikâye")
k("Replikler yayınlanan kurgudaki hâliyle. Parantez içi oyun tarifidir.")

h2("Bölüm 1 — Koca Bir Şehir")
k("68 saniye · köy girişi · Selin, Rıza, Naci, keçi · yayınlandı (22 Kasım 2026)")
p("<b>Özet:</b> Selin, kocasının bütün birikimleriyle aldığı “şehrin” üç nüfuslu bir köy olduğunu ve köyün borcuyla birlikte geldiğini öğrenir. <b>Bitiş sorusu:</b> borç ne kadar?")
e("Ekran yazısı: Kocam bütün birikimimizle bir ŞEHİR satın aldı. Çift köy girişinde yan yana. Rıza gururla köye bakıyor.")
r("SELİN", "Rıza… bunun neresi şehir?", "başını çevirmeden")
e("Boş taş sokak. Paslı, yana yatmış tabela: ŞEHİR MERKEZİ. Dibinde bir keçi.")
r("RIZA", "Şehir merkezi burası aşkım! Bak, tabelası bile var.", "coşkulu")
r("SELİN", "Tabelayı keçi yiyor, Rıza.")
e("Keçi tabelanın köşesini ağır ağır çiğner. Selin tapu dosyasını açar.")
r("SELİN", "On iki ev, bir depo, bir değirmen… Nüfus: üç.", "okur")
r("RIZA", "Üç bin mi?", "umutla")
r("SELİN", "Üç.")
r("SELİN", "Kimin parasıyla?")
r("RIZA", "Dedemden kalan… biraz da birikim.")
r("SELİN", "Biraz dediğin?")
r("RIZA", "Ev için ayırdığımız kadar.", "sesi alçalarak")
e("Selin bir şey demez. Sol göz kapağı bir kez seğirir.")
r("RIZA", "Ama potansiyele bak! Şuraya kafe, şuraya ortak çalışma alanı—", "satışçı coşkusuyla")
e("Arkadan metal gürültüsü. Rıza cümlenin ortasında donar. Tabela yerde; keçi yanında çiğnemeye devam ediyor. Duvarın dibinde, taburede, elinde çayla yaşlı bir adam.")
r("NACİ", "Yeni sahipler siz misiniz? … Öncekiler de böyle heyecanlıydı.", "acelesiz")
r("SELİN", "Öncekiler mi?")
r("NACİ", "Üç gün dayandılar.")
r("NACİ", "Bu arada… köyün elektrik borcu. Artık sizin.", "sarı zarfı uzatır")
e("Zarf Rıza'nın elinde, açık. Gülümsemesi siliniyor.")
r("SELİN", "Rıza. Kaç?")
e("Rıza yutkunur. Son kare donar.")

h2("Bölüm 2 — Muhtar")
k("62 saniye · köy girişi ve meydan (tek plan) · aynı dakikanın devamı")
p("<b>Özet:</b> Borcun rakamı ortaya çıkar. Borcu durduracak şalter muhtardadır ve muhtar keçidir. <b>Bitiş sorusu:</b> Rıza bir keçiyle pazarlık edebilir mi?")
e("Ekran yazısı: Kocamın aldığı ŞEHİR borcuyla geldi.")
r("SELİN", "Rıza. Kaç para?")
r("RIZA", "Üç…", "yutkunur")
r("SELİN", "Üç bin mi?", "ufak bir umutla")
r("RIZA", "Üç yüz otuz üç bin… üç yüz otuz üç lira, hayatım.", "sesi her kelimede küçülerek")
r("NACİ", "Otuz üç de kuruşu var.", "yardımsever")
r("SELİN", "Amca, burada üç kişi yaşıyorsunuz. Bu kadar elektriği kim yaktı ya?")
r("NACİ", "Meydandaki lambalar. … On iki senedir yanıyor. Gerisi faiz.")
e("Köy meydanı: güpegündüz yanan dört sokak lambası. Biri titrer, yanmaya devam eder.")
r("RIZA", "Ya tamam, sorun yok! Kapatırız, biter. Şalter nerede amca?", "çözüm bulmuş adam")
r("NACİ", "Muhtarda.")
r("RIZA", "Süper! Hemen bir toplantı ayarlayalım muhtarla.")
r("NACİ", "Kendisi şurada.", "çenesiyle işaret eder")
e("Yerdeki tabelanın yanında keçi. Ekran yazısı: MUHTAR.")
r("SELİN", "Rıza… bu muhtar keçi.")
r("RIZA", "Demokratik bir süreç olmuştur aşkım.", "hiçbir şey yokmuş gibi")
r("NACİ", "Üç oyla seçildi.", "sessiz bir gururla")
r("SELİN", "Hadi git konuş.")
r("RIZA", "Keçiyle mi ya?")
r("SELİN", "Muhtarla, hayatım.", "tatlı tatlı")

h2("Bölüm 3 — Toplantı")
k("69 saniye · köy girişi, sokak, meydan · Emine ile tanışma")
p("<b>Özet:</b> Rıza keçiyle “toplantıya” girer; keçi faturayı kapıp kaçar; kovalamaca meydanda Emine'nin önünde biter. Anahtar ondadır ve bir şartı vardır. <b>Bitiş sorusu:</b> Emine'nin şartı ne?")
e("Ekran yazısı: KOCAM KEÇİYLE TOPLANTIYA GİRDİ. Dosya Rıza'nın kolunda. Selin başparmağıyla arkayı, keçiyi gösterir.")
r("SELİN", "Hadi aşkım. Toplantın var.", "iğneli, şarkı söyler gibi")
e("Rıza keçinin önünde çömelir, yakasını düzeltir.")
r("RIZA", "Sayın Muhtar…", "resmî, fazla kibar")
e("Keçi çiğner, kulağını oynatır.")
r("RIZA", "Rıza ben. Yeni ortağınız. … Şalteri kapatıyoruz, tasarrufu paylaşıyoruz. Kazan kazan!")
e("Selin, Naci'nin yanında, eli ağzında gülmesini tutuyor.")
r("NACİ", "Öncekiler slayt getirmişti.", "kuru")
r("RIZA", "Bakın, fatura burada. Üç yüz otuz üç bin—", "cebinden faturayı çıkarır")
e("Keçi kâğıdı ağzıyla kapar ve köyün içine fırlar.")
r("RIZA", "Fatura!", "çığlık gibi")
r("SELİN", "Koş Rıza, koş!", "kahkahayla, bağırarak")
r("NACİ", "Yetişemez.", "çayına bakarak")
r("RIZA", "Sayın Muhtar! Muhtar Bey! Bir dakika!", "koşarken")
e("Meydan. Keçi, çeşmenin yanında yumrukları belinde duran Emine'nin dizinin dibinde durur. Emine faturayı ağzından alır.")
r("EMİNE", "Sen kimsin?", "sert, tek kaşı havada")
r("RIZA", "Yeni… sahip…", "soluk soluğa")
r("EMİNE", "Sahip mi?!", "kahkahayla")
r("EMİNE", "Şalter Muhtar'da. Muhtar bende. Anahtar da burada.", "boynundaki anahtarı sallar")
r("RIZA", "Verir misiniz?", "yalvaran satışçı")
r("EMİNE", "Veririm. Bir şartla.", "anahtarı yumruğuna kapatıp")
e("Rıza'nın gülümsemesi donar. Ekranda: EMİNE'NİN ŞARTI NE? · Tahminini yoruma yaz · Takip et.")
A.append(PageBreak())

# ───────────────────────── 6
h1("6. Şu an kim nerede, ne kimin elinde")
k("Bölüm 3'ün son karesi itibarıyla. Bölüm 4 buradan başlar.")
tablo([
    ["Kim / ne", "Nerede"],
    ["Rıza", "Meydanda, Emine'nin karşısında (solda), soluk soluğa, eli uzanmış."],
    ["Emine", "Meydanda, çeşmenin yanında (sağda). Anahtar yumruğunda; fatura onda."],
    ["Muhtar (keçi)", "Meydanda, Emine'nin dizinin dibinde."],
    ["Selin", "Giriş sokağında, Naci'nin yanında ayakta; kahkahadan gözü yaşlı. Elleri boş."],
    ["Naci", "Taburesinde, çayıyla."],
    ["Tapu dosyası", "Köy girişinde, yerde (Rıza koşarken düşürdü)."],
    ["Sarı zarf", "Rıza'nın ceketinin iç cebinde."],
    ["Fatura", "Emine'nin elinde."],
    ["Lambalar", "Hâlâ yanıyor. Borç işlemeye devam ediyor."],
    ["Zaman", "İlk günün ikindisi. Öncekilerin rekoru: üç gün."],
], [0.25, 0.75])

# ───────────────────────── 7
h1("7. Sonraki bölümler: plan önerisi")
p("Bu bölüm <b>öneridir</b>; hiçbiri onaylanmadı. Sezon iskeleti rapordaki 24 bölümlük yapıya dayanır: 2–6 yerleşme ve köylüler (bölüm başına bir tanışma), 7–12 köyü “şehir” yapma planı ve orta nokta sürprizi, 13–20 tırmanma (evlilik ve şehirdeki iş tehlikede), 21–24 final.")
p("Önerilen omurga: <b>üç gün.</b> Öncekiler üç gün dayandı. Emine'nin şartı çifti köyde tutar; izleyicinin sorusu “üçüncü günü çıkarabilecekler mi” olur. Her bölüm o günlerin bir parçasıdır.")

h2("Bölüm 4 — Şart (öneri)")
tablo([
    ["Tek cümle", "Emine'nin şartı: çift üç gece köyde kalacak; “öncekiler gibi” kaçmak yok. Pazarlığı Rıza değil Selin yapar."],
    ["Kanca", "Emine'nin kapalı yumruğu ve “Bir şartla.” Ekran yazısı: KOCAM ANAHTAR İÇİN PAZARLIĞA OTURDU."],
    ["Akış", "Emine üç parmağını kaldırır, sayacakmış gibi yapar, tek şart söyler: “Üç gece.” Rıza hemen kabul eder (“Deal!”). O sırada Selin meydana gelir, yolda yerdeki dosyayı almıştır; Rıza'yı kenara çeker, masaya kendisi oturur: “Üç gece kalırız. Ama lambalar bu gece sönecek.” Emine ilk kez birini ciddiye alır. El sıkışırlar."],
    ["Selin'in kararı", "Pazarlığı devralır; kalmaya o karar verir."],
    ["Şakalar", "“Üç”: üç gece. Plaza dili: “Deal”, “sözleşme”. Keçi: Rıza'nın uzattığı kartviziti kapar."],
    ["Bitiş sorusu", "Rıza: “Peki nerede kalacağız?” Emine: “Hüseyin gösterir.” Selin: “Hüseyin kim?” → Hüseyin kim, ev nasıl bir ev?"],
    ["Üretim notu", "Mekân meydan. Dosya yerden alınır (nesne takibi). Selin'in planları Rıza ya da Emine ile ikili."],
], [0.2, 0.8], baslik=False)

h2("Bölüm 5 — Olur (öneri)")
tablo([
    ["Tek cümle", "Hüseyin'le tanışırız: her şeye “olur” der, hiçbirini yapmaz. Çifti kalacakları eve götürmesi bir bölüm sürer."],
    ["Tanışma", "Hüseyin."],
    ["Akış", "Rıza: “Evi gösterir misiniz?” “Olur.” Kıpırdamaz. “Şimdi?” “Olur.” Kıpırdamaz. Selin çözer: Emine'ye seslenir; Emine bir kez bağırır, Hüseyin kalkar. Ev: kapısı var, çatısının yarısı yok."],
    ["Bitiş sorusu", "Rıza: “Açık konsept.” Selin'in yüzü. → Bu gece burada mı uyuyacaklar?"],
], [0.2, 0.8], baslik=False)

h2("Bölüm 6 — İlk Gece (öneri)")
tablo([
    ["Tek cümle", "İlk gece: telefon köyde tek bir noktada çeker; o nokta Naci'nin taburesidir."],
    ["Akış", "Selin'in işten araması gelir; çekmesi için tabureye çıkması gerekir, Naci kalkmaz. Gece, yıldızlar, yanan lambalar: Selin ilk kez köyü güzel bulur ama söylemez. Rıza: “Kızgın mısın?” Selin: “Ben daha seni seviyor muyum, onu düşünüyorum.” (ilk taslaktan saklanan replik)"],
    ["Bitiş sorusu", "Lambalar gece yarısı hâlâ yanıyor. Emine sözünü tutacak mı?"],
], [0.2, 0.8], baslik=False)

h2("Bölüm 7 — Şalter (öneri)")
tablo([
    ["Tek cümle", "Anahtar verilir, şalter iner; lambalarla birlikte beklenmedik bir şey de söner."],
    ["Akış", "Trafo kulübesi (yeni mekân). Rıza törenle şalteri indirir: “Tasarruf moduna geçtik.” Lambalar söner. Naci'nin çaydanlığı, Emine'nin süt sağma makinesi, köydeki her şey de söner: köyün bütün elektriği o tek hatta bağlıdır."],
    ["Bitiş sorusu", "Naci, soğuyan çayına bakarak: “Öncekiler de kapatmıştı.” → Lambalar neden on iki yıldır açık bırakıldı?"],
], [0.2, 0.8], baslik=False)

h2("Bölüm 8–12 — Köyü “şehir” yapma planı (taslak)")
m("<b>8:</b> Lambaların sebebi. Öneri: on iki yıl önce biri köyden gitti ve “dönersem ışığı göreyim” dedi; köy o günden beri söndürmedi. Dizinin duygusal çekirdeği; Selin'in köye bakışı burada değişir.",
  "<b>9:</b> Selin hesabı yapar: borç, faiz, köyün geliri (sıfır). Tahtaya “bütçe” yazar; ilk kalem keçi peyniri.",
  "<b>10:</b> Rıza'nın “şehir” planı: tabelayı diker, ikinci bir tabela yazar. Keçi ikisini de yer.",
  "<b>11:</b> Üçüncü gün. Çift, öncekilerin rekorunu geçer mi? Kaçma fırsatı çıkar: araba, anahtar, açık yol.",
  "<b>12 (orta nokta):</b> Öncekilerden biri geri gelir ya da köye yeni bir alıcı talip olur. Köyün gizli bir değeri olduğu anlaşılır.")
h2("Bölüm 13–24 (yön)")
m("<b>13–20:</b> Tırmanma. Rakip alıcıyla mücadele; Rıza'nın şehirdeki işi ve çiftin evliliği tehlikeye girer; Selin ile Rıza'nın istekleri yer değiştirir (Rıza satmak ister, Selin kalmak).",
  "<b>21–24:</b> Final: köy satılır mı? Nüfus üçten kaça çıkar? İkinci sezon kancası.")
A.append(PageBreak())

# ───────────────────────── 8
h1("8. Açık sorular ve kararlar")
k("Bunlar kesinleşince dizi kitabına ve bölüm senaryolarına işlenir.")
tablo([
    ["Konu", "Durum"],
    ["Emine'nin şartı", "Öneri: üç gece köyde kalmak. Karar senin."],
    ["Köyün adı", "Hiç söylenmedi. Bir isim seçilmeli ya da bilerek “şehir” denmeye devam edilmeli."],
    ["Lambalar neden yanıyor", "Öneri: gidenin dönüşü için. Alternatif: kimse şalterin yerini hatırlamıyor (yalnızca komedi)."],
    ["Köyün satış fiyatı", "Hiç söylenmedi; yalnızca “ev için ayırdığımız kadar”. Rakam vermek bahsi büyütür."],
    ["Köyün üç sakini", "Naci, Emine, Hüseyin. Muhtarı seçen üç oy da onlar."],
    ["Çiftin şehirdeki hayatı", "Henüz yok. Ev sahnesi (geri dönüş) kararı açık."],
    ["Hüseyin'in görselleri", "İfade ve jest sayfaları B05'ten önce üretilmeli."],
    ["Yeni mekânlar", "Çiftin evi, trafo kulübesi, Emine'nin ağılı: her biri gösterileceği bölümden önce plaka olarak üretilir ve krokiye işlenir."],
    ["Kıyafet", "Karakterler şimdilik hep aynı kıyafette (aynı gün). İlk gece ve sonraki günler için ikinci kıyafet gerekecek."],
], [0.28, 0.72])


def sayfa(c, d):
    c.setFont("D", 7.5); c.setFillColor(GRI)
    c.drawString(18 * mm, 10 * mm, "SIFIR ŞEHİR · dizi kitabı")
    c.drawRightString(A4[0] - 18 * mm, 10 * mm, str(d.page))


SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=17 * mm,
                  title="Sıfır Şehir — dizi kitabı", author="Sıfır Şehir").build(A, onFirstPage=sayfa, onLaterPages=sayfa)
print(OUT)
