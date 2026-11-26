#!/usr/bin/env python3
"""Üst sayaç paneli (PNG, saydam). Kullanım: python3 araclar/sayac_panel.py <çıktı.png> "ETİKET=DEĞER" ["ETİKET=DEĞER" ...] [--vurgu=SON]
Sabit tasarım: koyu yarı saydam kart, solda hardal şerit, her hücrede küçük etiket + büyük değer. --vurgu=SON son hücreyi hardal zeminle öne çıkarır."""
import sys
from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/inter/"
lab = ImageFont.truetype(F + "Inter-Bold.otf", 22)
val = ImageFont.truetype(F + "Inter-Black.otf", 44)
HARDAL = (242, 179, 61, 255); KREM = (245, 236, 220, 255); KOYU = (20, 18, 16, 255)
dikey = "--dikey" in sys.argv
out = sys.argv[1]; args = [a for a in sys.argv[2:] if not a.startswith("--")]
vurgu = "--vurgu=SON" in sys.argv
cells = [a.split("=", 1) for a in args]
PADX, PADY, GAP, BAR = 26, 16, 24, 8
def tw(f, t):
    b = f.getbbox(t); return b[2] - b[0]
if dikey:
    # sağ üst köşe için dar, alt alta satırlı kart: solda etiket, sağda değer
    lab2 = ImageFont.truetype(F + "Inter-Bold.otf", 20); val2 = ImageFont.truetype(F + "Inter-Black.otf", 34)
    RH, PX, PY = 50, 22, 12
    lw = max(tw(lab2, l) for l, v in cells); vw = max(tw(val2, v) for l, v in cells)
    W = BAR + PX + lw + 22 + vw + PX; H = PY * 2 + RH * len(cells)
    img = Image.new("RGBA", (W + 12, H + 12), (0, 0, 0, 0))
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((8, 10, W + 8, H + 10), 20, fill=(0, 0, 0, 90)); img.alpha_composite(sh)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, W, H), 20, fill=(20, 18, 16, 215))
    d.rounded_rectangle((W - BAR - 14, 0, W, H), 20, fill=HARDAL); d.rectangle((W - BAR - 14, 0, W - BAR, H), fill=(20, 18, 16, 215))
    for i, (l, v) in enumerate(cells):
        y = PY + i * RH; son = vurgu and i == len(cells) - 1
        if son: d.rounded_rectangle((8, y + 3, W - BAR - 6, y + RH - 3), 14, fill=HARDAL)
        if i and not son and not (vurgu and i == len(cells) - 1): d.line((PX, y, W - BAR - PX, y), fill=(245, 236, 220, 45), width=2)
        d.text((PX, y + 15), l, font=lab2, fill=KOYU if son else (245, 236, 220, 170))
        vx = W - BAR - PX - tw(val2, v)
        d.text((vx, y + 6), v, font=val2, fill=KOYU if son else (HARDAL if i == 0 else KREM))
    img.save(out); print(out, img.size); sys.exit()
def _unused(f, t):
    b = f.getbbox(t); return b[2] - b[0]
ws = [max(tw(lab, " ".join(l)), tw(val, v)) for l, v in cells]
W = BAR + PADX + sum(ws) + GAP * 2 * (len(cells) - 1) + PADX
H = PADY + 26 + 6 + 48 + PADY
img = Image.new("RGBA", (W + 12, H + 12), (0, 0, 0, 0))
sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((8, 10, W + 8, H + 10), 22, fill=(0, 0, 0, 90))
img.alpha_composite(sh)
d = ImageDraw.Draw(img)
d.rounded_rectangle((0, 0, W, H), 22, fill=(20, 18, 16, 215))
d.rounded_rectangle((0, 0, BAR + 14, H), 22, fill=HARDAL); d.rectangle((BAR, 0, BAR + 14, H), fill=(20, 18, 16, 215))
x = BAR + PADX
for i, ((l, v), w) in enumerate(zip(cells, ws)):
    son = vurgu and i == len(cells) - 1
    if son:
        d.rounded_rectangle((x - 14, 8, x + w + 14, H - 8), 16, fill=HARDAL)
    d.text((x, PADY), " ".join(l), font=lab, fill=KOYU if son else (245, 236, 220, 170))
    d.text((x, PADY + 26), v, font=val, fill=KOYU if son else (HARDAL if i == 0 else KREM))
    x += w
    if i < len(cells) - 1:
        x += GAP
        if not (vurgu and i + 1 == len(cells) - 1): d.line((x, PADY + 6, x, H - PADY - 6), fill=(245, 236, 220, 60), width=2)
        x += GAP
img.save(out)
print(out, img.size)
