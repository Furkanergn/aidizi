#!/usr/bin/env python3
"""Karşılaşma kapağı (1080x1920): iki yüz, çapraz bölme, ortada VS rozeti, altta büyük başlık.
Kullanım: python3 araclar/kapak_vs.py <üst kare> "x0,y0,x1,y1" <alt kare> "x0,y0,x1,y1" <çıktı> "<ÜST AD>" "<ALT AD>" "<BAŞLIK>" "<BÖLÜM>"
Kırpma kutuları kaynak karenin pikselleriyle verilir. Marka: marka/kapak-sistemi.md"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ust, ub, alt, ab, out, ad1, ad2, baslik, bolum = sys.argv[1:10]
KOYU, ACIK, VURGU = "#141414", "#FFF8EC", "#F2B33D"
F = "/usr/share/fonts/opentype/inter/"; W, H = 1080, 1920
YL, YR = 1050, 870          # bölme çizgisinin sol ve sağ ucu
def font(ad, boy): return ImageFont.truetype(F + ad, boy)
def kutu(metin, f, yazi, zemin, pad=(34, 18), aci=0):
    b = f.getbbox(metin); w, h = b[2] - b[0], b[3] - b[1]
    im = Image.new("RGBA", (w + 2 * pad[0], h + 2 * pad[1]), (0, 0, 0, 0))
    d = ImageDraw.Draw(im); d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 12, fill=zemin)
    d.text((pad[0] - b[0], pad[1] - b[1]), metin, font=f, fill=yazi)
    return im.rotate(aci, expand=True, resample=Image.BICUBIC) if aci else im
def golgeli(taban, katman, xy, g=0.6):
    s = Image.new("RGBA", taban.size, (0, 0, 0, 0)); a = katman.split()[3].point(lambda v: int(v * g))
    s.paste((0, 0, 0, 255), (xy[0] + 10, xy[1] + 14), a); taban.alpha_composite(s.filter(ImageFilter.GaussianBlur(11))); taban.alpha_composite(katman, xy)
def parca(yol, kutu_, en, boy):
    x0, y0, x1, y1 = map(int, kutu_.split(",")); im = Image.open(yol).convert("RGB").crop((x0, y0, x1, y1))
    s = max(en / im.size[0], boy / im.size[1]); im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
    xx = (im.size[0] - en) // 2; yy = (im.size[1] - boy) // 2
    return im.crop((xx, yy, xx + en, yy + boy)).convert("RGBA")
im = Image.new("RGBA", (W, H), KOYU)
u = parca(ust, ub, W, YL); m = Image.new("L", (W, YL), 0); ImageDraw.Draw(m).polygon([(0, 0), (W, 0), (W, YR), (0, YL)], fill=255); im.paste(u, (0, 0), m)
a = parca(alt, ab, W, H - YR); m = Image.new("L", (W, H - YR), 0); ImageDraw.Draw(m).polygon([(0, YL - YR), (W, 0), (W, H - YR), (0, H - YR)], fill=255); im.paste(a, (0, YR), m)
# alt karartma (başlık için) ve üstte hafif karartma
gr = Image.new("L", (1, H), 0)
for y in range(H): gr.putpixel((0, y), int(210 * (max(0, (y - 1280) / 640) ** 1.1) + 70 * max(0, 1 - y / 420)))
k = Image.new("RGBA", (W, H), (20, 20, 20, 255)); k.putalpha(gr.resize((W, H))); im.alpha_composite(k)
# bölme şeridi
kat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(kat)
d.polygon([(0, YL - 16), (W, YR - 16), (W, YR + 16), (0, YL + 16)], fill=VURGU); golgeli(im, kat, (0, 0), 0.45)
# VS rozeti
r = 118; roz = Image.new("RGBA", (2 * r + 8, 2 * r + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(roz)
d.ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=KOYU, outline=VURGU, width=12)
f = font("Inter-Black.otf", 104); b = f.getbbox("VS"); d.text((r + 4 - (b[2] + b[0]) / 2, r + 4 - (b[3] + b[1]) / 2), "VS", font=f, fill=VURGU)
golgeli(im, roz.rotate(-8, resample=Image.BICUBIC), (W // 2 - r - 4, (YL + YR) // 2 - r - 4))
# ad etiketleri
golgeli(im, kutu(ad1, font("Inter-Black.otf", 76), ACIK, KOYU, pad=(32, 20), aci=3), (W - 64 - 330, YR - 250))
golgeli(im, kutu(ad2, font("Inter-Black.otf", 76), KOYU, ACIK, pad=(32, 20), aci=-3), (64, YL + 60))
# başlık ve bölüm
boy = 170
while font("Inter-Black.otf", boy).getbbox(baslik)[2] + 88 > 960: boy -= 6
k2 = kutu(baslik, font("Inter-Black.otf", boy), KOYU, VURGU, pad=(44, 30), aci=-3)
golgeli(im, k2, ((W - k2.size[0]) // 2, 1610 - k2.size[1]))
e = kutu("SIFIR ŞEHİR  ·  " + bolum, font("Inter-Black.otf", 44), KOYU, ACIK, pad=(24, 13))
golgeli(im, e, (64, 300))
im.convert("RGB").save(out, quality=94); print(out)
