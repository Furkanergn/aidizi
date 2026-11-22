#!/usr/bin/env python3
"""B02 paketini üretir: yeni kare promptları, video promptları, klip klasörleri, plan ve B02_paket.md.
Çalıştır: python3 araclar/b02_paket.py (depo kökünden). Kullanıcının eklediği dosyalara dokunmaz."""
import os, shutil
OUT = "diziler/sifir-sehir/bolumler/B02"
B01 = "diziler/sifir-sehir/bolumler/B01"
VAR = "diziler/sifir-sehir/varliklar"

NACI = "Naci: thin man in his late sixties, grey swept-back hair, thick grey moustache, bushy grey eyebrows, faded blue work jacket over a checked shirt, grey trousers."

def img(body, light):
    return ("Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.\n\n"
        + body.strip() + "\n\n"
        + f"Light: late afternoon golden light, sun low on the {light} side of the frame, long soft shadows, warm and clean.\n"
        "Same stylization as the attached images (animated-film look, no photorealism). Nobody looks at the camera.")

VOICE = {
 "S": "- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.",
 "R": "- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.",
 "N": "- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused.",
}
def vid(dur, first, hands, beats, last, who, eyes, pron="", amb="light wind"):
    p = [f"Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration {dur} seconds.",
         "Start exactly from the first frame: " + first.strip()]
    if hands: p.append("Hands and objects (do not change):\n" + hands.strip())
    if who:
        p.append("Voices (must sound exactly the same in every clip of this series):\n" + "\n".join(VOICE[w] for w in who)
                 + "\n\nEvery character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.")
    p.append(beats.strip())
    p.append("Last frame: " + last.strip())
    p.append("Eyes: " + eyes.strip() + " Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.")
    if who:
        pr = 'Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza".'
        if pron: pr += " " + pron
        p.append(pr)
        p.append(f"Only the speaking character's mouth moves. Audio: the voices and {amb} only. No music, no subtitles, no on-screen text.")
    else:
        p.append(f"No dialogue. Nobody speaks. Audio: {amb} only. No music, no subtitles, no on-screen text.")
    return "\n\n".join(p)

# ---------- yeni kareler (yalnızca iki tane) ----------
REF = {
 "SB10 (B01 onaylı kare)": ("SB10_onayli.jpg", f"{B01}/kareler/onayli/SB10.jpg"),
 "Naci sayfası": ("Naci_sayfasi.jpg", f"{VAR}/mevcut/sheet_naci.jpg"),
 "Naci ifade sayfası": ("Naci_ifade_sayfasi.jpg", f"{VAR}/onayli/V3_naci_ifade.jpg"),
 "V8 plaka (köy girişi)": ("V8_plaka_koy_girisi.jpg", f"{VAR}/onayli/V8_plaka_koy_girisi.jpg"),
 "SB09 (B01 onaylı kare)": ("SB09_onayli.jpg", f"{B01}/kareler/onayli/SB09.jpg"),
}
K = {}
K["SB21"] = ("Naci taburede, orta plan, zarf yok", ["SB10 (B01 onaylı kare)", "Naci sayfası", "Naci ifade sayfası"], img(f"""
Recreate the attached approved frame EXACTLY: same man, same stool, same stone wall, same blue door, same vine, same camera position and framing (medium shot from the knees up). {NACI}
Change only two things:
1. The flat stone shelf beside him is now EMPTY. There is no envelope anywhere in the image.
2. His LEFT hand rests flat on his left knee.
Everything else stays: his RIGHT hand holds the small tulip-shaped tea glass full of dark red tea at chest height, between thumb and two fingers; his body is turned three-quarters toward the right of the frame; he looks toward the right edge of the frame at people outside the frame, eyes half closed, faintly amused, completely relaxed.""", "left"))
K["SB20"] = ("Köy sokağı, gündüz yanan sokak lambaları", ["V8 plaka (köy girişi)"], img("""
This is an EDIT of the attached image. Keep the attached image exactly as it is: the same empty cobbled village street, the same stone houses with closed blue shutters and terracotta roofs, the same camera position, framing, colors and light. There are NO people and NO animals in the image, and none may be added.
Change only two things:
1. REMOVE the road sign and its pole completely. Where it stood there is only gravel and weeds. There is no sign and no text anywhere in the image.
2. ADD four old-fashioned street lamps along the street: black iron brackets fixed to the house walls, each carrying a round glass lantern. Two lamps on the left row of houses, two on the right row, getting smaller with distance; the nearest one is large, in the upper left of the frame. ALL FOUR lamps are switched ON in broad daylight: each lantern glows a strong warm yellow-white with a small halo, clearly and absurdly lit against the sunny street.
The image is a landscape of an empty street only: no man, no stool, no tea glass, no goat, no vehicles.""", "left"))

# ---------- videolar ----------
FOLD = "- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size."
PAPER = "- Rıza's LEFT hand holds the torn-open mustard-yellow envelope at chest height and his RIGHT hand holds the single white sheet just above it, for the entire shot. The sheet's blank back faces the camera; no text is ever visible. He does not gesture, does not lower or drop them."
ARMS = "- Rıza's arms stay down, out of frame, for the entire shot. He makes no hand gestures."
TEA = "- Naci's RIGHT hand holds the small tea glass for the entire shot; the glass never leaves his hand and stays the same size."
F14 = "chest-up two-shot, Selin on the left hugging a burgundy folder and watching Rıza's face; Rıza on the right holding an open yellow envelope and a white sheet of paper, eyes lowered to the sheet."
F11 = "chest-up two-shot, Selin on the left hugging a burgundy folder, Rıza on the right with a stiff smile; both have their heads turned toward the left edge of the frame, looking at someone off screen."
F12 = "close-up of Naci, head and shoulders, tea glass held just below his chin, looking toward the right edge of the frame."
F21 = "medium shot of Naci sitting on a wooden stool against a stone wall, tea glass in his right hand at chest height, left hand on his knee, the stone shelf beside him empty."
STAY = "both stand exactly where they started, nobody walks;"

V = {}  # id -> (başlık, kare adı, kare kaynağı ya da None, süre, replikler, prompt)
V["P01"] = ("Kaç?", "SB14", f"{B01}/kareler/onayli/SB14.jpg", 6, 'SELİN: "Rıza. Kaç para?" / RIZA: "Üç…" / SELİN: "Üç bin mi?"', vid(6, F14,
 FOLD + "\n" + PAPER,
 """0-1.5 s: Selin, watching Rıza's face, says in Turkish, calm and quiet: "Rıza. Kaç para?"
1.5-3 s: Rıza swallows hard, eyes still on the sheet, and says in Turkish, in a small voice that trails off: "Üç…"
3-4.5 s: Selin answers in Turkish, with a little careful hope: "Üç bin mi?"
4.5-6 s: Nobody speaks. Rıza slowly shakes his head, very slightly, without looking up. Selin's face goes flat.""",
 STAY + " Rıza still looking down at the sheet, Selin still looking at Rıza, both mouths closed.",
 "SR", "Rıza looks only at the sheet. Selin looks only at Rıza's face.",
 '"üç" is one short syllable, like "ewch".'))
V["P02"] = ("Üç yüz otuz üç bin", "P01'in son karesi", None, 6, 'RIZA: "Üç yüz otuz üç bin… üç yüz otuz üç lira, hayatım."', vid(6, F14,
 FOLD + "\n" + PAPER,
 """0-5 s: Rıza reads from the sheet in Turkish, slowly, his voice getting smaller with every word, with a pause in the middle: "Üç yüz otuz üç bin… üç yüz otuz üç lira, hayatım."
5-6 s: Nobody speaks. Selin closes her eyes and breathes out slowly through her nose. Rıza stays bent over the sheet, not daring to look at her.""",
 STAY + " Selin's eyes closed, Rıza looking down at the sheet, both mouths closed.",
 "R", "Rıza looks only at the sheet. Selin looks at Rıza, then closes her eyes.",
 'The number is read as six clear words, then a pause, then five words and a meek little "hayatım" (my dear) at the end: "üç yüz otuz üç bin" (333 thousand), "üç yüz otuz üç lira" (333 lira). "üç" sounds like "ewch", "yüz" like "yewz", "otuz" like "oh-TOOZ".'))
V["P03"] = ("Otuz üç kuruş", "SB12", f"{B01}/kareler/onayli/SB12.jpg", 4, 'NACİ: "Otuz üç de kuruşu var."', vid(4, F12,
 TEA + " His other hand is not in the frame.",
 """0-0.5 s: Naci looks toward the right edge of the frame, face flat.
0.5-2.5 s: He adds in Turkish, dry and helpful, as if correcting a small detail: "Otuz üç de kuruşu var."
2.5-4 s: He does not speak. He raises the glass to his lips and takes one small sip, eyes half closed.""",
 "Naci in the same place, glass at his lips, mouth closed on the glass.",
 "N", "Naci looks toward the right edge of the frame, at people off screen.",
 '"kuruş" sounds like "koo-ROOSH".', "light wind and one soft sip"))
V["P04"] = ("Kim yaktı", "SB11", f"{B01}/kareler/onayli/SB11.jpg", 6, 'SELİN: "Amca, burada üç kişi yaşıyorsunuz. Bu kadar elektriği kim yaktı ya?"', vid(6, F11,
 FOLD + "\n" + ARMS,
 """0-0.5 s: Both look toward the left edge of the frame.
0.5-5 s: Selin says in Turkish toward the person off screen on the left, calm, precise, like an auditor: "Amca, burada üç kişi yaşıyorsunuz. Bu kadar elektriği kim yaktı ya?"
5-6 s: Nobody speaks. Rıza nods twice, quickly, as if it had been his question too. Selin keeps looking left, waiting.""",
 STAY + " both still looking toward the left edge of the frame, mouths closed.",
 "S", "Selin and Rıza look only toward the left edge of the frame, at someone off screen. Rıza does not speak.",
 '"elektriği" sounds like "eh-lek-tree-EE".'))
V["P05"] = ("Sokak lambaları", "SB21", f"{OUT}/kareler/onayli/SB21.jpg", 6, 'NACİ: "Sokak lambaları." / "On iki senedir yanıyor."', vid(6, F21,
 TEA + "\n- His LEFT hand stays flat on his left knee for the entire shot. He makes no hand gestures. The stone shelf stays empty.",
 """0-0.5 s: Naci looks toward the right edge of the frame, relaxed.
0.5-2 s: He says in Turkish, unhurried: "Sokak lambaları."
2-3 s: He does not speak. He glances up at the sky for a moment, then back.
3-5 s: He adds in Turkish, as plain fact: "On iki senedir yanıyor."
5-6 s: He does not speak. A tiny shrug of one shoulder.""",
 "Naci sitting exactly where he started, glass in his right hand at chest height, left hand on his knee, mouth closed.",
 "N", "Naci looks toward the right edge of the frame, at people off screen.",
 '"senedir" sounds like "seh-neh-DEER".'))
V["P06"] = ("Lambalar", "SB20", f"{OUT}/kareler/onayli/SB20.jpg", 4, "—", vid(4,
 "wide shot of the empty cobbled village street in golden daylight with four old street lamps on the house walls, all switched on.",
 "- All four lamps stay lit for the whole shot and stay in the same place. Nothing enters the frame.",
 """0-4 s: Nothing happens. The lamps glow uselessly in the sunshine. The nearest lamp flickers once and keeps burning. A few dry leaves drift along the cobbles.""",
 "the same street, all four lamps still lit.",
 "", "There are no people or animals in the shot.", amb="light wind and a faint electric hum from the lamps"))
V["P07"] = ("Şalter nerede", "SB11", f"{B01}/kareler/onayli/SB11.jpg", 6, 'RIZA: "Ya tamam, sorun yok! Kapatırız, biter. Şalter nerede amca?"', vid(6, F11,
 FOLD + "\n" + ARMS,
 """0-0.5 s: Both look toward the left edge of the frame. Rıza's stiff smile widens into a confident one.
0.5-4.5 s: Rıza says in Turkish toward the person off screen on the left, bright and fast, a man with a solution: "Ya tamam, sorun yok! Kapatırız, biter. Şalter nerede amca?"
4.5-6 s: Nobody speaks. Rıza keeps smiling left, eyebrows up, waiting. Selin's eyes slide sideways to Rıza for a moment, unimpressed, then back to the left.""",
 STAY + " both looking toward the left edge of the frame, mouths closed.",
 "R", "Rıza looks only toward the left edge of the frame. Selin looks left, glances at Rıza once, then left again. Selin does not speak.",
 '"şalter" sounds like "shal-TEHR".'))
V["P08"] = ("Muhtarda", "SB12", f"{B01}/kareler/onayli/SB12.jpg", 4, 'NACİ: "Muhtarda."', vid(4, F12,
 TEA + " His other hand is not in the frame.",
 """0-1 s: Naci looks toward the right edge of the frame, face flat. He blinks slowly.
1-2.5 s: He says in Turkish, one dry word: "Muhtarda."
2.5-4 s: He does not speak. One eyebrow rises a little, as if he knows what comes next.""",
 "Naci in the same place, glass below his chin, one eyebrow raised, mouth closed.",
 "N", "Naci looks toward the right edge of the frame, at people off screen.",
 '"Muhtarda" sounds like "mooh-tar-DAH", with a clearly breathed h.'))
V["P09"] = ("Toplantı", "SB11", f"{B01}/kareler/onayli/SB11.jpg", 6, 'RIZA: "Süper! Hemen bir toplantı ayarlayalım muhtarla."', vid(6, F11,
 FOLD + "\n" + ARMS,
 """0-0.5 s: Both look toward the left edge of the frame. Rıza's face lights up.
0.5-4 s: Rıza says in Turkish toward the person off screen on the left, delighted, office-meeting energy: "Süper! Hemen bir toplantı ayarlayalım muhtarla."
4-6 s: Nobody speaks. Rıza nods to himself, pleased. Selin stays perfectly still and blinks once, slowly.""",
 STAY + " both looking toward the left edge of the frame, mouths closed.",
 "R", "Selin and Rıza look only toward the left edge of the frame. Selin does not speak.",
 '"Muhtarla" sounds like "mooh-tar-LAH". "toplantı" ends with the dotless ı: "top-lan-TUH".'))
V["P10"] = ("Orada", "SB21", f"{OUT}/kareler/onayli/SB21.jpg", 4, 'NACİ: "Kendisi şurada."', vid(4, F21,
 TEA + "\n- His LEFT hand stays flat on his left knee for the entire shot. He does not point with his hands. The stone shelf stays empty.",
 """0-1 s: Naci looks toward the right edge of the frame.
1-2.5 s: He tips his chin once toward the right, pointing with his chin only, and says in Turkish, politely: "Kendisi şurada."
2.5-4 s: He does not speak. He looks down into his tea glass, faintly amused.""",
 "Naci sitting exactly where he started, looking down at his glass, mouth closed.",
 "N", "Naci looks toward the right edge of the frame, then down at his glass.", ""))
V["P11"] = ("Muhtar", "SB09", f"{B01}/kareler/onayli/SB09.jpg", 4, "—", vid(4,
 "wide shot of the village entrance: the road sign lies flat on the gravel in the left foreground, a white goat with a red collar and brass bell stands beside it.",
 "- The sign stays flat on the ground and does not move. Its text stays exactly \"ŞEHİR MERKEZİ\" and never changes.\n- The goat stays where it stands and does not walk away.",
 """0-4 s: The goat chews slowly, jaw sliding sideways, completely unbothered. It turns its head a little toward the right, as if it has noticed someone looking, and keeps chewing. One ear flicks. Its bell tinkles once.""",
 "the goat in the same place, still chewing, the sign on the ground.",
 "", "The goat looks toward the right side of the frame, not at the camera.", amb="slow chewing, one soft bell tinkle, light wind"))
V["P12"] = ("Demokratik süreç", "SB03", f"{B01}/kareler/onayli/SB03.jpg", 6, 'SELİN: "Rıza… bu muhtar keçi." / RIZA: "Demokratik bir süreç olmuştur aşkım."', vid(6,
 "chest-up two-shot, Selin on the left hugging a burgundy folder, Rıza on the right grinning; both look past the camera at something ahead.",
 FOLD + "\n" + ARMS,
 """0-1 s: Both stare ahead, past the camera. Rıza's grin slowly stiffens on his face.
1-3 s: Selin, without turning her head, says in Turkish, completely flat, with a pause: "Rıza… bu muhtar keçi."
3-5.5 s: Rıza, still staring ahead with the stuck grin, answers in Turkish, quick and reassuring, as if it were perfectly normal: "Demokratik bir süreç olmuştur aşkım."
5.5-6 s: Nobody speaks. Both keep staring ahead.""",
 STAY + " both still looking ahead past the camera, mouths closed.",
 "SR", "Selin and Rıza look only ahead, past the camera. They do not look at each other.",
 '"keçi" sounds like "keh-CHEE". "süreç" sounds like "sew-RECH". "Muhtar" sounds like "mooh-TAR".'))
V["P13"] = ("Üç oy", "SB12", f"{B01}/kareler/onayli/SB12.jpg", 4, 'NACİ: "Üç oyla seçildi."', vid(4, F12,
 TEA + " His other hand is not in the frame.",
 """0-0.5 s: Naci looks toward the right edge of the frame, face flat.
0.5-2.5 s: He says in Turkish, with quiet civic pride: "Üç oyla seçildi."
2.5-4 s: He does not speak. He gives one slow, satisfied nod.""",
 "Naci in the same place, glass below his chin, mouth closed.",
 "N", "Naci looks toward the right edge of the frame, at people off screen.",
 '"üç" sounds like "ewch". "seçildi" sounds like "seh-cheel-DEE".'))
V["P14"] = ("Git konuş", "SB06", f"{B01}/kareler/onayli/SB06.jpg", 6, 'SELİN: "Hadi git konuş." / RIZA: "Keçiyle mi ya?" / SELİN: "Muhtarla, hayatım."', vid(6,
 "chest-up two-shot, Selin on the left hugging a burgundy folder, her head turned toward Rıza, looking hard at him; Rıza on the right facing forward, eyes sliding toward her, tight nervous smile.",
 FOLD + "\n" + ARMS,
 """0-1.5 s: Selin, looking straight at Rıza, says in Turkish, calm, an order: "Hadi git konuş."
1.5-3.5 s: Rıza turns his head to her and asks in Turkish, small voice, hoping he misheard: "Keçiyle mi ya?"
3.5-5 s: Selin answers in Turkish, flat, final, with a sweetly sarcastic "hayatım" (my dear): "Muhtarla, hayatım."
5-6 s: Nobody speaks. Rıza swallows and slowly turns his face forward again. Selin keeps looking at him.""",
 STAY + " Selin looking at Rıza, Rıza facing forward with a frightened little smile, mouths closed.",
 "SR", "Selin looks only at Rıza. Rıza looks at Selin, then forward past the camera.",
 '"Keçiyle" sounds like "keh-chee-LEH". "Muhtarla" sounds like "mooh-tar-LAH".'))

# ---------- yaz ----------
for d in ("kareler/onayli","videolar","klipler/gelen","klipler/onayli","cikti"): os.makedirs(f"{OUT}/{d}", exist_ok=True)
for k,(t,refs,p) in K.items():
    d=f"{OUT}/kareler/{k}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/{k}_prompt.txt","w",encoding="utf-8").write(p+"\n")
    for i,r in enumerate(refs,1):
        dosya,kaynak=REF[r]; shutil.copyfile(kaynak, f"{d}/{i:02d}_{dosya}")
md=["# B02 üretim paketi","",
"Bu dosya `araclar/b02_paket.py` tarafından üretilir; elle düzenleme, betiği düzenle.","",
"## 1. Yeni kareler (yalnızca 2 tane; görsel üretimi, 9:16)","",
"Her karenin klasöründe (`kareler/SBxx/`) numaralı referanslar ve prompt var: klasördeki görselleri ekle, promptu yapıştır. Çıkan kareyi `kareler/onayli/SBxx.jpg` olarak koy (ya da sohbete yükle); kontrol etmeden videosu üretilmez.","",
"| Kare | Ne | Referanslar | Hangi klipte |","|---|---|---|---|"]
for k,(t,refs,p) in K.items():
    md.append(f"| {k} | {t} | {'; '.join(refs)} | {', '.join(c for c,v in V.items() if v[1]==k)} |")
md+=["","Diğer 12 klip B01'in onaylı karelerinden (SB03, SB06, SB09, SB11, SB12, SB14) başlar; yeniden üretilmez.","",
"## 2. Klipler","",
"Flow ayarı her klip için aynı: **kareden videoya · Veo 3.1 Lite · 9:16**. Başlangıç karesi olarak yalnızca klasördeki kareyi yükle. Çıkan mp4: `klipler/gelen/Pxx.mp4`.","",
"| Klip | Ne | Başlangıç karesi | Süre | Replikler | Kare |","|---|---|---|---|---|---|"]
tot=0; sec=[]
for k,(t,fr,src,dur,l,p) in V.items():
    d=f"{OUT}/klipler/{k}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/{k}_prompt_{dur}sn.txt","w",encoding="utf-8").write(p+"\n")
    open(f"{OUT}/videolar/{k}.txt","w",encoding="utf-8").write(p+"\n")
    kare=None
    if src and os.path.exists(src):
        kare=f"{k}_baslangic_karesi_{fr}.jpg"; shutil.copyfile(src, f"{d}/{kare}")
    else:
        mev=[x for x in os.listdir(d) if x.endswith(".jpg")]
        kare=mev[0] if mev else None
    md.append(f"| {k} | {t} | {fr} | {dur} sn | {l} | {'Hazır' if kare else 'Bekleniyor'} |"); tot+=dur
    sec+=[f"### {k} — {t}","",f"**Başlangıç karesi:** {fr} · **Süre:** {dur} sn",""]
    sec+=[f"![{fr}](klipler/{k}/{kare})",""] if kare else ["Kare henüz hazır değil.",""]
    sec+=["```",p,"```",""]
md+=[f"| **Toplam** | | | **{tot} sn** | | |","",
"Notlar:","- P02, P01 klibinin son karesinden başlar (P01 gelince çıkarılır).",
"- P05 ve P10, yeni SB21 karesini; P06, yeni SB20 karesini bekler.",
"- SB11 üç klipte (P04, P07, P09), SB12 üç klipte (P03, P08, P13) başlangıç karesidir; aralarında karşı açı olduğu için kurguda sıçrama görünmez.",
"- Ekran yazıları kurguda eklenir; kliplerde yazı istenmez.","","## 3. Promptlar",""]+sec
open(f"{OUT}/B02_paket.md","w",encoding="utf-8").write("\n".join(md))
print(len(K),"yeni kare,",len(V),"klip,",tot,"sn")
