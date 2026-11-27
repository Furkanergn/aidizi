#!/usr/bin/env python3
"""B06 video promptları. python3 araclar/b06_video.py → bolumler/B06/klipler/Pxx/"""
import os, shutil
B = "diziler/sifir-sehir/bolumler/B06"; K = f"{B}/kareler/onayli"
H = "Use the attached image as the FIRST FRAME of the video (image-to-video, start frame). Do not generate a new scene from text."
ST = "Stylized 3D animated look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 8 seconds."
V = {"R": "- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor.",
     "S": "- Selin: Turkish woman in her early thirties. Warm, slightly husky low voice. She has a wide emotional range: she can be sarcastic, reproachful, loud and laughing.",
     "N": "- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused.",
     "K": "- Kaan: Turkish young man in his mid twenties. Energetic, bright, fast, slightly nasal social-media influencer voice."}
NAT = "Every character speaks ONLY Turkish, with a natural Istanbul accent and the lively delivery of actors in a family animated comedy. No English."
WALL = "in front of an old stone wall with a vine, grapes, blue shutters and a blue door, golden late-afternoon light"
RZ = "a tall slim man with dark curls in a navy blazer (Rıza)"
NC = "a thin old man with grey hair and a grey moustache in a faded blue work jacket (Naci)"
SL = "a young woman with golden blonde curls, pink top and short burgundy ruffled skirt (Selin)"
KN = "a young man with light-brown wavy hair in a bright orange hooded windbreaker and cream cargo trousers (Kaan) holding a black phone gimbal in his RIGHT hand"
EYES_END = "Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame."
def yaz(ad, kare, start, order, hands, voices, perf, last, eyes, pron, audio=""):
    d = f"{B}/klipler/{ad}"; os.makedirs(d, exist_ok=True)
    if kare.startswith("SB") and os.path.exists(f"{K}/{kare}.jpg"): shutil.copyfile(f"{K}/{kare}.jpg", f"{d}/B06_{ad}_baslangic_karesi_{kare}.jpg")
    t = f"""{H}
Clip name (for the file only, never shown or spoken): B06_{ad}

{ST}

Start exactly from the first frame: {start}

{order}

Hands and objects:
{hands}

Voices (the same in every clip of this series):
{chr(10).join(V[v] for v in voices)}

{NAT}

Performance, second by second:
{perf}

Last frame: {last}

Eyes: {eyes} {EYES_END}

Pronunciation: {pron}

Only the speaking character's mouth moves. Audio: the voices{audio} and light wind only. No music, no subtitles, no on-screen text.
"""
    open(f"{d}/B06_{ad}_prompt_8sn.txt", "w").write(t)

yaz("P01", "SB70", f"wide full-body shot {WALL}, a cobbled lane running away on the right. From left to right: {RZ} standing, {NC} on a wooden stool with a tea glass, {SL} with a burgundy folder; all three turned to the right, surprised. On the lane on the right, {KN}, mid-step walking toward the left, grinning into his phone.",
 'SPEAKER ORDER: only the YOUNG MAN in the orange jacket, Kaan, speaks in this shot, one line:\n"Selam millet! İnterneti bile olmayan bir köydeyiz!"\nRıza, Naci and Selin do NOT speak.',
 "- Kaan keeps the gimbal up in front of his face in his RIGHT hand, screen toward himself, and gestures with his LEFT hand.\n- Kaan takes only two more steps to the LEFT, sideways across the frame, and stops about one metre to the right of Selin. He never walks toward the camera and stays the same size.\n- The others stay where they are. Naci keeps his tea glass in his RIGHT hand.",
 "K",
 "0-1.2 s: Kaan takes two steps to the left and stops, grinning into his phone.\n1.2-4.2 s: KAAN says in Turkish into his phone, a loud, bright vlogger voice, fast and excited, sweeping his LEFT hand toward the village, stressing \"interneti bile\": \"Selam millet! İnterneti bile olmayan bir köydeyiz!\"\n4.2-8 s: Nobody speaks. Rıza's mouth falls open in delight. Selin raises one eyebrow, unimpressed. Naci takes a slow sip of tea. Kaan keeps grinning into the phone and nods to his followers.",
 "all four in their places: Kaan standing one metre right of Selin, grinning into his phone; Rıza delighted; Selin with one eyebrow raised; Naci sipping; all mouths closed.",
 "Kaan looks at his phone. Rıza, Naci and Selin look at Kaan.",
 '"Selam millet" sounds like "seh-LAHM meel-LET". "İnterneti bile olmayan bir köydeyiz" sounds like "een-ter-neh-TEE bee-LEH ol-mah-YAHN beer kuy-deh-YEEZ".')
yaz("P02", "SB71", f"waist-up group {WALL}. From left to right: {RZ} shaking hands with {KN}; {NC} sits behind them on a stool with a tea glass; {SL} on the right, a burgundy folder in her RIGHT hand, unimpressed.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - Rıza, the man in the navy blazer: "Hoş geldin! Rıza ben, köyün CEO\'su."\nLine 2 - Selin, the blonde woman: "Kasa bende."\nKaan and Naci do NOT speak.',
 "- Rıza shakes Kaan's LEFT hand with his RIGHT hand until second 3, then lets go and puts his hand on his chest proudly.\n- Kaan keeps the gimbal in his RIGHT hand. Selin keeps the folder in her RIGHT hand. Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "RS",
 "0-0.3 s: Rıza pumps Kaan's hand eagerly.\n0.3-3 s: RIZA says in Turkish, over-polite and grand like a salesman meeting a VIP, stressing \"CEO'su\": \"Hoş geldin! Rıza ben, köyün CEO'su.\" Selin's mouth is closed.\n3-3.8 s: A beat. Rıza lets go and puts his hand on his chest, proud.\n3.8-5 s: SELIN says in Turkish, dry and flat, without moving, a tiny smirk: \"Kasa bende.\" Rıza's mouth is closed.\n5-8 s: Nobody speaks. Kaan laughs silently and turns his phone toward Selin, then Rıza. Rıza's smile freezes. Naci sips.",
 "all in their places: Kaan filming them with a grin; Rıza with a frozen smile, hand on his chest; Selin smirking; Naci sipping; all mouths closed.",
 "Rıza looks at Kaan, then at Selin. Selin looks at Rıza. Kaan looks at both. Naci looks at his tea.",
 '"Hoş geldin" sounds like "hosh gel-DEEN". "CEO\'su" sounds like "see-ee-OH-soo". "Kasa bende" sounds like "kah-SAH ben-DEH".')
yaz("P03", "P02son", f"waist-up group {WALL}. From left to right: {RZ}, {KN}, {SL}; {NC} sits behind Rıza and Kaan on a stool with a tea glass.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - Kaan, the young man in the orange jacket: "Abi… burası hiç çekmiyor."\nLine 2 - Rıza, the man in the navy blazer: "Bir yerde çekiyor!"\nSelin and Naci do NOT speak.',
 "- Kaan keeps the gimbal in his RIGHT hand; at second 0.5 he lifts it high and waves it around, looking for signal.\n- On \"bir yerde\" Rıza points his RIGHT index finger down at Naci on the stool.\n- Selin keeps the folder in her RIGHT hand. Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "KR",
 "0-0.5 s: Kaan glances at his phone; his grin fades.\n0.5-2.8 s: KAAN says in Turkish, whiny and panicked, lifting the phone high and waving it around: \"Abi… burası hiç çekmiyor.\" Rıza's mouth is closed.\n2.8-3.4 s: A beat. Rıza's eyes light up.\n3.4-4.8 s: RIZA says in Turkish, triumphant, pointing down at Naci with his RIGHT index finger: \"Bir yerde çekiyor!\" Kaan's mouth is closed.\n4.8-8 s: Nobody speaks. Kaan and Selin look down at Naci. Naci keeps sipping his tea without looking up.",
 "all in their places: Rıza pointing at Naci; Kaan and Selin looking at Naci; Naci sipping; all mouths closed.",
 "Kaan looks at his phone, then at Naci. Rıza looks at Kaan, then at Naci. Selin looks at Naci.",
 '"Abi" sounds like "ah-BEE". "burası hiç çekmiyor" sounds like "boo-rah-SUH heech chek-mee-YOR". "Bir yerde çekiyor" sounds like "beer yer-DEH cheh-kee-YOR".')
yaz("P04", "SB72", f"two-shot {WALL}. On the left {KN} crouches in front of the stool, looking up hopefully. On the right {NC} sits on a wooden stool sipping from a small tea glass in his RIGHT hand.",
 'SPEAKER ORDER: only the OLD MAN on the stool, Naci, speaks in this shot, one word:\n"Kalkmam."\nKaan does NOT speak.',
 "- Naci keeps the tea glass in his RIGHT hand. Kaan stays crouched and keeps the gimbal in his RIGHT hand. Nobody stands up.",
 "N",
 "0-1.5 s: Kaan looks up at Naci, hopeful. Naci sips, eyes half closed.\n1.5-2.6 s: Naci lowers the glass an inch. NACI says in Turkish, calm, dry and final, without looking at Kaan: \"Kalkmam.\" Kaan's mouth is closed.\n2.6-8 s: Nobody speaks. Kaan blinks, his face falls, he looks at his phone, then back up at Naci with puppy eyes. Naci sips again, unbothered.",
 "both in their places: Kaan crouched with pleading eyes; Naci sipping; both mouths closed.",
 "Kaan looks at Naci. Naci looks ahead at nothing.",
 '"Kalkmam" sounds like "kalk-MAHM".')
yaz("P05", "P04son", f"two-shot {WALL}. On the left {KN} crouches in front of the stool with pleading eyes. On the right {NC} sits on a wooden stool with a small tea glass in his RIGHT hand.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - Kaan, the young man crouching: "Amca, bir milyon kişi seni görecek!"\nLine 2 - Naci, the old man on the stool: "Bir milyon kişi beni görmesin."\nEach says ONLY his own line.',
 "- Kaan stays crouched and turns the gimbal so the phone faces Naci.\n- Naci keeps the tea glass in his RIGHT hand. Nobody stands up.",
 "KN",
 "0-0.4 s: Kaan turns the phone toward Naci.\n0.4-2.8 s: KAAN says in Turkish, sweet and pleading, eyes wide, stressing \"bir milyon\": \"Amca, bir milyon kişi seni görecek!\" Naci's mouth is closed.\n2.8-3.6 s: A beat. Naci slowly turns his eyes to the phone.\n3.6-5.6 s: NACI says in Turkish, slow and dry, with quiet dignity: \"Bir milyon kişi beni görmesin.\" Kaan's mouth is closed.\n5.6-8 s: Nobody speaks. Kaan's mouth falls open. Naci gently pushes the phone away with one finger of his LEFT hand and sips.",
 "both in their places: Kaan crouched, mouth open; Naci sipping; both mouths closed.",
 "Kaan looks at Naci. Naci looks at the phone, then away.",
 '"Amca" sounds like "ahm-JAH". "bir milyon kişi seni görecek" sounds like "beer meel-YON kee-SHEE seh-NEE gur-reh-JEK". "beni görmesin" sounds like "beh-NEE gur-meh-SEEN".')
yaz("P06", "SB73", f"waist-up two-shot {WALL}. On the left {KN}, surprised; at the far left edge half of Rıza in a navy blazer. On the right {SL}, a burgundy folder in her RIGHT hand, her LEFT index finger pointing down, a sly smile.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - Selin, the blonde woman: "Tabure kiralık. Saati beş yüz."\nLine 2 - Kaan, the young man in orange: "Beş yüz mü?!"\nRıza does NOT speak.',
 "- Selin keeps the folder in her RIGHT hand and points down at the stool with her LEFT index finger.\n- Kaan keeps the gimbal in his RIGHT hand. Nobody walks.",
 "SK",
 "0-0.5 s: Selin narrows her eyes, doing the math.\n0.5-3 s: SELIN says in Turkish, businesslike and crisp, pointing down at the stool, stressing \"beş yüz\": \"Tabure kiralık. Saati beş yüz.\" Kaan's mouth is closed.\n3-3.6 s: A beat. Kaan's jaw drops.\n3.6-4.6 s: KAAN squeaks in Turkish, shocked, voice cracking high: \"Beş yüz mü?!\" Selin's mouth is closed.\n4.6-8 s: Nobody speaks. Selin smiles sweetly and nods once. Kaan looks at his phone, then at Selin.",
 "both in their places: Selin smiling sweetly; Kaan stunned; both mouths closed.",
 "Selin looks at Kaan. Kaan looks at Selin, then the phone.",
 '"Tabure kiralık" sounds like "tah-boo-REH kee-rah-LUHK". "Saati beş yüz" sounds like "sah-ah-TEE besh YEWZ".')
yaz("P07", "P06son", f"waist-up two-shot {WALL}. On the left {KN}, stunned; at the far left edge half of Rıza. On the right {SL}, a burgundy folder in her RIGHT hand, smiling sweetly.",
 'SPEAKER ORDER: only Selin, the blonde woman, speaks in this shot, one line:\n"Manzara dahil."\nKaan does NOT speak.',
 "- Selin keeps the folder in her RIGHT hand; she sweeps her LEFT arm out toward the lane and the hills.\n- Kaan keeps the gimbal in his RIGHT hand. Nobody walks.",
 "S",
 "0-0.5 s: Selin lifts her LEFT arm.\n0.5-2 s: SELIN says in Turkish, sweet and sure, a salesman's flourish, sweeping her arm toward the view: \"Manzara dahil.\" Kaan's mouth is closed.\n2-8 s: Nobody speaks. Kaan follows her arm, looks at the view, swallows, looks at his phone, sighs and nods in defeat. Selin's smile widens.",
 "both in their places: Kaan nodding in defeat; Selin smiling; both mouths closed.",
 "Selin looks at Kaan. Kaan looks at the view, the phone, then Selin.",
 '"Manzara dahil" sounds like "mahn-zah-RAH dah-HEEL".')
yaz("P08", "SB74", f"two-shot {WALL}. On the left {NC} sits on a wooden stool, looking up at the woman with a shrewd face, his LEFT index finger raised. On the right {SL}, a burgundy folder in her RIGHT hand, her LEFT hand reaching out.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - Naci, the old man: "Yarısı benim."\nLine 2 - Selin, the blonde woman: "Anlaştık."\nEach says ONLY their own line.',
 "- Naci keeps the tea glass in his RIGHT hand on his knee; after his line he shakes Selin's LEFT hand with his LEFT hand.\n- Selin keeps the folder in her RIGHT hand. Nobody walks.",
 "NS",
 "0-0.5 s: Naci holds up his finger.\n0.5-2 s: NACI says in Turkish, calm and shrewd, bargaining: \"Yarısı benim.\" Selin's mouth is closed.\n2-2.8 s: A beat. Selin laughs softly through her nose.\n2.8-3.8 s: SELIN says in Turkish, warm and quick, holding out her hand: \"Anlaştık.\" Naci's mouth is closed.\n3.8-8 s: Nobody speaks. They shake hands firmly; Naci gives a small satisfied nod; Selin smiles.",
 "both in their places, still shaking hands, both smiling; both mouths closed.",
 "Naci looks at Selin. Selin looks at Naci.",
 '"Yarısı benim" sounds like "yah-ruh-SUH beh-NEEM". "Anlaştık" sounds like "ahn-lahsh-TUHK".')
yaz("P09", "SB75", f"wide full-body shot {WALL}. From left to right: {RZ}; {NC} on a wooden stool with both hands on his knees, about to stand; {KN} standing next to the stool, bouncing on his toes; {SL} with a burgundy folder.",
 'SPEAKER ORDER: only Rıza, the man in the navy blazer on the left, speaks in this shot, one whispered line:\n"Kalktı… Adam kalktı!"\nNaci, Kaan and Selin do NOT speak.',
 "- From second 0.5 to 3, Naci slowly stands up from the stool, holding his tea glass in his RIGHT hand, and takes one step to the LEFT, next to Rıza.\n- At second 3.5 Kaan sits down on the stool. He keeps the gimbal in his RIGHT hand.\n- Rıza and Selin stay where they are. Nobody walks toward the camera; everyone stays the same size.",
 "R",
 "0-0.5 s: Naci pushes on his knees.\n0.5-3 s: Naci slowly, with dignity, rises from the stool for the first time, and steps one step to the left. Everyone watches in silence.\n3-3.5 s: Kaan hops onto the stool.\n3.5-5 s: RIZA whispers in Turkish, stunned, eyes huge: \"Kalktı… Adam kalktı!\"\n5-8 s: Nobody speaks. Selin smiles, satisfied. Naci stands beside Rıza holding his tea, looking a little lost. Kaan settles on the stool and raises his phone.",
 "Rıza, Naci standing beside him, Kaan sitting on the stool, Selin on the right; all mouths closed.",
 "Everyone watches Naci stand, then Kaan sit.",
 '"Kalktı… Adam kalktı" sounds like "kalk-TUH… ah-DAHM kalk-TUH".')
yaz("P10", "SB76", f"knees-up group {WALL}. From left to right: {RZ} waving at the phone; {NC} standing with a tea glass; {KN} sitting on the wooden stool holding the gimbal high above his head; {SL} with a burgundy folder.",
 'SPEAKER ORDER: only Kaan, the young man on the stool, speaks in this shot, one line:\n"Canlıdayız millet! Seksen bin kişi izliyor!"\nThe others do NOT speak.',
 "- Kaan holds the gimbal high above his head in his RIGHT hand, screen toward himself.\n- Rıza waves with his RIGHT hand. Naci keeps the tea glass in his RIGHT hand. Selin keeps the folder in her RIGHT hand. Nobody walks.",
 "K",
 "0-0.4 s: Kaan's phone chimes; his face lights up.\n0.4-3.4 s: KAAN shouts in Turkish into his phone, overjoyed, a big vlogger voice, stressing \"seksen bin\": \"Canlıdayız millet! Seksen bin kişi izliyor!\"\n3.4-8 s: Nobody speaks. Rıza leans in behind him, waving and grinning at the phone. Naci stands holding his tea, looking at the empty spot where he used to sit. Selin shakes her head with a smile.",
 "all in their places: Kaan grinning into the raised phone; Rıza waving; Naci holding his tea; Selin smiling; all mouths closed.",
 "Kaan looks at his phone. Rıza looks at the phone. Naci looks down. Selin looks at Kaan.",
 '"Canlıdayız millet" sounds like "jahn-luh-dah-YUHZ meel-LET". "Seksen bin kişi izliyor" sounds like "sek-SEN been kee-SHEE eez-lee-YOR".', ", one live-stream chime")
yaz("P11", "P10son", f"knees-up group {WALL}. From left to right: {RZ}; {NC} standing with a tea glass; {KN} sitting on the stool holding the gimbal high; {SL} with a burgundy folder.",
 'SPEAKER ORDER: only Kaan, the young man on the stool, speaks in this shot, one line:\n"Bir yorum gelmiş… O köy benim. Geliyorum."\nThe others do NOT speak.',
 "- Kaan lowers the gimbal to his face and reads the screen; he keeps it in his RIGHT hand.\n- Naci keeps the tea glass in his RIGHT hand. Selin keeps the folder in her RIGHT hand. Nobody walks.",
 "K",
 "0-0.6 s: Kaan lowers the phone to his face, still smiling, reading comments.\n0.6-4.8 s: KAAN reads aloud in Turkish, his grin fading word by word, slowing down, confused, stressing \"benim\": \"Bir yorum gelmiş… O köy benim. Geliyorum.\"\n4.8-8 s: Nobody speaks. Rıza, Naci and Selin turn their heads to Kaan at the same moment and freeze. Kaan slowly looks up from the phone.",
 "all in their places, Rıza, Naci and Selin staring at Kaan, Kaan looking up from his phone, worried; all mouths closed.",
 "Kaan looks at the phone, then up. The others look at Kaan.",
 '"Bir yorum gelmiş" sounds like "beer yo-ROOM gel-MEESH". "O köy benim" sounds like "oh kuy beh-NEEM". "Geliyorum" sounds like "geh-lee-YO-room".')
print("ok")
