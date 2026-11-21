# AI Dizi Üretimi — çalışma kuralları

Bu depo, Instagram için AI ile üretilen dikey kısa dizilerin (ilk dizi: **Sıfır Şehir**) tek doğruluk kaynağıdır. Kullanıcıyla Türkçe konuş; önce sonuç, kısa, düz link.

## Önce bunları oku
- `rapor/RAPOR_Sifir_Sehir_ve_Uretim_Sistemi.md` — B01 teşhisi, karakter incelemesi, ses/model/maliyet araştırması, sistem tasarımı.
- `kaynaklar/SAHMERAN_OGRENILENLER_ve_SKILLER.md` — hatalardan çıkmış üretim kuralları (5a–5j, plan kartı, QC). Bu kurallar burada da geçerlidir.
- `kaynaklar/Sifir_Sehir_B01_Senaryo_Kurallar_Karakterler.pdf` — ilk B01 senaryosu, yapım kuralları, karakter sayfaları.

## Durum (21 Kasım 2026)
Sistem **henüz kurulmadı**. Rapor teslim edildi; raporun 9. bölümündeki kararlar kullanıcıdan bekleniyor. Karşılaştırma testleri (ses, model, karakter sayfası) yapılmadı. Aşağıdaki "kilitli" kararlar testlerden sonra buraya yazılacak; yazılana kadar varsayım yapma, sor.

- Kilitli video modeli: —
- Kilitli karakter sesleri: —
- Bölüm kredi tavanı: —

## Değişmez ilkeler
1. **Önce ses, sonra görüntü.** Türkçe replik sesi üretilip doğrulanmadan video üretilmez. Kling/Seedance/Veo'nun kendi Türkçe sesi kullanılmaz (Türkçe desteklemiyorlar). İngilizce hazır sesler (Archie, Delia, Maya vb.) Türkçe replikte kullanılmaz.
2. **Kare kusursuz olmadan video yok.** Her plan onaylı başlangıç karesinden üretilir; görünen her karakterin sayfası bağlanır.
3. **Telefonda yüz okunmalı.** Diyalog planları yakın ya da orta plan; aynı geniş açıda 6 saniyeden uzun kalınmaz.
4. **Her bölüm ilk 2 saniyede kancayla açılır, soruyla biter.** Senaryo, rapordaki 7.2 kalite kapısından geçmeden üretime girmez.
5. **Kredi:** harcamadan önce `estimate_*_cost` ile fiyat al. Kullanıcı bir bölüm tavanı vermediyse her harcama önce sorulur. Her üretim `bolumler/Bxx/kayit.md` dosyasına model, referanslar, kredi ve sonuçla yazılır.
6. **Bir plan iki denemede geçmezse** üçüncü kez aynı şeyi üretme; planı yeniden tasarla.
7. **Kontrol edilmemiş çıktı gösterilmez.** QC: kontak sayfası, ilk/orta/son kare, yüz = sayfa büyütmesi, komşu planla yan yana, konuşmanın yazıya dökümü, ses seviyeleri.
8. **Sesi duyamazsın.** Ölçüm ve yazıya dökme "iyi ses" demek değildir; teslimde bunu açıkça yaz.
9. Kullanıcı bir hata yakalarsa: kural olarak buraya ya da dizi dosyasına yazılır.

## Ortam notları
- Bu bulut ortamından `upload.higgsfield.ai` ve `huggingface.co` adreslerine erişim engelli (21 Kasım). Yerel dosyayı Higgsfield'a yüklemek için ortamın izinli adreslerine eklenmesi gerekir.
- Konuşma tanıma: `sherpa-onnx` + GitHub'daki `sherpa-onnx-whisper-small` modeli bu ortamda çalışıyor (HuggingFace gerekmez). Higgsfield sandbox'ında `faster-whisper` hazır.
- Higgsfield Unlimited yalnızca web arayüzünde çalışır; MCP üzerinden üretim kredi harcar.
