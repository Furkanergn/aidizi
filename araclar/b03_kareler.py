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
 "dosya":("Nesne_dosya.jpg",f"{V}/onayli/nesne_dosya_kapali.jpg","kapalı dosya: yalnızca dosyanın görünüşü"),
}
ENTR="Place and light: the village entrance from the attached approved frame: gravel road, old stone houses with blue shutters, autumn vines, hazy green hillside, golden late-afternoon sun."
MEYDAN="Place and light: the village square from the attached approved frame: cobbles, the dry round stone fountain, the big plane tree with yellow leaves, old stone houses, the shabby rusty street lamps switched on in daylight, golden late-afternoon sun low on the left."

K={}
K["SB31"]=("P01","Selin dosyayı Rıza'nın göğsüne bastırıyor",["SB03","selin","selin_ifade2","riza","dosya"],f"""
Two-shot from the hips up. {ENTR} Same background as the attached approved frame (road, dark grey car far behind on the left, hillside).
Selin stands on the LEFT, turned three-quarters toward Rıza. Rıza stands on the RIGHT, facing her.
{SELIN} With BOTH hands she presses {FOLDER.replace('his forearm','her forearm')} flat against the middle of Rıza's chest, arms almost straight, leaning into him. Her face: a sweet, sugary smile that is clearly a threat: eyebrows raised high, head tilted, dimples showing, eyes locked on his.
{RIZA} He is leaning back a little from the push, both hands coming up, open, about to catch the folder against his chest. His face: startled, eyebrows up, a nervous half-smile, eyes on Selin.""")
K["SB32"]=("P02","Rıza keçiye yürümek üzere, boy plan",["SB09","riza","riza_jestB","keci","dosya"],f"""
Wide full-body shot. {ENTR} Same place as the attached approved frame: the fallen road sign lies flat on the gravel in the left foreground (its text exactly "ŞEHİR MERKEZİ"), the cobbled street runs away between the stone houses.
{KECI} It stands in the middle of the road, right of the fallen sign, in profile facing LEFT, chewing, ignoring everyone.
{RIZA} He stands on the LEFT side of the frame, about three metres from the goat, seen full body from head to shoes, turned toward the goat, mid-step. {FOLDER[0].upper()+FOLDER[1:]} is tucked under his LEFT arm. His RIGHT hand straightens his blazer lapel. His face: chin up, a formal, over-polite smile, like a man walking into a business meeting.
No other people.""")
K["SB33"]=("P03","Keçi yakın plan, çiğniyor",["keci","SB09"],f"""
Close-up of the goat's head and neck, three-quarter front view, filling most of the frame. {KECI} Its jaw is pushed sideways mid-chew, one cheek bulging, a few blades of dry grass at the corner of its mouth, eyes half closed, utterly bored.
Background: the stone houses and cobbled street of the attached approved frame, softly out of focus. No people.""")
K["SB34"]=("P04, P06","Rıza keçinin önünde çömelmiş, sunum yapıyor",["SB09","riza","riza_ifade","riza_jestA","keci","dosya"],f"""
Medium shot at crouching eye level. {ENTR} The cobbled street and stone houses of the attached approved frame are behind, softly out of focus.
{RIZA} He is CROUCHING on his heels in the center-left of the frame, seen from the knees up, body turned three-quarters to the right. {FOLDER[0].upper()+FOLDER[1:]} is tucked under his LEFT arm, pressed against his ribs. His RIGHT hand is raised at shoulder height, fingers spread, drawing something in the air, like a man starting a presentation. His face: bright salesman smile, eyebrows high, eyes on the goat.
{KECI} Only its head and neck are in the frame, in the RIGHT foreground, seen from behind in three-quarter rear view (we see its brown ear, one horn and the red collar), facing Rıza at his eye level.
No other people.""")
K["SB35"]=("P05","Selin ve Naci: Selin gülmesini tutuyor",["SB21","selin","selin_ifade2","selin_jestB","naci_ifade"],f"""
Medium-wide two-shot. Place and light: exactly the attached approved frame: the stone wall, the blue door, the vine, the wooden stool.
{NACI} He sits on the stool exactly as in the attached approved frame, in the LEFT half of the image: tea glass in his RIGHT hand at chest height, left hand on his knee, looking toward the right edge of the frame, eyes half closed, faintly amused.
{SELIN} She STANDS beside him on the RIGHT, close to him, seen from the knees up, her body turned toward the right edge of the frame. Her RIGHT hand is clamped over her mouth, her LEFT arm is wrapped across her stomach, shoulders hunched up: she is trying desperately not to laugh. Her eyes are wide and sparkling, cheeks puffed, looking toward the right edge of the frame at something off screen.
Her hands hold nothing. The stone shelf beside Naci is empty.""")
K["SB36"]=("P07","Keçi kâğıtla kaçıyor, Rıza donakalmış",["SB09","riza","riza_ifade","riza_jestA","keci_hareket","dosya"],f"""
Wide full-body shot. {ENTR} Same place as the attached approved frame; the fallen road sign lies in the left foreground (text exactly "ŞEHİR MERKEZİ").
{RIZA} He is CROUCHING on his heels in the left third of the frame, seen full body, both EMPTY hands still held out in front of him where the paper was a moment ago, fingers spread. His face: pure shock, mouth open, eyebrows up, staring after the goat. The closed burgundy folder is still tucked under his LEFT arm.
{KECI} It is already two metres away from him, in the RIGHT half of the frame, galloping away toward the cobbled street in the background, seen in three-quarter rear view, ears back, a crumpled blank white sheet of paper clamped in its mouth and flapping. Small puffs of dust behind its hooves.
The paper is blank: no writing on it. No other people.""")
K["SB37"]=("P08","Kovalamaca, yan takip",["V8","riza","riza_jestA","keci_hareket"],f"""
Wide side-on tracking shot in the cobbled village street of the attached location image: old stone houses with closed blue shutters on the far side, weeds between the stones. The road sign is NOT in this image.
Both run from LEFT to RIGHT, seen in full-body profile, with motion in their poses.
{KECI} It gallops in the RIGHT half of the frame, all four hooves off the ground, ears back, a crumpled blank white sheet of paper clamped in its mouth.
{RIZA} He sprints two metres behind it, in the LEFT half of the frame, mid-stride, arms pumping, blazer flapping open behind him, hair blown back, one loafer almost slipping on the cobbles. His hands are EMPTY: no folder. His face: panicked and out of breath, mouth open.
Dust and a few dry leaves kicked up behind them. No other people. The paper is blank.""")
K["SB38"]=("P10","Meydan geniş: Emine, keçi geliyor, Rıza uzakta",["SB20","emine","emine_ifade","keci_hareket","riza"],f"""
Wide shot of the village square. {MEYDAN} Same camera position as the attached approved frame.
{EMINE} She stands full body beside the fountain, right of center, both fists on her hips, feet apart, facing LEFT, watching the goat arrive. Her face: stern, one eyebrow raised.
{KECI} It trots toward her from the LEFT side of the frame, in profile facing right, about three metres from her, slowing down, a crumpled blank white sheet of paper in its mouth.
{RIZA} He is small and far away in the background on the LEFT, at the mouth of a street between the houses, running toward the square, arms flailing, hands empty.
The paper is blank. No other people.""")
K["SB39"]=("P11","Emine ve Rıza: sen kimsin",["SB20","emine","emine_ifade","riza","riza_ifade","riza_jestA"],f"""
Two-shot from the knees up in the village square. {MEYDAN} The fountain and the plane tree are behind them, softly out of focus; one lit rusty street lamp is visible.
{EMINE} She stands on the LEFT, upright, facing Rıza. In her RIGHT hand, at waist height, she holds a crumpled blank white sheet of paper. Her LEFT fist is on her hip. Her face: stern, one eyebrow raised, lips pressed, looking him up and down.
{RIZA} He stands on the RIGHT, bent forward with BOTH hands on his knees, out of breath, hair messier than usual, head lifted to look up at her, mouth open, panting, a weak polite smile trying to form. His hands are empty: no folder.
At the bottom edge of the frame between them, the head of the goat (cream-white, one brown ear, red rope collar with brass bell) looks up at Emine.
The paper is blank.""")
K["SB40"]=("P12","Emine yakın plan, anahtarı gösteriyor",["SB39","emine_ifade","emine"],f"""
Close shot of Emine from the chest up, slightly left of center, in the same place and light as the attached approved frame (village square, fountain and lit street lamp softly out of focus behind her). She is the same woman as in the attached frame.
{EMINE} With her RIGHT hand she holds up, at shoulder height, an old dark iron key about as long as her finger; the key hangs on a thin leather cord that goes around her neck. Her LEFT hand is not in the frame. Her face: delighted with herself, a sly bargaining smile, eyes narrowed, chin slightly raised, looking toward the right edge of the frame.
In the RIGHT foreground edge of the frame, out of focus, the dark navy shoulder and a few dark curls of Rıza, seen from behind.""")
K["SB41"]=("P13","Emine ve Rıza: verir misiniz",["SB39","emine_ifade","riza","riza_ifade"],f"""
Two-shot from the hips up, same place, same light and same positions as the attached approved frame: Emine on the LEFT, Rıza on the RIGHT, in the village square.
{RIZA} He now stands UPRIGHT, facing Emine, his hair hastily smoothed. His RIGHT hand is held out toward her at waist height, palm up, asking for something. His LEFT hand is pressed flat on his own chest. His face: his sweetest, most charming pleading smile, eyebrows up in the middle.
{EMINE} She holds an old dark iron key on a thin leather cord (the cord goes around her neck) in her RIGHT hand, in front of her chest, pinched between thumb and fingers, clearly visible. Her LEFT fist is on her hip. Her face: amused, sly, one eyebrow up, in no hurry.
Rıza's hands hold nothing.""")

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
