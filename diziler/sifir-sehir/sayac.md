# Üst sayaç (her bölümde kurgunun sol üstünde)

Tasarım: `araclar/sayac_panel.py` (koyu yarı saydam kart, solda hardal şerit, küçük etiket + büyük değer). Kurgu betiğinde `SAYAC` ve `SAYAC_SON`; kancadan sonra (3. sn) gelir, bölüm boyunca aynı yerde sabit durur (1080×1920'de x=40, y=200). Bölümde yeni bir sayı çıkarsa finalde vurgulu üçüncü hücre olarak eklenir.

Kurallar (kullanıcı, 24 Kasım):
- **Nüfus** köydekiler + çift: Naci, Emine, Hüseyin + Selin, Rıza = **5**. Gelen her yeni kişiyle artar.
- **Kasa** çiftin kendi parasıyla başlar: **8.500.000 TL**. Borçla başlamaz. Hedef: parayı katlamak, nüfusu artırmak.
- Elektrik faturası (333.333,33 TL) bir bölümde hesap yapılırken ödenir ve kasadan düşülür; o bölümden sonra kasa 8.166.666,67 TL olur.

| Bölüm | Nüfus | Kasa | Finalde |
|---|---|---|---|
| B04 | 5 | 8.500.000 TL | BAŞVURU 333 |
| B05 | (gelenlerle artar) | (fatura ödenirse 8.166.666,67 TL) | — |
