#!/usr/bin/env python3
"""B06 kare promptları (ChatGPT, onaylı karenin düzenlemesi). python3 araclar/b06_kareler.py"""
import os, shutil
B = "diziler/sifir-sehir/bolumler/B06/kareler"; R = f"{B}/ref"
KAAN = ("Kaan (the young man from the Kaan character sheet): mid twenties, slim, short light-brown wavy hair styled up, clean-shaven, small silver stud in his left ear, "
        "bright orange hooded windbreaker open over a white T-shirt, cream cargo trousers, white sneakers; he holds a black handheld phone gimbal with a smartphone in his RIGHT hand, screen facing himself.")
TAIL = ("Keep the stylized 3D animated look, the golden late-afternoon light, the stone wall, vine with grapes, blue shutters, wooden stool and cobbles, and every face, hairstyle and costume EXACTLY as in the attached images "
        "(Rıza: messy dark curls, NO moustache, navy blazer with red pocket square; Naci: grey hair, grey moustache, faded blue work jacket; Selin: golden blonde curls, pink sweetheart-neck top, SHORT burgundy two-tier ruffled mini skirt, brown Mary-Jane flats, burgundy folder; Kaan exactly as in his character sheet). "
        "Correct hands with five fingers. Nobody looks at the camera. ONE single continuous image, vertical 2:3 (1024x1536), highest quality, people inside the middle 85% of the width. No text, no panels.")
K = {}
K["SB70"] = ("P01", ["B05_SB65.jpg", "Kaan_sayfasi.jpg"], f"""This is an EDIT of the FIRST attached image (wide full-body shot: Rıza standing on the left, Naci on his stool in the center, Selin standing on the right, the cobbled lane running away on the right). Keep the place, camera, light and these three people EXACTLY as they are, but all three now turn their heads to the RIGHT, surprised, looking at the newcomer.

Add {KAAN} He walks in on the lane on the RIGHT side of the frame, about two metres to the right of Selin, at the SAME distance from the camera as the others (the same size as them), full body, mid-step walking toward the LEFT. He holds the gimbal up in front of his face with his RIGHT hand and grins into his phone as if filming a vlog. His face is clearly visible in three-quarter view.""")
K["SB71"] = ("P02, P03", ["B05_SB63.jpg", "Kaan_sayfasi.jpg"], f"""This is an EDIT of the FIRST attached image (waist-up group in front of the stone wall). Keep the place, light and camera. New arrangement, from LEFT to RIGHT: Rıza standing, Kaan standing, Selin standing; Naci sits on his stool BEHIND and between Rıza and Kaan, lower in the frame, sipping tea, his face visible.

Add {KAAN} He stands in the center, waist up, his gimbal held up in his RIGHT hand, a big friendly vlogger grin.
Rıza (left): shaking Kaan's LEFT hand with his RIGHT hand, leaning in with an over-eager salesman smile.
Selin (right): the burgundy folder in her RIGHT hand against her hip, her LEFT arm across her waist, one eyebrow raised, dry and unimpressed, looking at Rıza.""")
K["SB72"] = ("P04, P05", ["B05_SB63.jpg", "Kaan_sayfasi.jpg"], f"""Using the place, light and people of the FIRST attached image, make a TWO-SHOT: Naci sitting on his wooden stool on the RIGHT, facing three-quarters toward the camera, seen from the knees up, his small tea glass at his lips in his RIGHT hand, eyes half closed, completely unbothered. Rıza and Selin are outside the frame.

Add {KAAN} He CROUCHES on his heels on the LEFT, in front of Naci's knees, seen in three-quarter view from the side so his face is visible, holding the gimbal up toward Naci with his RIGHT hand, the phone screen turned toward Naci, a pleading puppy-eyed face.""")
K["SB73"] = ("P06, P07", ["B05_SB63.jpg", "Kaan_sayfasi.jpg"], f"""Using the place, light and people of the FIRST attached image, make a waist-up TWO-SHOT: Kaan on the LEFT and Selin on the RIGHT, facing each other in three-quarter view. At the far LEFT edge of the frame, cut by the edge, only the shoulder and half of the face of Rıza (navy blazer) is visible, looking at Selin hopefully.

{KAAN} He holds the gimbal in his RIGHT hand at his chest, surprised, eyebrows up, mouth slightly open.
Selin: businesslike and confident, a small sly smile; the burgundy folder in her RIGHT hand against her hip; her LEFT index finger points down toward the stool (outside the bottom of the frame).""")
K["SB74"] = ("P08", ["B05_SB64.jpg"], """This is an EDIT of the attached image (Naci on his stool, Selin standing on his right). Keep the place, light, framing and both people EXACTLY. Change only the poses: Naci now turns his head up toward Selin with a shrewd, bargaining look, one eyebrow raised, the tea glass held in his RIGHT hand on his knee and his LEFT index finger raised. Selin looks down at him with an amused smile, the folder in her RIGHT hand against her hip, her LEFT hand starting to reach out toward him for a handshake. Kaan and Rıza are outside the left edge of the frame.""")
K["SB75"] = ("P09", ["B05_SB65.jpg", "Kaan_sayfasi.jpg"], f"""This is an EDIT of the FIRST attached image (wide full-body shot in front of the stone wall). Keep the place, camera and light. From LEFT to RIGHT: Rıza standing, Naci sitting on his stool, Kaan standing right next to the stool, Selin standing.

Naci: both hands on his knees, the tea glass in his RIGHT hand, leaning forward as if about to stand up, a dignified face.
Add {KAAN} Full body, the same size as the others, standing just to the right of the stool, gimbal in his RIGHT hand, bouncing on his toes, impatient and eager, looking at the stool.
Rıza: staring at Naci in disbelief, mouth half open. Selin: calm, satisfied smile, folder in her RIGHT hand at her hip.""")
K["SB76"] = ("P10, P11", ["B05_SB63.jpg", "Kaan_sayfasi.jpg"], f"""Using the place, light and people of the FIRST attached image, make a knees-up group shot. From LEFT to RIGHT: Rıza standing, Naci STANDING (holding his tea glass in his RIGHT hand, looking a little lost without his stool), Kaan SITTING on the wooden stool in the center, Selin standing on the right.

Add {KAAN} He sits on Naci's stool, his RIGHT arm raised, holding the gimbal and phone high above his head, screen toward himself, a huge live-stream grin, talking to the phone.
Rıza: leaning in behind Kaan, waving at the phone with a big smile, trying to get into the shot. Selin: the folder in her RIGHT hand at her hip, LEFT hand on her hip, amused.""")
for k, (klip, refs, body) in K.items():
    d = f"{B}/{k}"; os.makedirs(d, exist_ok=True)
    for f in os.listdir(d): os.remove(f"{d}/{f}")
    for i, r in enumerate(refs, 1): shutil.copyfile(f"{R}/{r}", f"{d}/{k}_ref{i}_{r}")
    open(f"{d}/{k}_prompt.txt", "w").write(f"Output file name: B06_{k}\n\n{body}\n\n{TAIL}\n")
print("ok")
