# Sıfır Şehir — ses seçimi ve kilitleme

**Durum (21 Kasım 2026):** başlamadı. ElevenLabs bağlantısı bekleniyor (aşağıda).

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
