# SIFIR ŞEHİR B01 İNCELEMESİ VE AI DİZİ ÜRETİM SİSTEMİ RAPORU

**21 Kasım 2026 · hazırlayan: Claude**

Bu rapor dört şeyi kapsar: (1) Sıfır Şehir B01'in neden kötü çıktığı, (2) karakterlerin incelemesi, (3) Türkçe ses, model seçimi ve maliyet için araştırma sonuçları, (4) "sıradaki bölümü yap" dediğinde bölümü baştan sona çıkaracak sistemin tasarımı ve kurulması için gerekenler.

## Bu rapora ne kadar güvenebilirsin

| Bilgi türü | Kaynak | Güven |
|---|---|---|
| B01 video bulguları (kareler, kesmeler, ses seviyeleri, eksik replik) | Videoyu kare kare çıkardım, ses ölçümlerini ffmpeg ile aldım, konuşmayı yazıya döktüm | Yüksek |
| Higgsfield kredi fiyatları, plan fiyatları, kredi dökümü | Bugün hesabından canlı olarak çekildi | Yüksek |
| Model yetenekleri, Türkçe desteği, Instagram verileri, dış servis fiyatları | Web araştırması. Bu oturumda sayfalar açılamadı, yalnızca arama sonuç özetleri okunabildi | Orta: yön gösterir, karar öncesi test edilmeli |
| Hangi modelin bizim karakterlerde en iyi sonucu verdiği, hangi sesin Türkçede doğal olduğu | Hiçbir kaynak Pixar tarzı 3D karakterde Türkçe diyalog test etmemiş | Bilinmiyor: yalnızca kendi testimizle çözülür |

İki sınırım var ve ikisi de sistemi etkiliyor: **sesi duyamıyorum** (yalnızca ölçebiliyor ve yazıya dökebiliyorum) ve bu oturumda **hiç üretim yapmadım** (hesapta 23 kredi var).

---

## 1. Özet: en önemli 8 bulgu

1. **Asıl sorun model değil, yöntem.** B01'de 90 saniyenin 39'u aynı geniş açıdan, 26'sı aynı araba içi açısından. Toplam 3 ana kadraj var, yüz yakın planı yok. Telefonda yüzler küçük kaldığı için hangi model kullanılırsa kullanılsın mimik okunmaz.
2. **Bir bölüm 500 değil, yaklaşık 814 krediye mal olmuş.** 20–21 Kasım dökümü: Kling 4.0 466, Sync Lipsync 253, Kling 3.0 68, görsel 22, ses 5 kredi. Lipsync'e giden 253 kredi boşa gitmiş, çünkü final Kling'in kendi sesini kullanıyor.
3. **Türkçe aksan sorununun iki belgelenmiş nedeni var.** Kling, Seedance ve Veo'nun desteklediği diller listesinde Türkçe yok; model Türkçeyi "tahmin ederek" konuşuyor. ElevenLabs'te kullanılan Archie, Delia ve Maya ise İngilizce seslerdir; ElevenLabs'in kendi yardım sayfası bu seslerin başka dilde aksanlı çıkabileceğini söylüyor. Higgsfield'ın hazır ses listesinde Türkçe ses görmedim.
4. **Çözüm: sesi video modelinden almak.** Önce Türkçe ses üretilir (anadili Türkçe olan bir sesle), sonra görüntü o sese göre üretilir. Higgsfield'da bunu yapan araçlar var: ses referansı kabul eden Seedance 2.5, Wan 3.0, MiniMax H3 ve doğrudan bu iş için yapılmış **Intone** (1–2 karakter, senin ses kayıtların, 5 plana kadar).
5. **Aynı katalogda 2–5 kat ucuz modeller var.** 10 saniyelik 9:16 klip: Kling 4.0 1080p 37,5 kredi; Wan 3.0 720p ve Kling 4.0 Flash 15 kredi; Seedance 2.0 Mini 10 kredi; Wan 3.0 480p 7,5 kredi.
6. **Gerçekçi hedef bölüm başına 200–300 kredi.** Bu, önce sesin ve başlangıç karelerinin kilitlenmesine ve tekrar üretim sayısının düşmesine bağlı.
7. **Senaryonun kancası yok.** En güçlü cümle ("Koca bir şehir satın aldım") 8. saniyede geliyor, köy 79. saniyede görünüyor, bölüm izleyicinin zaten tahmin ettiği şeyle bitiyor. Instagram'da en büyük kayıp ilk 1,5–3 saniyede yaşanıyor.
8. **Rıza arabada başka biri oluyor.** 52–69. saniyeler arasında yüzü gerçekçi oranlara kayıyor, karikatür burnu ve kaşları kayboluyor. Final karede Rıza Selin'den bir baş uzun; kendi kuralınız "aynı boy" diyor.

---

## 2. B01 incelemesi: neden berbat çıktı

Videoyu saniyede bir kare olacak şekilde çıkardım (`gorseller/kontak_*.jpg`), kesme noktalarını ve ses seviyelerini ölçtüm, konuşmaları yazıya döktüm.

### 2.1 Senaryo

| Sorun | Kanıt | Sonuç |
|---|---|---|
| Kanca yok | İlk 12 saniye: Selin laptopta yazıyor, Rıza ayakta duruyor | İzleyici kaydırır |
| Vaat geç ödeniyor | Köy ilk kez 79. saniyede görünüyor, bölüm 90 saniye | Bölümün asıl konusu son 11 saniyeye sıkışmış |
| Bitiş soru değil cevap | "Bunun neresi şehir?" izleyicinin zaten bildiği şey | Sonraki bölümü bekletecek merak yok |
| Köylüler yok | Naci, Emine, Hüseyin B01'de hiç görünmüyor | Dizinin komedi motoru ilk bölümde çalışmıyor |
| Bahis hissedilmiyor | Paranın miktarı, ev hayali, Selin'in kaybı gösterilmiyor | Selin'in tepkisi hafif kalıyor |
| Yol sahnesi dolgu | 26 saniye araba içi, tek açı | Hikâye ilerlemiyor |

İyi olan: önerme güçlü ve Türk izleyiciye çok uygun (şehirlinin taşraya uyumu). "Ben daha seni seviyor muyum, onu düşünüyorum" ve "Navigasyon bile emin konuştu" iyi replikler; sorun yazıda değil, yerleşimde ve oynanışta.

### 2.2 Çekim ve kurgu

- **Üç kadraj, sıfır yakın plan.** 0–39 sn aynı geniş salon açısı (10–11. saniyede yalnızca kırpılarak yakınlaştırılmış), 43–69 sn aynı ön cam açısı.
- **27. saniyede ışınlanma.** Selin otururken bir sonraki karede ayakta, omzunda daha önce olmayan çanta, elinde anahtar (`gorseller/kesme_noktalari.jpg`). Kalkma hareketi hiç gösterilmemiş.
- **Araba kadrajı kayıyor.** 54–60. saniyelerde Rıza kadrajın dışına taşıyor.
- **Işık sürekliliği belirsiz.** Ev altın saat, yol öğle güneşi, köy gün batımı. Saat geçişi hikâyede söylenmiyor.
- **Final oynanışı senaryoya uymuyor.** Senaryo "Rıza mahcup, yarım gülümser" diyor; karede Rıza yere bakıyor, Selin ona dönük değil.

### 2.3 Ses

Sesi duyamadığım için aşağıdakiler ölçüm ve otomatik yazıya dökme sonucudur.

| Bulgu | Ölçüm | Olması gereken |
|---|---|---|
| Bir replik tamamen yok | "Ev için ayırdığımız kadar" yerine 21,9–25,9 sn arası 4 saniye sessizlik. Bu, sahnenin vurucu cümlesiydi | Her replik var ve anlaşılır |
| Seviye uçurumu | Açılış −16,5 dB, final repliği −33 dB: 16 dB fark | Replikler arası en fazla 3–4 dB |
| Dinamik aralık | 19,6 LU | Telefon için 6–8 LU |
| Tepe seviyesi | −0,2 dBTP | −1 dBTP veya altı |
| Telaffuz | Tanıma motoru şunları duydu: "Koço bir şehir", "Kimim parasıyla", "bir kimden", "dedik aç para", "bir sene hiç adres vermedin" | Senaryoyla birebir |

Telaffuz satırı için not: kullandığım tanıma modeli küçük bir modeldi, hataların bir kısmı ona ait olabilir. Ama eksik replik ve seviye farkı kesin.

### 2.4 Teknik format

720×1280, 24 fps, 2,1 Mbps. Instagram için 1080×1920 standarttır. Altyazı, başlık ve müzik yok ("ham" sürüm olduğu için beklenen bir durum, ama yayın sürümünde zorunlu).

### 2.5 Kredi dökümü (hesaptan çekildi)

| Kalem | Adet | Kredi | Not |
|---|---|---|---|
| Kling 4.0 (20 Kasım) | 11 | 206 | Her biri 18,75 |
| Kling 4.0 (21 Kasım) | 10 | 260 | 10–37,5 arası |
| Sync Lipsync 3 | 6 (1 iade hariç) | 253 | Finalde kullanılmadı |
| Kling 3.0 | 9 | 68 | Deneme |
| GPT Image 2.6 | 8 | 22 | Kareler |
| Eleven v4 | ~23 | 5 | Ses |
| **Toplam** | | **~814** | |

9 planlık bölüm için 21 Kling 4.0 üretimi yapılmış: plan başına 2,3 deneme. Tekrarın nedeni model değil; başlangıç karesi ve ses kilitlenmeden üretime girilmesi.

---

## 3. Karakter incelemesi

### 3.1 Genel değerlendirme

Tasarımlar güçlü: siluetler ayırt edilebilir, renk paleti sıcak, köylüler özellikle iyi (doku, yaş, karakter). Sorun tasarımda değil, **sheet'lerin video modeline verdiği bilgide**.

| # | Sorun | Neden önemli | Öneri |
|---|---|---|---|
| 1 | **İfade sayfası yok.** Her karakter yalnızca hafif gülümseyen nötr yüzle var | "Mimik yok" şikâyetinin başladığı yer. Model karakterin şaşkın, öfkeli ya da mahcup hâlini hiç görmedi | Rıza ve Selin için 6–8 ifadeli sayfa: şaşkın, öfkeli, mahcup, alaycı, panik, kahkaha, üzgün, ağzı açık konuşurken |
| 2 | **Cilt, kaş, saç makro panelleri** | Gözenekli gerçek cilt dokusu modeli gerçekçiliğe çekiyor. Rıza'nın arabada gerçek insana dönmesi bununla tutarlı | Bu panelleri kaldır, yerlerine ifade kafaları koy |
| 3 | **Saf yan profil paneli** | Kendi Şahmeran kuralın bunu yasaklıyor. Ayrıca arkadan görünüm yok; B01'de karakterler kapıdan çıkarken arkadan görünüyor | Önden, 3/4 önden, 3/4 arkadan |
| 4 | **Boy kuralı ile görseller çelişiyor** | Kural "Selin ve Rıza aynı boyda" diyor. Kapak görselinde ve final karede Rıza belirgin uzun | Karar ver ve kilitle. Önerim Rıza'nın yarım baş uzun olması: model zaten buna meyilli, modelin eğilimiyle savaşmak tekrar üretim demek |
| 5 | **Ölçek sayfası yok** | Beş karakterin yan yana durduğu tek bir kare olmadığı için boy ilişkileri her planda yeniden uyduruluyor | Beş karakter tek karede, aynı zeminde, boy çizgili |
| 6 | **Stil düzeyi tutarsız** | Rıza ve Selin karikatür; Naci, Emine, Hüseyin neredeyse gerçekçi yaşlı insan | Köylüleri bir kademe stilize et ya da başrolleri bir kademe gerçekçi yap; tek seviye |
| 7 | **Ses kimliği yok** | Sheet'te ses yok; kullanılan sesler İngilizce hazır sesler | Karakter başına tek Türkçe ses, kimliği ve örnek kaydı dizi dosyasında |
| 8 | **Nesne sayfaları yok** | Kural 4 dosya, çanta, anahtar, araba için ayrı referans istiyor; B01'de çanta ve anahtar birden beliriyor | Dosya, çanta, anahtar, araba için tek sayfa |

### 3.2 Karakter karakter

**Rıza.** En iyi tasarım: uzun burun, kalın kaşlar, dağınık bukleler hemen tanınıyor. Videoda bu özellikler ilk kaybolan şeyler oluyor. Her üretime yüz yakın planı ayrıca bağlanmalı. Kostüm ayrıntıları (cep mendili, püsküllü ayakkabı) tutarlı kalmış.

**Selin.** Tasarım daha genel bir "animasyon filmi kadını"; Rıza kadar ayırt edici değil. Finans kökenini gösteren hiçbir görsel işaret yok. İki önerim var:
- Ayırt edici bir işaret ekle (örneğin başının üstünde gözlük, hiç bırakmadığı telefon ya da not defteri).
- Kıyafeti gözden geçir. Çok kısa fırfırlı etek ve derin yaka, stilize 3D vücut oranlarıyla birlikte cinselleştirilmiş okunuyor. Bu senin kararın, ama hedef marka iş birliğiyse aile ve gıda markaları için risk; ayrıca köyde çamur, keçi, merdiven sahnelerinde hem komediyi hem üretimi zorlaştırır. Şehirli ama rahat bir kıyafet (blazer, midi etek ya da pantolon, topuklu ayakkabı) komediye daha çok malzeme verir: topuklu ayakkabı çamurda başlı başına bir tekrar eden şakadır.

**Naci, Emine, Hüseyin.** Görsel olarak hazırlar. Eksik olan yazı tarafı: her birinin komedideki işlevi tanımlı değil. Öneri: Naci her şeyi bilen ama hiçbir şeyi doğrudan söylemeyen adam; Emine köyün gerçek patronu; Hüseyin her işe "olur" deyip hiçbirini yapmayan adam. Araştırmadaki taşra komedisi çalışması da aynı şeyi söylüyor: izleyici şehirlinin beceriksiz uyumuna güler, köylüye değil. Köylüler akıllı taraf olmalı.

### 3.3 Karakter yazımı

Rıza ve Selin'in birer somut isteği ve kusuru yazılmalı:
- **Rıza:** başarısız olmadığını kanıtlamak istiyor; kusuru, sorunları saklaması.
- **Selin:** parayı geri almak istiyor; gizlice köyü sevmeye başlıyor.

B01'de Selin yalnızca tepki veriyor. Her bölümde bir karar alan o olmalı.

---

## 4. Türkçe ses sorunu ve çözümü

### 4.1 Neden kötü

1. **Video modelleri Türkçe bilmiyor.** Bulunan dil listeleri: Kling 3.0 Çince, İngilizce, Japonca, Korece, İspanyolca; Kling 4.0 buna Portekizce, Almanca, Fransızca, Hintçe/Endonezce ekliyor; Seedance 2.5 on bir dil sayıyor. Hiçbirinde Türkçe yok.
2. **Kullanılan ElevenLabs sesleri İngilizce.** ElevenLabs yardım sayfası hazır seslerin başka dillerde doğru aksana sahip olmayabileceğini söylüyor ve o dilde klonlanmış topluluk seslerine yönlendiriyor.
3. **Ses görüntüden sonra eklendi.** Kling önce kendi sesiyle ve kendi dudak hareketiyle video üretti; sonra üstüne başka ses ve lipsync bindirildi. Vücut dili ve mimik ilk sese göre oynanmış olduğu için ikinci ses ne kadar iyi olursa olsun yabancı durur.

### 4.2 Çözüm: önce ses

Sıra tersine döner: **replik sesi üretilir ve onaylanır → görüntü o sese göre üretilir.**

**Adım 1: Türkçe sesi üretmenin üç yolu**

| Yol | Nasıl | Kalite beklentisi | Tam otomasyona uygun mu |
|---|---|---|---|
| A. İnsan oynar, ses dönüştürülür | Anadili Türkçe biri replikleri telefona oynayarak okur. Ses dönüştürücü (ElevenLabs Voice Changer ya da Higgsfield `voice_change`) tınıyı karakterin sesine çevirir; vurgu, duraklama ve duygu oynayandan gelir | En yüksek. Türkçe prozodi hiçbir modelin Türkçe bilgisine bağlı kalmaz | Hayır: her bölümde biri replikleri okumalı (yaklaşık 10 dakika) |
| B. Türkçe sesle TTS | ElevenLabs v4 ile ses kütüphanesinden İstanbul aksanlı Türkçe ses, duygu etiketleriyle. Alternatifler: Gemini TTS, Fish Audio, Cartesia | İyi olması bekleniyor ama oyunculuk kalitesi teste bağlı | Evet |
| C. Türk bir sesi klonlamak | Rızası olan bir kişinin 1–2 dakikalık kaydından Higgsfield'da özel ses oluşturulur, TTS bu sesle konuşur | B ile benzer, ses dizimize özel olur | Evet |

Araştırmada Türkçe için öne çıkanlar: ElevenLabs v3/v4 (bir karşılaştırmada en düşük Türkçe kelime hata oranı), Gemini TTS (bir Türk ajansının testinde Zephyr, Callirrhoe ve Charon sesleri tam puan almış; tek cümlelik bir test) ve Cartesia Sonic. Bağımsız, kapsamlı bir Türkçe dinleme testi bulunamadı.

**Hangisinin doğal olduğuna yalnızca Türkçe bilen bir kulak karar verebilir.** Bu yüzden ilk iş kör dinleme testi: aynı iki replik 4–5 farklı sesle üretilir, sen hangisinin hangisi olduğunu bilmeden sıralarsın. Maliyeti birkaç kredi.

**Adım 2: Görüntüyü sese göre üretmek**

Higgsfield'da ses dosyasını girdi olarak alan modeller (hesabından doğrulandı):

| Araç | Ne yapar | 10 sn maliyet |
|---|---|---|
| **Intone** | 1–2 karakter, 1–6 ses kaydı, karşılıklı konuşma, 5 plana kadar, 4–30 sn | Ses yüklemeden fiyat alınamadı |
| **Wan 3.0** | Başlangıç karesi ya da 10 görsel + 5 ses referansı | 480p 7,5 · 720p 15 |
| **Seedance 2.5** | 30 görsel + 10 ses referansı | 480p 30 · 720p 70 |
| **MiniMax H3** | 9 görsel + 3 ses referansı | 20 |
| Sync Lipsync 3 | Üretilmiş videoya ses bindirir | B01'de klip başına 43–54 |

Ses referansının dudak hareketini gerçekten o kayda göre sürüp sürmediği konusunda kaynaklar çelişiyor; Pixar tarzı yüzlerde hiç test bulunamadı. Bu da testle çözülecek.

**Sync Lipsync yalnızca yedek olarak kalır:** B01'de en pahalı tek kalem oydu ve iki kez üretim (önce video, sonra lipsync) anlamına geliyor.

### 4.3 Ses için kalite kapısı

Her replik için otomatik kontrol: yazıya dökülen metin senaryoyla birebir mi, süre plana uyuyor mu, seviye hedefte mi. Bunlar benim yapabildiklerim. Yapamadığım: tonun doğal olup olmadığını duymak. Bu yüzden karakter sesleri bir kez senin onayınla kilitlenir ve sonra değişmez.

---

## 5. Model ve maliyet

### 5.1 Higgsfield fiyatları (bugün hesabından, 10 saniyelik 9:16 klip)

| Model | Kredi | Ses referansı | Not |
|---|---|---|---|
| Wan 3.0 480p | 7,5 | Evet | Taslak için |
| Seedance 2.0 Mini 720p | 10 | Evet | En ucuz 720p |
| Veo 3.1 Lite (8 sn) | 12 | Hayır | 8 sn sınırı |
| **Wan 3.0 720p** | **15** | Evet | 30 sn'ye kadar |
| **Kling 4.0 Flash 720p** | **15** | Hayır | 20 sn'ye kadar |
| Kling 3.0 Turbo | 15 | Hayır | |
| Seedance 2.5 Flash 480p | 20 | Evet | |
| MiniMax H3 | 20 | Evet | |
| Gemini Omni Flash 1.2 720p | 22,5 | Hayır | |
| Kling 4.0 720p | 25 | Hayır | B01'in modeli |
| Wan 3.0 1080p | 30 | Evet | |
| Seedance 2.5 480p | 30 | Evet | Şahmeran'ın modeli |
| Kling 4.0 1080p | 37,5 | Hayır | B01'in modeli |
| Seedance 2.5 Flash 720p | 50 | Evet | |
| Seedance 2.5 720p | 70 | Evet | En pahalı |

Görseller: Nano Banana Pro 2 kredi, GPT Image 2.6 2,75 kredi.

### 5.2 Başkaları ne kullanıyor

- Belgelenmiş ortak iş akışı: senaryo → karakter sayfaları (ifade sayfası dâhil) → görsel modelde başlangıç kareleri (en çok Nano Banana Pro) → Seedance ya da Kling ile videoya çevirme → ses ElevenLabs'ten, çoğu zaman modelin kendi sesinin yerine → CapCut ya da Premiere'de kurgu.
- Mikro dizi rehberleri ilk sırada Seedance 2.5'i, alternatif olarak Kling 4.0'ı sayıyor. Karşılaştırmalarda ortak desen: çok karakterli, referans ağırlıklı anlatıda Seedance; kamera ve aksiyon yönetiminde Kling. Kling 4.0'ın istenmeyen sert kesme eklediği bildirilmiş.
- En çok izlenen stilize 3D dizilerin hangi araçları kullandığına dair doğrulanmış bir döküm bulunamadı.
- Bildirilen bölüm maliyetleri: tek kişilik bir Seedance 2.5 dizisinde bölüm başına yaklaşık 19 dolar; 90 saniyelik bölüm için 45–65 dolar; Batılı bağımsız yapımcılarda bitmiş dakika başına 50–150 dolar.
- Higgsfield dışına çıkmak ucuzlatmıyor: Kling ve Seedance'ın kendi API fiyatları aynı model için Higgsfield'daki kredi karşılığının 2–5 katı görünüyor.

### 5.3 Önerilen düzen

| Aşama | Model | Neden |
|---|---|---|
| Başlangıç kareleri | Nano Banana Pro (2 kredi) | Şahmeran'da kanıtlandı; bölüm başına 15–20 kare = 30–40 kredi |
| Taslak (hareket ve zamanlama denemesi) | Wan 3.0 480p | Saniyesi 0,75 kredi |
| Diyalog planları | Intone ya da Wan 3.0 720p + ses referansı | Ses önce, lipsync'e ayrıca para yok |
| Diyalogsuz planlar (yürüme, tepki, mekân) | Kling 4.0 Flash 720p ya da Wan 3.0 720p | Saniyesi 1,5 kredi |
| Bölümde 1–2 "vitrin" planı | Kling 4.0 ya da Seedance 2.5 | Yalnızca gerektiğinde |
| Final | 720p üret, 1080p'ye büyüt | Instagram zaten sıkıştırıyor |

Bu düzen bir önerme; hangi modelin bizim karakterlerde yüzü koruduğu ancak testle belli olur.

### 5.4 Bölüm bütçesi (75 saniyelik bölüm, 10–12 plan)

| Kalem | Kredi |
|---|---|
| Başlangıç kareleri (18 kare, tekrarlar dâhil) | 36 |
| Ses (replikler, tekrarlar dâhil) | 5–10 |
| Video: 75 sn × 1,5 kredi × 1,6 tekrar katsayısı | 180 |
| Vitrin planı ve yedek lipsync payı | 40 |
| **Toplam hedef** | **~260–270** |

B01'e göre yaklaşık üçte bir. Tekrar katsayısı 1,6'nın üstüne çıkarsa bütçe aşılır; katsayıyı düşük tutan şey başlangıç karesi ve ses disiplinidir.

### 5.5 Plan ve aylık maliyet

| Plan | Kredi/ay | Fiyat | 265 kredilik bölümden kaç tane |
|---|---|---|---|
| Plus (şu anki) | 1.000 | 27–49 $ | 3–4 |
| Ultra | 3.000 | 50–79 $ | 11 |
| Ek kredi paketi | 4.000 | ~150 $ (90 gün geçerli) | 15 |

Haftada 3 bölüm (ayda 13) için yaklaşık 3.500 kredi gerekir: Ultra artı küçük bir ek paket. Haftada 5 bölüm için yaklaşık 5.700 kredi.

**Unlimited hakkında:** hesapta şu an etkin Unlimited yok. Yıllık planlardaki Unlimited yalnızca görsel modelleri kapsıyor (Plus'ta Nano Banana Pro hariç). Video Unlimited, plan alımında verilen 7 günlük geçici bir bonus ve yalnızca web arayüzünde çalışıyor; bu oturumdan kullanamam. Plan sayfasındaki indirimli fiyatlar için "22 Kasım'a kadar" notu var; satın alma kararı senin.

**Higgsfield Short Drama Studio:** Higgsfield birkaç gün önce senaryodan oyuncu kadrosuna, sahnelere ve seslendirilmiş bölümlere giden bir araç yayınlamış (`/short-drama`). İncelemedim. Türkçe ses sorununu çözmesi beklenmez (aynı modelleri kullanır), ama test listesine eklenmeye değer.

---

## 6. Instagram'da tutan dizi: araştırma bulguları

### 6.1 Algoritma ve biçim

- Instagram'ın yöneticisi Mosseri'nin saydığı üç ana sinyal: izlenme süresi, beğeni ve **gönderme (arkadaşa yollama)**. Takipçi olmayanlara ulaşmada gönderme daha ağır basıyor.
- En büyük izleyici kaybı ilk 1,5–3 saniyede. Hedef: 3. saniyede izleyicinin en az %60'ı hâlâ izliyor olmalı.
- Tamamlama oranı uzunlukla düşüyor (satıcı verisi): 30–60 sn için %46–49, 60 sn üstü için %36–46. Öneri: **60–75 saniyeyle başla**, izlenme süresi %45–50'nin üstüne çıkarsa uzat.
- Mikro dizilerde bölümden bölüme kayıp sert: 13 dizilik bir ölçümde izlenme 1. bölümden sonra %47 düşmüş. Sonuç: **her bölüm, diziyi hiç görmemiş biri için de çalışmalı.**
- Altyazı zorunlu: kısa videoların yaklaşık %80'i altyazılı.
- Instagram'ın "Reel bağlama" özelliğinin Ekim sonunda kaldırıldığı bildiriliyor; ayrı bir "Dizi" özelliği testte. İkisine de güvenme: sabitlenmiş "Bölüm 1", tutarlı kapak tasarımı ve her bölümde sonraki bölüme işaret eden sabit yorum kullan.

### 6.2 Başarılı ve başarısız örnekler

- **Fruit Love Island** (Mart 2026): 9–10 günde 3 milyondan fazla takipçi, bölüm başına 10–39 milyon izlenme. Günlük yayın, izleyici oylaması, bir sonraki bölümde oylamaya atıf. Sonra hesap kapatıldı: başkasının formatının parodisiydi, AI etiketi yoktu, tek platformdaydı. Yapımcı para kazanmadığını söyledi.
- **Çin'deki AI evcil hayvan mikro dizileri:** 90 saniye ve altı bölümler. Bir yapımcının gelirinin yaklaşık %70'i marka anlaşmalarından (Prada, Peet's Coffee yerleştirmeleri dâhil).
- **Başarısız marka dizisi (Bilt):** karakterler marka bilgisi vermek için var olunca tutmadı. Kural: ürün şakaya hizmet eder, karakter satış elemanı olmaz.
- Sevilen ile "AI çöpü" arasındaki fark: istekleri olan tekrar eden karakterler, yazılmış şakalar, süreklilik, izleyici katılımı, etiketleme. Cezalandırılan: şablon klipler, ödünç alınmış fikir, hafızasız hikâye, etiketsiz AI.
- Türkiye'de doğrulanmış rakamları olan bir AI dizi hesabı bulunamadı; GZT ve NTV formatın Keşfet'te görünür olduğunu yazmış. Yayından önce Instagram'da elle rakip taraması yapılmalı.

### 6.3 Gelir ve kurallar

- Instagram'ın Türkiye'deki doğrudan ödemeleri küçük. Gerçekçi gelir: marka iş birliği, bölüm sponsorluğu, hikâye içi ürün yerleştirme.
- Türkiye'de bildirilen 2026 Reels ücretleri (ajans blogları, geniş aralık): 10–100 bin takipçi için 3.000–20.000 TL; 100 bin–1 milyon için 20.000–250.000 TL. Diziyi takipçiyle değil **bölüm başına ortalama izlenmeyle** fiyatla.
- **AI etiketi:** Meta gerçekçi görüntü ya da gerçekçi ses içeren AI içerik için bildirim istiyor. Stilize animasyon için muafiyet doğrulanamadı; ses gerçekçi olduğundan her bölümü etiketle.
- **Reklam:** Türkiye'de influencer reklam kurallarının Ağustos 2026'da yönetmeliğe girdiği ve açık "Reklam" etiketi beklendiği bildiriliyor. Ceza tutarları kaynaklar arasında çelişiyor; ilk anlaşmadan önce bir avukata doğrulat.
- **Müzik:** işletme hesapları Instagram'ın lisanslı kütüphanesini ticari içerikte kullanamaz. Özgün bir jenerik melodisi yaptır; aynı zamanda marka varlığı olur.
- **Ses klonu:** gerçek bir kişinin sesi yazılı izin olmadan klonlanmaz.

---

## 7. Senaryo sistemi ve B01 için yeniden yazım önerisi

### 7.1 Bölüm şablonu (70–75 saniye)

| Süre | Vuruş |
|---|---|
| 0–2 sn | Soğuk açılış: bölümün en güçlü görüntüsü ya da cümlesi + ekranda 4–6 kelimelik yazı |
| 2–10 sn | Durum ve bu bölümün isteği, yeni izleyicinin anlayacağı tek cümleyle |
| 10–40 sn | Tırmanma: tek bir "oyunun" üç kademesi, 8–12 saniyede bir gülme ya da ters köşe |
| 40–60 sn | Dönüş: plan ters teper ya da yeni bilgi gelir |
| 60–72 sn | Kapanış şakası |
| Son 3 sn | Soru bırakan bitiş, tepki yüzü üstünde |

Kurallar:
- Replik en fazla 12 kelime, 2–3 saniye.
- 2–4 saniyede bir plan değişimi: bölümde 20–30 plan. Bu, Şahmeran'daki "10–12 çekim" kuralından farklı; komedi daha hızlı kesilir. Uzun bir üretim klibi kurguda birkaç plana bölünebilir.
- Bölümde tek ana mekân, en fazla üç konuşan karakter.
- Yalnızca bilgi veren replik olmaz; her replikte tavır olur.
- Her bölüm bir soruyla biter, cevapla değil.

### 7.2 Yazım kalite kapısı

Senaryo üretime girmeden önce şu sorulardan geçer; biri "hayır" ise yeniden yazılır:
1. İlk 2 saniye, sessiz izleyen birini durdurur mu?
2. Diziyi hiç görmemiş biri 10. saniyede durumu anlar mı?
3. En az üç gülme anı var mı ve her biri karakterden mi geliyor?
4. Selin bu bölümde bir karar alıyor mu?
5. Bitiş bir soru mu ve cevabı izleyicinin tahmin edemeyeceği kadar açık mı?
6. Her plan fiziksel olarak üretilebilir mi (Şahmeran 5h soruları)?
7. İzleyicinin bir arkadaşına yollayacağı tek bir an var mı?

### 7.3 B01 için öneri: "Koca Bir Şehir" yeniden

Mevcut bölüm ev → araba → köy sırasıyla ilerliyor ve köye 79. saniyede varıyor. Öneri: **bölüm köyde başlasın ve köyde geçsin.**

| Süre | Ne olur |
|---|---|
| 0–3 | Selin'in yüzü yakın planda, arkadan keçi sesi. "Rıza… bunun neresi şehir?" Ekranda: "Kocam bütün birikimimizle bir ŞEHİR satın aldı." |
| 3–6 | Geniş plan: boş taş sokak, eğri duran paslı tabela "ŞEHİR MERKEZİ". Başlık: SIFIR ŞEHİR |
| 6–18 | Rıza satışçı coşkusuyla: "Evler, depo, değirmen… hepsi bizim!" Selin tapuyu okur: "Nüfus: üç." Rıza: "Üç bin mi?" Selin: "Üç." |
| 18–30 | Selin: "Kimin parasıyla?" Rıza: "Dedemden kalan… biraz da birikim." Selin: "Biraz dediğin?" Rıza: "Ev için ayırdığımız kadar." Sessizlik; Selin'in göz kapağı seğirir |
| 30–45 | Rıza "potansiyeli" gösterirken tabela düşer. Naci elinde çay bardağıyla belirir: "Yeni sahipler siz misiniz? Öncekiler de böyle heyecanlıydı." |
| 45–60 | Selin: "Öncekiler?" Naci: "Üç gün dayandılar." Rıza gülmeye çalışır |
| 60–72 | Naci cebinden kalın bir zarf çıkarır: "Bu arada… köyün elektrik borcu. Artık sizin." Selin zarfı açar, yüzü değişir. Kesme. Ekranda: "Borç ne kadar? Bölüm 2" |

Bunun getirdikleri: kanca ilk 3 saniyede, mevcut iyi replikler korunuyor, tek mekân (üretim ucuz ve tutarlı), üçüncü karakter ilk bölümde, bitiş gerçek bir soru. Ev ve araba sahneleri atılıyor; istersen ev sahnesi 2. bölümde kısa bir geri dönüş olarak kullanılabilir.

### 7.4 Sezon iskeleti (24 bölüm)

- 1: önerme. 2–6: yerleşme ve köylüler, bölüm başına bir tanışma. 7–12: köyü "şehir" yapma planı ve orta nokta sürprizi (köyün gizli bir değeri ya da rakip alıcı). 13–20: tırmanma, evlilik ve şehirdeki iş tehlikede. 21–24: final ve ikinci sezon kancası.
- Üç-dört tekrar eden şaka, her üç bölümde bir büyütülür: telefonun tek noktada çekmesi, Rıza'nın köyde plaza diliyle konuşması, isimli keçi, Selin'in topukluları.
- Her 3–4 bölümde izleyiciye küçük bir karar oylatılır ve sonraki bölüm sonuca atıf yapar.

---

## 8. Sistem: "sıradaki bölümü yap" nasıl çalışacak

### 8.1 Tasarım

Her şey bu depoda durur; her oturum buradan okur ve buraya yazar.

```
CLAUDE.md                     Her oturumda otomatik okunan kurallar
diziler/sifir-sehir/
  dizi-dosyasi.md             Kanon, karakterler, ses kimlikleri, referans görsel kimlikleri
  sezon-plani.md              Bölüm özetleri, tekrar eden şakalar, açık sorular
  bolumler/B02/
    senaryo.md
    plan-kartlari.md
    kayit.md                  Her üretim: model, referanslar, kredi, sonuç, hata nedeni
araclar/                      Kalite kontrol ve kurgu betikleri
kaynaklar/                    Şahmeran dersleri, B01 dosyası
rapor/                        Bu rapor
```

### 8.2 Bölüm hattı

| # | Aşama | Kalite kapısı |
|---|---|---|
| 1 | Sezon planından bölüm özeti → senaryo | 7.2'deki yedi soru |
| 2 | Plan kartları (saniye saniye, bağlanacak sayfalar) | Şahmeran 5h soruları |
| 3 | Replik sesleri (kilitli karakter sesleriyle) | Yazıya dökme senaryoyla birebir, süre, seviye |
| 4 | Başlangıç kareleri | Yüz = sayfa, boy, konum, nesne durumu; önceki planın son karesiyle yan yana |
| 5 | Video: ses + kare ile | Beş büyütme, yazıya dökme, dudak-ses hizası, istenmeyen kesme |
| 6 | Kurgu: birleştirme, altyazı, müzik, ses dengesi, 1080×1920 | Seviye hedefi, altyazı güvenli alanı, süre |
| 7 | Son kontrol ve teslim | Kontak sayfası, kredi dökümü, bilinen kusurların listesi |

Aşama 4 ve 5'te bir plan iki denemede geçmezse üçüncü deneme yerine plan yeniden tasarlanır (açı değişir ya da plan bölünür). Bölüm bütçeyi aşacaksa durur ve sana yazarım.

### 8.3 Tam otomasyonun önündeki engeller

"Sadece bitti, yayınlayabilirsin" noktasına gelmek için aşağıdakilerin çözülmesi gerekiyor. Hepsi çözülebilir, ama bugün çözülmüş değiller.

| Engel | Durum | Çözüm |
|---|---|---|
| Sesi duyamıyorum | Kalıcı | Karakter sesleri bir kez senin onayınla kilitlenir; sonrası ölçümle denetlenir. Ton hatasını yalnızca sen duyarsın |
| Bu ortam Higgsfield'a dosya yükleyemiyor | Ağ ayarı engelliyor (`upload.higgsfield.ai`) | Ortamın izinli adreslerine eklenmeli; senden onay isteyeceğim |
| Kredi | 23 kredi var | Test için ~300, sonra bölüm başına ~265 |
| Kredi harcama izni | Şahmeran kuralı "her harcama önce sorulur" diyor; tam otomasyonla çelişiyor | Bölüm başına bir tavan belirle (örneğin 300 kredi); tavanın altında sormadan ilerlerim |
| Video Unlimited | Yalnızca web arayüzünde | Bu oturumdan kullanılamaz; bilgisayarın bağlanırsa mümkün |
| Instagram'a yükleme | Bağlantı yok | Dosyayı, kapağı, açıklama metnini ve etiketleri hazır veririm; sen yüklersin |
| "Kusursuz" | Söz veremem | İlk 2–3 bölümü birlikte gözden geçirelim; her yakaladığın hata kurala dönüşür. Sonra bilinen kusurları teslimde açıkça yazarım |

### 8.4 Kurulum planı

**Aşama 0 — Kararlar (senden):** aşağıdaki 9. bölüm.

**Aşama 1 — Karşılaştırma testleri (~300 kredi):**
1. *Ses testi:* aynı iki replik, 4–5 Türkçe sesle. Kör dinlersin, sıralarsın. Birkaç kredi.
2. *Model testi:* aynı başlangıç karesi ve aynı ses ile iki karakterli 10 saniyelik bir diyalog planı; Intone, Wan 3.0 720p, Kling 4.0 Flash, Seedance 2.0 Mini, Kling 4.0 ve Seedance 2.5 Flash üzerinde. Yaklaşık 150–200 kredi. Ölçülen: yüz sayfaya benziyor mu, dudak sese oturuyor mu, mimik var mı.
3. *Karakter sayfası testi:* yeni ifade sayfasıyla ve onsuz aynı plan. Yaklaşık 40 kredi.

**Aşama 2 — Karakter paketi:** ifade sayfaları, ölçek sayfası, nesne sayfası, köy mekân plakaları, kilitli sesler. Yaklaşık 60–80 kredi.

**Aşama 3 — B01 yeniden çekim:** yeni senaryo ve yeni hat ile. Hedef 265 kredi. Bu bölüm sistemin gerçek sınavı.

**Aşama 4 — B02–B03:** senin gözden geçirmenle; hatalar kurala dönüşür.

**Aşama 5 — Otonom üretim:** bölüm tavanı içinde, teslimde kusur listesiyle.

Yayına başlamadan önce 8–10 bitmiş bölüm biriktirilmesi öneriliyor; ilk üç bölüm art arda günlerde, sonrası haftada 3–5.

---

## 9. Senden beklenen kararlar

1. **Ses yolu:** tam otomatik TTS (B/C) mi, yoksa her bölümde birinin replikleri okuduğu yol (A) mu? Önerim testte ikisini de denemek; A belirgin iyi çıkarsa bölüm başına 10 dakikalık kayıt karşılığında en doğal sonucu verir.
2. **Test bütçesi:** yaklaşık 300 kredi için onay ve kredi yüklemesi.
3. **Bölüm kredi tavanı:** sormadan harcayabileceğim üst sınır.
4. **B01:** köyde başlayan yeniden yazımı onaylıyor musun?
5. **Selin'in kıyafeti, boy farkı ve stil seviyesi:** 3. bölümdeki öneriler.
6. **Bölüm süresi ve yayın sıklığı:** 60–75 saniye ve haftada 3 önerim.

---

## 10. Kaynaklar

Araştırma kaynaklarının tamamı arama sonuç özetlerinden okundu; sayfalar açılamadı.

**Türkçe ses ve dudak senkronu**
- https://help.elevenlabs.io/hc/en-us/articles/19450861739409-Which-voices-in-the-voice-library-are-native-to-a-specific-language
- https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4
- https://elevenlabs.io/voice-changer
- https://arxiv.org/html/2603.08823v1
- https://reklamuret.com/blog/turkce-yapay-zeka-seslendirme-testi
- https://joinvoicedata.com/benchmarks/ai-voices
- https://kling.ai/release-note/release-notes/Kling_4
- https://the-decoder.com/kling-ai-drops-version-4-0-with-stereo-audio-multilingual-lip-sync-and-a-lighter-flash-variant/
- https://runware.ai/docs/models/bytedance-seedance-2-5/guides/multilingual
- https://sync.so/docs/models/sync-3
- https://seedancetips.com/guides/seedance-lip-sync/

**Modeller ve maliyet**
- https://higgsfield.ai/blog/higgsfield-short-drama-studio
- https://higgsfield.ai/blog/best-ai-tools-micro-dramas-2026
- https://higgsfield.ai/blog/keep-ai-character-consistent
- https://artificialanalysis.ai/video/leaderboard/image-to-video
- https://chatcut.io/blog/seedance-vs-kling
- https://cellcog.ai/blog/seedance-2-5-vs-kling-4-0/
- https://www.alibabacloud.com/blog/wan3-0-at-general-availability-capabilities-benchmarks-pricing-and-the-workflows-it-changes_603505
- https://blog.segmind.com/we-made-a-30-second-micro-drama-in-one-seedance-2-5-generation-full-test-output/
- https://invideo.io/blog/ai-micro-drama-cost/
- https://wavespeed.ai/blog/ai-guides/how-to-make-an-ai-short-drama-with-seedance-2-5-wan-3-0-and-kling-4-0/

**Instagram, dizi biçimi, gelir**
- https://www.listenfirstmedia.com/quick-dip-micro-dramas/
- https://techcrunch.com/2026/06/02/meta-tests-series-for-episodic-reels-on-instagram-and-facebook/
- https://buffer.com/resources/instagram-reels-length/
- https://adage.com/technology/ai/aa-fruit-love-island-marketers-tiktok/
- https://gizmodo.com/whatever-just-happened-with-fruit-love-island-nobody-won-2000739498
- https://english.news.cn/20261110/e6c7c07f28864b98bac027b283c6bacd/c.html
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- https://www.gzt.com/teknoloji/instagrami-yapay-zeka-dizileri-sardi-birini-izleyen-neden-birakamiyor-yeni-bagimliligimiz-hayirli-olsun-4257980
- https://dergipark.org.tr/tr/download/article-file/4739491
- https://karatalent.co/akademi/influencer-fiyatlari-2026/?lang=en
- https://www.cbhukuk.com/influencer-reklam-kurallari/
- https://www.soundstripe.com/blogs/instagram-music-library
