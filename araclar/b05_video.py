#!/usr/bin/env python3
"""B05 video promptları. Çalıştır: python3 araclar/b05_video.py → bolumler/B05/klipler/Pxx/B05_Pxx_prompt_8sn.txt"""
B = "diziler/sifir-sehir/bolumler/B05/klipler"
H = "Use the attached image as the FIRST FRAME of the video (image-to-video, start frame). Do not generate a new scene from text."
ST = "Stylized 3D animated look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 8 seconds."
V = {"R": "- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor.",
     "S": "- Selin: Turkish woman in her early thirties. Warm, slightly husky low voice. She has a wide emotional range: she can be sarcastic, reproachful, loud and laughing.",
     "N": "- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused."}
NAT = "Every character speaks ONLY Turkish, with a natural Istanbul accent and the lively delivery of actors in a family animated comedy. No English."
WALL = "in front of an old stone wall with a vine, grapes and blue shutters, golden late-afternoon light"
RZ = "a tall slim man with dark curls in a navy blazer (Rıza)"
NC = "a thin old man with grey hair and a grey moustache in a faded blue work jacket (Naci) sitting on a wooden stool"
SL = "a young woman with golden blonde curls, pink top and short burgundy ruffled skirt (Selin)"
END = "Only the speaking character's mouth moves. Audio: the voices{x} and light wind only. No music, no subtitles, no on-screen text."
EYES_END = "Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame."

def yaz(ad, start, order, hands, voices, perf, last, eyes, pron, extra_audio=""):
    t = f"""{H}
Clip name (for the file only, never shown or spoken): B05_{ad}

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

{END.format(x=extra_audio)}
"""
    open(f"{B}/{ad}/B05_{ad}_prompt_8sn.txt", "w").write(t)

yaz("P02",
 f"knees-up three-shot {WALL}. On the left {RZ} stares at a black phone held in his LEFT hand. In the center {NC}, sipping from a small tea glass in his RIGHT hand. On the right {SL} leans toward the phone, a burgundy folder in her RIGHT hand by her thigh.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - the YOUNG MAN on the left, Rıza: "Sıkışırız! Ev başına yirmi sekiz kişi."\nLine 2 - the OLD MAN on the stool, Naci: "Tuvalet bir tane."\nSelin does NOT speak; her mouth stays closed.',
 "- Rıza holds the phone in his LEFT hand until second 6; his RIGHT hand counts on its fingers.\n- At second 6 Selin reaches over Naci's head with her LEFT hand and takes the phone out of Rıza's hand; she keeps it in her LEFT hand at chest height. Her folder stays in her RIGHT hand.\n- Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "RN",
 "0-0.4 s: Rıza looks up from the phone, already back to his optimistic self.\n0.4-2.8 s: RIZA says in Turkish, upbeat and fast like a salesman who has solved it, counting on the fingers of his RIGHT hand, stressing \"yirmi sekiz\": \"Sıkışırız! Ev başına yirmi sekiz kişi.\" Naci's and Selin's mouths are closed.\n2.8-3.6 s: A beat. Naci slowly lowers the tea glass from his lips. Selin closes her eyes for a moment.\n3.6-4.8 s: NACI says in Turkish, dry and slow, without looking up, stressing \"bir\": \"Tuvalet bir tane.\" Rıza's mouth is closed.\n4.8-6 s: Nobody speaks. Rıza's smile freezes with his counting finger still in the air. Selin presses her lips together, holding back a laugh.\n6-8 s: Selin reaches over Naci's head with her LEFT hand and firmly plucks the phone out of Rıza's hand. Rıza blinks at his empty hand.",
 "all three in the same places: Selin holding the phone in her LEFT hand at chest height, folder in her RIGHT hand; Rıza looking at his empty left hand; Naci with his tea; all mouths closed.",
 "Rıza looks at the phone, at his fingers, then at Selin. Naci looks at his tea. Selin looks at Rıza, then at the phone.",
 '"Sıkışırız" sounds like "suh-kuh-shuh-RUHZ". "yirmi sekiz kişi" sounds like "yeer-MEE seh-KEEZ kee-SHEE". "Tuvalet bir tane" sounds like "too-vah-LET beer tah-NEH".')

yaz("P03",
 f"waist-up three-shot {WALL}. On the left {RZ} with his RIGHT index finger raised, mouth open. In the center {NC}, sipping tea, eyes half closed. On the right {SL} holds a black phone in her LEFT hand at chest height and a burgundy folder in her RIGHT hand against her hip, a sly half-smile.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - the YOUNG WOMAN on the right, Selin: "Önce borcu kapatıyoruz."\nLine 2 - the YOUNG MAN on the left, Rıza: "Aşkım, önce yatırım!"\nNaci does NOT speak.',
 "- Selin keeps the phone in her LEFT hand and the folder in her RIGHT hand the whole time; she taps the screen with her LEFT thumb.\n- Rıza's hands are empty. Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "SR",
 "0-0.5 s: Rıza lowers his finger and closes his mouth, waiting. Selin glances down at the phone.\n0.5-2.2 s: SELIN says in Turkish, decisive and matter-of-fact like a finance manager, tapping the screen with her thumb, stressing \"borcu\": \"Önce borcu kapatıyoruz.\" Rıza's mouth is closed.\n2.2-2.8 s: A beat. Rıza gasps, eyes wide, as if she proposed burning money.\n2.8-4.6 s: RIZA protests in Turkish like a salesman in a meeting, his RIGHT index finger shooting up, voice rising: \"Aşkım, önce yatırım!\" Selin's mouth is closed.\n4.6-8 s: Nobody speaks. Rıza holds his finger up, mouth still open. Selin slowly turns her head to him, raises one eyebrow and gives him a sly, unimpressed half-smile. Naci keeps sipping.",
 "all three in the same places: Rıza with his right index finger raised and mouth open; Selin holding the phone, one eyebrow raised; Naci sipping; Selin's and Naci's mouths closed.",
 "Selin looks at the phone, then at Rıza. Rıza looks at Selin. Naci looks at his tea.",
 '"borcu kapatıyoruz" sounds like "bor-JOO kah-pah-TUH-yo-rooz". "Aşkım" sounds like "ash-KUHM". "yatırım" sounds like "yah-tuh-RUHM".')

yaz("P04",
 f"waist-up three-shot {WALL}. On the left {RZ} with his RIGHT index finger raised, mouth open in an objection. In the center {NC}, sipping tea. On the right {SL} holds a black phone in her LEFT hand at chest height and a burgundy folder in her RIGHT hand against her hip, one eyebrow raised.",
 'SPEAKER ORDER: only the YOUNG WOMAN, Selin, speaks in this shot, one line:\n"Elektrik kesilirse yatırımı karanlıkta mı yapacaksın?"\nRıza and Naci do NOT speak; Rıza only opens and closes his mouth without a sound.',
 "- Selin keeps the phone in her LEFT hand and the folder in her RIGHT hand the whole time.\n- Rıza's hands are empty. Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "SR",
 "0-0.4 s: Selin leans slightly toward Rıza over Naci's head.\n0.4-3.8 s: SELIN says in Turkish, slow, sweet and poisonous, each word placed carefully, stressing \"karanlıkta\": \"Elektrik kesilirse yatırımı karanlıkta mı yapacaksın?\" Rıza's mouth is closed.\n3.8-6 s: Nobody speaks. Rıza opens his mouth to answer, closes it, opens it again, closes it; his raised finger slowly sinks. Naci hides a smile behind his tea glass.\n6-8 s: Selin turns away from him, rises onto her tiptoes and lifts the phone in her LEFT hand high above Naci's head, looking up at the screen. Naci does not move.",
 "Selin on tiptoe with the phone held high above Naci's head, folder still at her right hip; Rıza with his hand down and mouth closed; Naci with his tea; all mouths closed.",
 "Selin looks at Rıza, then up at the phone. Rıza looks at Selin. Naci looks at his tea.",
 '"Elektrik kesilirse" sounds like "eh-lek-TREEK keh-see-leer-SEH". "karanlıkta" sounds like "kah-rahn-luhk-TAH". "yapacaksın" sounds like "yah-pah-JAHK-suhn".')

yaz("P06",
 f"waist-up two-shot {WALL}. On the left {RZ} stands with his RIGHT hand pressed on his chest, a wounded face. On the right {NC}, looking up toward the right edge of the frame with raised eyebrows and an impressed smile, his tea glass on his knee in his RIGHT hand. A young woman is just outside the right edge of the frame.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - the OLD MAN on the stool, Naci: "Öncekiler ödemezdi."\nLine 2 - the YOUNG MAN, Rıza: "Dedemin parası…"\nEach says ONLY his own line.',
 "- Naci keeps the tea glass in his RIGHT hand on his knee. Rıza keeps his RIGHT hand on his chest. Nobody walks.",
 "NR",
 "0-0.5 s: Naci keeps looking up toward the right edge, eyebrows high, genuinely impressed for the first time.\n0.5-2.4 s: NACI says in Turkish, slow and warm, almost moved, nodding once with respect, stressing \"ödemezdi\": \"Öncekiler ödemezdi.\" Rıza's mouth is closed.\n2.4-3.2 s: A beat. Rıza's face crumples.\n3.2-5 s: RIZA says in Turkish, a mournful half-whisper, voice breaking, hand pressed on his heart: \"Dedemin parası…\" Naci's mouth is closed.\n5-8 s: Nobody speaks. Rıza sniffs and looks up at the sky. Naci glances at him, faintly amused, and takes a slow sip of tea.",
 "both in the same places: Rıza looking up, hand on his chest; Naci sipping his tea; both mouths closed.",
 "Naci looks toward the right edge, then at Rıza. Rıza looks toward the right edge, then at the sky.",
 '"Öncekiler ödemezdi" sounds like "un-jeh-kee-LER u-deh-mez-DEE". "Dedemin parası" sounds like "deh-deh-MEEN pah-rah-SUH".')

yaz("P08",
 f"waist-up three-shot {WALL}. On the left {RZ} holds a black phone in both hands in front of his chest, reading eagerly. In the center {NC}, tea glass at his chin. On the right {SL}, a burgundy folder in her RIGHT hand against her hip, her LEFT fist on her hip, skeptical.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - the YOUNG MAN on the left, Rıza, reading a message aloud: "Emekli öğretmenim. Sessizlik arıyorum."\nLine 2 - the OLD MAN on the stool, Naci: "Doğru yere gelmiş."\nSelin does NOT speak.',
 "- Rıza holds the phone in BOTH hands the whole time; the screen faces him.\n- Selin keeps the folder in her RIGHT hand and her LEFT fist on her hip.\n- Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "RN",
 "0-0.5 s: The phone pings. Rıza's eyes light up as he reads.\n0.5-3 s: RIZA reads aloud in Turkish, putting on a prim, polite old-teacher voice for fun: \"Emekli öğretmenim. Sessizlik arıyorum.\" Naci's and Selin's mouths are closed.\n3-3.8 s: A beat. Rıza looks up from the phone, delighted. Naci lowers his glass.\n3.8-5.2 s: NACI says in Turkish, dry, slow and pleased, with a tiny satisfied nod: \"Doğru yere gelmiş.\" Rıza's mouth is closed.\n5.2-8 s: Nobody speaks. Selin snorts a small laugh through her nose and shakes her head. Rıza nods eagerly and goes back to the phone. Naci sips.",
 "all three in the same places: Rıza reading the phone in both hands; Naci sipping; Selin smiling, fist on her hip; all mouths closed.",
 "Rıza looks at the phone, at Naci, then the phone. Naci looks ahead. Selin looks at Rıza.",
 '"Emekli öğretmenim" sounds like "eh-mek-LEE ur-ret-meh-NEEM". "Sessizlik arıyorum" sounds like "ses-seez-LEEK ah-RUH-yo-room". "Doğru yere gelmiş" sounds like "doh-ROO yeh-REH gel-MEESH".', ", one phone ping")

yaz("P11",
 f"waist-up three-shot {WALL}. On the left {RZ} holds a black phone in both hands in front of his chest. In the center {NC}, tea glass at his chin. On the right {SL}, a burgundy folder in her RIGHT hand against her hip, her LEFT fist on her hip.",
 'SPEAKER ORDER (exactly two lines, in this order):\nLine 1 - the YOUNG WOMAN on the right, Selin: "Mülakat falan yok. Kim gelirse gelsin."\nLine 2 - the YOUNG MAN on the left, Rıza: "Ya kaçarlarsa?"\nNaci does NOT speak.',
 "- Rıza holds the phone in BOTH hands; at second 3.5 he lowers it to his waist.\n- Selin keeps the folder in her RIGHT hand on her hip; she gestures only with her LEFT hand.\n- Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "SR",
 "0-0.4 s: Selin straightens up: the decision is made.\n0.4-3.2 s: SELIN says in Turkish, firm and clear, a boss ending a meeting, chopping the air once with her LEFT hand on \"yok\", stressing \"falan yok\": \"Mülakat falan yok. Kim gelirse gelsin.\" Rıza's mouth is closed.\n3.2-4 s: A beat. Rıza looks up from the phone and lowers it, worried.\n4-5.2 s: RIZA asks in Turkish, small and anxious, eyebrows up in the middle: \"Ya kaçarlarsa?\" Selin's mouth is closed.\n5.2-8 s: Nobody speaks. Selin puts her LEFT fist back on her hip and gives him a calm, knowing look. Naci raises one eyebrow and sips.",
 "all three in the same places: Rıza worried, phone at his waist; Selin calm, fist on her hip; Naci sipping; all mouths closed.",
 "Selin looks at Rıza. Rıza looks at the phone, then at Selin. Naci looks at Selin.",
 '"Mülakat falan yok" sounds like "mew-lah-KAHT fah-LAHN yok". "Kim gelirse gelsin" sounds like "keem geh-leer-SEH gel-SEEN". "Ya kaçarlarsa" sounds like "yah kah-char-lar-SAH".')

yaz("P12",
 f"knees-up two-shot {WALL}, a blue door on the right. On the left {NC}, looking up at the woman, smiling, his tea glass lifted a little toward her in his RIGHT hand. On the right {SL}, calm and confident, a burgundy folder in her RIGHT hand against her hip, her LEFT fist on her hip, looking toward the left edge of the frame. Rıza is just outside the left edge of the frame.",
 'SPEAKER ORDER: only the YOUNG WOMAN, Selin, speaks in this shot, one line:\n"Üç gün dayanan kalır."\nNaci does NOT speak.',
 "- Selin keeps the folder in her RIGHT hand and her LEFT fist on her hip.\n- Naci keeps the tea glass in his RIGHT hand. Nobody walks.",
 "SN",
 "0-0.5 s: Selin takes a calm breath.\n0.5-2.6 s: SELIN says in Turkish, low, calm and certain, a small smile, each word weighted, stressing \"üç gün\": \"Üç gün dayanan kalır.\" Naci's mouth is closed.\n2.6-8 s: Nobody speaks. Naci's smile widens; he lifts his tea glass toward her in a small toast and nods slowly. Selin turns her head to him and gives a small nod back, pleased.",
 "both in the same places: Naci with his glass raised in a toast; Selin nodding to him; both mouths closed.",
 "Selin looks toward the left edge, then at Naci. Naci looks at Selin.",
 '"Üç gün dayanan kalır" sounds like "ewch gewn dah-yah-NAHN kah-LUHR".')

yaz("P13",
 f"full-body wide three-shot {WALL}; on the right side a cobbled lane runs away toward the village entrance and leaves the frame on the right. On the left {RZ} with a black phone in his LEFT hand. In the center {NC}, his tea glass raised slightly. On the right {SL}, a burgundy folder in her RIGHT hand, her LEFT fist on her hip.",
 'SPEAKER ORDER: only the YOUNG MAN, Rıza, speaks in this shot, one whispered line:\n"Biri geldi…"\nNaci and Selin do NOT speak.',
 "- Rıza keeps the phone in his LEFT hand. Selin keeps the folder in her RIGHT hand. Naci keeps the tea glass in his RIGHT hand.\n- Nobody walks. NO car, vehicle or person appears anywhere in the frame; the lane stays empty.",
 "R",
 "0-1.5 s: Quiet. Naci holds his glass up toward Selin; Selin and Rıza look at each other.\n1.5-2 s: A car horn honks twice, off screen to the RIGHT.\n2-3.5 s: All three turn their heads sharply to the RIGHT edge of the frame at the same moment. Naci freezes with his glass in mid-air. Selin's hand drops from her hip.\n3.5-5 s: RIZA whispers in Turkish, eyes huge: \"Biri geldi…\" Selin's and Naci's mouths are closed.\n5-8 s: Nobody speaks. Nobody moves; all three stare toward the right edge. A car engine idles quietly off screen.",
 "all three in the same places, heads turned to the RIGHT, staring at the empty lane; Naci's glass in mid-air; all mouths closed.",
 "Before the horn they look at each other; after it all three look toward the RIGHT edge of the frame.",
 '"Biri geldi" sounds like "bee-REE gel-DEE".', ", a car horn honking twice off screen right, a car engine idling off screen")
print("ok")
