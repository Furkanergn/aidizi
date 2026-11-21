# AI DİKEY DİZİ ÜRETİMİ — ÖĞRENİLENLER, YÖNTEM VE SKILL'LER
**Şahmeran: Yeniden Doğuş (B01–B04) deneyiminden çıkarılmış tam rehber · BAF Films · 21 Kasım 2026 · hazırlayan: Claude**

Bu dosya iki şeyi tek yerde toplar: (A) bu projede gerçekten işe yarayan skill'ler ve araçlar; (B) 13–21 Kasım arasında Seedance 2.5 + Nano Banana Pro ile üç bölüm üretirken öğrenilen her şey — senaryo nasıl yazılır, sahne nasıl kurulur, storyboard nasıl üretilir, prompt nasıl yazılır, çıktı nasıl kontrol edilir, kurgu nasıl yapılır. Kurallar hatalardan çıktı; her birinin yanında hangi hatadan doğduğu yazılı. Kling için ayrı bir bölüm var (§9); orası bu projede denenmedi, genel bilgidir.

---

## BÖLÜM A — SKILL'LER VE ARAÇLAR

### A1. Bu projede işe yarayan skill'ler (önem sırasıyla)
| # | Skill | Ne işe yaradı | Ne zaman çağrılır | Not |
|---|---|---|---|---|
| 1 | **`cinematic-director`** (DirectorSKILL) | Sahne analizi (alt metin, beat sheet), blocking/kroki, çekim listesi, kamera yerleşimi, süreklilik kitabı, prompt sözlüğü, hata teşhis kodları, image-to-video hareket promptları | Her bölümün senaryosu bitince, plan kartları yazılmadan ÖNCE; kurgu düzeltmelerinden önce analiz için | En çok kullanılan skill. "Mode H" (ses dramaturjisi) çıktıları B01 v7'de onaysız uygulandı ve reddedildi → ses kararları her zaman A/B ile sorulur (bkz. §12). |
| 2 | **`sahmeran-kurgu-editoru`** (kullanıcının yazdığı) | Resolve kurgu iş akışı: Murch'ün 6 ölçütü, Fairlight ses post, ffmpeg QC filtreleri, faster-whisper replik zamanlaması, eksik plan talep şablonu, `qc.py` (Extend birleşim kontrolü) | Her kurguda, timeline'a dokunmadan önce | `KURGU_KURALLARI.md` ile birlikte okunur. |
| 3 | **`video-prompt-builder`** (Seedance 2.0 shot-by-shot) | Prompt bölümleme mantığı (shot/camera/action/audio), "ingredients" referans anlatımı, zaman damgalı prompt yazımı | İlk promptları yazarken şablon; sonra projeye özel şablon (§8) onu aştı | Seedance 2.5'e uyarlanmış hâli §8'dedir. |
| 4 | **`ai-prompt-builder`** | Görsel promptları (karakter sayfası, mekân plakası, storyboard) için yapı: özne → kostüm → ışık → kamera → stil → yasaklar | Karakter sayfası ve plaka üretiminde | Nano Banana Pro için "ONE single continuous photograph, no split screen, no panels" eklemesi bizden. |
| 5 | **`short-drama-skills`** (LuxReal) | Senaryoyu dikey dizi plan dizisine bölme; duygu/diyalog sahnesi ile aksiyon sahnesinin farklı planlanması; bölüm uzunluğu ve kanca mantığı | Bölüm sayısını artırıp sahne sayısını azaltma kararında | Wan/LTX tarifleri İblis Avcısı'nda kullanıldı, Şahmeran'da değil. |
| 6 | **`chrome-browser`** / **`built-in-browser`** | Higgsfield web arayüzünü kullanıcının Chrome'unda Unlimited modda sürmek (kredi harcamamak için MCP ile üretim yapılmadı) | Her üretim | Koordinatlar ve tuzaklar §13. |
| 7 | **`computer-use`** | DaVinci Resolve ekranını görmek, MCP'nin yapamadığı tıklamalar | Kurgu | Resolve için asıl araç `davinci-resolve` MCP. |
| 8 | `docx` / `pdf` | Bölüm içerik PDF'leri ve teslim paketleri | Bölüm sonu | — |

Kullanılmayan/az kullanılan: `video-edit-pipeline` (ham çekim için; AI klipte gereksiz), `ai-video-from-brief` (avatar videosu için), `premiere-*` (Premiere yok, Resolve var), `dizi-yonetmeni` (kullanıcı kaldırdı).

### A2. Araçlar (MCP ve yerel)
| Araç | Kullanım |
|---|---|
| **Higgsfield web (Chrome üzerinden)** | Tüm üretim: Nano Banana Pro (görsel, Unlimited), Seedance 2.5 480p 9:16 (video, Unlimited). Start Frame ve Extend Video modları. |
| **Higgsfield MCP — yalnız yardımcı** | `show_generations` (bitti mi?), `sandbox_exec` (curl + ffmpeg + faster-whisper ile QC; zip paketleme), `media_upload`/`media_confirm` (dosya teslimi için CDN linki). Üretim için kullanılmadı (kredi harcar). |
| **faster-whisper** | Replik doğrulama ve zamanlama: `base.en` normal; fısıltıda `medium.en` + `initial_prompt` (yoksa hallüsinasyon). Kullanıcının PC'sinde de çalışır. |
| **ffmpeg** | Contact sheet (fps 1–1.5), ilk/orta/son kare, crop+zoom, iki karenin yan yana montajı (`hstack`), RMS (`astats`), altyazı yakma (ASS). |
| **DaVinci Resolve + `davinci-resolve` MCP** | Kurgu, grade kopyalama, Fairlight, render. |
| **ElevenLabs (kullanıcı hesabı, Chrome)** | Müzik; tek üretim, varyasyon yok (kredi). |
| **Claude projesi "BAF Films"** | Tüm md dokümanlar, plan kartları, kayıtlar. |

---

## BÖLÜM B — ÖĞRENİLENLER

## 1. Temel ilke: AI video bir "çekim" değil, bir "kurulum" işidir
Seedance/Kling gibi modeller **verdiğin kareyi devam ettirir, verdiğin yüzü taklit eder, verdiğin metni yarım anlar**. İyi sonucun %80'i videodan önce kilitlenir: karakter sayfası, mekân plakası, konum krokisi, başlangıç karesi. Video promptu bu kilitlenmiş durumun üstüne yalnızca **2–3 hareket** ekler. Metinle düzeltmeye çalıştığın her şey (yüz, nesne yönü, ışık, konum) başarısız olur; görselle düzelttiğin her şey tutar.

**Dört taşıyıcı sütun:**
1. Karakter sayfası (yüz + kostüm) → her üretime bağlanır.
2. Mekân plakası (insansız, ışık yönü sabit) → her kareye bağlanır.
3. Başlangıç karesi (storyboard) → açı değişen her plan için.
4. Zincir (Extend) → aynı açı devam ediyorsa önceki klibin son karesi.

## 2. Senaryo nasıl yazılmalı (AI videoya göre)
Senaryo "güzel yazı" değil, **üretilebilir plan listesi**dir. Kurallar:

1. **Bölüm = tek mekân, tek kesintisiz zaman.** 90–100 sn. En fazla iki sahne; mekân değişimi bölüm sınırına konur. Bu, süreklilik hatasını kökten azaltır (B01 v5'ten beri ilke).
2. **Zaman atlamaz, kamera açısı değişir.** Replikler arasındaki yürüme, dönme, bakış, sessizlik gösterilir. "Sonra sarayda…" yok; köprü planı (nesne, ses, kişi taşınır) var.
3. **10–12 çekim, 8–10 klip, klip başına 8–12 sn.** 8 sn'ye **en fazla 2–3 ayrı eylem**. Fazlası varsa plan bölünür.
4. **Her çekime PERFORMANCE notu.** Duygu çekim içinde değişir (sakin → iğrenme). Dinleyenin tepkisi de yazılır; donuk yüz istenmez.
5. **Bilgi önce görüntüyle, replik sonra kısa onay.** "Vezir öldü!" diye bağırtmak yerine çan sesi + boş platform; replik 1–2 cümle. Kullanıcı düz açıklamalardan hoşlanmaz.
6. **Karşılıklı konuşma tek karede olabilir:** iki kişilik, omuz üstü, derin odak. Her replik tek kişiye kesilmez; ama **konuşan yüzü görünsün** (dudak senkronu yalnız görünür ağızda çalışır).
7. **Replik kime söyleniyorsa o kişi kadrajda ya da bir önceki/sonraki planda** olmalı; "boşluğa konuşma" yok.
8. **Şiddet:** darbe anında kesme (açı değişimi); sonrası kansız, ışık/ses/temiz nesneyle anlatılır. Filtreye takılmaz, dramatik olarak daha güçlüdür.
9. **Efekt mantığı sırayla yazılır:** kaynak → aktarım → sonuç. (Et: tepside parlar → koparılan parça elde parlar → yutulur → yüzde kısa ışık. Su: kadeh SÖNÜK → mataradan ışık → akan su parlar → kadehin içi ışıldar → içer.) Sıra yazılmazsa model ışığı en baştan koyar.
10. **Her karakterin fiziksel erişimi senaryoda doğrulanır:** ayak ucundan ağza lokma verilmez; vermesi gereken kişi yanında diz çöker. Bu, kroki çizilince ortaya çıkar — kroki senaryonun parçasıdır.
11. **Dil:** tüm diyalog İngilizce (dudak senkronu ve telaffuz İngilizcede çok daha iyi); Türkçe altyazı kurguda. Her promptta "ALL dialogue in ENGLISH ONLY".
12. **Anlatıcı** (dış ses) bölüm açıp kapatmak için; görüntüde ağız oynamaz, promptta "voice-over" yazılır.
13. **Motifler ve geri çağırma** (örn. "Forgive me" B02 S9 → B04 P06) ucuz ve güçlü; model için ekstra maliyet yok.
14. **Bölüm sonu kancası + bir sonraki bölümün ilk karesi** senaryoda yazılır (5j: sonraki bölüm bu kareden konum kilidiyle başlar).

## 3. Plan kartı — senaryodan üretime köprü (her plan için zorunlu)
| Alan | İçerik |
|---|---|
| Kimlik | `B04_S01_P05` |
| Süre | 6/8/10/12 sn (Seedance seçenekleri) |
| Mod | Start Frame = SBx-xx **veya** Extend (kaynak klip id) |
| Kamera | Konum (odanın neresi, yükseklik), yön, odak; sabit mi, çok yavaş push-in mi |
| Saniye saniye eylem | "0–3 … / 3–6 … / 6–10 …" — kim ne zaman neye uzanır, nereye bakar |
| Replik | Birebir, konuşan, zamanı |
| Bitiş karesi | Sonraki planın devralacağı konum/nesne durumu |
| Bağlanacak sayfalar | O planda görünen **her** karakter (5f) + nesne/plaka |
| 5h kontrolü | 5 soru cevaplanmış (aşağıda) |

**5h — Generate'ten önce beş soru:** (1) Her karakter yaptığı eylemi bulunduğu yerden fiziksel olarak yapabilir mi? (2) Nesnelerin durumu önceki planın son durumuyla aynı mı? (3) Işık/efekt sırası doğru mu? (4) Kaç eylem var, süreye sığar mı? (5) Replikler senaryoyla birebir mi?

## 4. Karakter sayfaları (character sheet)
- **Nano Banana Pro, 16:9, 2K, Unlimited.** Tek görselde: tam boy önden, 3/4, (arkadan) + 2–3 yüz yakını. **Saf yan profil yok** (anatomiyi bozar). Sayfada başka figür, siluet, yazı yok. Düz gri fon.
- **Yüz referansı ayrı dosya:** Cemşab'ta yüz tutarlılığı ancak ayrı "yüz referansı" kareleri bağlanınca oturdu. Kostüm sayfası + yüz referansı birlikte bağlanır.
- **Kostüm kararları yazıya dökülür ve asla değişmez:** "Kahir'in kaftanı HER ZAMAN kapalı ve düğmeli; krem sarık; tek kılıç sol kalçada." Model kaftanı açmaya, ikinci kılıç eklemeye meyillidir; promptta her seferinde tekrar edilir.
- **Yan karakterler** (asker, hizmetkâr) onaylı bir kareden referans alır: "dressed exactly like the soldier in reference X" — dönem dışı kıyafet sızmaz.
- **Her yeni karakter için sayfa** (Padişah, Hekim, yaşlı asker) — "benzer biri" yazmak yetmez.
- Kullanıcı sayfaları kendisi sıfırdan üretmeyi tercih etti (kalite ve kredi kontrolü); Claude promptu yazar, kullanıcı üretir, onaylanan sayfa upload edilir.

## 5. Mekân plakası (location plate)
- İnsansız, sabit ışık yönü ("güneş kadrajın sağında"), 9:16 ya da 16:9.
- Yasaklar yazılır: kubbe/minare, Avrupa kıyafeti, üç köşeli şapka, ip/kablo/darağacı, yazı.
- Platform/direk/basamak gibi geometri **ilk onaylı kareye kilitlenir**; sonraki her kare onunla yan yana karşılaştırılır (SB3-09 v1 "platform masaya dönmüş" diye reddedildi).
- Gece hâli gerekiyorsa ayrı plaka ya da onaylı bir gece karesi referans olur.

## 6. Storyboard kareleri (SB)
- Yalnız **açı değişen** planlar için üretilir; Extend ile devam eden planlara kare gerekmez.
- **Her kareye bağlanır:** o karede görünen tüm karakterlerin sayfaları (5f) + mekân plakası + **önceki planın son karesi (konum referansı, 5j)** + onaylı bir bakış (look) karesi ("no HDR, no cartoon").
- **Promptta mutlaka:** "ONE single continuous photograph, no split screen, no panels"; kamera konumu ve yüksekliği; kim nerede, yüzü nereye dönük, hangi elinde ne; nesnelerin durumu (örtülü/açık, sönük/parlak); ışık kaynağı; "no one looks at the camera".
- **Kontrol (büyütülerek):** anatomi/el/ayak yönü; ölçek (Şahmeran'ın başı ayaktaki erkeğin başı hizasında); kostüm ve dönem; kolaj/bölünme var mı; gökyüzünde istenmeyen öğe; **yüz = sayfa**; **konum = önceki planın son karesi** (yan yana).
- **Hatalı kare edit ile düzeltilmez (5d).** Kompozisyon/yön hatası editte miras kalır; sıfırdan üretilir. Edit yalnız yüz eşleme ve küçük nesne için.
- Nano Banana Pro "orta plan" istense de geniş çıkabilir; "MEDIUM SHOT, camera inside the room, door not visible" gibi fiziksel tarif daha iyi çalışır.
- Model başlangıç karesini **neredeyse birebir** devam ettirir: karedeki her kusur (fazladan matara, yatan Padişah) videoya geçer. Kare mükemmel olmadan video üretilmez.

## 7. Üretim modları — hangi durumda hangisi
| Durum | Mod | Neden |
|---|---|---|
| Aynı açı, aynı an devam ediyor | **Extend Video** (kaynak = önceki klip) + karakter sayfaları | Kesintisiz zincir; konum/ışık otomatik korunur |
| Açı değişiyor | **Start Frame** = onaylı SB karesi + sayfalar | Konum kilidi karede; kesme temiz |
| Önceki klibin son karesinde istenmeyen miras var (kadeh parlıyor) | Extend **yapılmaz**; yeni temiz kare üretilir, Start Frame | Miras metinle silinmez (B03 P05 v1/v2) |
| Yüz görünmeyen detay planı (kadeh yerde) | Start Frame; sayfa gerekmez | — |
| Nesnenin dönmesi/yer değiştirmesi gerekiyor | Dönüşü kaldır, nesneyi karede baştan doğru yönde koy | Metinle nesne döndürme çalışmıyor (B02 sandık) |

**Süre:** diyaloglu plan 8–10 sn, 3 replik 12 sn; tepki/detay 6–7 sn. Daha uzun tek klipte model kendi kesmesini ekler.

## 8. Seedance 2.5 prompt yazımı — şablon ve kurallar
**Şablon (sıra değişmez):**
```
[Format] Vertical 9:16, N seconds, single continuous shot, realistic live-action cinematic, <zaman/ışık>.
[References] @Image1 = first frame (SBx). @Image2 <karakter> face sheet, @Image3 <karakter> costume sheet, @Image4 <mekân/nesne>. Faces must match the sheets exactly.
[First image] Exactly @Image1: <kim nerede, yüzü nereye dönük, elinde ne, nesne durumu>.
[Action and acting] 0–3 s: … 3–6 s: … 6–10 s: … (en fazla 3 vuruş; kim, hangi el, hangi yöne; duygu değişimi)
[Background life] 2–3 küçük figüran/nesne hareketi (sessiz, kameraya bakmaz, ana karakterin önünden geçmez).
[Camera] Locked off, no movement, no zoom, no cut.  (ya da: one very slow push-in; one slow crane up)
[Sound] Ortam, efekt; zaman damgalı.
[Last image] Sonraki planın devralacağı durum.
[Style] Realistic, <tek ışık kaynağı>, no glow unless stated, no HDR, no cartoon.
[Continuity] Dekor geometrisi ilk kareyle aynı; kimse yer/taraf değiştirmez; kostüm sabitleri (kaftan kapalı…).
[Audio] <KARAKTER>, <ton>, ENGLISH ONLY, lips in sync: "…"  / Narrator voice-over: "…"  / No dialogue.
```
**Kurallar (hatalardan):**
- **Yasak kelimeler:** "flame/fire/candle" kadeh yakınında (kadeh kandile döndü). Işıklı nesne için "glow/light", ve **ne zaman** başlayıp bittiği yazılır; öncesi/sonrası "dark" diye ayrıca yazılır.
- **"Sırtı dönük"** yazıldığında ek: "no faces visible; only the backs of heads and helmets" (yoksa yüz üretir, yanlış yüz olur).
- **Nesne yönü ve el:** "right hand holds the flask, left hand the DARK goblet"; "the chest is carried handle-first toward the stairs". Yazılmazsa model rastgele seçer.
- **İçmeme/yapmama:** "does NOT drink; the goblet never touches the lips" — aksi hâlde planın sonunda bir sonraki eylemi başlatır (P05 v1 12. sn'de içti).
- **Kesme yasağı:** "ABSOLUTELY NO cut, NO dissolve, NO change of framing" — model 7. sn'de kendi yakın planına geçebiliyor (S02 v1).
- **Replik birebir ve tırnak içinde;** birden fazla replikte sıra ve konuşan yazılır. Model repliği kısaltabilir ("visor" / "Vizier" telaffuzu) — Whisper ile doğrulanır.
- **Fısıltı** çok kısık çıkar (−30 dB); kabul edip kurguda +6–9 dB yükseltmek, yeniden üretmekten daha güvenli.
- **Kamera hareketi** dekor geometrisini bozar (direk boyu, platform yüksekliği): push-in/crane yalnız sahne gerektiriyorsa, çok yavaş, bölümde 1–2 kez.
- **Kalabalık/figüran** her promptta 2–3 küçük eylem: dürtme, ağız örtme, ağırlık değiştirme, güvercin, köpek, örtü/duman. Yoksa kalabalık donuk "mankenler" olur.
- **Olumsuz liste değil, pozitif durum:** "no second sword" yerine "ONE sword, in its scabbard on the left hip" daha iyi çalışır; yasaklar yine eklenir ama asıl iş pozitif tarif.
- Prompt yazıldıktan sonra **baştan okunur, 5h soruları cevaplanır**; sonra Generate.

## 9. Kling için notlar (bu projede denenmedi — aktarılabilir ilkeler)
Yöntemin tamamı model-bağımsızdır: sayfa + plaka + başlangıç karesi + 2–3 eylem + kontrol. Kling'e geçerken dikkat:
- **Start/End Frame:** Kling'in bitiş karesi desteği, Seedance'ta yapamadığımız "varış kompozisyonunu kilitleme"yi verir; açı değişimli planlarda bitiş karesini bir sonraki planın SB'si yaparak kesme daha temiz olur. Ama iki kare arası mesafe büyükse model "morph" yapar; eylemi küçük tut.
- **Referans/Elements (çoklu görsel):** karakter sayfası + kostüm + mekân aynı mantıkla bağlanır; "@Image" yerine arayüzün kendi etiketleme biçimi kullanılır. Yüz tutarlılığı Seedance'tan farklı olabilir; ilk testte 3 açıdan yüz = sayfa kontrolü yapılır.
- **Diyalog/dudak senkronu:** Kling'de yerleşik konuşma Seedance 2.5 kadar güvenilir değilse, sessiz üretip sesi ayrı (ElevenLabs/IndexTTS) ekleyip lip-sync aracıyla bağlamak gerekir — o zaman "konuşan yüzü görünür ve sabit" kuralı daha da önemli.
- **Prompt uzunluğu:** Kling kısa, net cümlelerle daha iyi çalışır; §8 şablonunun [Action] ve [Camera] kısımları aynen kalır, [Audio] bölümü aracın desteğine göre düşer.
- **Kamera kontrolü:** Kling'in kamera preset'leri (pan/tilt/push) varsa metin yerine onlar kullanılır; "locked off" tercih edilir.
- **Süre:** 5/10 sn seçenekleri; 10 sn'de yine ≤3 eylem.
- **Aynı QC:** contact sheet, ilk/orta/son kare, yüz büyütmesi, komşu planla yan yana; Whisper (ses varsa).

## 10. Kalite kontrol (QC) — "geçti" demenin şartları
Hiçbir klip şu **beş büyütme** yazılmadan onaylı sayılmaz (5e):
1. Her figürün yüzü görünüyor mu / görünmemeli mi; **yüz = sayfa** (büyütülmüş karşılaştırma).
2. Sayım: her roldeki kişi sayısı (4 asker istendi, 4 mü?).
3. Nesnenin yönü ve kaç elde/hangi elde olduğu.
4. Dekor geometrisi ilk–orta–son karede (direk boyu, platform, duvar).
5. Komşu planla giriş–çıkış durumu **yan yana** yazılı karşılaştırma.
Ek: Whisper transkripti senaryoyla birebir mi; ses doğru karakterden mi; istenmeyen kesme/dissolve var mı; kamera "sabit" denmişken hareket etmiş mi; kimse lense bakıyor mu.

**Araç tarifi (sandbox):** `curl` klip → `ffmpeg -vf fps=1.5,scale=…,tile=…` contact sheet → ilk/orta/son kare `-ss` ile → `crop` + `scale` ile yüz/nesne büyütmesi → `hstack` ile önceki klibin son karesi + yeni klibin ilk karesi → `faster-whisper base.en` (fısıltıda `medium.en`, `initial_prompt="Kahir? She knew."`) → `astats` ile RMS.

**İlk bakışta kaçanlar (kullanıcının yakaladığı):** S13'te sırtı dönük denmişken yüzler; köprü klibinde asker yönü; Kahir'in yüzünün sayfayla uyuşmaması (bütün bir zincir boyunca!); P01→P02 konum kopukluğu. Hepsi büyütme ve yan yana karşılaştırma yapılmadığı için kaçtı.

## 11. Süreklilik (continuity) kuralları
- **5f:** planda görünen her karakterin sayfası bağlanır — hem SB'de hem videoda. Bağlanmadan Generate yok.
- **5j — konum kilidi:** açı değişen her yeni kare önceki planın son karesini konum referansı alır; kim hangi tarafta, ne nerede birebir aynı; yalnız kamera yer değiştirir. Yer değiştirme gerekiyorsa **bir planda gösterilir**; kesmeyle ışınlanma yok.
- Kostüm/aksesuar sabitleri her promptta tekrar yazılır (kaftan kapalı, tek kılıç, iki zincir).
- Nesnelerin yolculuğu plan plan yazılır (kâse: asker eli → taş → Cemşab eli → sol yan).
- Yüz referansı bağlı olsa bile **her çıktıda** yüz kontrolü (model bazen sayfayı yok sayar).
- Önceki bölümün son karesi, sonraki bölümün ilk karesinin referansıdır (B03 S02 → B04 P01).
- Kanon dosyası tutulur: kılıç nerede, kim öldü, hangi su kime; çelişki çıkarsa senaryo düzeltilir (B03'te "kılıç meydanda" → "kılıç sarayda").

## 12. Kurgu dersleri (DaVinci Resolve)
- **Extend zinciri kesintisizdir:** birleşimde yalnız sonraki klibin ilk (tekrar) karesi atılır; başka hiçbir şey yok (blend, dejudder, retime, insert, punch-in denendi, hepsi kötüleştirdi).
- **Tek grade** zincirin tamamına; kaynaklara renk gömülmez.
- **Onaylı render temel alınır**, buluttaki "aynı adlı" kopya değil (v8/v9 felaketi: −30 dB farklı miks). Yeni deneme onaylı timeline'ın kopyasında.
- **Yorum değişikliği (ses dramaturjisi, müzik, efekt) onaysız uygulanmaz;** kısa A/B ön izleme ile sorulur. DirectorSKILL'in ses önerileri tek seferde uygulandı → tamamen reddedildi (v7).
- Ses: A1 diyalog Voice Isolation %85, Leveler −15 dB; tek kesintisiz ambiyans; müzik diyalog altında −4 dB duck; fısıltı +6–9 dB.
- Dudak senkronu yakın planda 0 ms; uzak planlara dokunulmaz.
- TR altyazı ffmpeg + ASS (Inter SemiBold 60, ≤2 satır, ≤28 kr/satır); cue zamanları Whisper'dan.
- Müzik: bölge etnik (kanun, ney, bağlama, def, Hicaz), ElevenLabs tek üretim; bitiş yavaş push-in → vuruşta siyah → 2–3 sn yankı.
- Logo: **SHAHMARAN** (İngilizce).
- Claude sesi duyamaz: LUFS doğruluğu "iyi ses" demek değildir; teslimde açıkça yazılır ve kullanıcı dinler.

## 13. Higgsfield arayüzü — operasyon dersleri
- **Unlimited kuyruğu:** video ≈ 20 dk, görsel ≈ 8 dk; aynı anda tek üretim. Nadiren "Failed / Credits refunded" → aynı ayarla tekrar.
- **Prompt kutusu eski metni tutabilir:** temizle (`selectAll`+`delete`, ctrl+A Backspace) ve `[Format]` sayısının 1 olduğunu doğrula; yoksa iki prompt birleşir.
- **Uploads ızgarası kayar:** yeni upload gelince sıra değişir; thumb'a tıklamadan zoom ile doğrula. **Bu yüzden bütün bir zincir yanlış Kahir'le üretildi** (asker sayfası tıklanmıştı).
- **Duration slider** klavyeyle: knob'a tıkla → Left/Right; panel kaydırılmamışsa oklar başka kontrole gider; "Total duration" yazısını doğrula.
- "Generating" metni bayat kalabilir; yeni mp4 URL'sine bak (`show_generations`).
- Chrome bağlantısı kopunca birden fazla tarayıcı listelenir; giriş yapılmış olanı seç (kullanıcı: "Higgsfield hangisinde açıksa").
- Start Frame = 20 px'lik küçük buton; JS ile `hf_…_<id8>` id'siyle thumb bul.
- Model adı, mod, bağlanan referans id'leri **her denemede** plan kartına yazılır; aksi hâlde hata ayıklanamaz.

## 14. Hata → kural günlüğü (bir daha olmasın)
| Hata | Nerede | Kural |
|---|---|---|
| Yanlış karakter sayfası bağlandı, bütün zincir yanlış yüzle üretildi | B03 v1 | 5f + her çıktıda yüz = sayfa büyütmesi + strip zoom |
| Hekim ayak ucundan lokma uzatıyor (fiziksel imkânsız) | B03 | 5g kroki + 5h erişim sorusu |
| P01→P02 konumlar değişti (Hekim yatağa oturmuş, Kahir taraf değiştirmiş) | B03 v2 | 5j konum kilidi, yan yana karşılaştırma |
| Kadeh baştan parlıyor / aleve dönüyor | B03 P05 | 5i ışık sırası; "flame" yasak; parlak kareden Extend yok |
| Planın sonunda bir sonraki eylem başlıyor (içiyor) | B03 P05 | "does NOT drink" + bitiş karesi açıkça yazılır |
| Model kendi dissolve/yakın planını ekledi | B03 S02 | "NO cut, NO dissolve, NO change of framing" |
| Sandık metinle döndürülemedi | B02 Köprü | Nesne karede baştan doğru yönde |
| "Sırtı dönük" denince yüzler üretildi | B02 S13 | "no faces visible; only the backs of heads and helmets" |
| Kalabalık donuk | B01 | 5a figüran eylemleri her promptta |
| Fısıltı kısık, Whisper hallüsinasyon | B03 P06 | medium.en + initial_prompt; kurguda yükselt |
| Kamera hareketi direk boyunu bozdu | B01/B03 | 5c kamera sabit/çok yavaş |
| Şahmeran'ın boyu tutarsız | B01 | Ölçek kilidi sayfada ve her promptta |
| Edit ile düzeltilen karede hata miras kaldı | B02 | 5d |
| Ses dramaturjisi onaysız uygulandı → red | B01 v7 | A/B ön izleme ile sor |
| Bulut kopyasıyla kurgu kuruldu → −30 dB | B01 v8/v9 | Onaylı render'ı stage et, doğrula |
| Extend birleşimine blend/dejudder → tutukluk | B01 v3/v4 | Yalnız tekrar kare atılır |
| "Geçti" dendi, kullanıcı yüz/yön hatası yakaladı | B02/B03 | 5e beş büyütme yazılmadan onay yok |

## 15. Bölüm üretim akışı (sıra)
1. Senaryo (İngilizce diyalog, PERFORMANCE, kroki, efekt sırası, bitiş kancası) → **kullanıcı onayı**.
2. Plan kartları (kimlik, mod, saniye saniye, bağlanacak sayfalar, 5h).
3. Eksik karakter sayfaları ve plaka → onay.
4. SB kareleri (yalnız açı değişenler) → her biri önceki planın son karesiyle yan yana + 5 madde + yüz = sayfa.
5. Video: Start Frame / Extend sırasıyla; her üretimde sayfalar bağlı; prompt şablonu; 5h.
6. QC: 5 büyütme + Whisper + komşu planla yan yana → plan kartına kayıt (id, mod, referanslar, sonuç, hata nedeni).
7. Onay sayfası (HTML, oynatıcılı) → **kullanıcı onayı**. Onaysız sonraki bölüme geçilmez.
8. Kurgu (yalnız istenince): `KURGU_KURALLARI.md` + editör skill'i; A/B ile yorum kararları.
9. Teslim paketi: senaryo, plan kartları, kayıtlar, linkler, onay sayfası, proje özeti.

## 16. İletişim kuralları (kullanıcı tercihleri)
- Türkçe; sonuçlar düz link olarak (widget değil); kısa, önce sonuç.
- Hiçbir üretim kontrol edilmeden gösterilmez; "seçenek" olarak bile.
- Durum sorulduğunda: hangi planlar onaylı, hangileri üretimde, ne kaldı — tablo.
- Hata kullanıcı tarafından yakalanınca: kural eklenir, dosyaya yazılır, bir daha olmaz.
- Kredi harcayan her şey önce sorulur; Unlimited varsa Unlimited.

---
**Kısa özet:** Kaliteyi prompt değil, **kilitlenmiş görsel durum + küçük hareket + acımasız kontrol** verir. Senaryo tek mekânda, saniye saniye, fiziksel olarak mümkün yazılır; her karakterin sayfası her üretime bağlanır; açı değişiminde konum kilitlenir; 8 saniyeye 3 eylem; kamera sabit; her çıktı büyütülür ve komşusuyla yan yana konur; hata çıktığında metinle değil görselle düzeltilir ve kural olarak yazılır.
