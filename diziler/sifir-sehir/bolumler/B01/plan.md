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
