# B01 üretim paketi — plan tablosu

Bu dosya `araclar/b01_paket.py` tarafından üretilir; elle düzenleme, betiği düzenle.

## 1. Kareler (görsel üretimi, 9:16)

Her karenin kendi klasörü var: `kareler/SBxx/`. İçinde o kare için eklenecek referanslar (numaralı) ve `SBxx_prompt.txt` bulunur: klasördeki bütün görselleri ekle, promptu yapıştır. Referansların tamamı ayrıca `referanslar/` klasöründe durur. Üretilen kareyi sohbete yükle; onaylanmadan videosu üretilmez.

| Kare | Ne | Eklenecek referanslar | Hangi klipte |
|---|---|---|---|
| SB01 | Selin yakın plan | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; V10_plaka_ters_aci.jpg | P01, P07 |
| SB02 | Köy girişi geniş, tabela ve keçi | V8_plaka_koy_girisi.jpg; V6_tabela.jpg; V7_keci.jpg | P02 |
| SB03 | Selin + Rıza ikili, Rıza gururlu | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; Boy_sayfasi.jpg; V10_plaka_ters_aci.jpg; Nesne_kapali_dosya.jpg | P03 |
| SB04 | Keçi tabelayı yiyor, yakın plan | V7_keci.jpg; V6_tabela.jpg; V8_plaka_koy_girisi.jpg | P04 |
| SB05 | Selin tapuyu okuyor, Rıza omzundan bakıyor | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; Boy_sayfasi.jpg; V10_plaka_ters_aci.jpg; Nesne_kapali_dosya.jpg | P05 |
| SB06 | Selin + Rıza ikili, Selin Rıza'ya dönük | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; Boy_sayfasi.jpg; V10_plaka_ters_aci.jpg; Nesne_kapali_dosya.jpg; SB03_onayli.jpg | P06a |
| SB08 | Rıza tek, satışa hazırlanıyor | Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; V10_plaka_ters_aci.jpg | P08 |
| SB09 | Köy girişi geniş, tabela yerde | V8_plaka_koy_girisi.jpg; V6_tabela.jpg; V7_keci.jpg; SB02_onayli.jpg | P09 |
| SB10 | Naci taburede, orta plan | Naci_sayfasi.jpg; Naci_ifade_sayfasi.jpg; V9_plaka_naci_duvari.jpg; Nesne_cay_bardagi.jpg; Nesne_zarf.jpg | P10, P13 |
| SB11 | Selin + Rıza ikili, Naci'ye bakıyorlar | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; Boy_sayfasi.jpg; V10_plaka_ters_aci.jpg; Nesne_kapali_dosya.jpg; SB03_onayli.jpg | P11 |
| SB12 | Naci yakın plan | Naci_sayfasi.jpg; Naci_ifade_sayfasi.jpg; V9_plaka_naci_duvari.jpg; Nesne_cay_bardagi.jpg; SB10_onayli.jpg | P12 |
| SB14 | Selin + Rıza ikili, Rıza kâğıdı okuyor | Selin_sayfasi.jpg; Selin_ifade_sayfasi.jpg; Riza_sayfasi.jpg; Riza_ifade_sayfasi.jpg; Boy_sayfasi.jpg; V10_plaka_ters_aci.jpg; Nesne_kapali_dosya.jpg; Nesne_zarf.jpg; SB03_onayli.jpg | P14 |

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
