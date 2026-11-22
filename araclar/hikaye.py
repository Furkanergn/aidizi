#!/usr/bin/env python3
"""Instagram hikâye görselleri (1080x1920). Güvenli alan: üstte 250, altta 340 piksel boş bırakılır.
Kullanım: python3 araclar/hikaye.py   (B01 duyurusu ve genel tanıtım hikâyesini üretir)
Marka sistemi: marka/kapak-sistemi.md"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
KOYU, ACIK, HARDAL = "#141414", "#FFF8EC", "#F2B33D"
F = "/usr/share/fonts/opentype/inter/"; W, H = 1080, 1920
B = "diziler/sifir-sehir/bolumler/B01"; O = f"{B}/cikti"
def font(ad, boy): return ImageFont.truetype(F + ad, boy)
def kutu(metin, f, yazi, zemin, pad=(34, 18), aci=0):
    b = f.getbbox(metin); w, h = b[2] - b[0], b[3] - b[1]
    im = Image.new("RGBA", (w + 2 * pad[0], h + 2 * pad[1]), (0, 0, 0, 0))
    d = ImageDraw.Draw(im); d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), 10, fill=zemin)
    d.text((pad[0] - b[0], pad[1] - b[1]), metin, font=f, fill=yazi)
    return im.rotate(aci, expand=True, resample=Image.BICUBIC) if aci else im
def koy(taban, katman, xy, golge=True):
    if golge:
        g = Image.new("RGBA", taban.size, (0, 0, 0, 0)); a = katman.split()[3].point(lambda v: int(v * 0.5))
        g.paste((0, 0, 0, 255), (xy[0] + 8, xy[1] + 12), a); taban.alpha_composite(g.filter(ImageFilter.GaussianBlur(10)))
    taban.alpha_composite(katman, xy)
def ortala(taban, katman, y, kay=0): koy(taban, katman, ((W - katman.size[0]) // 2 + kay, y))
def doldur(yol):
    im = Image.open(yol).convert("RGB"); s = max(W / im.size[0], H / im.size[1])
    im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
    x0 = (im.size[0] - W) // 2; y0 = (im.size[1] - H) // 2
    return im.crop((x0, y0, x0 + W, y0 + H)).convert("RGBA")
def karart(im, bas, guc=235):
    gr = Image.new("L", (1, H), 0)
    for y in range(H): gr.putpixel((0, y), int(guc * min(1, max(0, (y - bas) / 420)) ** 1.2))
    k = Image.new("RGBA", (W, H), (20, 20, 20, 255)); k.putalpha(gr.resize((W, H))); im.alpha_composite(k)
def kart(yol, gen, aci):
    im = Image.open(yol).convert("RGB"); yuk = int(gen * 1.25)
    s = max(gen / im.size[0], yuk / im.size[1]); im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
    x0 = (im.size[0] - gen) // 2; y0 = int((im.size[1] - yuk) * 0.22); im = im.crop((x0, y0, x0 + gen, y0 + yuk))
    c = Image.new("RGBA", (gen + 28, yuk + 28), ACIK); c.paste(im, (14, 14))
    return c.rotate(aci, expand=True, resample=Image.BICUBIC)

# ---- 1) B01 yayında ----
im = doldur(f"{B}/kareler/onayli/SB04.jpg"); karart(im, 900)
ortala(im, kutu("SIFIR ŞEHİR", font("Inter-Black.otf", 64), ACIK, KOYU, pad=(30, 18), aci=2), 930, -150)
ortala(im, kutu("BÖLÜM 1", font("Inter-Black.otf", 150), ACIK, KOYU, pad=(42, 28), aci=3), 1020, -40)
ortala(im, kutu("YAYINDA!", font("Inter-Black.otf", 176), KOYU, HARDAL, pad=(46, 32), aci=-3), 1238, 40)
d = ImageDraw.Draw(im); f = font("Inter-SemiBold.otf", 44); t = "Kocam bir şehir satın aldı. Nüfusu: üç."
d.text(((W - d.textlength(t, font=f)) // 2, 1505), t, font=f, fill=ACIK)
im.convert("RGB").save(f"{O}/hikaye_B01_yayinda.jpg", quality=93)

# ---- 2) genel tanıtım ----
im = Image.new("RGBA", (W, H), KOYU)
koy(im, kart(f"{B}/kareler/onayli/SB10.jpg", 400, 5), (560, 250))
koy(im, kart(f"{B}/kareler/onayli/SB03.jpg", 440, -5), (90, 280))
koy(im, kart(f"{B}/kareler/onayli/SB04.jpg", 300, 3), (400, 610))
ortala(im, kutu("YAPAY ZEKÂYLA", font("Inter-Black.otf", 96), KOYU, ACIK, pad=(40, 26), aci=3), 1000, -50)
ortala(im, kutu("DİZİLER", font("Inter-Black.otf", 190), KOYU, HARDAL, pad=(48, 32), aci=-3), 1168, 40)
d = ImageDraw.Draw(im); f = font("Inter-SemiBold.otf", 42)
t = "Yeni bölümler, yeni hikâyeler yolda."
d.text(((W - d.textlength(t, font=f)) // 2, 1446), t, font=f, fill=ACIK)
ortala(im, kutu("TAKİPTE KAL", font("Inter-Black.otf", 56), KOYU, HARDAL, pad=(30, 18), aci=-2), 1520)
im.convert("RGB").save(f"{O}/hikaye_genel_tanitim.jpg", quality=93)
print("yazıldı")
