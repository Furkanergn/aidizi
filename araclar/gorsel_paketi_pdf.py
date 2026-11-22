#!/usr/bin/env python3
"""ChatGPT'ye gönderilecek görsel üretim paketi (PDF). Her görev kendi sayfasında başlar ve referans görselleri hemen ardından gelir.
Çalıştır: python3 araclar/gorsel_paketi_pdf.py"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from PIL import Image
V="diziler/sifir-sehir/varliklar"; B1="diziler/sifir-sehir/bolumler/B01/kareler/onayli"
OUT=f"{V}/ek-b03/B03_ek_gorseller_chatgpt.pdf"
pdfmetrics.registerFont(TTFont("D","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

STYLE=("Stylized 3D animated feature film look, the same film as the reference images: slightly enlarged eyes, smooth simplified animated-film skin with no pores, "
"realistic cloth and hair detail, soft warm lighting. NOT photorealistic, NOT a photo, NOT 2D, NOT anime. Highest quality: sharp focus, clean edges, correct hands with five fingers, no extra limbs, no warped faces.")
SELIN=("Selin: woman in her early thirties, golden blonde curls to the jaw, freckles across nose and cheeks, dimples, brown eyes, small gold hoop earrings, "
"pink ribbed top with flutter sleeves tucked into a burgundy tiered midi skirt, tan flat shoes.")
RIZA=("Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream open-collar shirt, "
"brown trousers with a brown belt, burgundy loafers. He is half a head taller than Selin.")
EMINE=("Emine: sturdy woman in her mid sixties, grey hair in a braided bun under a burgundy floral headscarf tied at the back, thick dark-grey eyebrows, brown eyes, small gold hoop earrings, "
"rust-brown cable-knit buttoned vest with two pockets over a navy floral dress with rolled-up sleeves, black rubber boots.")
SHEET="Plain light beige studio background, even soft warm key light from the left, the same on every figure. No text, no labels, no numbers, no captions, no borders between figures, no extra people."

G=[]  # (kod, başlık, oran, açıklama (tr), prompt (en), kontrol (tr), referanslar [(dosya, ne işe yarar)])
G.append(("G1","Selin — ikinci ifade sayfası (güçlü duygular)","YATAY 3:2 (1536×1024)",
"Selin'in mevcut ifade sayfasındaki yüzler hep kısık. Bu sayfa güçlü duyguları ekler. Kıyafet, saç, yüz birebir aynı kalır; yalnızca ifade değişir.",
f"""Character expression sheet of the SAME woman shown in the reference images. Keep her face, hairstyle, freckles, proportions and clothes EXACTLY as in the references. {SELIN}

Layout: one single landscape image, two rows of four head-and-shoulders portraits, eight portraits in total, evenly spaced, all the same size, all in three-quarter view (no pure side profile). Shoulders and upper chest visible in each.

The eight expressions, in this order (left to right, top row then bottom row):
1. laughing out loud, head tipped back a little, eyes squeezed, mouth wide open, teeth showing
2. furious, shouting, eyebrows pulled down hard, mouth open wide mid-shout
3. exasperated eye-roll, eyes turned up, lips pressed, a sharp exhale
4. reproachful and hurt ("how could you"), eyebrows up in the middle, head tilted, mouth slightly open
5. shocked, eyebrows high, eyes wide, mouth open
6. trying NOT to laugh: lips pressed tight and trembling, cheeks puffed, eyes sparkling
7. mocking, one eyebrow high, crooked smirk, chin raised
8. warm genuine smile, dimples deep, eyes soft

{STYLE}
{SHEET}""",
"8 portre var mı (2 sıra × 4)? · Hepsi aynı kadın mı: sarı bukleler çeneye kadar, çiller, altın halka küpe, pembe üst? · 8 ifade birbirinden açıkça farklı mı ve sıraları doğru mu? · Yazı ya da numara yok mu? · Stil referanslarla aynı mı (3D animasyon, fotoğraf değil)?",
[(f"{V}/mevcut/sheet_selin.jpg","Selin karakter sayfası: yüz, saç, kıyafet, oranlar buradan alınır"),(f"{V}/onayli/V2_selin_ifade.jpg","Selin'in mevcut ifade sayfası: stil, ışık ve sayfa düzeni buradaki gibi olur")]))
G.append(("G2","Selin — beden ve jest sayfası (dosyasız, tam boy)","YATAY 3:2 (1536×1024)",
"Selin'in elleri boşken nasıl durduğunu ve jest yaptığını sabitler. Elinde HİÇBİR ŞEY yok (dosya, çanta, telefon yok).",
f"""Full-body pose sheet of the SAME woman shown in the reference images. Keep her face, hairstyle, proportions and clothes EXACTLY as in the references. {SELIN} Her hands are EMPTY in every pose: no folder, no bag, no phone, nothing.

Layout: one single landscape image, ONE row of five full-body figures of the same woman, head to shoes fully visible, evenly spaced, all the same height, feet on the same floor line.

The five poses, in this order from left to right:
1. both fists on her hips, weight on one leg, chin up, annoyed
2. right arm stretched out pointing at something off to the side, left fist on her hip, mouth open mid-sentence, scolding
3. both arms out to the sides, palms up, shoulders raised, eyebrows up: "what is this?!"
4. right palm pressed to her forehead (facepalm), eyes closed, left arm across her waist
5. arms loosely crossed, leaning back a little, laughing

{STYLE}
{SHEET}""",
"5 tam boy figür var mı, baştan ayakkabıya görünüyor mu? · Hepsi aynı kadın ve aynı kıyafet mi (pembe üst eteğin içinde, bordo katlı etek, ten rengi düz ayakkabı)? · Eller boş mu? · Her elde beş parmak var mı? · Yazı yok mu?",
[(f"{V}/mevcut/sheet_selin.jpg","Selin karakter sayfası: yüz, saç, kıyafet, boy oranları buradan alınır")]))
G.append(("G3","Rıza — beden ve jest sayfası (tam boy)","YATAY 3:2 (1536×1024)",
"Rıza'nın hareketli pozlarını sabitler: çömelme, koşma, sunum yapma.",
f"""Full-body pose sheet of the SAME man shown in the reference images. Keep his face, hairstyle, proportions and clothes EXACTLY as in the references. {RIZA.replace(' He is half a head taller than Selin.','')}

Layout: one single landscape image, ONE row of five full-body figures of the same man, head to shoes fully visible, evenly spaced, feet on the same floor line.

The five poses, in this order from left to right:
1. standing, both arms opened wide like a salesman presenting something, big confident grin
2. crouching down on his heels, forearms on his knees, leaning forward, polite hopeful smile, as if talking to a small animal
3. running in profile toward the right, arms pumping, blazer flapping, panicked face, mouth open
4. standing bent forward with both hands on his knees, out of breath, hair messier, mouth open, exhausted
5. standing, both hands raised to shoulder height, palms forward, shoulders up, sheepish apologetic smile

His hands are empty in every pose.
{STYLE}
{SHEET}""",
"5 tam boy figür var mı? · Hepsi aynı adam ve aynı kıyafet mi (lacivert ceket, kırmızı cep mendili, krem gömlek, kahverengi pantolon, bordo makosen)? · Poz sırası doğru mu: sunum, çömelme, koşma, soluklanma, teslim? · Eller boş ve beş parmaklı mı? · Yazı yok mu?",
[(f"{V}/mevcut/sheet_riza.jpg","Rıza karakter sayfası: yüz, saç, kıyafet, boy oranları buradan alınır"),(f"{V}/onayli/V1_riza_ifade.jpg","Rıza ifade sayfası: yüz ifadeleri ve stil buradan alınır")]))
G.append(("G4","Emine — ifade sayfası (stil eşitlemesiyle)","YATAY 3:2 (1536×1024)",
"Emine yeni karakter. İlk referanstaki kadın, ikinci referanstaki ÇİZİM STİLİNE çekilir. İkinci referanstaki adam bu görselde YOKTUR; yalnızca stil örneğidir.",
f"""Character expression sheet of the SAME old woman shown in the FIRST reference image. Keep her face shape, headscarf, hair, earrings and clothes exactly as in the first reference. {EMINE}

Important: redraw her at the SAME level of stylization as the old man in the SECOND reference image, so both clearly belong to the same animated film: slightly enlarged eyes, simplified smooth skin with a few clean wrinkle lines, no pores, no photorealistic skin texture. The old man from the second reference must NOT appear in the image; he is only a style example.

Layout: one single landscape image, ONE row of six head-and-shoulders portraits of the same woman, evenly spaced, all the same size, all in three-quarter view (no pure side profile).

The six expressions, in this order from left to right:
1. warm, motherly smile, eyes crinkled
2. stern, lips pressed, one eyebrow raised: "don't you dare"
3. sharp bargaining look, eyes narrowed, tiny sly smile
4. calling out loudly, mouth wide open, chin up
5. hearty laugh, head back a little
6. unimpressed, flat stare, arms-crossed attitude, chin slightly down

{STYLE}
{SHEET}""",
"6 portre var mı, tek sıra? · Hepsi aynı kadın mı: bordo çiçekli başörtüsü, gri saç, altın halka küpe, kiremit rengi örgü yelek, lacivert çiçekli elbise? · Görselde erkek YOK mu? · Cilt fotoğraf gibi mi (YANLIŞ) yoksa ikinci referanstaki gibi sade animasyon cildi mi (DOĞRU)? · Yazı yok mu?",
[(f"{V}/mevcut/sheet_emine.jpg","BİRİNCİ referans: Emine. Yüz, başörtüsü, kıyafet buradan alınır (bu sayfa fazla gerçekçi; stili DEĞİL, kişiyi al)"),(f"{V}/onayli/V3_naci_ifade.jpg","İKİNCİ referans: yalnızca STİL örneği (animasyon düzeyi, cilt, ışık, sayfa düzeni). Buradaki adam çizilmez")]))
G.append(("G5","Keçi — hareket sayfası","YATAY 3:2 (1536×1024)",
"Keçinin hareketli pozları: koşma, inat, ağzında kâğıt.",
f"""Pose sheet of the SAME goat shown in the reference image. Keep it exactly as in the reference: a medium-sized white village goat with one brown ear, short curved horns, a small beard, heavy-lidded bored eyes, a frayed red rope collar with a small brass bell.

Layout: one single landscape image, ONE row of four full-body figures of the same goat, evenly spaced, hooves on the same floor line.

The four poses, in this order from left to right:
1. running in profile toward the right at full gallop, ears back, a crumpled white sheet of paper clamped in its mouth
2. standing stiff with all four legs braced, head lowered, refusing to move, stubborn glare
3. standing three-quarter front view, chewing a crumpled white sheet of paper, half of it hanging from its mouth, eyes half closed, completely unbothered
4. sitting down on its haunches like a dog, looking up, bored

{STYLE}
{SHEET}""",
"4 keçi figürü var mı? · Hepsi aynı keçi mi: beyaz, TEK kulak kahverengi, kısa kıvrık boynuz, küçük sakal, kırmızı ip tasma ve pirinç çan? · 1. ve 3. pozda ağzında beyaz kâğıt var mı? · Kâğıtta yazı yok mu? · İnsan yok mu?",
[(f"{V}/onayli/V7_keci.jpg","Keçi sayfası: görünüş, renk, tasma, stil buradan alınır")]))
G.append(("G6","Deneme karesi SB30 — Selin dosyasız, Rıza dosyayı tutuyor","DİKEY 2:3 (1024×1536); sonra 9:16'ya kırpılacak, o yüzden iki karakter de ortada kalsın, yanlarda boşluk olsun",
"Video denemesinin başlangıç karesi. Birinci referanstaki kareyle AYNI yer, AYNI ışık, AYNI iki kişi; ama kadraj bel hizasına kadar genişler, dosya artık Rıza'dadır ve Selin sinirli bir jestin ortasındadır.",
f"""Stylized 3D animated feature film still, vertical. ONE single continuous image: no split screen, no panels, no borders, no captions, no text.

The SAME two people, in the SAME place and the SAME golden late-afternoon light as the first reference image (village road behind them, a dark grey car far in the background on the left, a hazy green hillside). Selin stands on the LEFT, Rıza on the RIGHT, shoulder to shoulder. The framing is WIDER than the reference: both are visible from the hips up, with their hands in frame.

{SELIN} Her hands are EMPTY: she is NOT holding a folder. Her LEFT fist is on her hip. Her RIGHT arm is raised to chest height, palm up, fingers spread, an impatient "explain this to me" gesture. Her head is turned toward the LEFT edge of the frame, looking at someone outside the frame. Her face is openly annoyed: eyebrows pulled together and raised, eyes wide, mouth open as if she has just started to speak.

{RIZA} He holds a closed burgundy leather A4 folder with a thin elastic band tucked under his LEFT arm (the arm on the right side of the frame), pressed against his ribs; the folder is about as long as his forearm. His RIGHT arm hangs at his side. He also looks toward the left edge of the frame, with a small nervous smile and raised eyebrows.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean. Sharp focus on both faces, background slightly soft. Nobody looks at the camera.
{STYLE}""",
"İki kişi de kalçadan yukarı görünüyor mu, elleri kadrajda mı? · Selin'in elleri BOŞ mu (dosya yok)? Sol yumruğu belinde, sağ avucu yukarı açık mı? · Dosya Rıza'nın sol kolunun altında mı? · Selin'in yüzü belirgin biçimde sinirli mi (düz ifade YANLIŞ)? · İkisi de sola, kadraj dışına bakıyor mu; kameraya bakan yok mu? · Yüzler, saçlar, kıyafetler referanslarla aynı mı? · Mekân ve ışık birinci referansla aynı mı? · Eller beş parmaklı mı? · Yazı yok mu?",
[(f"{B1}/SB11.jpg","BİRİNCİ referans: onaylı kare. Mekân, ışık, iki karakterin yüzü, kıyafeti ve yan yana duruşu buradan alınır. Kadraj bundan GENİŞ olacak, dosya el değiştirecek"),(f"{V}/mevcut/sheet_selin.jpg","Selin karakter sayfası: belden aşağısı (etek) ve oranlar için"),(f"{V}/mevcut/sheet_riza.jpg","Rıza karakter sayfası: belden aşağısı (kemer, pantolon) ve oranlar için"),(f"{V}/onayli/nesne_dosya_kapali.jpg","Kapalı dosya: yalnızca dosyanın görünüşü için")]))

W,H=A4; M=46
c=canvas.Canvas(OUT,pagesize=A4)
state={"y":H-M,"page":1}
def newpage(size=A4):
    c.showPage(); state["page"]+=1; c.setPageSize(size); state["y"]=H-M
def write(k,t):
    f,s,l=("DB",13,18) if k=="h" else ("DB",10,14.5) if k=="b" else ("D",8.4,11.6) if k=="c" else ("D",10,14.5)
    if k=="h": state["y"]-=6
    for par in t.split("\n"):
        for line in (simpleSplit(par,f,s,W-2*M) or [""]):
            if state["y"]<M+l: newpage()
            c.setFont(f,s); c.drawString(M,state["y"],line); state["y"]-=l
    state["y"]-=5

# sayfa numaralarını önceden hesaplamak için iki geçiş: önce kuru geçiş
def build(pages):
    write("h","Sıfır Şehir — ek görsel paketi (ChatGPT için)")
    write("p","Bu PDF'i okuyan ChatGPT için talimat. Bir animasyon dizisi için 6 görsel üreteceksin. Aşağıdaki kuralları eksiksiz uygula; emin olmadığın yerde tahmin yürütme, sor.")
    write("h","1. Çalışma düzeni (en önemli kural)")
    write("p","• Görevler G1'den G6'ya sırayla yapılır. HER MESAJDA YALNIZCA BİR GÖRSEL üret. Görseli verdikten sonra dur ve kullanıcının 'devam' yazmasını bekle; yazınca sıradaki göreve geç.")
    write("p","• Her görevin kendi referans görselleri vardır ve o görevin sayfasının HEMEN ARKASINDAKİ sayfalardadır. Bir görevde YALNIZCA o görevin referanslarını kullan. Başka görevin referansındaki kişiyi, nesneyi ya da mekânı görsele koyma. Önceki görevde ürettiğin görseli sonraki görevde referans alma.")
    write("p","• İki görevi tek görselde birleştirme. Kolaj yapma.")
    write("h","2. Referansları kullanma")
    write("p","• Referanslar PDF sayfalarına özgün JPEG olarak gömülüdür. Görsel üretim aracına onları GÖRSEL olarak ver (referanslı üretim / düzenleme). Sayfaları doğrudan kullanamıyorsan önce kod aracıyla PDF'ten ilgili sayfaların görsellerini çıkar (pypdf ya da PyMuPDF) ve o dosyaları referans olarak ver.")
    write("p","• Referansları hiç görsel olarak kullanamıyorsan ÜRETME. Kullanıcıya şunu yaz: 'Referansları kullanamıyorum, şu sayfalardaki görselleri ayrıca yükle: …'. Yalnızca metinden üretilmiş karakter kabul edilmez, çünkü yüz tutmaz.")
    write("h","3. Kalite")
    write("p","• En yüksek kalite ayarını kullan (quality: high). Boyut her görevde yazılı: yatay görevlerde 1536×1024, dikey görevde 1024×1536. Daha küçük üretme.")
    write("p","• Stil her görselde aynı: stilize 3D animasyon filmi karesi; fotoğraf, 2D çizim, anime DEĞİL. Net odak, temiz kenarlar, bozulmamış yüzler, beş parmaklı eller.")
    write("p","• Görsellere yazı, etiket, numara, logo, filigran, çerçeve koyma.")
    write("h","4. Tutarlılık (karakterler her görselde aynı kişi olmalı)")
    write("p","Aşağıdaki tarifler değişmez. Promptlarda da aynen geçer; hiçbirini değiştirme, süsleme, 'iyileştirme'.")
    write("c","• "+SELIN); write("c","• "+RIZA); write("c","• "+EMINE)
    write("c","• Keçi: orta boy beyaz köy keçisi, TEK kulağı kahverengi, kısa kıvrık boynuzlar, küçük sakal, yarı kapalı bıkkın gözler, yıpranmış kırmızı ip tasma ve küçük pirinç çan.")
    write("p","Yaş, saç rengi ve uzunluğu, kıyafet parçaları ve renkleri, küpe, çil, sakal, boy farkı referanstakiyle aynı kalır. Karakteri gençleştirme, güzelleştirme, makyaj ekleme, kıyafeti modernleştirme.")
    write("h","5. Promptlar")
    write("p","Promptlar İngilizcedir. Kelimesi kelimesine kullan; kısaltma, yeniden yazma, çevirme.")
    write("h","6. Her görselden sonra")
    write("p","Görevin 'Kontrol' listesine kendin bak. Bir madde tutmuyorsa aynı promptla bir kez daha üret. İkincide de tutmuyorsa dur ve hangi maddenin tutmadığını yaz; üçüncü kez üretme. Tutuyorsa görseli tam çözünürlükte ver, başına görev kodunu yaz (örnek: 'G1') ve 'devam' beklediğini söyle.")
    write("h","7. Görev listesi")
    for g,(p0,refp) in zip(G,pages):
        write("p",f"{g[0]} · {g[1]} · {g[2].split(' (')[0]} · görev sayfası {p0}, referanslar sayfa {', '.join(map(str,refp))}")
    out=[]
    for g,(p0,refp) in zip(G,pages):
        kod,bas,oran,acik,prompt,kontrol,refs=g
        newpage(); start=state["page"]
        write("h",f"GÖREV {kod}: {bas}")
        write("b",f"Boyut ve oran: {oran} · Kalite: en yüksek")
        write("p",acik)
        write("b","Bu görevin referansları (yalnızca bunlar):")
        for (f,ne),pn in zip(refs,refp): write("p",f"• Sayfa {pn}: {ne}")
        write("b","Prompt (kelimesi kelimesine):"); write("c",prompt)
        write("b","Kontrol:"); write("p",kontrol)
        rp=[]
        for f,ne in refs:
            w,h=Image.open(f).size
            c.showPage(); state["page"]+=1; c.setPageSize((w,h)); c.drawImage(f,0,0,w,h); rp.append(state["page"])
        c.setPageSize(A4)  # sonraki newpage için
        out.append((start,rp))
        # görsel sayfasından sonra A4'e dönmek için işaret
        state["after_img"]=True
    return out
# kuru geçiş
import io
real=c
c=canvas.Canvas(io.BytesIO(),pagesize=A4); state={"y":H-M,"page":1}
pages=build([(0,[0]*len(g[6])) for g in G])
c=canvas.Canvas(io.BytesIO(),pagesize=A4); state={"y":H-M,"page":1}
pages2=build(pages)
assert pages==pages2, (pages,pages2)
c=canvas.Canvas(OUT,pagesize=A4); state={"y":H-M,"page":1}
build(pages); c.showPage(); c.save()
print(OUT, pages)
