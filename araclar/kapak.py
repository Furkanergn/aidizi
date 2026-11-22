#!/usr/bin/env python3
"""Reels kapağı üretir (1080x1920; önemli her şey ortadaki 4:5 alanda kalır).
Kullanım: python3 araclar/kapak.py <kare> <çıktı.jpg> "<SATIR1>" "<SATIR2>" "<BÖLÜM ETİKETİ>" "<alt yazı>" [vurgu rengi #RRGGBB]
Marka sistemi: marka/kapak-sistemi.md"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src, out, l1, l2, bolum, alt = sys.argv[1:7]
VURGU = sys.argv[7] if len(sys.argv) > 7 else "#F2B33D"
KOYU, ACIK = "#141414", "#FFF8EC"
F = "/usr/share/fonts/opentype/inter/"
W, H = 1080, 1920
def font(ad, boy): return ImageFont.truetype(F + ad, boy)
def kutu(metin, f, yazi, zemin, pad=(34, 18), aci=0):
    """Dolu zeminli, hafif eğik yazı kutusu (markanın imza öğesi)."""
    b = f.getbbox(metin); w, h = b[2] - b[0], b[3] - b[1]
    im = Image.new("RGBA", (w + 2 * pad[0], h + 2 * pad[1]), (0, 0, 0, 0))
    d = ImageDraw.Draw(im); d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 10, fill=zemin)
    d.text((pad[0] - b[0], pad[1] - b[1]), metin, font=f, fill=yazi)
    return im.rotate(aci, expand=True, resample=Image.BICUBIC) if aci else im
def golgeli(taban, katman, xy):
    g = Image.new("RGBA", taban.size, (0, 0, 0, 0)); a = katman.split()[3].point(lambda v: int(v * 0.55))
    g.paste((0, 0, 0, 255), (xy[0] + 8, xy[1] + 10), a); g = g.filter(ImageFilter.GaussianBlur(9))
    taban.alpha_composite(g); taban.alpha_composite(katman, xy)

im = Image.open(src).convert("RGB")
s = max(W / im.size[0], H / im.size[1]); im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
x0 = (im.size[0] - W) // 2; y0 = (im.size[1] - H) // 2; im = im.crop((x0, y0, x0 + W, y0 + H)).convert("RGBA")
# alt karartma
gr = Image.new("L", (1, H), 0)
for y in range(H):
    t = max(0, (y - 1000) / (H - 1000)); gr.putpixel((0, y), int(225 * min(1, t * 1.25) ** 1.3))
kar = Image.new("RGBA", (W, H), (20, 20, 20, 255)); kar.putalpha(gr.resize((W, H))); im.alpha_composite(kar)
# bölüm etiketi (sol üst, 4:5 alanın içinde)
golgeli(im, kutu(bolum, font("Inter-Black.otf", 46), KOYU, VURGU, pad=(28, 16)), (70, 330))
# başlık: iki eğik kutu
f1 = font("Inter-Black.otf", 150); k1 = kutu(l1, f1, ACIK, KOYU, pad=(40, 26), aci=3)
f2 = font("Inter-Black.otf", 190); k2 = kutu(l2, f2, KOYU, VURGU, pad=(44, 30), aci=-3)
golgeli(im, k1, (70, 1075))
golgeli(im, k2, (70 + 60, 1075 + k1.size[1] - 40))
# alt yazı
d = ImageDraw.Draw(im); fa = font("Inter-SemiBold.otf", 36)
yy = 1075 + k1.size[1] - 40 + k2.size[1] + 26
d.rectangle((70, yy + 2, 78, yy + 2 + 46 * min(2, len(alt) // 48 + 1)), fill=VURGU)
kel = alt.split(); sat = [""]
for k in kel:
    if d.textlength((sat[-1] + " " + k).strip(), font=fa) > 900: sat.append(k)
    else: sat[-1] = (sat[-1] + " " + k).strip()
for i, sx in enumerate(sat[:2]): d.text((100, yy + i * 46), sx, font=fa, fill=ACIK)
im.convert("RGB").save(out, quality=94)
print(out, "| alt sınır:", yy + 46 * len(sat[:2]) + 6, "(4:5 güvenli alan 285–1635)", "| alt yazı satırı:", len(sat))
