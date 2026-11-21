# AI Dizi Üretimi — çalışma kuralları

Bu depo, Instagram için AI ile üretilen dikey kısa dizilerin (ilk dizi: **Sıfır Şehir**) tek doğruluk kaynağıdır. Kullanıcıyla Türkçe konuş; önce sonuç, kısa, düz link.

## Önce bunları oku
- `rapor/RAPOR_Sifir_Sehir_ve_Uretim_Sistemi.md` — B01 teşhisi, karakter incelemesi, ses/model/maliyet araştırması, sistem tasarımı.
- `kaynaklar/SAHMERAN_OGRENILENLER_ve_SKILLER.md` — hatalardan çıkmış üretim kuralları (5a–5j, plan kartı, QC). Bu kurallar burada da geçerlidir.
- `kaynaklar/Sifir_Sehir_B01_Senaryo_Kurallar_Karakterler.pdf` — ilk B01 senaryosu, yapım kuralları, karakter sayfaları.

## Durum (21 Kasım 2026, akşam)
Sistem **henüz kurulmadı**. Ses yolu testlerle belirlendi; ayrıntı `diziler/sifir-sehir/ses-testi.md` içinde.

- **Ses kararı:** ses ayrı seslendirme aracından değil, video modelinin kendi sesinden gelecek. ElevenLabs kütüphane sesleri ve tasarlanmış sesler kullanıcıya uymadı ("tiplemeye oturmuyor").
- **Model:** Veo 3.1 Lite ve Wan 3.0 Türkçe replikleri doğru söyledi; kullanıcı Veo'yu daha kaliteli buldu. Seedance (2.0 Mini, kullanıcının deneyimine göre 2.5 de) Türkçeyi bozuyor; Kling 4.0'ın sesi B01'de beğenilmedi.
- **Nereden üretilecek (kullanıcı kararı):** Veo klipleri Google Flow'da, kullanıcının Google AI Pro üyeliğiyle (klip başına 10 kredi, doğrulandı; ses Higgsfield'daki Veo ile neredeyse aynı). **İş bölümü:** Claude her bölüm için paketi hazırlar (senaryo, plan listesi, her plan için başlangıç karesi ya da kare promptu, video promptu, ayarlar); kullanıcı Flow'da üretir ve mp4'leri sohbete yükler; Claude kontrol eder (yazıya dökme, kareler) ve kurguyu yapar.
- **Ses sabitliği (tur 4):** kullanıcı üç klibi Flow'da üretti ve "ses ile ilgili sıkıntı yok" dedi. Klipler sohbete yüklenmedi; Claude ölçüm yapmadı, karar kullanıcının kulağına dayanıyor. Her promptta sabit "Voices" bölümü kullanılır (`ses-testi/tur4-ses-sabitligi/`).
- **Yeni sorun:** sahnelerde fizik hataları (Selin el hareketi yaparken tapu dosyası gövdesinde havada asılı kaldı). Kural 10 eklendi.
- Higgsfield'da ~1 kredi kaldı. ElevenLabs MCP bağlı.

- Kilitli video modeli: Veo 3.1 Lite, Google Flow üzerinden
- Kilitli karakter sesleri: Veo'nun kendi sesi + her promptta sabit ses tarifi (Rıza: sıcak, parlak, hafif genizden tenor, hızlı; Selin: sakin, sıcak, hafif boğuk alçak ses, kuru mizah)
- Bölüm kredi tavanı: —

## Değişmez ilkeler
1. **Türkçe replik prompt kalıbıyla yazılır ve her klipte doğrulanır.** Prompt İngilizce; replikler tırnak içinde Türkçe harflerle; "native Turkish speakers from Istanbul, speak ONLY Turkish"; her replik için zaman aralığı, konuşan ve duygu; zor kelimeler ve "Rıza" için okunuş notu. Kalıp `diziler/sifir-sehir/ses-testi/tur3_prompt.txt` içinde. Her klibin konuşması yazıya dökülüp senaryoyla karşılaştırılır. İngilizce hazır sesler (Archie, Delia, Maya vb.) Türkçe replikte kullanılmaz.
2. **Kare kusursuz olmadan video yok.** Her plan onaylı başlangıç karesinden üretilir; görünen her karakterin sayfası bağlanır.
3. **Telefonda yüz okunmalı.** Diyalog planları yakın ya da orta plan; aynı geniş açıda 6 saniyeden uzun kalınmaz.
4. **Her bölüm ilk 2 saniyede kancayla açılır, soruyla biter.** Senaryo, rapordaki 7.2 kalite kapısından geçmeden üretime girmez.
5. **Kredi:** harcamadan önce `estimate_*_cost` ile fiyat al. Kullanıcı bir bölüm tavanı vermediyse her harcama önce sorulur. Her üretim `bolumler/Bxx/kayit.md` dosyasına model, referanslar, kredi ve sonuçla yazılır.
6. **Bir plan iki denemede geçmezse** üçüncü kez aynı şeyi üretme; planı yeniden tasarla.
7. **Kontrol edilmemiş çıktı gösterilmez.** QC: kontak sayfası, ilk/orta/son kare, yüz = sayfa büyütmesi, komşu planla yan yana, konuşmanın yazıya dökümü, ses seviyeleri.
8. **Sesi duyamazsın.** Ölçüm ve yazıya dökme "iyi ses" demek değildir; teslimde bunu açıkça yaz.
9. Kullanıcı bir hata yakalarsa: kural olarak buraya ya da dizi dosyasına yazılır.
10. **Eller ve nesneler her promptta yazılır.** Karakter elinde bir şey tutuyorsa: hangi el/kol tutuyor, plan boyunca orada kalıyor mu, serbest el hangisi ve yalnızca onunla mı jest yapıyor. Yazılmazsa model konuşurken iki eliyle jest yaptırır ve nesne havada kalır (tur 4, Selin'in tapu dosyası). Önce tasarımla çöz: diyalog planında nesne gerekmiyorsa önceki planda bırakılır (çantaya, kaputa, masaya) ya da plan göğüs üstü çerçevelenir. Nesnenin referans görseli bu hatayı çözmez; o yalnızca nesnenin görünüşünü sabitler.

## Ortam notları
- Ortamın izinli adresleri: `upload.higgsfield.ai`, `elevenlabsusercontent.com`. Higgsfield sonuç dosyaları (`*.cloudfront.net`) ve `huggingface.co` buradan indirilemez; klip incelemesi Higgsfield sandbox'ında (`sandbox_exec`) yapılır.
- Konuşma tanıma: `sherpa-onnx` + GitHub'daki `sherpa-onnx-whisper-small` modeli bu ortamda çalışıyor (HuggingFace gerekmez). Higgsfield sandbox'ında `faster-whisper` hazır.
- Higgsfield Unlimited yalnızca web arayüzünde çalışır; MCP üzerinden üretim kredi harcar.
