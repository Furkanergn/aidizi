# Tur 4 — kullanıcının Flow'da ürettiği klip 1 ve klip 3'ün incelemesi

Kontak sayfaları: `k1_sheet.jpg`, `k3_sheet.jpg`; büyütmeler: `zoom.jpg`.

Konuşma (tanıma motoru): klip 1 birebir; klip 3'te "potansiyele" yerine "potansiyeli", gerisi birebir. Seviye −17,9 ve −19,0 LUFS.

| Klip | An | Hata | Neden |
|---|---|---|---|
| 1 | 2,5–8 sn | Selin iki kolunu indiriyor, dosya gövdesinde asılı kalıyor | Promptta kollar ve dosya yazılmadı |
| 1 | 6,5–8 sn | Selin kameraya dönüyor | "Kameraya bakmaz" yazılmadı; replikten sonra 3 sn boş kaldı |
| 1 | 7–8 sn | Rıza'nın yüzü değişiyor (daha genç, farklı) | Tam boy geniş plan, yüz küçük; boş sürede model doğaçlama yapıyor |
| 3 | 0 sn | Rıza ilk karede birden bağırır gibi | Başlangıç karesi üzgün, prompt coşkulu başlıyor; geçiş yazılmadı |
| 3 | 4–8 sn | Dosya göğüsten kalçaya iniyor ve cüzdan boyutuna küçülüyor | Kollar ve dosya yazılmadı |
| 3 | 5–7 sn | Selin repliği Rıza'ya değil kameraya söylüyor | Bakış hedefi yeterince kesin değildi |
| 3 | 5–7 sn | Selin'in üstü kısalıyor, karnı görünüyor | Kostüm sabiti yazılmadı |
| 3 | 7–8 sn | İkisi yürüyüp gidiyor, kamera kayıyor | Replikler 6. saniyede bitti; son 2 sn için eylem ve bitiş karesi yazılmadı |

Ortak kök nedenler: (1) 8 sn'lik klipte replikler 5–6 sn sürüyor, kalan süreyi model kendi doldurdu; (2) eller, nesneler, bakış ve bitiş karesi yazılmadı; (3) kareler B01'den alınmıştı, bu planlar için tasarlanmamıştı (tam boy, elde nesne).

Düzeltilmiş promptlar: `klip1_prompt_v2.txt`, `klip3_prompt_v2.txt` (6 sn).
