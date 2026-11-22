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
