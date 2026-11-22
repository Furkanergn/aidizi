# B01 üretim kaydı

## Kareler (21 Kasım 2026) — kullanıcı üretti, Claude kontak sayfasından inceledi

| Kare | Sonuç | Not |
|---|---|---|
| SB01 | **Kullanılmıyor** | İki ayrı kare (yüz yakın planı; belden yukarı üç çeyrek) Flow'da telif filtresine takıldı; üç cümlelik isimsiz, repliksiz test promptuyla bile. Aynı oturumda ikili plan (P03) geçti. Sonuç: Selin'in tek başına olduğu kare kabul edilmiyor. P01 artık SB03'ten, P07 P06b'nin son karesinden başlıyor |
| SB02 | Onaylı | Tabela yazısı doğru; keçinin burnu tabelanın köşesinde |
| SB03 | Onaylı | Selin solda dosyayı iki koluyla sarmış, Rıza sağda; Rıza yaklaşık bir baş uzun (boy sayfasındaki yarım baştan fazla ama diğer ikili karelerle tutarlı) |
| SB04 | Onaylı (2. üretim) | İlk üretim 3:4 çıktı. İkincisi 9:16 (941×1671); yazı doğru, keçi tabelanın sağ kenarını ısırıyor |
| SB05 | Onaylı | Açık dosya iki elde, kamera yalnızca dış yüzü görüyor |
| SB06 | Onaylı | |
| SB08 | Onaylı | |
| SB09 | Onaylı | Tabela yerde, yazı doğru, toz ve çukur var |
| SB10 | Onaylı | Bardak sağ elde, sol el dizde, zarf rafta |
| SB11 | Onaylı | İkisi de kadrajın soluna bakıyor (Naci'nin bakışının tersi) |
| SB12 | Onaylı | |
| SB14 | Onaylı | Zarf SB10'dakinden büyük ve koyu; aralarında başka planlar olduğu için kabul edildi |

Onaylı kareler: `kareler/onayli/`. Kullanıcının özgün PNG'leri kendi klasörlerinde duruyor.

## Klipler
Henüz üretilmedi. Her klibin karesi ve promptu `klipler/Pxx/` içinde. Gelen klipler `klipler/gelen/Pxx.mp4`.

## Klipler — Flow, Veo 3.1 Lite, 1080×1920 çıktı

| Klip | Deneme | Sonuç | Konuşma (tanıma motoru) | Seviye | Not |
|---|---|---|---|---|---|
| P01 | SB01 ile 5+ deneme reddedildi (telif filtresi); SB03 ile 1 | Onaylı | "Rıza bunun neresi şehir?" (birebir) | −21,4 LUFS | Kamera sabit, dosya yerinde, Rıza gülümsüyor. Son yarım saniyede Selin'in yüzü biraz yumuşuyor |
| P02 | 1 | Onaylı | — (replik yok) | −35,3 LUFS | Tabela yazısı değişmiyor, keçi yerinde çiğniyor, yapraklar uçuşuyor |
| P03 | 1 | Onaylı, dinleme kontrolü kullanıcıda | "Şehir merkezi burası aşkım. Bak tabelası bile var." (birebir) / Selin'in repliği "Tabelayı keçi yiyoruz" olarak tanındı (senaryo: "Tabelayı keçi yiyor, Rıza.") | −19,6 LUFS | Selin 4–5,5 sn arasında Rıza'ya dönüp konuşuyor; Rıza'nın gülüşü sonda yerinde kalıyor. Son kelimenin ("Rıza") anlaşılırlığını kullanıcı dinleyecek |
| P05 | 1 | Onaylı | "12 ev, bir depo, bir değirmen, nüfus 3. 3 bin mi? 3." (birebir) | −20,9 LUFS | Açık dosya iki elde sabit, yazı görünmüyor; Rıza sonda süngüsü düşmüş. 3. saniyede Selin okurken kısa bir an gülümsüyor |
| P06a | 1 | Onaylı | "Kimin parasıyla? / Dedemden kalan / biraz da birikim." (birebir) | −23,6 LUFS | Dosya sabit, Selin bakışını ayırmıyor. Son karede Rıza Selin'e mahcup yarım gülüşle bakıyor (promptta "yere bakıyor" yazıyordu); P06b promptu bu kareye göre güncellendi |
| P04 | 1 | Onaylı | — (replik yok) | −25,8 LUFS | Keçi tabelanın kenarını çiğniyor, yazı değişmiyor |
| P06b | 1 | Onaylı | "Biraz dediğin? / Ev için ayırdığımız kadar." (birebir) | −23,9 LUFS | İki replik arasında ~2 sn sessizlik; Rıza'nın gülüşü sönüyor, gözleri yere iniyor. Son kare P07'nin başlangıcı |
| P08 | 1 | Onaylı, dinleme kontrolü kullanıcıda | "Ama potansiyelere bak, şuraya kafe, şuraya ortak çalışma alanı..." (senaryo: "potansiyele") | −19,7 LUFS | Rıza tek başına kare telif filtresinden geçti. 4. saniyeden sonra kolu havada duruyor, gözleri sağa kayıyor. Kadraj dışı metal gürültüsünün olup olmadığı ölçümden anlaşılmıyor; yoksa kurguda eklenecek. Önce sağ eliyle de işaret ediyor (promptta yalnız sol kol yazıyordu) |
| P09 | 1 | Onaylı | — (replik yok) | −27,3 LUFS | Tabela yerde, yazı doğru, toz dağılıyor, keçi bir adım atıyor |
| P07 | 1 | Onaylı | — (replik yok) | −48,2 LUFS | Zincirin üçüncü halkası (P06a → P06b → P07). Selin profilden göründüğü için göz seğirmesi tek gözle yavaş bir göz kırpma olarak okunuyor (1,8. sn). Keçi melemesi yok; neredeyse tam sessiz. Selin'in saçı önceki kliplere göre biraz daha açık renkte |
| P11 | 1 | Onaylı | "Öncekiler mi?" (birebir) | −22,3 LUFS | İkisi de sola bakıyor; Rıza'nın gülüşü geriliyor |
| P12 | 1 | Onaylı | "3 gün dayandılar." (birebir) | −17,1 LUFS | Naci yüz yakın planı telif filtresinden geçti. Bardak yerinde |
| P13 | 3 (ilk ikisi Flow'da hata verdi) | Onaylı | "Bu arada, köyün elektrik borcu. / Artık sizin." (birebir) | −20,1 LUFS | Sol eliyle zarfı raftan alıp uzatıyor, bardak sağ elde kalıyor, oturuyor. En riskli sayılan hareket sorunsuz |
| P14 | 1 | Onaylı | "Rıza. / Kaç?" (birebir) | −26,7 LUFS | Rıza'nın gülüşü siliniyor, kâğıdın yalnız arkası görünüyor; Selin hafif gülümseyerek onu izliyor |

Kalan: P10 (Naci'nin ilk planı).

Seviye notu: klipler −17 ile −27 LUFS arasında; kurguda replikler eşitlenecek.
| P10 | 1 | Onaylı | "Yeni sahipler siz misiniz? / Öncekiler de böyle heyecanlıydı." (birebir) | −20,0 LUFS | Bardak sağ elde, 2,5–3 sn arasında bir yudum, sol el dizde, zarf rafta dokunulmadan duruyor |

## Ham birleştirme (22 Kasım 2026)
`bash araclar/b01_ham_birlestir.sh` → `cikti/B01_ham_birlesik.mp4` (depoya eklenmez). 15 klip senaryo sırasıyla, işlemsiz; zincirlenen P06b ve P07'nin ilk karesi atıldı. Süre 77,1 sn, 1080×1920, 24 fps. Ses: −20,9 LUFS, tepe −0,5 dBTP, dinamik aralık 11,8 LU (kurguda eşitlenecek).
Kontak sayfasında görülen: P07'de (yaklaşık 0:37–0:41) Selin'in saçı komşu planlara göre belirgin açık renkte.

## Kurgu v1 (22 Kasım 2026)
`python3 araclar/b01_kurgu.py` → `cikti/B01_kurgu_v1.mp4` (depoya eklenmez), altyazı dosyası `cikti/B01.ass`.

- Süre 66,9 sn (ham 77,1 sn): kliplerin başındaki ve sonundaki boşluklar kırpıldı; bütün geçişler düz kesme.
- Yazılar: açılış kancası (0–3 sn, üstte), başlık "SIFIR ŞEHİR / BÖLÜM 1" (P02 üstünde), Türkçe altyazı (Inter SemiBold 40 px, alt üçte birde), bitiş "Borç ne kadar? / BÖLÜM 2'DE" (son kare 1,8 sn dondurulup karartıldı).
- Ses: her diyalog klibi yaklaşık −18 LUFS'a çekildi; replik aralıkları dışında klibin kendi sesi ~−26 dB kısıldı (konuşma kapısı); P08'deki kadraj dışı metal gürültüsü korundu (kaynakta 5,1. sn'de var); bölüm boyunca kesintisiz yapay ortam yatağı (~−45 dB). Sonuç: −15,1 LUFS, tepe −1,3 dBTP, dinamik aralık 10,9 LU.
- Kullanıcı geri bildirimi (ham sürüm): "sahne geçişlerinde arka plan sesleri geçişi hissettiriyor" → konuşma kapısı ve sürekli yatak bunun için eklendi. Claude sonucu dinleyemedi.
- Bilinenler: ortam yatağı yapay (süzülmüş gürültü), gerçek köy ortamı değil; müzik yok; P07'de keçi melemesi yok; P06b'de iki replik arasında ~2 sn sessizlik (tek plan, kesilemiyor).

## Kurgu v2 ve kapak (22 Kasım 2026)
Kullanıcı geri bildirimi (v1): açılış yazısı daha karakteristik ve gösterişli olsun (altyazı sade kalsın); sonda "Borç ne kadar? Bölüm 2'de" olmasın, son kare donsun ve takip çağrısı gelsin; sayfa için marka renkleri ve tarzı olan bir kapak sistemi, kapakta dizinin bir ânı.
- Açılış kancası: iki eğik kutu ("KOCAM BÜTÜN BİRİKİMİMİZLE" koyu, "BİR ŞEHİR SATIN ALDI" hardal), sırayla büyüyerek açılıyor.
- Kapanış: son kare 2,8 sn donuyor; "DEVAMI İÇİN" + "TAKİP ET" aynı kutu diliyle.
- Altyazı değişmedi. Süre 67,9 sn; −15,2 LUFS.
- Kapak: `cikti/B01_kapak.jpg` (SB03 karesi üstüne), sistem `marka/kapak-sistemi.md`, betik `araclar/kapak.py`.

## Kurgu v2 ve kapak (22 Kasım 2026)
Kullanıcı geri bildirimi (v1): açılış yazısı daha karakteristik ve gösterişli olsun (altyazı sade kalsın); sonda "Borç ne kadar? Bölüm 2'de" olmasın, son kare donsun ve takip çağrısı gelsin; sayfa için marka renkleri ve tarzı olan bir kapak sistemi, kapakta dizinin bir ânı.
- Açılış kancası: iki eğik kutu ("KOCAM BÜTÜN BİRİKİMİMİZLE" koyu, "BİR ŞEHİR SATIN ALDI" hardal), sırayla büyüyerek açılıyor.
- Kapanış: son kare 2,8 sn donuyor; "DEVAMI İÇİN" + "TAKİP ET" aynı kutu diliyle.
- Altyazı değişmedi. Süre 67,9 sn; −15,2 LUFS, tepe −1,3 dBTP.
- Kapak: `cikti/B01_kapak.jpg` (SB03 karesi üstüne), `cikti/B01_kapak_izgara_4x5.jpg`; sistem `marka/kapak-sistemi.md`; betik `araclar/kapak.py`.
