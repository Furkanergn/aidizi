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
- **B01:** senaryo v2.1 (`bolumler/B01/senaryo.md`); promptları `araclar/b01_paket.py` üretir (yeniden çalıştırmak `kareler/SBxx/` içindeki prompt ve numaralı referansları günceller, kullanıcının dosyalarına dokunmaz; `klipler/Pxx/` promptları ayrıca kopyalanmalı). Varlıkların hepsi `varliklar/onayli/` içinde (V1–V10, nesneler). **Kareler:** 11 kare kullanımda ve onaylı (`bolumler/B01/kareler/onayli/`); SB01 Flow filtresine takıldığı için kullanılmıyor (P01 SB03'ten, P07 P06b'nin son karesinden başlar). Kayıt: `bolumler/B01/kayit.md`. **Klipler:** her klibin başlangıç karesi ve promptu `bolumler/B01/klipler/Pxx/` içinde; kullanıcı Flow'da üretip `klipler/gelen/Pxx.mp4` olarak gönderecek ya da sohbete yükleyecek. P06b, P06a'nın; P07, P06b'nin son karesini bekliyor. **Sıradaki:** gelen klipleri kontrol et (yazıya dökme, kontak sayfası, kurallar 10–13), P06b karesini çıkar, sonra kurgu.
- **Girdi kuralı:** karakter sayfaları ve plakalar **storyboard karesi** üretimine bağlanır; Veo'ya (Flow, kareden videoya) yalnızca onaylı kare + prompt verilir. Flow'da Lite ile kareye ek referans bağlanıp bağlanamadığı doğrulanmadı.
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
11. **Klibin her saniyesi yazılır; boş süre bırakılmaz.** Replikler bittikten sonra kalan süreyi model kendi doldurur (yürüyüp gitme, kamera kayması, kameraya bakma, yüz değişimi; tur 4). Replikler 5 sn sürüyorsa klip 6 sn seçilir (Veo Lite: 4/6/8 sn) ve son saniye için sessiz bir eylem yazılır.
12. **Her video promptunda sabit bölümler:** kamera kilidi ("no pan, no zoom, no cut"); eller ve nesneler; bakış ("look only at each other, nobody looks at the camera"); bitiş karesi ("both stand exactly where they started, nobody walks"); kostüm ve yüz sabiti; ses tarifi; telaffuz notu. Örnek: `diziler/sifir-sehir/ses-testi/tur4-ses-sabitligi/klip1_prompt_v2.txt`.
13. **Başlangıç karesi planın ilk anındaki duyguyu ve duruşu gösterir.** Karede üzgün duran karakter ilk saniyede coşkulu konuşturulmaz; ya kare o duyguyla üretilir ya da promptun ilk saniyesi geçişe ayrılır.
14. **Selin tek başına kadrajda olan başlangıç karesi kullanılmaz.** Flow'da Veo, Selin'in tek olduğu iki farklı kareyi (yüz yakın planı; belden yukarı üç çeyrek) telif filtresiyle reddetti ("üçüncü taraf içerik sağlayıcıların menfaatleri"), isimsiz ve repliksiz üç cümlelik promptla bile; Selin + Rıza ikili planı geçti. Selin'in planları ikili kurulur. Rıza'nın ve Naci'nin tek planları henüz denenmedi. Filtre hatasında aynı istek bir kez daha denenir; iki kez takılırsa plan yeniden tasarlanır. Promptlarda film adıyla çakışan kelimeler (frozen vb.) kullanılmaz.

## Ortam notları
- Ortamın izinli adresleri: `upload.higgsfield.ai`, `elevenlabsusercontent.com`. Higgsfield sonuç dosyaları (`*.cloudfront.net`) ve `huggingface.co` buradan indirilemez; klip incelemesi Higgsfield sandbox'ında (`sandbox_exec`) yapılır.
- Konuşma tanıma: `sherpa-onnx` + GitHub'daki `sherpa-onnx-whisper-small` modeli bu ortamda çalışıyor (HuggingFace gerekmez). Higgsfield sandbox'ında `faster-whisper` hazır.
- Higgsfield Unlimited yalnızca web arayüzünde çalışır; MCP üzerinden üretim kredi harcar.
