#!/usr/bin/env python3
"""B03 kare (storyboard) paketini üretir: her kare için klasör (numaralı referanslar + ChatGPT promptu) ve tek zip.
Çalıştır: python3 araclar/b03_kareler.py (depo kökünden)"""
import os, shutil, zipfile
OUT="diziler/sifir-sehir/bolumler/B03"; V="diziler/sifir-sehir/varliklar"
B1="diziler/sifir-sehir/bolumler/B01/kareler/onayli"; B2="diziler/sifir-sehir/bolumler/B02/kareler/onayli"; B3=f"{OUT}/kareler/onayli"

SELIN="Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with a sweetheart neckline and flutter sleeves, tucked into a SHORT burgundy two-tier ruffled mini skirt (ends well above the knee), bare legs, brown leather Mary-Jane flats. Keep her exact body proportions from her character sheet (curvy hourglass figure); do not slim her."
RIZA="Rıza: man in his mid thirties, tall and slim, messy dark brown curls, long nose, thick dark eyebrows, light stubble, dark navy blazer (unbuttoned) with a red pocket square over a cream open-collar shirt, brown belt, brown pleated trousers, burgundy tassel loafers. His face must match his character sheet: smooth, in his thirties, NOT wrinkled, NOT older. He is half a head taller than Selin."
NACI="Naci: thin man in his late sixties, grey swept-back hair, thick grey moustache, bushy grey eyebrows, faded blue work jacket over a checked shirt, grey trousers, brown boots."
EMINE="Emine: short, sturdy woman in her mid sixties, round face, thick dark-grey eyebrows, grey hair in a bun under a burgundy floral headscarf tied at the back, small gold hoop earrings, rust-brown cable-knit vest with two pockets over a navy floral dress with rolled-up sleeves (below the knee), black rubber boots. She is a full head shorter than Rıza."
KECI="The goat: medium-sized cream-white village goat with ONE brown ear, curved horns, a small beard, heavy-lidded bored eyes, a frayed red rope collar with a small brass bell. Its back is at the height of a man's hip."
FOLDER="a closed burgundy leather A4 folder with brass corners, about as long as his forearm"
END=("Style: stylized 3D animated feature film still, exactly the look of the attached images: smooth animated-film skin, realistic cloth and hair, warm golden late-afternoon light, long soft shadows. Not photorealistic, not 2D. "
"Sharp focus on the faces, background slightly soft. Correct hands with five fingers. Nobody looks at the camera. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.")

R={ # ad -> (dosya, kaynak, rol)
 "SB03":("B01_SB03.jpg",f"{B1}/SB03.jpg","onaylı kare: köy girişindeki yer, ışık ve Selin–Rıza ikilisinin görünüşü"),
 "SB09":("B01_SB09.jpg",f"{B1}/SB09.jpg","onaylı kare: köy girişi, yerde tabela ve keçi; mekân ve ışık buradan"),
 "SB21":("B02_SB21.jpg",f"{B2}/SB21.jpg","onaylı kare: Naci taburede; mekân, ışık ve Naci buradan"),
 "SB20":("B02_SB20.jpg",f"{B2}/SB20.jpg","onaylı kare: köy meydanı (çeşme, çınar, yanan lambalar); mekân ve ışık buradan"),
 "SB39":("B03_SB39.jpg",f"{B3}/SB39.jpg","bu bölümün onaylı karesi: meydanda Emine ve Rıza; yer, ışık ve iki karakterin görünüşü buradan"),
 "SB32":("B03_SB32.jpg",f"{B3}/SB32.jpg","bu bölümün onaylı karesi: köy girişi; tabela, keçi, Rıza, arkada Naci ve Selin. Mekân, ışık, kimin nerede durduğu buradan"),
 "SB34":("B03_SB34.jpg",f"{B3}/SB34.jpg","bu bölümün onaylı karesi: Rıza keçinin önünde çömelmiş. Mekân, ışık, kamera yönü, keçinin yeri ve Rıza'nın YÜZÜ buradan"),
 "V8":("V8_koy_sokagi.jpg",f"{V}/onayli/V8_plaka_koy_girisi.jpg","köy sokağı: mekân ve ışık buradan (tabela bu karede olmayacak)"),
 "selin":("Selin_sayfasi.jpg",f"{V}/mevcut/sheet_selin.jpg","Selin karakter sayfası: yüz, vücut, kıyafet"),
 "selin_ifade2":("Selin_ifade2.jpg",f"{V}/onayli/V11_selin_ifade2.jpg","Selin ifade sayfası: yüz ifadesi örnekleri"),
 "selin_jestB":("Selin_jest_B.jpg",f"{V}/onayli/V14_selin_jest_B.jpg","Selin jest sayfası: beden ve duruş örnekleri"),
 "selin_jestA":("Selin_jest_A.jpg",f"{V}/onayli/V13_selin_jest_A.jpg","Selin jest sayfası: beden ve duruş örnekleri"),
 "riza":("Riza_sayfasi.jpg",f"{V}/mevcut/sheet_riza.jpg","Rıza karakter sayfası: yüz, vücut, kıyafet (yüz için ESAS budur)"),
 "riza_ifade":("Riza_ifade.jpg",f"{V}/onayli/V1_riza_ifade.jpg","Rıza ifade sayfası: yüz ifadesi örnekleri"),
 "riza_jestA":("Riza_jest_A.jpg",f"{V}/onayli/V15_riza_jest_A.jpg","Rıza jest sayfası: çömelme, koşma, soluklanma pozları"),
 "riza_jestB":("Riza_jest_B.jpg",f"{V}/onayli/V16_riza_jest_B.jpg","Rıza jest sayfası: yürüme ve duruş pozları"),
 "naci_ifade":("Naci_ifade.jpg",f"{V}/onayli/V3_naci_ifade.jpg","Naci ifade sayfası"),
 "emine":("Emine_jest.jpg",f"{V}/onayli/V21_emine_jest.jpg","Emine tam boy sayfası: vücut, kıyafet, duruşlar"),
 "emine_ifade":("Emine_ifade.jpg",f"{V}/onayli/V19_emine_ifade.jpg","Emine ifade sayfası: yüz ve ifadeler"),
 "keci":("Keci_sayfasi.jpg",f"{V}/onayli/V7_keci.jpg","keçi sayfası: görünüş"),
 "keci_hareket":("Keci_hareket_A.jpg",f"{V}/onayli/V22_keci_hareket_A.jpg","keçi hareket sayfası: koşma ve ağzında kâğıt pozları"),
 "fatura":("Nesne_fatura.jpg",f"{V}/onayli/nesne_fatura.jpg","buruşuk elektrik faturası: yalnızca kâğıdın görünüşü (beyaz kâğıt, mavi başlık, sarı şerit). Karede küçük ve buruşuk görünür; yazıları okunmaz"),
 "dosya":("Nesne_dosya.jpg",f"{V}/onayli/nesne_dosya_kapali.jpg","kapalı dosya: yalnızca dosyanın görünüşü"),
}
# ---- MEKÂN KROKİSİ (diziler/sifir-sehir/mekan-krokisi.md; kullanıcı düzeltti) ----
# Kuzey = köyün içi. Güneyden kuzeye: araba (çakıl yol) -> K: keçi ve yerdeki tabela (köy girişi) -> A: çiftin durduğu yer, sokağın içinde,
# Naci'nin duvarının önü -> N: Naci'nin duvarı ve taburesi (sokağın doğu yanı, A'nın 3 m yanı) -> sokak -> meydan.
# Yani Selin, Rıza ve Naci bir arada, sokağın İÇİNDE; keçi ve tabela onlardan 6 m GÜNEYDE, girişte.
# C1: girişten (keçinin güneyinden) kuzeye bakar (V8/SB09): önde tabela ve keçi, sağ geride Naci'nin duvarı ve insanlar. Keçiye gelen kişi KAMERAYA DOĞRU gelir.
# C2: sokağın içinden güneye bakar (V10/SB03): çift önde, arkalarında uzakta keçi-tabela, çakıl yol, araba. Keçiye giden kişi KAMERADAN UZAKLAŞIR.
# C3: sokaktan doğuya, Naci'nin duvarına bakar (V9/SB21): kadrajın SAĞI güney (keçi, giriş), SOLU kuzey (meydan).
MEYDAN="Place and light: the village square from the attached approved frame: cobbles, the dry round stone fountain, the big plane tree with yellow leaves, old stone houses, the shabby rusty street lamps switched on in daylight, golden late-afternoon sun low on the left. The street from the village entrance opens into the square on the LEFT side of the frame."
R["V10"]=("V10_ters_aci.jpg",f"{V}/onayli/V10_plaka_ters_aci.jpg","mekân plakası: köyün içinden dışarı bakış (çakıl yol, araba, tepe); arka plan buradan")
R["V9"]=("V9_naci_duvari.jpg",f"{V}/onayli/V9_plaka_naci_duvari.jpg","mekân plakası: Naci'nin duvarı")
R["naci"]=("Naci_sayfasi.jpg",f"{V}/mevcut/sheet_naci.jpg","Naci karakter sayfası")

K={}
K["SB31"]=("P01","C2 · Selin dosyayı Rıza'nın göğsüne bastırıyor",["SB03","selin","selin_ifade2","riza","dosya"],f"""
Two-shot from the hips up, in exactly the same place, camera direction and light as the attached approved frame: the camera stands in the village street and looks back toward the village entrance; behind them the road, the dark grey car far behind on the left, the hazy hillside. Golden late-afternoon sun low on the right.
Selin stands on the LEFT, turned three-quarters toward Rıza. Rıza stands on the RIGHT, facing her.
{SELIN} With BOTH hands she presses a closed burgundy leather A4 folder with brass corners (about as long as her forearm) flat against the middle of Rıza's chest, arms almost straight, leaning into him. Her face: a sweet, sugary smile that is clearly a threat: eyebrows raised high, head tilted, dimples showing, eyes locked on his.
{RIZA} He is leaning back a little from the push, both hands coming up, open, about to catch the folder against his chest. His face: startled, eyebrows up, a nervous half-smile, eyes on Selin.
No other people in the frame.""")
K["SB32"]=("P02","C1 · SB09'un düzenlemesi: önde keçi arkadan ve tabela; Rıza Selin'in yanından kameraya doğru geliyor; arkada Naci ve Selin",["SB09","SB21","riza","riza_jestB","selin","keci","dosya"],f"""
This is an EDIT of the FIRST attached image (the approved frame of the village entrance). Keep that scene and camera exactly: the same tree, stone houses, cobbled street, hills, light, the fallen road sign in the left foreground with the text "ŞEHİR MERKEZİ", ONE hole in the ground, and the goat standing beside the sign in the foreground. Do not move the sign. Do not add a second hole.

Change 1 - the goat: it stays in the same place beside the sign, but it has TURNED AROUND: we now see it from BEHIND in three-quarter rear view (its back, tail, the back of its head, the brown ear, the red collar). It stands at a slight angle and looks up the street at the man who is coming toward it, still chewing.

Change 2 - add two people in the BACKGROUND on the RIGHT side of the street, in front of the low stone wall and the blue door where the empty stool stands in the first image (see the second attached image for this spot): Naci sits on that stool with his tea glass in his right hand, and Selin stands right beside him with both fists on her hips. Both look toward the goat, watching. They are small in the image but recognizable: Naci, a thin old man with grey swept-back hair and a grey moustache, faded blue work jacket; Selin, golden blonde curls, pink top, SHORT burgundy two-tier ruffled mini skirt, brown Mary-Jane flats.

Change 3 - add Rıza in the MIDDLE GROUND: he has just left Selin's side and is walking down the middle of the street TOWARD the camera and toward the goat. We see him from the FRONT, full body from head to shoes, mid-step, about three metres beyond the goat and three metres in front of Selin and Naci, with empty road between him and the goat. He is clearly smaller in the image than the goat in the foreground and clearly bigger than Selin and Naci behind him.
{RIZA} {FOLDER[0].upper()+FOLDER[1:]} is tucked under his LEFT arm. His RIGHT hand straightens his blazer lapel. His face: chin up, a formal, over-polite business smile, eyes on the goat.

Three depth layers, in this order from the camera: the fallen sign and the goat seen from behind (foreground, largest) - Rıza walking toward us (middle ground) - Naci and Selin by the wall (background, smallest). Rıza comes FROM Selin and Naci, not from the camera side.
No other people. No car in this frame.""")
K["SB33"]=("P03","C2 yönü · Keçi yakın plan, yüzü; geride çakıl yol ve araba",["keci","V10"],f"""
Close-up of the goat's head and neck, three-quarter front view, filling most of the frame. {KECI} Its jaw is pushed sideways mid-chew, one cheek bulging, a few blades of dry grass at the corner of its mouth, eyes half closed, utterly bored.
Camera position: the camera is on the village side of the goat and looks OUT of the village, the same direction as the attached location image. Background, strongly out of focus: the gravel road leading away, a dark grey car far behind, scrub and the hazy green hillside. Golden late-afternoon sun low on the right.
No people.""")
K["SB34"]=("P04, P06","C1 · Keçinin omzunun üstünden Rıza çömelmiş, yüzü kameraya; arkada Naci ve Selin",["SB32","riza","riza_ifade","riza_jestA","keci","dosya"],f"""
Medium shot at crouching eye level. Camera position: the same place and camera direction as the first attached approved frame, but closer and lower: the camera is at the village entrance and looks INTO the village along the cobbled street. Golden late-afternoon sun low on the left.
{KECI} Only its head and neck are in the frame, in the RIGHT foreground, close to the camera, seen from BEHIND in three-quarter rear view (brown ear, one horn, red collar), facing Rıza at his eye level.
{RIZA} He is CROUCHING on his heels in the center-left of the frame, one and a half metres beyond the goat, FACING the camera and the goat, seen from the knees up. {FOLDER[0].upper()+FOLDER[1:]} is tucked under his LEFT arm, pressed against his ribs. His RIGHT hand is raised at shoulder height, fingers spread, drawing something in the air, like a man starting a presentation. His face: bright salesman smile, eyebrows high, eyes on the goat.
At the bottom LEFT corner, on the gravel, one rusty corner of the fallen road sign and its pole are visible; no text of the sign is in the frame.
Background, softly out of focus, on the RIGHT side of the street behind Rıza: the low stone wall and the blue door, with Naci sitting on his stool and Selin standing beside him exactly where they are in the first attached frame, small and blurred (an old man in a blue jacket; a woman with blonde curls, pink top, short burgundy skirt), watching.
No other people.""")
K["SB42"]=("P02b","C1 · SB34'ün düzenlemesi: Rıza keçinin önüne gelmiş, AYAKTA, yüzü büyük ve net; birazdan çömelecek",["SB34","riza","riza_jestB","dosya"],f"""
This is an EDIT of the FIRST attached image (the approved frame: Rıza crouching in front of the goat at the village entrance). Keep the place, the light, the goat's head in the right foreground seen from behind, the rusty corner of the fallen sign at the bottom left, and the two small blurred people far in the background on the right exactly as they are. Keep Rıza's FACE exactly as in the first image and in his character sheet: the same man, smooth face, light stubble, NO moustache.

Change 1 - camera: raise the camera to standing chest height and pull it back about one metre, so there is room for a standing man. The goat's head is now lower in the frame, in the bottom right.

Change 2 - Rıza: he is NOT crouching yet. He STANDS in the center-left of the frame, one and a half metres beyond the goat, facing the camera and the goat, seen from the knees up; his head is in the upper third of the image and his face is large and sharp. He has just arrived and stopped. {FOLDER[0].upper()+FOLDER[1:]} is tucked under his LEFT arm. His RIGHT hand holds his blazer lapel, straightening it. His face: chin up, eyes OPEN and looking down at the goat, a formal, over-polite business smile.
{RIZA}
No other people.""")
K["SB35"]=("P05","C3 · Selin ve Naci: Selin gülmesini tutuyor",["SB21","selin","selin_ifade2","selin_jestB","naci_ifade"],f"""
Medium-wide two-shot. Place, camera direction and light: exactly the attached approved frame: the camera faces the stone wall, the blue door, the vine, the wooden stool.
{NACI} He sits on the stool exactly as in the attached approved frame, in the LEFT half of the image: tea glass in his RIGHT hand at chest height, left hand on his knee, looking toward the RIGHT edge of the frame, eyes half closed, faintly amused.
{SELIN} She STANDS beside him on the RIGHT, close to him, seen from the knees up, her body turned toward the RIGHT edge of the frame. Her RIGHT hand is clamped over her mouth, her LEFT arm is wrapped across her stomach, shoulders hunched up: she is trying desperately not to laugh. Her eyes are wide and sparkling, cheeks puffed.
Both look toward the RIGHT edge of the frame, at Rıza and the goat, who are off screen on the right. Her hands hold nothing. The stone shelf beside Naci is empty.""")
K["SB36"]=("P07","C1 · Keçi kâğıtla Rıza'nın yanından geçip sokağa kaçıyor; Rıza dönüp bakıyor; sağda Naci ve Selin",["SB32","riza","riza_jestA","keci_hareket","selin","dosya"],f"""
Wide full-body shot. Same place, same camera and same light as the first attached approved frame: at the village entrance, looking INTO the village along the cobbled street; the fallen road sign lies in the LEFT foreground (text exactly "ŞEHİR MERKEZİ"); ONE hole in the ground; no dust around the sign. Golden late-afternoon sun low on the left. The spot beside the sign where the goat stood is now EMPTY.
{RIZA} He is in the middle ground, in the middle of the road, three metres from the camera, still CROUCHING but twisted around: his body faces the camera, his head and shoulders are turned back to look up the street behind him, one hand on the gravel for balance, the other EMPTY hand stretched out after the goat, fingers spread. We see his face in profile: mouth open, eyebrows up, pure shock. The closed burgundy folder lies on the gravel beside his knee.
{KECI} It has just bolted PAST him and is now three metres BEYOND him, galloping AWAY from the camera up the street into the village, seen from behind, ears back, a crumpled blank white sheet of paper in its mouth flapping to one side. Puffs of dust behind its hooves.
On the RIGHT side of the street, level with the running goat, in front of the low stone wall and the blue door, exactly where they are in the first attached frame: Naci sits on his stool with his tea glass, and Selin stands beside him bent forward with laughter, one hand on her stomach, both watching the goat race past them. They are small in the frame but recognizable: a thin old man with grey hair and moustache in a faded blue jacket; a woman with golden blonde curls, pink top, SHORT burgundy ruffled mini skirt.
Depth order from the camera: sign (foreground) - Rıza crouching (middle) - goat running away, with Naci and Selin at the right (background).
The paper is blank: no writing on it. No other people.""")
K["SB37"]=("P08","Sokak içi · Kovalamaca, yandan; soldan sağa",["V8","riza","riza_jestA","keci_hareket","fatura"],f"""
Wide side-on shot in the cobbled village street deeper inside the village (the same street as the attached location image, seen from the side): a row of old stone houses with closed blue shutters behind them, weeds between the stones. The road sign, the stool and the blue door are NOT in this image. Golden late-afternoon light.
Both run from LEFT to RIGHT across the frame, seen in full-body profile.
{KECI} It gallops in the RIGHT half of the frame, all four hooves off the ground, ears back, the crumpled electricity bill from the attached prop image (white paper with a blue header and a yellow band, crumpled and small in the frame, its text far too small to read) clamped in its mouth.
{RIZA} He sprints two metres behind it, in the LEFT half of the frame, mid-stride, arms pumping, blazer flapping open behind him, hair blown back, one loafer almost slipping on the cobbles. His hands are EMPTY: no folder. His face: panicked and out of breath, mouth open.
Dust and a few dry leaves kicked up behind them. No other people. No readable text anywhere.""")
K["SB38"]=("P10","Meydan · Emine bekliyor, keçi soldan geliyor, Rıza uzakta",["SB20","emine","emine_ifade","keci_hareket","riza","fatura"],f"""
Wide shot of the village square. {MEYDAN} Same camera position as the attached approved frame.
{EMINE} She stands full body beside the fountain, RIGHT of center, both fists on her hips, feet apart, facing LEFT, watching the goat arrive. Her face: stern, one eyebrow raised.
{KECI} It trots toward her from the LEFT side of the frame, in profile facing RIGHT, about three metres from her, slowing down, the crumpled electricity bill from the attached prop image (white paper with a blue header and a yellow band, crumpled and small in the frame, its text far too small to read) in its mouth.
{RIZA} He is small and far away in the background on the LEFT, at the mouth of the street between the houses, running toward the square, arms flailing, hands empty.
No readable text anywhere. No other people.""")
K["SB39"]=("P11","Meydan · Rıza (solda) ve Emine (sağda): sen kimsin",["SB20","emine","emine_ifade","riza","riza_ifade","riza_jestA","fatura"],f"""
Two-shot from the knees up in the village square. {MEYDAN} The fountain and the plane tree are behind them, softly out of focus; one lit rusty street lamp is visible.
{RIZA} He stands on the LEFT (the side he ran in from), bent forward with BOTH hands on his knees, out of breath, hair messier than usual, head lifted to look up at Emine, mouth open, panting, a weak polite smile trying to form. His hands are empty: no folder.
{EMINE} She stands on the RIGHT, upright, facing LEFT toward Rıza. In her RIGHT hand, at waist height, she holds the crumpled electricity bill from the attached prop image (white paper with a blue header and a yellow band, crumpled and small in the frame, its text far too small to read). Her LEFT fist is on her hip. Her face: stern, one eyebrow raised, lips pressed, looking him up and down.
At the bottom edge of the frame between them, the head of the goat (cream-white, one brown ear, red rope collar with brass bell) looks up at Emine.
No readable text anywhere. No other people.""")
K["SB40"]=("P12","Meydan · Emine yakın plan, anahtarı gösteriyor; solda Rıza'nın omzu",["SB39","emine_ifade","emine"],f"""
Close shot of Emine from the chest up, slightly RIGHT of center, in the same place and light as the attached approved frame (village square, fountain and lit street lamp softly out of focus behind her). She is the same woman as in the attached frame and still faces LEFT.
{EMINE} With her RIGHT hand she holds up, at shoulder height, an old dark iron key about as long as her finger; the key hangs on a thin leather cord that goes around her neck. Her LEFT hand is not in the frame. Her face: delighted with herself, a sly bargaining smile, eyes narrowed, chin slightly raised, looking toward the LEFT edge of the frame.
In the LEFT foreground edge of the frame, out of focus, the dark navy shoulder and a few dark curls of Rıza, seen from behind.""")
K["SB41"]=("P13","Meydan · Rıza (solda) ve Emine (sağda): verir misiniz",["SB39","emine_ifade","riza","riza_ifade"],f"""
Two-shot from the hips up, same place, same light and same positions as the attached approved frame: Rıza on the LEFT, Emine on the RIGHT, in the village square.
{RIZA} He now stands UPRIGHT, facing Emine, his hair hastily smoothed. His RIGHT hand is held out toward her at waist height, palm up, asking for something. His LEFT hand is pressed flat on his own chest. His face: his sweetest, most charming pleading smile, eyebrows up in the middle.
{EMINE} She holds an old dark iron key on a thin leather cord (the cord goes around her neck) in her RIGHT hand, in front of her chest, pinched between thumb and fingers, clearly visible. Her LEFT fist is on her hip. Her face: amused, sly, one eyebrow up, in no hurry.
Rıza's hands hold nothing. No other people.""")

os.makedirs(f"{OUT}/kareler/onayli",exist_ok=True)
ozet=["# B03 kareleri (SB31–SB41)","","Bu dosya `araclar/b03_kareler.py` tarafından üretilir.","",
"Her kare için: yeni bir ChatGPT sohbeti aç, klasördeki numaralı görselleri sırayla ekle, `SBxx_prompt.txt` içeriğini yapıştır. Çıkan kareyi `kareler/onayli/SBxx.jpg` olarak koy ya da sohbete yükle.","",
"| Kare | Klip | Ne | Referanslar |","|---|---|---|---|"]
for k,(klip,bas,refs,body) in K.items():
    d=f"{OUT}/kareler/{k}"; os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f[:2].isdigit() or f.endswith("_prompt.txt") or f=="EKSIK.txt": os.remove(f"{d}/{f}")
    liste=[]; eksik=[]
    for i,r in enumerate(refs,1):
        dosya,kaynak,rol=R[r]
        if os.path.exists(kaynak): shutil.copyfile(kaynak,f"{d}/{i:02d}_{dosya}")
        else: eksik.append(dosya)
        liste.append(f"{i}. {dosya} — {rol}")
    if eksik: open(f"{d}/EKSIK.txt","w",encoding="utf-8").write("Henüz hazır olmayan referanslar (önce o kare onaylanmalı):\n"+"\n".join(eksik)+"\n")
    p=(f"Ekte {len(refs)} görsel var, sırasıyla:\n"+"\n".join(liste)+"\n\n"
       "Bu referanslardaki karakterlerin ve mekânın AYNISINI kullanarak tek bir yeni film karesi üret. Karakterleri yeniden tasarlama; yüz, saç, vücut oranları ve kıyafet referanstakiyle birebir aynı olacak. "
       "En yüksek kalite. Oran: DİKEY 9:16 (ör. 1024×1792; destekleyemiyorsan en yakın dikey boyut ve 9:16'ya kırpılabilecek şekilde yanlarda boşluk bırak). Promptu değiştirme, kısaltma.\n"
       f"Çıktı dosyasının adı: B03_{k}\n\n"
       "Stylized 3D animated feature film still, vertical 9:16.\n\n"+body.strip()+"\n\n"+END+"\n")
    open(f"{d}/{k}_prompt.txt","w",encoding="utf-8").write(p)
    ozet.append(f"| {k} | {klip} | {bas} | {', '.join(R[r][0] for r in refs)}{' (BEKLİYOR: '+', '.join(eksik)+')' if eksik else ''} |")
ozet+=["","Sıra: SB31–SB39 birbirinden bağımsız. SB40 ve SB41, onaylı SB39'u referans alır; SB39 onaylanınca betik yeniden çalıştırılır.",
"P06, SB34'ten; P09, P05 klibinin son karesinden başlar.",""]
open(f"{OUT}/kareler/OKU.md","w",encoding="utf-8").write("\n".join(ozet))
z=f"{OUT}/B03_kareler_paketi.zip"
with zipfile.ZipFile(z,"w",zipfile.ZIP_STORED) as zf:
    for k in K:
        d=f"{OUT}/kareler/{k}"
        for f in sorted(os.listdir(d)):
            if f[:2].isdigit() or f.endswith("_prompt.txt"): zf.write(f"{d}/{f}",f"{k}/{f}")
print(len(K),"kare;",z,round(os.path.getsize(z)/1e6,1),"MB")
