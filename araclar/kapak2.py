#!/usr/bin/env python3
"""Reels kapağı, sürüm 2 (dikkat çekici düzen): büyük başlık yüzü ve olayı kapatmayacak yere (alt ya da üst) konur, isteğe bağlı halka + etiket olayı işaretler.
Kullanım: python3 araclar/kapak2.py <kare> <çıktı.jpg> "<ÜST SATIR>" "<BÜYÜK SATIR>" "<BÖLÜM>" [yakınlaştırma=1.0] [kayma_x=0] [kayma_y=0] [halka=x,y,rx,ry,ETİKET ya da -] [alt|ust]
Önemli her şey ortadaki 4:5 alanda (y 285–1635) kalır. Marka sistemi: marka/kapak-sistemi.md"""
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src, out, l1, l2, bolum = sys.argv[1:6]
zoom = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
kx = int(sys.argv[7]) if len(sys.argv) > 7 else 0; ky = int(sys.argv[8]) if len(sys.argv) > 8 else 0
halka = sys.argv[9] if len(sys.argv) > 9 and sys.argv[9] != "-" else None
YER = sys.argv[10] if len(sys.argv) > 10 else "alt"   # başlık altta (yüz üstteyse) ya da üstte
KOYU, ACIK, VURGU = "#141414", "#FFF8EC", "#F2B33D"
F = "/usr/share/fonts/opentype/inter/"; W, H = 1080, 1920
def font(ad, boy): return ImageFont.truetype(F + ad, boy)
def kutu(metin, f, yazi, zemin, pad=(34, 18), aci=0):
    b = f.getbbox(metin); w, h = b[2] - b[0], b[3] - b[1]
    im = Image.new("RGBA", (w + 2 * pad[0], h + 2 * pad[1]), (0, 0, 0, 0))
    d = ImageDraw.Draw(im); d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 12, fill=zemin)
    d.text((pad[0] - b[0], pad[1] - b[1]), metin, font=f, fill=yazi)
    return im.rotate(aci, expand=True, resample=Image.BICUBIC) if aci else im
def golgeli(taban, katman, xy):
    g = Image.new("RGBA", taban.size, (0, 0, 0, 0)); a = katman.split()[3].point(lambda v: int(v * 0.6))
    g.paste((0, 0, 0, 255), (xy[0] + 10, xy[1] + 14), a); taban.alpha_composite(g.filter(ImageFilter.GaussianBlur(11))); taban.alpha_composite(katman, xy)
def sigdir(metin, ad, boy, en, pad):
    while True:
        f = font(ad, boy); b = f.getbbox(metin)
        if b[2] - b[0] + 2 * pad <= en or boy < 60: return f
        boy -= 6
im = Image.open(src).convert("RGB")
s = max(W / im.size[0], H / im.size[1]) * zoom; im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
x0 = min(max((im.size[0] - W) // 2 + kx, 0), im.size[0] - W); y0 = min(max((im.size[1] - H) // 2 + ky, 0), im.size[1] - H)
im = im.crop((x0, y0, x0 + W, y0 + H)).convert("RGBA")
# üstte ve altta hafif karartma (yazı okunsun, olay açık kalsın)
gr = Image.new("L", (1, H), 0)
for y in range(H):
    ust = (max(0, 1 - y / 760) ** 1.4) * (1 if YER == "ust" else 0.45); alt = (max(0, (y - 1100) / 820) ** 1.2) * (1 if YER == "alt" else 0.5)
    gr.putpixel((0, y), int(215 * min(1, ust + alt)))
k = Image.new("RGBA", (W, H), (20, 20, 20, 255)); k.putalpha(gr.resize((W, H))); im.alpha_composite(k)
# halka + etiket
if halka:
    hx, hy, rx, ry, et = halka.split(","); hx, hy, rx, ry = int(hx), int(hy), int(rx), int(ry)
    kat = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(kat)
    if rx > 0:   # rx=0 verilirse halka çizilmez, yalnızca etiket konur
        for i in range(3): d.ellipse((hx - rx - i * 3, hy - ry - i * 2, hx + rx + i * 3, hy + ry + i * 2), outline=VURGU, width=9)
        golgeli(im, kat, (0, 0))
    e = kutu(et, font("Inter-Black.otf", 54), KOYU, VURGU, pad=(24, 14), aci=-5)
    golgeli(im, e, (min(max(hx + rx - 40, 60), W - 60 - e.size[0]), hy - ry - e.size[1] + 6))
f1 = sigdir(l1, "Inter-Black.otf", 120, 880, 40); k1 = kutu(l1, f1, ACIK, KOYU, pad=(40, 26), aci=3)
f2 = sigdir(l2, "Inter-Black.otf", 190, 940, 44); k2 = kutu(l2, f2, KOYU, VURGU, pad=(44, 30), aci=-3)
a1 = kutu("SIFIR ŞEHİR", font("Inter-Black.otf", 46), KOYU, ACIK, pad=(24, 13), aci=0)
a2 = kutu(bolum, font("Inter-Black.otf", 54), KOYU, VURGU, pad=(28, 16), aci=-2)
yb = 318 if YER == "ust" else 1600 - (k1.size[1] - 36 + k2.size[1])   # başlık bloğunun üst kenarı
ye = 1480 if YER == "ust" else 318                                     # dizi adı + bölüm etiketi
golgeli(im, k1, (64, yb)); golgeli(im, k2, (64 + 40, yb + k1.size[1] - 36))
if YER == "alt":   # bölüm etiketi sol üstte (B01-B02 kapaklarındaki yer); dizi adı başlığın hemen üstünde, sola yaslı
    golgeli(im, a2, (44, 322)); golgeli(im, a1, (64, yb - a1.size[1] + 14))
else:
    golgeli(im, a1, (64, ye)); golgeli(im, a2, (64 + a1.size[0] - 10, ye + 12))
im.convert("RGB").save(out, quality=94); print(out)
