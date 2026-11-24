#!/usr/bin/env python3
"""B04 kare paketi (ChatGPT için tek PDF): talimat, her kare için görev sayfası + hemen ardından o görevin referans görselleri.
Çalıştır: python3 araclar/b04_kareler_pdf.py  →  diziler/sifir-sehir/bolumler/B04/B04_kareler_chatgpt.pdf"""
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from PIL import Image

D = "diziler/sifir-sehir"; V = f"{D}/varliklar"; B4 = f"{D}/bolumler/B04"
B3 = f"{D}/bolumler/B03/kareler/onayli"
OUT = f"{B4}/B04_kareler_chatgpt.pdf"
pdfmetrics.registerFont(TTFont("D", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

SELIN = ("Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with a sweetheart neckline and flutter sleeves, "
         "tucked into a SHORT burgundy two-tier ruffled mini skirt (ends well above the knee), bare legs, brown leather Mary-Jane flats. Keep her exact body proportions from her character sheet (curvy hourglass figure); do not slim her. She is half a head shorter than Rıza.")
RIZA = ("Rıza: man in his mid thirties, tall and slim, messy dark brown curls, long nose, thick dark eyebrows, light stubble, NO moustache, dark navy blazer (unbuttoned) with a red pocket square over a cream open-collar shirt, "
        "brown belt, brown pleated trousers, burgundy tassel loafers. His face must match his character sheet and the attached approved frames: smooth, in his thirties, NOT wrinkled, NOT older.")
NACI = "Naci: thin man in his late sixties, grey swept-back hair, thick grey moustache, bushy grey eyebrows, faded blue work jacket over a checked shirt, grey trousers, brown boots."
EMINE = ("Emine: short, sturdy woman in her mid sixties, round face, thick dark-grey eyebrows, grey hair in a bun under a burgundy floral headscarf tied at the back, small gold hoop earrings, "
         "rust-brown cable-knit vest with two pockets over a navy floral dress with rolled-up sleeves (below the knee), black rubber boots. She is a full head shorter than Rıza. "
         "A thin dark leather cord hangs around her neck; the old iron key on it is tucked INSIDE her vest and is not visible.")
KECI = "The goat: medium-sized cream-white village goat with ONE brown ear, curved horns, a small beard, heavy-lidded bored eyes, a frayed red rope collar with a small brass bell. Its back is at the height of a man's hip."
FOLDER = "a closed burgundy leather A4 folder (brass corners, thin elastic band, about as long as her forearm)"
PHONE = "a slim black smartphone; its screen faces him, so we only see the back of the phone (no readable screen)"
SQUARE = ("Place and light: the village square from the attached approved frames: cobbles, the dry round stone fountain, the big plane tree with yellow leaves, old stone houses with blue shutters, "
          "an old rusty street lamp switched ON in daylight, warm golden late-afternoon sun from the LEFT, long soft shadows. The camera stays on the same side of the people as in the approved frames.")
ORDER = "From LEFT to RIGHT the people always stand in this order: Selin, Rıza, Emine. Never swap them."
END = ("Style: stylized 3D animated feature film still, exactly the look of the attached frames: smooth animated-film skin, realistic cloth and hair, warm golden late-afternoon light. Not photorealistic, not 2D, not anime. "
       "Sharp focus on the faces, background slightly soft. Correct hands with five fingers. Nobody looks at the camera. ONE single continuous image: no split screen, no panels, no borders, no captions, no text, no logos.")
SIZE = "DİKEY 2:3, 1024×1536 · kalite: en yüksek. Sonradan 9:16'ya kırpılacak: kişiler ve önemli her şey görselin ortadaki %85'lik genişliğinde kalsın."

R = {
    "P01": (f"{B4}/klipler/P01/B04_P01_baslangic_karesi.jpg", "onaylı son kare (bir önceki klibin bittiği an): meydan, ışık, Rıza'nın ve Emine'nin yüzü, kıyafeti ve yerleri buradan"),
    "SB39": (f"{B3}/SB39.jpg", "onaylı kare: meydan; keçinin Emine'nin dibindeki yeri, Rıza solda, Emine sağda"),
    "SB41": (f"{B3}/SB41.jpg", "onaylı kare: meydan, ışık; Rıza ve Emine'nin yüzü ve duruşu"),
    "SB38": (f"{B3}/SB38.jpg", "onaylı kare: meydanın geniş açısı (çeşme, çınar, lamba); mekân, kamera ve ışık buradan"),
    "SB35": (f"{B3}/SB35.jpg", "onaylı kare: Naci'nin duvarı, Naci taburede, Selin yanında; mekân, kamera, ışık ve ikisinin yeri buradan"),
    "selin": (f"{V}/mevcut/sheet_selin.jpg", "Selin karakter sayfası: yüz, vücut oranları, kıyafet (kısa bordo fırfırlı etek, babet)"),
    "selin_i2": (f"{V}/onayli/V11_selin_ifade2.jpg", "Selin ifade sayfası: güçlü yüz ifadeleri"),
    "selin_jA": (f"{V}/onayli/V13_selin_jest_A.jpg", "Selin jest sayfası: beden ve el hareketleri"),
    "riza": (f"{V}/mevcut/sheet_riza.jpg", "Rıza karakter sayfası: yüz (ESAS), vücut, kıyafet"),
    "riza_i": (f"{V}/onayli/V1_riza_ifade.jpg", "Rıza ifade sayfası: yüz ifadeleri"),
    "riza_jA": (f"{V}/onayli/V15_riza_jest_A.jpg", "Rıza jest sayfası: kollarını açma, çömelme, koşma pozları"),
    "riza_jB": (f"{V}/onayli/V16_riza_jest_B.jpg", "Rıza jest sayfası: yürüme ve duruş pozları"),
    "naci": (f"{V}/onayli/V3_naci_ifade.jpg", "Naci ifade sayfası"),
    "emine": (f"{V}/onayli/V21_emine_jest.jpg", "Emine tam boy sayfası: vücut, kıyafet, duruşlar"),
    "emine_i": (f"{V}/onayli/V19_emine_ifade.jpg", "Emine ifade sayfası"),
    "emine_i2": (f"{V}/onayli/V20_emine_ifade2.jpg", "Emine ifade sayfası 2: kahkaha dâhil güçlü ifadeler"),
    "keci": (f"{V}/onayli/V7_keci.jpg", "keçi sayfası: görünüş"),
    "dosya": (f"{V}/onayli/nesne_dosya_kapali.jpg", "kapalı bordo dosya: yalnızca nesnenin görünüşü"),
}

G = []  # (kod, klip, başlık, açıklama, [ref], prompt, kontrol)
G.append(("SB50", "P03", "Meydan, geniş: Selin soldan giriyor; Rıza ona dönüyor; Emine ve keçi sağda",
"Birinci referans bir önceki klibin son karesi. Bu kare onun DÜZENLEMESİ: aynı yer, aynı ışık, aynı Rıza ve Emine; kamera biraz geri çekilir ve soldan Selin girer.",
["P01", "SB39", "selin", "selin_i2", "dosya", "keci"],
f"""This is an EDIT of the FIRST attached image (the last frame of the previous shot in the village square). Keep the place, the camera side, the light, the fountain, the plane tree, the lit street lamp, and Rıza's and Emine's faces, hair and clothes EXACTLY as in the first image.

Change 1 - camera: pull the camera back about two metres and slightly to the LEFT, so that the people are seen from the KNEES UP and there is free space on the LEFT side of the frame.

Change 2 - Emine (RIGHT): {EMINE} Both fists on her hips, feet apart, face amused, one eyebrow raised, looking toward Selin on the left.

Change 3 - {KECI} It stands at Emine's feet, between Emine and Rıza, its head and neck visible at the bottom of the frame, looking toward the left.

Change 4 - Rıza (CENTER): {RIZA} His hands are lowered and EMPTY. He turns his head and shoulders toward the LEFT edge of the frame, toward Selin, with a surprised half-smile and raised eyebrows.

Change 5 - add Selin (LEFT): {SELIN} She has just walked in from the LEFT edge and is mid-step, walking toward the right, about one and a half metres to the left of Rıza. Her whole figure from the knees up is INSIDE the frame; her face is in three-quarter view and clearly visible. {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm, pressed against her ribs. Her RIGHT hand is raised at chest height, palm up: "what is going on now?". Her face: suspicious, one eyebrow raised, lips pursed, eyes on Rıza.

{ORDER}
{SQUARE}
No other people.""",
"Selin, Rıza, Emine soldan sağa bu sırada mı? · Üçü de dizden yukarı görünüyor ve kadrajın içinde mi? · Selin adım atarken mi, yüzü net mi? · Dosya Selin'in SOL kolunun altında mı, sağ eli boş ve avucu yukarı mı? · Selin'in eteği KISA bordo fırfırlı mı? · Emine'nin anahtarı görünmüyor, yalnızca ip mi? · Keçi Emine'nin dibinde mi? · Rıza ve Emine'nin yüzü birinci görseldekiyle aynı mı, Rıza'da bıyık yok mu? · Meydan, çeşme, yanan lamba ve ışık aynı mı?"))

G.append(("SB51", "P04", "Meydan, ikili bel üstü: Selin (sol) Rıza'ya soru soruyor",
"Selin ve Rıza yakın ikili. Emine kadrajın hemen sağ dışında (görünmez). Selin konuşmanın ortasında.",
["SB41", "P01", "selin", "selin_i2", "selin_jA", "riza", "dosya"],
f"""Two-shot from the WAIST UP in the village square, the same place, camera side and light as the first two attached images, the camera a little closer. Behind them, softly out of focus: the dry stone fountain and one lit rusty street lamp.
Selin stands on the LEFT, Rıza on the RIGHT, facing each other in three-quarter view, about one metre apart. Emine is just outside the RIGHT edge of the frame (not visible).

{SELIN} {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm, pressed against her ribs. Her RIGHT hand is raised in front of her chest, palm up, fingers spread toward Rıza: a "think about it" gesture. Her face: skeptical and lecturing, both eyebrows raised, head tilted, mouth open in the middle of a sentence, eyes on Rıza.

{RIZA} His hands hang loosely at his sides, EMPTY. He listens: eyebrows up, an uncertain little smile, eyes on Selin.

{SQUARE}
No other people.""",
"Selin solda, Rıza sağda mı, bel üstü mü? · Emine kadrajda değil mi? · Dosya Selin'in sol kolunun altında, sağ eli jest yapıyor mu? · Selin'in yüzü belirgin şüpheci, konuşurken mi (düz ifade YANLIŞ)? · Rıza'nın yüzü onaylı karelerle aynı mı, bıyık yok mu? · Arkada çeşme ve yanan lamba var mı? · Kameraya bakan yok mu?"))

G.append(("SB52", "P05", "Meydan, bel üstü: Rıza kollarını açmış, 'Bedava ev vereceğiz!'; Selin donmuş (KANCA KARESİ)",
"Bölümün açılış kancası bu klipten gelir: Rıza'nın coşkusu ve Selin'in donmuş yüzü çok net olmalı.",
["SB41", "P01", "riza", "riza_i", "riza_jA", "selin", "selin_i2", "dosya"],
f"""Medium shot from the HIPS UP in the village square, the same place, camera side and light as the first two attached images. Behind them, softly out of focus: the stone fountain, the plane tree, one lit rusty street lamp.
Selin stands on the LEFT, Rıza in the CENTER-RIGHT; at the far RIGHT edge of the frame, only Emine's shoulder, headscarf and half of her amused face are visible (she is cut by the frame edge).

{RIZA} He has just had the idea of his life: BOTH arms flung wide open to the sides, palms up, chest pushed out, a huge thrilled grin, eyes shining, mouth wide open in the middle of a shout, looking at Selin. Both his open hands stay INSIDE the frame.

{SELIN} {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm. Her body is turned toward Rıza; her RIGHT hand has stopped in mid-air near her chest. Her face: frozen in disbelief, eyebrows high, eyes wide, mouth slightly open.

Emine (only partly visible at the right edge): one eyebrow raised, amused.
{ORDER}
{SQUARE}
No other people.""",
"Rıza'nın iki kolu açık ve elleri kadrajın İÇİNDE mi? · Rıza'nın yüzü coşkulu, ağzı açık mı; yüzü onaylı karelerle aynı mı, bıyık yok mu? · Selin donmuş şaşkınlıkta mı, dosya sol kolunun altında mı? · Emine yalnızca sağ kenarda kısmen mi görünüyor? · Sıra soldan sağa Selin, Rıza, Emine mi? · Kameraya bakan yok mu?"))

G.append(("SB53", "P07", "Meydan: Rıza'nın omzunun üstünden Selin; kırgın ve öfkeli",
"Bölümün duygusal anı. Rıza'nın başı ve omzu sağ önde, arkadan, büyük ve bulanık; Selin önden, ona bakıyor. Rıza kadrajda net biçimde bulunmalı (Selin tek başına olmamalı).",
["SB41", "selin", "selin_i2", "selin_jA", "riza", "dosya"],
f"""Over-the-shoulder two-shot in the village square, same light as the first attached image. The camera is just behind Rıza, on the same side of the people as in the approved frames.
In the RIGHT third of the frame, close to the camera and softly out of focus: the back of Rıza's head (messy dark brown curls), his right ear and the shoulder of his dark navy blazer, seen from behind. He is clearly a second person in the shot.
{SELIN} She stands in the LEFT-CENTER, about one metre beyond Rıza, seen from the chest up, facing the camera in three-quarter view and looking toward the RIGHT, up into Rıza's face. The top of {FOLDER} is visible under her LEFT arm. Her RIGHT hand is pressed flat on her own chest, fingers spread ("we!"). Her face: hurt AND angry at the same time: eyebrows pulled together and up in the middle, eyes glossy, lips tight, chin raised.
Background, softly out of focus: old stone houses of the square with blue shutters, one lit rusty street lamp, yellow plane tree leaves. Golden late-afternoon light from the left on her face.
No other people.""",
"Rıza'nın başının arkası ve omzu sağ önde, büyük ve bulanık mı (kadrajda açıkça ikinci kişi var mı)? · Selin sol-ortada, göğüs üstü, SAĞA (Rıza'ya) bakıyor mu? · Sağ eli göğsünde mi, dosya sol kolunun altında mı? · Yüzü hem kırgın hem öfkeli mi (gözler parlak, kaşlar ortada kalkık)? · Selin'in yüzü sayfasıyla aynı mı (çiller, kahverengi gözler, altın küpe)? · Kameraya bakmıyor mu?"))

G.append(("SB54", "P09, P10, P11", "Meydan, üçlü: Rıza telefondan ilan yazıyor, keçi telefonu kokluyor",
"Üç kişi kalçadan yukarı. Bu kare üç klipte zincirlenecek, o yüzden üç yüz de net ve temiz olmalı.",
["SB39", "SB41", "selin", "riza", "riza_i", "emine", "keci", "dosya"],
f"""Three-shot from the HIPS UP in the village square, the same place, camera side and light as the first two attached images. Behind them, softly out of focus: the stone fountain in the center, the plane tree, one lit rusty street lamp.
The three stand in a loose half circle facing the camera side, Rıza in the middle and slightly forward.

{RIZA} He holds {PHONE} in BOTH hands at waist height, thumbs on it, typing. His head is bent toward the phone, an eager salesman grin, eyebrows up.

{KECI} Between Rıza and Emine, at the bottom of the frame, the goat has stretched its neck up and is sniffing the phone from below, its nose almost touching it.

{EMINE} She stands on the RIGHT with her arms crossed over her chest, deadpan, one eyebrow raised, looking down at the phone.

{SELIN} She stands on the LEFT. {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm. Her RIGHT fist is on her hip. Head tilted, skeptical, one eyebrow raised, looking at Rıza.

{ORDER}
{SQUARE}
No readable text anywhere. No other people.""",
"Soldan sağa Selin, Rıza, Emine mi; üçü de kalçadan yukarı mı? · Rıza telefonu İKİ eliyle bel hizasında tutuyor mu, ekran görünmüyor mu? · Keçinin başı Rıza ile Emine arasında, telefonu kokluyor mu? · Emine kollarını kavuşturmuş mu, anahtar görünmüyor mu? · Dosya Selin'in sol kolunun altında, sağ eli belinde mi? · Üç yüz de net ve sayfalarla aynı mı, Rıza'da bıyık yok mu? · Kameraya bakan yok mu?"))

G.append(("SB56", "P13, P14", "Meydan, üçlü: SB54'ün düzenlemesi; Rıza sönmüş, Selin alaycı, Emine gülmeye başlıyor",
"BU GÖREVİN BİRİNCİ REFERANSI, BU SOHBETTE AZ ÖNCE ÜRETTİĞİN B04_SB54 GÖRSELİDİR (PDF'te yok). Onu düzenle. Yeni bir sohbetteysen kullanıcıdan B04_SB54'ü yüklemesini iste. Aşağıdaki sayfalardaki referanslar yalnızca yüz ifadeleri için.",
["selin_i2", "riza_i", "emine_i2"],
f"""This is an EDIT of the image B04_SB54 you generated earlier in this conversation (the three-shot in the village square). Keep the place, the camera, the light, the framing, the positions, the faces, the hair and the clothes EXACTLY the same. Change ONLY the poses and expressions:

Rıza (CENTER): he has lowered the phone; it hangs in his RIGHT hand at his side. His shoulders are slumped, his face has fallen: mouth turned down, eyebrows sad, eyes on Selin.
Selin (LEFT): the folder is still under her LEFT arm. Her RIGHT hand is now held out toward Rıza at chest height, palm up, as if presenting him. Her face: a sweet, sarcastic smile, head tilted, eyebrows raised.
Emine (RIGHT): she is starting to laugh: head tipped back a little, mouth open, eyes squeezed, her RIGHT hand on her belly, her LEFT hand still on her crossed arm.
The goat: at the bottom between Rıza and Emine, chewing, looking up at Rıza.

{ORDER}
Nobody looks at the camera. No readable text. ONE single continuous image.""",
"Görsel B04_SB54'ün aynısı mı (yer, kadraj, kişilerin yerleri, kıyafetler)? · Rıza'nın telefonu sağ elinde, aşağıda mı; yüzü düşmüş mü? · Selin'in sağ avucu Rıza'ya açık, alaycı tatlı gülümseme mi? · Emine gülmeye başlamış, eli göbeğinde mi? · Dosya hâlâ Selin'in sol kolunun altında mı? · Yüzler değişmedi mi?"))

G.append(("SB55", "P12", "Meydan, geniş: Rıza ortada telefonu havaya kaldırmış, sinyal arıyor",
"Birinci referans meydanın onaylı geniş karesi. Bu kare onun DÜZENLEMESİ: kamera üç metre yaklaşır, üç kişi boy boy görünür ve her biri görselin yaklaşık yarısı kadar yüksek olur (yüzler tanınmalı).",
["SB38", "P01", "selin", "riza", "riza_jB", "emine", "dosya"],
f"""This is an EDIT of the FIRST attached image (the approved wide shot of the village square). Keep the square, the camera direction, the light, the fountain, the plane tree and the lit rusty street lamp exactly as they are.

Change 1 - camera: move the camera about three metres FORWARD, so that the people below are seen FULL BODY and each of them is about HALF the height of the image. Their faces must be clear and recognizable.

Change 2 - Emine (RIGHT, beside the fountain, where she stands in the first image): {EMINE} Arms crossed over her chest, a smirk, watching the man in the middle. The goat ({KECI}) stands calmly at her feet, chewing, with NOTHING in its mouth.

Change 3 - add Rıza in the CENTER, in front of the fountain: {RIZA} Full body, standing on tiptoe, his RIGHT arm stretched straight up holding {PHONE} high above his head, his LEFT arm out to the side for balance. His head is tilted back, squinting up at the phone, desperately hopeful. We see his face in three-quarter view.

Change 4 - add Selin on the LEFT: {SELIN} Full body, standing still with her weight on one leg. {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm, her RIGHT fist on her hip. She watches Rıza, unimpressed.

The three are at about the same distance from the camera; nobody is much bigger than the others. Rıza has empty cobbles all around him (room to walk sideways).
{ORDER}
No readable text anywhere. No other people.""",
"Meydan, çeşme, çınar, yanan lamba ilk görseldeki gibi mi? · Üç kişi boy boy ve her biri görselin yaklaşık yarısı kadar mı; yüzler tanınıyor mu? · Rıza ortada, parmak uçlarında, telefon sağ elinde havada mı? · Selin solda, dosya sol kolunun altında, sağ eli belinde mi? · Emine sağda, çeşmenin yanında, kolları kavuşturmuş mu; keçi dibinde, ağzında kâğıt YOK mu? · Rıza'da bıyık yok mu? · Kameraya bakan yok mu?"))

G.append(("SB57", "P15, P16, P17", "Naci'nin duvarı: SB35'in düzenlemesi; Rıza telefonu Naci'nin başının üstünde tutuyor, Selin sağda",
"Birinci referans Naci'nin duvarının onaylı karesi. Bu kare onun DÜZENLEMESİ: duvar, kapı, asma, tabure, Naci aynı; Selin aynı yerde ama artık gülmüyor; Naci'nin SOLUNA Rıza eklenir. Bu kare üç klipte zincirlenecek ve bölümün son karesi olacak.",
["SB35", "riza", "riza_i", "riza_jB", "selin", "selin_i2", "naci", "dosya"],
f"""This is an EDIT of the FIRST attached image (the approved frame at Naci's wall). Keep the stone wall, the blue door, the vine with grapes, the stone shelf, the wooden stool, the cobbles and the light EXACTLY as they are. Keep Naci EXACTLY as he is: same place on the stool, same pose, the tea glass in his RIGHT hand.

Change 1 - camera: pull the camera back about one metre and slightly to the LEFT, so there is room for a third person on the LEFT of Naci. Frame: the three from the knees up (Naci seated).

Change 2 - Naci (CENTER, on the stool): {NACI} He is about to sip his tea, eyes half closed, completely ignoring what is happening above his head.

Change 3 - add Rıza on the LEFT of Naci, standing close to the stool, body turned toward Naci: {RIZA} His LEFT arm (the arm nearer to Naci) is stretched up, holding {PHONE} high, directly ABOVE Naci's head. He looks up at the phone with a triumphant open-mouthed grin, eyebrows high. His RIGHT hand is a small victory fist at chest height.

Change 4 - Selin on the RIGHT of Naci, in the SAME spot as in the first image: {SELIN} She is no longer laughing. {FOLDER[0].upper()+FOLDER[1:]} is tucked under her LEFT arm; her RIGHT fist is on her hip. A skeptical half-smile, one eyebrow raised, looking at Rıza on the left.

From LEFT to RIGHT: Rıza (standing), Naci (sitting), Selin (standing).
Golden late-afternoon light as in the first image. No readable text anywhere. No other people.""",
"Duvar, mavi kapı, asma, tabure, ışık ilk görseldeki gibi mi? · Naci aynı yerde, aynı pozda, çay sağ elinde mi? · Soldan sağa Rıza, Naci, Selin mi? · Rıza'nın sol kolu yukarıda, telefon tam Naci'nin başının ÜSTÜNDE mi; ekran görünmüyor mu? · Selin'in dosyası sol kolunun altında, sağ eli belinde mi; eteği KISA bordo fırfırlı mı? · Üç yüz sayfalarla aynı mı, Rıza'da bıyık yok mu? · Kameraya bakan yok mu?"))

W, H = A4; M = 46
c = None; state = {}


def newpage():
    c.showPage(); state["page"] += 1; c.setPageSize(A4); state["y"] = H - M


def write(k, t):
    f, s, l = ("DB", 13, 18) if k == "h" else ("DB", 10, 14.5) if k == "b" else ("D", 8.4, 11.6) if k == "c" else ("D", 10, 14.5)
    if k == "h": state["y"] -= 6
    for par in t.split("\n"):
        for line in (simpleSplit(par, f, s, W - 2 * M) or [""]):
            if state["y"] < M + l: newpage()
            c.setFont(f, s); c.drawString(M, state["y"], line); state["y"] -= l
    state["y"] -= 5


def build(pages):
    write("h", "Sıfır Şehir — Bölüm 4 kare paketi (ChatGPT için)")
    write("p", f"Bu PDF'i okuyan ChatGPT için talimat. Bir animasyon dizisinin 4. bölümü için {len(G)} film karesi (storyboard) üreteceksin. Bunlar bir önceki bölümün tam devamıdır: aynı gün, aynı ışık, aynı kıyafetler, aynı mekân. Aşağıdaki kuralları eksiksiz uygula; emin olmadığın yerde tahmin yürütme, sor.")
    write("h", "1. Çalışma düzeni (en önemli kural)")
    write("p", "• Görevler listedeki sırayla yapılır. HER MESAJDA YALNIZCA BİR GÖRSEL üret. Görseli verdikten sonra dur ve kullanıcının 'devam' yazmasını bekle; yazınca sıradaki göreve geç. Kullanıcı 'tekrar' derse aynı görevi aynı promptla yeniden üret.")
    write("p", "• Her görevin kendi referans görselleri vardır ve o görevin sayfasının HEMEN ARKASINDAKİ sayfalardadır. Bir görevde YALNIZCA o görevin referanslarını kullan. Başka görevin referansındaki kişiyi, nesneyi ya da mekânı görsele koyma.")
    write("p", "• Tek istisna SB56: o görev, bu sohbette ürettiğin B04_SB54 görselinin düzenlemesidir.")
    write("p", "• İki görevi tek görselde birleştirme. Kolaj, ızgara, yan yana panel yapma.")
    write("h", "2. Referansları kullanma")
    write("p", "• Referanslar PDF sayfalarına özgün JPEG olarak gömülüdür. Görsel üretim aracına onları GÖRSEL olarak ver (referanslı üretim / düzenleme). Sayfaları doğrudan kullanamıyorsan önce kod aracıyla PDF'ten ilgili sayfaların görsellerini çıkar (pypdf ya da PyMuPDF) ve o dosyaları referans olarak ver.")
    write("p", "• 'EDIT' (düzenleme) yazan görevlerde BİRİNCİ referans görseli temel al ve yalnızca yazılan değişiklikleri yap: mekân, kamera, ışık ve kişilerin yüzü aynı kalır. Sahneyi sıfırdan kurma.")
    write("p", "• Referansları hiç görsel olarak kullanamıyorsan ÜRETME. Kullanıcıya şunu yaz: 'Referansları kullanamıyorum, şu sayfalardaki görselleri ayrıca yükle: …'. Yalnızca metinden üretilmiş karakter kabul edilmez, çünkü yüz tutmaz.")
    write("h", "3. Boyut ve kalite")
    write("p", "• " + SIZE)
    write("p", "• Stil her görselde aynı: stilize 3D animasyon filmi karesi; fotoğraf, 2D çizim, anime DEĞİL. Net odak, temiz kenarlar, bozulmamış yüzler, beş parmaklı eller. Görsellere yazı, etiket, numara, logo, filigran, çerçeve koyma.")
    write("h", "4. Karakterler (değişmez tarifler; promptlarda da aynen geçer)")
    for t in (SELIN, RIZA, NACI, EMINE, KECI): write("c", "• " + t)
    write("p", "Yaş, saç, kıyafet parçaları ve renkleri, küpe, çil, sakal, boy farkı referanstakiyle aynı kalır. Karakteri gençleştirme, güzelleştirme, makyaj ekleme, kıyafeti değiştirme. Selin'in eteği HER ZAMAN kısa bordo iki katlı fırfırlı mini etek, ayağında kahverengi babet. Rıza'da bıyık YOK.")
    write("h", "5. Sahne düzeni (her karede geçerli)")
    write("p", "• Meydanda kişiler soldan sağa HER ZAMAN şu sırada durur: Selin, Rıza, Emine. Keçi Emine'nin dibindedir. Kamera her karede grubun aynı tarafındadır (arkada çeşme, sağ arkada çınar, yanan lamba).")
    write("p", "• Selin'in dosyası her karede SOL kolunun altındadır; sağ eli boştur ve jest yapar. Emine'nin anahtarı yeleğinin içindedir, yalnızca boynundaki ip görünür. Kimse kameraya bakmaz.")
    write("h", "6. Promptlar")
    write("p", "Promptlar İngilizcedir. Kelimesi kelimesine kullan; kısaltma, yeniden yazma, çevirme.")
    write("h", "7. Her görselden sonra")
    write("p", "Görevin 'Kontrol' listesine kendin bak. Bir madde tutmuyorsa aynı promptla bir kez daha üret. İkincide de tutmuyorsa dur ve hangi maddenin tutmadığını yaz; üçüncü kez üretme. Tutuyorsa görseli tam çözünürlükte ver, başına dosya adını yaz (örnek: 'B04_SB50') ve 'devam' beklediğini söyle.")
    write("h", "8. Görev listesi")
    for g, (p0, refp) in zip(G, pages):
        write("p", f"{g[0]} (klip {g[1]}) · {g[2]} · görev sayfası {p0}" + (f", referanslar sayfa {refp[0]}–{refp[-1]}" if refp else ""))
    out = []
    for g, (p0, refp) in zip(G, pages):
        kod, klip, bas, acik, refs, prompt, kontrol = g
        newpage(); start = state["page"]
        write("h", f"GÖREV {kod} (klip {klip}): {bas}")
        write("b", f"Çıktı dosyasının adı: B04_{kod}")
        write("b", "Boyut: " + SIZE)
        write("p", acik)
        write("b", "Bu görevin referansları (yalnızca bunlar, bu sırayla):")
        for i, (r, pn) in enumerate(zip(refs, refp), 1): write("p", f"{i}. Sayfa {pn}: {R[r][1]}")
        write("b", "Prompt (kelimesi kelimesine):")
        write("c", "Stylized 3D animated feature film still, vertical 2:3.\n\n" + prompt.strip() + "\n\n" + END)
        write("b", "Kontrol:"); write("p", kontrol)
        rp = []
        for r in refs:
            f = R[r][0]; w, h = Image.open(f).size
            c.showPage(); state["page"] += 1; c.setPageSize((w, h)); c.drawImage(f, 0, 0, w, h); rp.append(state["page"])
        out.append((start, rp))
    return out


for i in range(3):
    final = i == 2
    c = canvas.Canvas(OUT if final else io.BytesIO(), pagesize=A4); state = {"y": H - M, "page": 1}
    pages = build(pages if i else [(0, [0] * len(g[4])) for g in G])
c.save()
print(OUT, [p for p, _ in pages])
