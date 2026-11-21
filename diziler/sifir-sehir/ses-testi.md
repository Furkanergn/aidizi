# Sıfır Şehir — ses seçimi ve kilitleme

**Durum (21 Kasım 2026):** ElevenLabs MCP bağlı. Tur 1 (Rıza, Selin) üretildi, kullanıcının dinlemesi bekleniyor.

## Bağlantı
- Kullanıcının ElevenLabs üyeliği var ve MCP ile bağlanmak istiyor.
- ElevenLabs'in barındırdığı MCP adresi: `https://api.elevenlabs.io/v1/mcp` (ElevenLabs hesabıyla giriş, API anahtarı gerekmez).
- Bulut oturumunda bu, claude.ai bağlayıcısı olarak eklenir; bağlayıcılar oturum başında okunur, yani ekledikten sonra yeni oturum gerekir.
- Ortamda `api.elevenlabs.io` için kayıtlı bir API anahtarı var ama **geçersiz** (anahtarın kendisi yerine kimliği girilmiş; ElevenLabs `api_key_id_used_as_api_key` döndürüyor). MCP çalışıyorsa bu kayda gerek yok.

## Yöntem
1. Ses kütüphanesinde **anadili Türkçe** sesleri ara (dil: Türkçe; başroller için İstanbul aksanı). İngilizce hazır sesler (Archie, Delia, Maya) aday olamaz.
2. Karakter başına 3–4 aday seç. Yaş, tını ve enerji karakter tarifine uymalı.
3. Her adayla aşağıdaki aynı replikleri, aynı modelle ve aynı ayarlarla üret. Önce en güncel model (v4; yoksa v3), duygu etiketleriyle.
4. Dosyaları kör adlandır (`riza_A.mp3`, `riza_B.mp3` …); hangi harfin hangi ses olduğu `ses-testi-anahtar.md` dosyasında durur, kullanıcıya dinlemeden önce gösterilmez.
5. Otomatik kontrol: yazıya dökme senaryoyla birebir mi, süre, seviye. Bu, sesin doğal olduğunu göstermez; yalnızca telaffuzun anlaşılır olduğunu gösterir.
6. Kullanıcı dinler ve sıralar. Kazanan sesle ikinci tur: aynı repliğin 2–3 farklı okuma yönlendirmesi (hız, vurgu, duygu etiketi).
7. Kazanan ses kimliği, model ve ayarlar `dizi-dosyasi.md` ile `CLAUDE.md` içine "kilitli" olarak yazılır. Sonra değişmez.

Claude sesi duyamaz: hangi sesin doğal olduğuna yalnızca kullanıcı karar verir.

## Karakter tarifleri ve test replikleri

Her karakter için üç replik: biri düz, biri duygulu, biri komedi zamanlaması isteyen.

### Rıza — 30'ların ortası, satış yöneticisi. Sıcak, hızlı, çabuk heyecanlanır; sıkışınca cümlenin sonu alçalır.
1. (coşkulu) "Aşkım, yarın istifanı ver. Koca bir şehir satın aldım!"
2. (kaçamak, alçalarak) "Dedemden kalanla… biraz da birikimden."
3. (satışçı coşkusu, zorlama) "Evler, depo, değirmen… hepsi bizim! Bak şu potansiyele!"

### Selin — 30'ların başı, finans kökenli. Sakin, net; ince alayı kısa durakla kurar.
1. (kuru, sakin) "Kimin parasıyla?"
2. (alaycı, duraklı) "Ben daha seni seviyor muyum… onu düşünüyorum."
3. (şaşkın, kısık) "Rıza… bunun neresi şehir?"

### Naci — 60'ların sonu, eski sulama görevlisi. Ağır, acelesiz; her şeyi bilir, hiçbirini doğrudan söylemez.
1. (sakin, hafif keyifli) "Yeni sahipler siz misiniz? Öncekiler de böyle heyecanlıydı."
2. (düz) "Üç gün dayandılar."
3. (önemsizmiş gibi) "Bu arada… köyün elektrik borcu. Artık sizin."

### Emine — 60'lar, köyün gerçek patronu. Tok, kararlı, şefkatli ama lafını esirgemez.
1. (misafirperver) "Hoş geldiniz kızım. Aç mısınız?"
2. (kesin) "O iş öyle olmaz. Ben sana göstereyim."
3. (iğneleyici) "Şehirde böyle mi yapıyorlar bunu?"

### Hüseyin — 60'lar, her işe "olur" deyip hiçbirini yapmayan adam. Yumuşak, rahat, güler yüzlü.
1. (rahat) "Olur olur, hallederiz."
2. (erteleyerek) "Yarın bakarız ona. Yarın olmazsa öbür gün."
3. (şaşırmış, saf) "Bunu siz mi aldınız? Parayla mı?"

### Navigasyon — nötr kadın sesi, sabit hız.
1. "Hedefinize ulaştınız."
2. "Rota bulunamadı. Lütfen geri dönün."

## Sonuç
- Kilitli sesler: —

## Tur 1 — Rıza ve Selin (21 Kasım 2026)

Model: `eleven_v4`, duygu etiketleriyle, ses başına iki okuma. Dosyalar: `ses-testi/tur1/`. ElevenLabs akışı: `DNnwpfAyWm9YWpSEHxzA`. Harcama: yaklaşık 2.700 ElevenLabs kredisi.

Otomatik kontrol (küçük tanıma modeli): sekiz sesin hepsinde replikler neredeyse birebir tanındı; B01'deki "Koço", "kimim" türü hatalar yok. Bu, sesin doğal olduğunu göstermez.

| Dosya | Ses | ElevenLabs ses kimliği | Seviye (LUFS) |
|---|---|---|---|
| riza_HappyMan | Happy Man | 01p4omegjS2n3rSDCM5u | −22,7 |
| riza_Hasan | Hasan – Energetic, Expressive, Playful | TA7RCSTD5b2z14h1TDTX | −20,2 |
| riza_Mert | Mert - Natural Conversations | 0BX3wAZlkPgb0coEupyY | −24,0 |
| riza_Orcun | Orcun Togan | c9eIhSvMHBxtYhLX4oBt | −19,3 |
| selin_Ahu | Ahu | xyqF3vGMQlPk3e7yA4DI | −27,2 |
| selin_ElifOzder | Elif Özder | i50A6Mcx7A7vVwCVZVeZ | −19,6 |
| selin_ElifWarm | Elif - Warm, Natural, Friendly | 4XsbOSxQHw4NUVaEeo2o | −24,7 |
| selin_Nazli | Nazlı | o9DOmAyPjfFu8AfoFAnM | −24,2 |

Kullanıcı kararı: bekleniyor.

Köylüler için aday notları (tur 2): Seyfullah Kartal `mF7tIc9VLrznhGooGjaT`, Ozan Karaca `5nr6ATQepuidiLb6OT3B`, Ergun Kalbak `0DihkedLJYKoWg7H1u4d`, Arif Yaşaroğlu (dublaj sanatçısı) `oafr6pIDZj0XlLA4eHub`, Nihat (Karadeniz aksanı) `MuOq11XzQTthwLhmGZ2V`, Veyzel (Anadolu aksanı) `qiYSibuYxMVcoiWBNsky`. Yaşlı kadın sesi henüz bulunmadı.

### Tur 1 sonucu
Kullanıcı: "Hiçbiri istediğim gibi değil; izlediğim dizilerdeki sesler belli ki AI ama tiplemeye daha iyi oturuyor." Çıkarım (Claude): kütüphane sesleri seslendirme sanatçısı/reklam sesi; karakter sesi değil. Kütüphaneden hazır ses seçme yolu bırakıldı.

## Tur 2 — tasarlanmış karakter sesleri (21 Kasım 2026)

ElevenLabs Voice Design (`eleven_ttv_v3`): karakter tarifinden sıfırdan ses. Dosyalar: `ses-testi/tur2-tasarim/`. Önizlemeler kaydedilmedi; kullanıcı seçerse `creative_save_designed_voice` ile kaydedilir.

| Dosya | Önizleme kimliği |
|---|---|
| riza_tasarim_A | k8uRysD61JbSiFiTp2qw |
| riza_tasarim_B | U86eCrHJie8wzpRW15ft |
| riza_tasarim_C | TeyXH5FVc2LNqAi7Xoat |
| selin_tasarim_A | 6iNriVq8zvqfxi9XjNh7 |
| selin_tasarim_B | Q9jmdx5aZiqV7Zv2uuQR |
| selin_tasarim_C | EGYWeGTuBhkFLgXp9gw1 |

Kullanıcı kararı: bekleniyor.

## Açık hipotez: video modelinin kendi sesi
Kullanıcının beğendiği dizilerde ses büyük olasılıkla video modelinin (Veo 3.x, Seedance 2.x) görüntüyle birlikte ürettiği ses: model karakterin görünüşüne uyan bir ses uyduruyor, bu yüzden tiplemeye oturuyor. Türkçe rehberler Veo ve Seedance ile Türkçe diyalog üretildiğini anlatıyor (İngilizce prompt + tırnak içinde Türkçe replik). B01'de yalnızca Kling 4.0'ın sesi denendi. Test edilmedi: Veo 3.1 Lite, Seedance 2.0/2.5, Wan 3.0, Gemini Omni Flash ile aynı karakter karesi ve aynı Türkçe replik. Higgsfield kredisi gerekir (hesapta ~23).

## Tur 3 — video modelinin kendi Türkçe sesi (21 Kasım 2026)

Aynı başlangıç karesi (B01 son karesi, Selin + Rıza; Higgsfield medya kimliği `1bf11d77-6006-4021-9ece-a4f40a3c434c`), aynı prompt, 8 sn, 9:16. Replikler: Selin "Rıza… bunun neresi şehir?" / Rıza "Koca bir şehir, aşkım… sadece biraz küçük."

| Model | Kredi | Tanıma motorunun duyduğu | Seviye | İş kimliği |
|---|---|---|---|---|
| Veo 3.1 Lite (720p) | 12 | "Rıza, bunun neresi şehir? / Koca bir şehir aşkım, sadece biraz küçük." (birebir) | −18,1 LUFS | cde12be8-0b5e-4286-920e-011d8cfbb5a6 |
| Wan 3.0 (480p) | 6 | "Rıza, bunun neresi şehir? / Koca bir şehir aşkım, sadece biraz küçük." (birebir) | −8,5 LUFS (çok yüksek) | 2f149104-82db-4629-bbd8-52530db72493 |
| Seedance 2.0 Mini (480p) | 4 | "Riza, bunu neresi şir? / Koku bir şir aşkım. Sadece biraz kükük." (bozuk) | −21,2 LUFS | ced8cb4d-61a2-4cc0-924b-01dadc0bea91 |

Görsel: üçünde de karakterler korunmuş, tek plan, kesme yok. Veo'da Rıza elleriyle oynuyor ve Selin tepki veriyor; Wan'da Rıza ellerini açıyor; Seedance'ta hareket az.

Kullanılan prompt kalıbı (Türkçe için):
- Prompt İngilizce; replikler tırnak içinde Türkçe ve Türkçe harflerle.
- "Both characters are native Turkish speakers from Istanbul. They speak ONLY Turkish… No English."
- Her replik için zaman aralığı, konuşan, duygu ve "says in Turkish".
- Telaffuz notu: `"Rıza" contains the Turkish dotless ı. Say it "RUH-zah", never "Riza"`; zor kelimeler için okunuş.
- "Only the speaking character's mouth moves. No music, no subtitles."

Tek deneme yapıldı; tutarlılık (aynı promptla tekrar) ve klipler arası ses sabitliği test edilmedi. Kullanıcının dinlemesi bekleniyor.
