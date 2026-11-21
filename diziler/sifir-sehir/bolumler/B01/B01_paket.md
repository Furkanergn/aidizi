# B01 üretim paketi — plan tablosu

Bu dosya `araclar/b01_paket.py` tarafından üretilir; elle düzenleme, betiği düzenle.

## 1. Kareler (görsel üretimi, 9:16)

Her kare için: listedeki referansları ekle, `kareler/SBxx.txt` içindeki promptu yapıştır. Üretilen kareyi sohbete yükle; onaylanmadan videosu üretilmez.

| Kare | Ne | Eklenecek referanslar | Hangi klipte |
|---|---|---|---|
| SB01 | Selin yakın plan | Selin sayfası; Selin ifade sayfası; V10 plaka (ters açı) | P01, P07 |
| SB02 | Köy girişi geniş, tabela ve keçi | V8 plaka (köy girişi); V6 tabela; V7 keçi | P02 |
| SB03 | Selin + Rıza ikili, Rıza gururlu | Selin sayfası; Selin ifade sayfası; Rıza sayfası; Rıza ifade sayfası; Boy sayfası; V10 plaka (ters açı); Nesne: kapalı dosya | P03 |
| SB04 | Keçi tabelayı yiyor, yakın plan | V7 keçi; V6 tabela; V8 plaka (köy girişi) | P04 |
| SB05 | Selin tapuyu okuyor, Rıza omzundan bakıyor | Selin sayfası; Selin ifade sayfası; Rıza sayfası; Rıza ifade sayfası; Boy sayfası; V10 plaka (ters açı); Nesne: kapalı dosya | P05 |
| SB06 | Selin + Rıza ikili, Selin Rıza'ya dönük | Selin sayfası; Selin ifade sayfası; Rıza sayfası; Rıza ifade sayfası; Boy sayfası; V10 plaka (ters açı); Nesne: kapalı dosya; SB03 (onaylı kare, konum için) | P06a |
| SB08 | Rıza tek, satışa hazırlanıyor | Rıza sayfası; Rıza ifade sayfası; V10 plaka (ters açı) | P08 |
| SB09 | Köy girişi geniş, tabela yerde | V8 plaka (köy girişi); V6 tabela; V7 keçi; SB02 (onaylı kare, konum için) | P09 |
| SB10 | Naci taburede, orta plan | Naci sayfası; Naci ifade sayfası; V9 plaka (Naci'nin duvarı); Nesne: çay bardağı; Nesne: zarf | P10, P13 |
| SB11 | Selin + Rıza ikili, Naci'ye bakıyorlar | Selin sayfası; Selin ifade sayfası; Rıza sayfası; Rıza ifade sayfası; Boy sayfası; V10 plaka (ters açı); Nesne: kapalı dosya; SB03 (onaylı kare, konum için) | P11 |
| SB12 | Naci yakın plan | Naci sayfası; Naci ifade sayfası; V9 plaka (Naci'nin duvarı); Nesne: çay bardağı; SB10 (onaylı kare, konum için) | P12 |
| SB14 | Selin + Rıza ikili, Rıza kâğıdı okuyor | Selin sayfası; Selin ifade sayfası; Rıza sayfası; Rıza ifade sayfası; Boy sayfası; V10 plaka (ters açı); Nesne: kapalı dosya; Nesne: zarf; SB03 (onaylı kare, konum için) | P14 |

Üretim sırası: önce SB03 ve SB10 (diğer kareler bunları konum referansı olarak kullanıyor) ve SB01, SB02; sonra kalanlar.

## 2. Klipler (Flow, Veo 3.1 Lite, 9:16, kareden videoya)

Her klip için: başlangıç karesi olarak onaylı kareyi yükle, süreyi seç, `videolar/Pxx.txt` içindeki promptu yapıştır. Çıkan mp4'ü sohbete yükle.

| Klip | Ne | Başlangıç karesi | Süre | Replikler |
|---|---|---|---|---|
| P01 | Soğuk açılış | SB01 | 4 sn | SELİN: "Rıza… bunun neresi şehir?" |
| P02 | Şehir merkezi | SB02 | 4 sn | — |
| P03 | Tabelası bile var | SB03 | 6 sn | RIZA: "Şehir merkezi burası aşkım! Bak, tabelası bile var." / SELİN: "Tabelayı keçi yiyor, Rıza." |
| P04 | Keçi | SB04 | 4 sn | — |
| P05 | Tapu | SB05 | 8 sn | SELİN: "On iki ev, bir depo, bir değirmen… Nüfus: üç." / RIZA: "Üç bin mi?" / SELİN: "Üç." |
| P06a | Kimin parasıyla | SB06 | 6 sn | SELİN: "Kimin parasıyla?" / RIZA: "Dedemden kalan… biraz da birikim." |
| P06b | Biraz dediğin | P06a'nın son karesi | 6 sn | SELİN: "Biraz dediğin?" / RIZA: "Ev için ayırdığımız kadar." |
| P07 | Göz | SB01 | 4 sn | — |
| P08 | Potansiyel | SB08 | 6 sn | RIZA: "Ama potansiyele bak! Şuraya kafe, şuraya ortak çalışma alanı—" |
| P09 | Tabela | SB09 | 4 sn | — |
| P10 | Naci | SB10 | 6 sn | NACİ: "Yeni sahipler siz misiniz?" / "Öncekiler de böyle heyecanlıydı." |
| P11 | Öncekiler | SB11 | 4 sn | SELİN: "Öncekiler mi?" |
| P12 | Üç gün | SB12 | 4 sn | NACİ: "Üç gün dayandılar." |
| P13 | Zarf | SB10 | 6 sn | NACİ: "Bu arada… köyün elektrik borcu." / "Artık sizin." |
| P14 | Kaç | SB14 | 6 sn | SELİN: "Rıza. Kaç?" |
| **Toplam** | | | **78 sn** | |

Notlar:
- P06b'nin başlangıç karesi P06a klibinin son karesidir: P06a'yı yükleyince son kareyi ben çıkarıp sana veririm.
- P01 ve P07 aynı kareden (SB01), P10 ve P13 aynı kareden (SB10) başlar; aralarında başka planlar olduğu için kurguda sıçrama görünmez.
- Ekran yazıları ve başlık kurguda eklenir; kliplerde yazı istenmez.


---

# Kare promptları

## SB01

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Close-up of Selin, head and shoulders, centered in the frame. Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt.
Expression: frozen, flat disbelief, lips slightly parted, eyes fixed on something far ahead, just above and to the left of the lens. A light breeze lifts a few curls. Her hands and the folder are NOT in the frame.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB02

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Wide shot of the empty village entrance, exactly as in the attached location plate: gravel road in the foreground, cobbled street between old stone houses with closed blue shutters, the leaning rusty road sign in the left foreground reading exactly "ŞEHİR MERKEZİ" (two lines: ŞEHİR / MERKEZİ).
At the foot of the sign stands the goat from the attached sheet (white, one brown ear, red rope collar with a brass bell), side on, head raised toward the lower corner of the sign, bored half-closed eyes. The goat is about knee-high to the sign's panel; the sign is taller than the goat.
No people anywhere.

Light: late afternoon golden light, sun low on the left side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB03

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Two-shot from the chest up. Selin stands on the LEFT, Rıza on the RIGHT, shoulder to shoulder, both facing the camera direction and looking past the camera at the village, slightly to the right of the lens.
Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt. She hugs a closed burgundy leather A4 folder with a thin elastic band, about as wide as her torso flat against her chest with BOTH arms crossed over it. Her face is completely flat, unimpressed.
Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. His arms hang at his sides, out of frame. He beams with a proud, overexcited salesman grin, chest out.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB04

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Close shot. The rusty road sign fills the left two thirds of the frame, seen slightly from below, its text fully readable and exactly: "ŞEHİR MERKEZİ" (two lines: ŞEHİR / MERKEZİ). Its top right corner is already bitten off and ragged.
On the right, the head and neck of the goat from the attached sheet (white, one brown ear, short curved horns, small beard, red rope collar with a brass bell) reach up to that bitten corner; its teeth are closed on the metal edge, jaw pushed sideways, eyes half closed and bored.
Background: the stone houses of the village street from the attached plate, softly out of focus. No people.

Light: late afternoon golden light, sun low on the left side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB05

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Chest-up shot. Selin stands slightly left of center, facing the camera direction. Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt. She holds a burgundy leather A4 folder OPEN in BOTH hands at chest height, like an open book, one hand on each edge; the open folder is as wide as her shoulders. The inside of the folder faces HER: the camera sees only its burgundy leather outside, no text. Her eyes are lowered, reading, with a small frown.
Rıza stands half a step behind her on the RIGHT edge of the frame, leaning in to peek over her shoulder at the folder. Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. His hands are not visible. His face is hopeful, eyebrows up, a small nervous smile.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB06

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Two-shot from the chest up, same framing and same positions as the attached approved frame: Selin on the LEFT, Rıza on the RIGHT, shoulder to shoulder.
Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt. She hugs a closed burgundy leather A4 folder with a thin elastic band, about as wide as her torso flat against her chest with BOTH arms crossed over it. Her head is turned toward Rıza; she looks straight at his face, calm and hard, jaw set.
Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. His arms hang at his sides, out of frame. He faces forward but his eyes slide sideways toward Selin: caught, a tight nervous smile, shoulders slightly raised.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB08

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Medium shot of Rıza alone, from the waist up, centered. Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. Brown trousers, belt visible. Both hands are raised to chest height, palms up and open, as if about to present something. His smile is wide but forced, eyebrows high: a man rallying himself.
He looks past the camera at the village, slightly to the right of the lens.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB09

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Wide shot of the empty village entrance, same camera position as the attached approved frame and the attached location plate.
The rusty road sign has just fallen: it now lies flat on the gravel in the left foreground, panel facing up, its bent pole beside it, a small hole in the ground where it stood. The text on the fallen panel is readable and exactly "ŞEHİR MERKEZİ". A low cloud of pale dust hangs around it.
The goat from the attached sheet (white, one brown ear, red rope collar with a brass bell) stands one step to the right of the fallen sign, side on, calmly chewing, not looking at it.
No people anywhere.

Light: late afternoon golden light, sun low on the left side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB10

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Medium shot, from the knees up. Naci sits on the small wooden stool against the low stone wall, exactly as in the attached location plate: the faded blue door on the right, the flat stone shelf sticking out of the wall beside the stool. Naci: thin man in his late sixties, grey swept-back hair, thick grey moustache, bushy grey eyebrows, faded blue work jacket over a checked shirt. Grey trousers.
His body is turned three-quarters toward the right of the frame. His RIGHT hand holds a small tulip-shaped tea glass full of dark red tea at chest height, between thumb and two fingers; the glass is about as tall as his palm is wide. His LEFT hand rests flat on his left knee.
On the flat stone shelf beside him lies a thick mustard-yellow paper envelope, slightly bigger than a man's open hand, flap closed.
He looks toward the right edge of the frame, at people outside the frame, eyes half closed, faintly amused, completely relaxed.

Light: late afternoon golden light, sun low on the left side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB11

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Two-shot from the chest up, same framing and same positions as the attached approved frame: Selin on the LEFT, Rıza on the RIGHT, shoulder to shoulder.
Both have turned their heads toward the LEFT edge of the frame and look at someone outside the frame on the left.
Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt. She hugs a closed burgundy leather A4 folder with a thin elastic band, about as wide as her torso flat against her chest with BOTH arms crossed over it. One eyebrow raised, wary.
Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. His arms hang at his sides, out of frame. His smile is still in place but stiff; his eyes are worried.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB12

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Close-up of Naci, head and shoulders, centered, the same man in the same place as in the attached approved frame. Naci: thin man in his late sixties, grey swept-back hair, thick grey moustache, bushy grey eyebrows, faded blue work jacket over a checked shirt.
His RIGHT hand holds the small tulip-shaped tea glass just below his chin, at the bottom edge of the frame. His face is flat and unreadable, stating a fact. He looks toward the right edge of the frame, at people outside the frame.
Background: the stone wall and the faded blue door from the attached location plate, softly out of focus.

Light: late afternoon golden light, sun low on the left side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```

## SB14

```
Stylized 3D animated feature film still, vertical 9:16. ONE single continuous image: no split screen, no panels, no borders, no captions, no text overlays.

Two-shot from the chest up, same framing and same positions as the attached approved frame: Selin on the LEFT, Rıza on the RIGHT, shoulder to shoulder.
Rıza: man in his mid thirties, messy dark curls, long nose, thick dark eyebrows, light stubble, navy blazer with a red pocket square over a cream shirt. He is half a head taller than Selin. His LEFT hand holds the torn-open mustard-yellow envelope at chest height. His RIGHT hand holds a single white sheet of paper just above it; the printed side faces HIM, the camera sees only the blank white back of the sheet. His eyes are lowered to the sheet; the last of a smile is still on his mouth but his eyebrows are already rising in alarm.
Selin: woman in her early thirties, golden blonde curls to the jaw, freckles, small gold hoop earrings, pink ribbed top with flutter sleeves tucked into a burgundy tiered skirt. She hugs a closed burgundy leather A4 folder with a thin elastic band, about as wide as her torso flat against her chest with BOTH arms crossed over it. Her head is turned toward Rıza; she watches his face, not the paper, perfectly calm.
Background: the view out of the village from the attached reverse-angle plate, softly out of focus: gravel road, a dark grey car on the left, scrub and a hazy hillside.

Light: late afternoon golden light, sun low on the right side of the frame, long soft shadows, warm and clean.
Characters must match the attached character sheets and expression sheets exactly: same faces, hair, proportions and clothes, same stylization (animated-film skin, no pores, no photorealism). The background must match the attached location plate.
Nobody looks at the camera. Sharp focus on the faces, background slightly soft.
```


---

# Video promptları

## P01

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: close-up of Selin, frozen, staring past the camera at something far ahead. A light breeze moves her curls.

Hands and objects (do not change):
- Selin's hands and the folder stay out of the frame for the entire shot.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1 s: Selin stares ahead without blinking. A goat bleats once, off screen, far away.
1-3.5 s: Without moving her eyes, she says in Turkish, quiet and flat, with a pause after the name: "Rıza… bunun neresi şehir?"
3.5-4 s: She holds the stare. One slow blink.

Last frame: the same close-up, Selin still staring ahead, mouth closed.

Eyes: Selin looks only at the far point ahead, just above and left of the lens. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "şehir" sounds like "sheh-HEER".

Only the speaking character's mouth moves. Audio: the voices and light wind and one distant goat bleat only. No music, no subtitles, no on-screen text.
```

## P02

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: wide shot of the empty village entrance with the leaning road sign and the goat at its foot.

Hands and objects (do not change):
- The road sign stays standing, at the same angle, for the entire shot. Its text stays exactly "ŞEHİR MERKEZİ" and never changes.
- The goat stays at the foot of the sign and does not walk.

0-4 s: Nothing happens. A few dry leaves drift across the gravel. The sign creaks once in the wind. The goat chews slowly, ear flicking once. Its bell gives one soft tinkle.

Last frame: the same wide shot, sign standing, goat in the same place.

Eyes: The goat looks at the sign. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

No dialogue. Nobody speaks. Audio: light wind, one metal creak, one soft bell tinkle only. No music, no subtitles, no on-screen text.
```

## P03

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: chest-up two-shot, Selin on the left hugging a burgundy folder, Rıza on the right grinning proudly; both look past the camera at the village.

Hands and objects (do not change):
- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size.
- Rıza gestures only with his LEFT arm (the arm away from Selin, on the right side of the frame). His right arm stays down, out of frame.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.
- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-3 s: Rıza points with his LEFT arm toward something off screen on the right and says in Turkish, proud and overexcited: "Şehir merkezi burası aşkım! Bak, tabelası bile var."
3-5 s: Selin turns only her head toward Rıza and answers in Turkish, completely flat: "Tabelayı keçi yiyor, Rıza."
5-6 s: Nobody speaks. Rıza's grin freezes, his arm still half raised. Selin keeps looking at him.

Last frame: both stand exactly where they started; Selin looks at Rıza, Rıza looks ahead with a frozen grin.

Eyes: Rıza looks past the camera toward the right. Selin looks ahead, then at Rıza. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "şehir" sounds like "sheh-HEER". "keçi" sounds like "keh-CHEE".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P04

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: close shot of the goat's head biting the ragged top corner of the rusty road sign.

Hands and objects (do not change):
- The sign does not move or fall. Its text stays exactly "ŞEHİR MERKEZİ" and never changes.
- The goat's head stays at the corner of the sign.

0-4 s: The goat chews the metal corner slowly, jaw sliding sideways, eyes half closed. It blinks once. One ear flicks. The bell on its collar tinkles softly.

Last frame: the goat still chewing the same corner, the sign unchanged.

Eyes: The goat looks at nothing in particular. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

No dialogue. Nobody speaks. Audio: slow crunchy chewing, one soft bell tinkle, light wind only. No music, no subtitles, no on-screen text.
```

## P05

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 8 seconds.

Start exactly from the first frame: chest-up shot of Selin reading from an open burgundy folder held in both hands; Rıza leans in behind her on the right edge of the frame, peeking over her shoulder.

Hands and objects (do not change):
- Selin holds the open folder with BOTH hands, one on each edge, at chest height, for the entire shot. She never lets go, never closes it, never gestures. The folder keeps the same size. The camera only ever sees its burgundy outside.
- Rıza's hands stay out of the frame.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.
- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1 s: Selin's eyes move along a line in the folder.
1-4.5 s: Still reading, she says in Turkish, like someone reading a list aloud, slowing down at the end: "On iki ev, bir depo, bir değirmen… Nüfus: üç."
4.5-6 s: Rıza, hopeful, eyebrows up, asks in Turkish: "Üç bin mi?"
6-7.5 s: Selin answers in Turkish without lifting her eyes from the folder, flat: "Üç."
7.5-8 s: Nobody speaks. Rıza's hopeful face drops.

Last frame: Selin still reading the open folder in both hands; Rıza behind her, deflated.

Eyes: Selin looks only down at the folder. Rıza looks at the folder, then at the back of Selin's head. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "değirmen" sounds like "deh-eer-MEN". "nüfus" sounds like "new-FOOS". "üç" sounds like "ewch".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P06a

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: chest-up two-shot, Selin on the left hugging the burgundy folder and looking hard at Rıza; Rıza on the right, facing forward, eyes sliding toward her, nervous smile.

Hands and objects (do not change):
- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size.
- Rıza's arms stay down, out of frame. He makes no gestures.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.
- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-0.5 s: Selin stares at Rıza.
0.5-2 s: Selin asks in Turkish, quiet and precise: "Kimin parasıyla?"
2-5.5 s: Rıza looks away from her, clears nothing, and answers in Turkish, light at first and slower after the pause: "Dedemden kalan… biraz da birikim."
5.5-6 s: Nobody speaks. Selin does not blink.

Last frame: both stand exactly where they started; Selin still looking at Rıza, Rıza looking down and away.

Eyes: Selin looks only at Rıza's face. Rıza looks down and away from her. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P06b

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: chest-up two-shot, Selin on the left hugging the burgundy folder and looking at Rıza; Rıza on the right, looking down and away.

Hands and objects (do not change):
- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size.
- Rıza's arms stay down, out of frame. He makes no gestures.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.
- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1.5 s: Selin, still looking at him, asks in Turkish, even quieter: "Biraz dediğin?"
1.5-2.5 s: Rıza swallows. His shoulders rise a little.
2.5-5 s: Rıza answers in Turkish, his voice dropping lower with every word until it is almost a mumble: "Ev için ayırdığımız kadar."
5-6 s: Nobody speaks. Selin's face does not move at all.

Last frame: both stand exactly where they started; Selin staring at Rıza, Rıza shrunk into his shoulders, looking at the ground.

Eyes: Selin looks only at Rıza's face. Rıza looks at the ground. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P07

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: close-up of Selin, frozen, staring past the camera. A light breeze moves her curls.

Hands and objects (do not change):
- Selin's hands and the folder stay out of the frame for the entire shot.

0-2 s: Selin does not move and does not blink. Only her curls move in the breeze.
2-2.5 s: Her LEFT eyelid twitches once, small and sharp. Nothing else in her face moves.
2.5-4 s: She stays frozen. A goat bleats once, off screen, far away.

Last frame: the same close-up, Selin still frozen, mouth closed.

Eyes: Selin looks only at the far point ahead, just above and left of the lens. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

No dialogue. Nobody speaks. Audio: light wind and one distant goat bleat only. No music, no subtitles, no on-screen text.
```

## P08

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: waist-up shot of Rıza alone, both palms open at chest height, a wide forced smile, looking past the camera at the village.

Hands and objects (do not change):
- Rıza gestures only with his LEFT arm (on the right side of the frame). His right hand lowers to his side at the start and stays there.

Voices (must sound exactly the same in every clip of this series):
- Rıza: Turkish man in his mid thirties. Warm, bright, slightly nasal tenor. Talks fast, easily excited, salesman energy.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1 s: Rıza takes a quick breath and pulls his smile wider.
1-4 s: He sweeps his LEFT arm toward the right of the frame, pointing at one spot and then another, and says in Turkish, fast, in full salesman mode: "Ama potansiyele bak! Şuraya kafe, şuraya ortak çalışma alanı—"
4 s: A loud metal CLANG and a heavy thud come from off screen on the right. He stops in the middle of the word.
4-6 s: Rıza freezes: arm still in the air, smile stuck on his face. Only his eyes slide slowly toward the sound.

Last frame: Rıza frozen in place, arm raised, smile stuck, eyes turned toward the right edge of the frame.

Eyes: Rıza looks past the camera at the village, then toward the right edge of the frame. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "potansiyele" sounds like "po-tan-see-yeh-LEH". "çalışma" sounds like "cha-lush-MAH".

Only the speaking character's mouth moves. Audio: the voices and light wind, then one loud metal clang with a heavy thud at 4 seconds only. No music, no subtitles, no on-screen text.
```

## P09

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: wide shot of the village entrance; the road sign lies flat on the gravel in a low cloud of dust, the goat stands beside it chewing.

Hands and objects (do not change):
- The sign lies flat on the ground and does not move. Its text stays exactly "ŞEHİR MERKEZİ".
- The goat takes at most one slow step.

0-4 s: The dust cloud drifts and slowly thins. The goat keeps chewing, takes one unhurried step away from the sign, and stops. Its bell tinkles once. It never looks at the sign.

Last frame: the sign flat on the ground, the dust nearly settled, the goat standing one step further right, chewing.

Eyes: The goat looks away from the sign. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

No dialogue. Nobody speaks. Audio: light wind, soft chewing, one bell tinkle only. No music, no subtitles, no on-screen text.
```

## P10

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: knees-up shot of Naci sitting on a wooden stool against a stone wall, a small tea glass in his right hand, a thick yellow envelope lying on the stone shelf beside him; he looks toward people off screen on the right.

Hands and objects (do not change):
- Naci's RIGHT hand holds the tea glass for the entire shot. The glass keeps the same size.
- His LEFT hand stays flat on his left knee and does not move.
- The yellow envelope stays untouched on the stone shelf.
- He stays seated.

Voices (must sound exactly the same in every clip of this series):
- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-2 s: Naci asks in Turkish, slow and unbothered: "Yeni sahipler siz misiniz?"
2-3.5 s: He lifts the glass and takes one slow sip, eyes still on them.
3.5-5.5 s: He lowers the glass and says in Turkish, dry, as a simple observation: "Öncekiler de böyle heyecanlıydı."
5.5-6 s: A very small smile under his moustache.

Last frame: Naci seated exactly as at the start, glass at chest height, left hand on his knee, envelope on the shelf.

Eyes: Naci looks only toward the right edge of the frame. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "heyecanlıydı" sounds like "heh-yeh-jan-LUY-duh".

Only the speaking character's mouth moves. Audio: the voices and light wind, one faint clink of glass only. No music, no subtitles, no on-screen text.
```

## P11

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: chest-up two-shot, Selin on the left hugging the burgundy folder, Rıza on the right; both look at someone off screen on the left.

Hands and objects (do not change):
- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size.
- Rıza's arms stay down, out of frame. He makes no gestures.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1 s: Both stare toward the left. Selin's eyebrow rises.
1-2.5 s: Selin asks in Turkish, sharp and quiet: "Öncekiler mi?"
2.5-4 s: Nobody speaks. Rıza's stiff smile twitches at one corner. He does not say anything.

Last frame: both stand exactly where they started, still looking off screen to the left.

Eyes: Selin and Rıza look only toward the left edge of the frame. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "Öncekiler" sounds like "urn-jeh-kee-LEHR".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P12

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 4 seconds.

Start exactly from the first frame: close-up of Naci, the tea glass just below his chin in his right hand, a flat unreadable face, looking toward people off screen on the right.

Hands and objects (do not change):
- Naci's RIGHT hand holds the tea glass just below his chin for the entire shot. He does not drink.

Voices (must sound exactly the same in every clip of this series):
- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-1 s: Naci looks at them, unhurried.
1-3 s: He says in Turkish, flat, a plain fact: "Üç gün dayandılar."
3-4 s: One slow blink. His face does not change.

Last frame: the same close-up, Naci unmoved, glass in the same place.

Eyes: Naci looks only toward the right edge of the frame. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "üç" sounds like "ewch". "gün" sounds like "gewn". "dayandılar" sounds like "da-yan-duh-LAR".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```

## P13

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: knees-up shot of Naci sitting on a wooden stool against a stone wall, a small tea glass in his right hand, a thick yellow envelope lying on the stone shelf beside him; he looks toward people off screen on the right.

Hands and objects (do not change):
- Naci's RIGHT hand holds the tea glass at chest height for the entire shot. He does not drink.
- His LEFT hand lifts from his knee, picks up the yellow envelope from the stone shelf and holds it out toward the right edge of the frame at arm's length. The envelope keeps the same size and stays closed.
- He stays seated.

Voices (must sound exactly the same in every clip of this series):
- Naci: Turkish man in his late sixties. Slow, dry, gravelly low voice. Never in a hurry, faintly amused.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-2.5 s: Naci says in Turkish, as if he has just remembered something small: "Bu arada… köyün elektrik borcu." While he speaks, his LEFT hand picks up the yellow envelope from the stone shelf.
2.5-4 s: He holds the envelope out toward the right edge of the frame, arm straight, without getting up.
4-5.5 s: He says in Turkish, casual, almost kind: "Artık sizin."
5.5-6 s: He keeps the envelope held out. His face does not change.

Last frame: Naci seated, tea glass in his right hand, left arm stretched out holding the envelope toward the right edge of the frame.

Eyes: Naci looks only toward the right edge of the frame. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "köyün" sounds like "kur-YEWN". "borcu" sounds like "bor-JOO". "artık" sounds like "ar-TUK".

Only the speaking character's mouth moves. Audio: the voices and light wind, a soft rustle of paper only. No music, no subtitles, no on-screen text.
```

## P14

```
Stylized 3D animated feature film look, single continuous shot. Camera is locked off for the whole shot: no pan, no zoom, no cut. Duration 6 seconds.

Start exactly from the first frame: chest-up two-shot, Rıza on the right holding a torn-open yellow envelope in his left hand and a single white sheet in his right hand, reading it; Selin on the left hugging the burgundy folder, watching his face.

Hands and objects (do not change):
- Selin keeps BOTH arms crossed over the burgundy folder against her chest for the entire shot. She makes no hand gestures. The folder never moves and keeps the same size.
- Rıza's LEFT hand holds the envelope and his RIGHT hand holds the sheet at chest height for the entire shot. He does not lower them, turn the sheet or gesture. The camera only ever sees the blank back of the sheet.

Voices (must sound exactly the same in every clip of this series):
- Selin: Turkish woman in her early thirties. Calm, warm, slightly husky low voice. Dry, deadpan humor, never loud.

Every character is a native Turkish speaker. They speak ONLY Turkish, with a natural Istanbul accent and the lively, expressive delivery of actors in a Turkish animated comedy film. No English.

0-2 s: Rıza's eyes move down the sheet. The last of his smile disappears. His eyebrows climb.
2-3.5 s: Selin, watching his face, says in Turkish, calm and very quiet, two separate words: "Rıza. Kaç?"
3.5-5 s: Rıza swallows hard. He opens his mouth slightly, closes it again and says nothing. His eyes stay on the sheet.
5-6 s: Nobody moves. Selin keeps looking at him.

Last frame: both stand exactly where they started; Rıza staring at the sheet, pale, mouth closed; Selin watching him.

Eyes: Rıza looks only at the sheet. Selin looks only at Rıza's face. Nobody looks at the camera. Faces, hair and clothes stay identical to the first frame.

Pronunciation: the name "Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza" or "Reeza". "Kaç" sounds like "kach".

Only the speaking character's mouth moves. Audio: the voices and light wind only. No music, no subtitles, no on-screen text.
```
