#!/usr/bin/env python3
"""Bölüm duyurusu hikâyesi (1080x1920). Yardımcı işlevleri araclar/hikaye.py'den alır.
Kullanım: python3 araclar/hikaye_bolum.py <arka plan karesi> <çıktı.jpg> <bölüm no> "<alt satır>" [başlangıç_y]"""
import sys
src = open("araclar/hikaye.py", encoding="utf-8").read().split("# ---- 1)")[0]
exec(src)
kare, cikti, no, alt = sys.argv[1:5]; y0 = int(sys.argv[5]) if len(sys.argv) > 5 else 930
im = doldur(kare); karart(im, y0 - 30)
ortala(im, kutu("SIFIR ŞEHİR", font("Inter-Black.otf", 64), ACIK, KOYU, pad=(30, 18), aci=2), y0, -150)
ortala(im, kutu(f"BÖLÜM {no}", font("Inter-Black.otf", 150), ACIK, KOYU, pad=(42, 28), aci=3), y0 + 90, -40)
ortala(im, kutu("YAYINDA!", font("Inter-Black.otf", 176), KOYU, HARDAL, pad=(46, 32), aci=-3), y0 + 308, 40)
d = ImageDraw.Draw(im); f = font("Inter-SemiBold.otf", 44)
d.text(((W - d.textlength(alt, font=f)) // 2, y0 + 575), alt, font=f, fill=ACIK)
im.convert("RGB").save(cikti, quality=93); print(cikti)
