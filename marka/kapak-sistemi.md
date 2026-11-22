# Sayfa görsel sistemi — kapaklar ve ekran yazıları

**Durum:** v1 taslak, kullanıcı onayı bekleniyor · 22 Kasım 2026

Amaç: sayfada farklı diziler ve konseptler olacak. Izgaraya bakan biri (1) bunların hepsinin aynı sayfaya ait olduğunu, (2) hangi kapağın hangi diziye ait olduğunu bir bakışta anlamalı.

## Sabit olanlar (bütün dizilerde aynı)
- **İmza öğesi: eğik kutu.** Başlık iki dolu kutudan oluşur: üstte koyu zeminli açık renk yazı (+3°), altta vurgu rengi zeminli koyu yazı (−3°), biraz sağa kaymış ve üsttekine binmiş. Aynı dil video içinde de kullanılır: açılış kancası ve kapanış çağrısı.
- **Yazı tipi:** Inter. Başlık ve etiket Black, açıklama ve altyazı SemiBold.
- **Nötr renkler:** koyu `#141414`, açık `#FFF8EC`.
- **Yerleşim (1080×1920):** bölüm etiketi sol üstte (x 70, y 330); başlık sol altta (y ≈ 1075'ten başlar); altında tek satır açıklama ve solunda ince vurgu çizgisi. Önemli her şey ortadaki 4:5 alanda (y 285–1635) kalır; ızgarada kırpılmaz.
- **Görsel:** dizinin kendi bir karesi, tam ekran; yüzler üst-orta bölgede, başlık yüzleri kapatmaz. Altta hafif koyu geçiş.
- **Altyazı (video):** sade; Inter SemiBold 40 px, beyaz, ince koyu kenar, ekranın alt üçte birinde. Kutusuz, renksiz, animasyonsuz.
- **Kapanış (video):** son kare donar; "DEVAMI İÇİN" (koyu kutu) + "TAKİP ET" (vurgu kutusu). "Bölüm N'de" gibi ifade kullanılmaz.

## Diziye göre değişenler
- **Vurgu rengi:** her dizinin tek bir vurgu rengi vardır; kutu, etiket ve çizgi bu renkle boyanır. Izgarada dizileri ayıran şey budur.
- **Başlık metni** ve **karenin dünyası** (ışık, mekân).

| Dizi / konsept | Vurgu rengi | Not |
|---|---|---|
| Sıfır Şehir | Hardal `#F2B33D` | Köyün altın ışığıyla uyumlu |
| (sonraki dizi) | belirlenecek | Hardaldan uzak bir renk: örn. turkuaz `#2EC4B6`, mercan `#FF5A4F`, mor `#7B5CFF`, çimen `#7BC950` |

## Üretim
```
python3 araclar/kapak.py <kare> <çıktı.jpg> "SATIR1" "SATIR2" "BÖLÜM N" "Tek satır açıklama" [#vurgu]
```
Örnek: `diziler/sifir-sehir/bolumler/B01/cikti/B01_kapak.jpg` (tam kapak) ve `B01_kapak_izgara_4x5.jpg` (ızgarada görünecek kırpım).

## Açık konular
- Sayfanın adı ve logosu yok; kapakta logo için yer ayrılmadı. Logo gelirse sağ üste (4:5 alanın içine) konur.
- Diziler çoğalınca etikete dizi kısaltması eklenebilir.
