#!/usr/bin/env python3
"""B05 kurgusu: kırpma, sıralama, altyazı ve ekran yazıları, seviye eşitleme, ortam yatağı.
Çalıştır: python3 araclar/b04_kurgu.py  (depo kökünden)
Çıktı: diziler/sifir-sehir/bolumler/B03/cikti/B05_kurgu_v1.mp4 ve B05.ass
"""
import subprocess, os, re, sys

B = "diziler/sifir-sehir/bolumler/B05"
SRC = f"{B}/klipler/onayli"
OUT = f"{B}/cikti"
SURUM = "v1"
FPS = 24
os.makedirs(OUT, exist_ok=True)

# Klip listesi: (ad, giriş sn, çıkış sn, ses kazancı dB, altyazılar[(başla, bitir, metin)] kaynak klip zamanıyla)
# Kazançlar: diyalog klipleri yaklaşık -18 LUFS'a çekilir (ölçülen değerler kayit.md içinde); ortam klipleri kısılır.
EDL = [
 ("P01", 0.30, 6.00, -2.1, [(0.90, 3.40, "Üç yüz otuz üç başvuru! Köy doldu aşkım!"), (3.90, 5.20, "On iki ev var, Rıza.")]),
 ("P02", 0.40, 7.90, -3.5, [(0.60, 3.10, "Sıkışırız! Ev başına yirmi sekiz kişi."), (4.30, 5.50, "Tuvalet bir tane.")]),
 ("P03", 0.80, 5.20, -1.4, [(1.10, 2.30, "Önce borcu kapatıyoruz."), (3.00, 4.80, "Aşkım, önce yatırım!")]),
 ("P04", 0.40, 7.90, +1.4, [(0.70, 3.70, "Elektrik kesilirse yatırımı karanlıkta mı yapacaksın?")]),
 ("P05", 0.20, 6.00, +1.0, [(1.10, 2.60, "Otuz üç kuruşu dahil…"), (4.30, 5.10, "Ödendi.")]),
 ("P06", 0.60, 5.60, +1.9, [(1.10, 2.40, "Öncekiler ödemezdi."), (3.40, 4.50, "Dedemin parası…")]),
 ("P07", 0.60, 6.20, +6.0, [(3.10, 4.10, "Hayırlı olsun.")]),
 ("P08", 0.00, 6.40, -2.1, [(0.60, 3.20, "\"Emekli öğretmenim. Sessizlik arıyorum.\""), (4.10, 4.90, "Doğru yere gelmiş.")]),
 ("P09", 0.00, 6.60, -2.6, [(0.30, 2.70, "Bu da fenomen! Bir milyon takipçisi var!"), (3.70, 6.00, "Takipçileri tabureye sırayla mı oturacak?")]),
 ("P10", 0.40, 6.20, -2.0, [(0.60, 2.40, "\"Muhtarla görüşmek istiyorum.\""), (3.20, 4.90, "Muhtar randevu vermez.")]),
 ("P11", 0.30, 6.40, -2.1, [(0.50, 3.10, "Mülakat falan yok. Kim gelirse gelsin."), (4.10, 5.00, "Ya kaçarlarsa?")]),
 ("P12", 0.80, 6.40, +2.1, [(1.30, 2.70, "Üç gün dayanan kalır.")]),
 ("P13", 0.80, 6.20, +6.0, [(4.30, 5.50, "Biri geldi…")]),
]
EDL = [e for e in EDL if os.path.exists(f"{SRC}/{e[0]}.mp4")]
PANEL_CELLS = {   # üst sayaç durumları (diziler/sifir-sehir/sayac.md)
 "a": ["NÜFUS=5", "KASA=8.500.000 TL", "BAŞVURU=333"],
 "b": ["NÜFUS=5", "KASA=8.166.666,67 TL", "BAŞVURU=333"],
 "c": ["NÜFUS=5", "KASA=8.166.666,67 TL", "BAŞVURU=748"],
 "d": ["NÜFUS=5", "KASA=8.166.666,67 TL", "BAŞVURU=1.204"],
}
SAYAC_XY = (40, 200)   # eksik klip atlanır (ön izleme)
DONUK = 3.6          # son karenin dondurulduğu süre (bitiş yazısı)
HEDEF_LUFS = -15.0
YATAK_DB = -17       # ortam yatağı kaynağının seviyesi (dB); süzgeçlerden sonra bitmiş kurguda yaklaşık -44 dB
KAPI = 0.35          # replik dışındaki anlarda klibin kendi sesinin çarpanı (yaklaşık -26 dB)
RAMPA = 0.22         # kapının açılıp kapanma süresi (sn)
PAY = 0.20           # repliğin önüne ve arkasına bırakılan pay (sn)
# Replik olmayan ama korunması gereken sesler (kaynak klip zamanı)
SUS = {}   # tamamen susturulan aralıklar (kaynak klip zamanı): P11'de "Sahip mi?" yanlış karakterin sesiyle söylendi
EK_SES = {"P01": [(0.3, 0.9)], "P05": [(3.0, 3.9)], "P07": [(4.3, 5.0)], "P08": [(0.0, 0.6)], "P09": [(0.0, 0.4)], "P10": [(0.4, 0.7)]}   # bildirim ve ödeme sesleri
# Replik içermeyen klipler: kendi sesleri bu çarpanla, yumuşak giriş-çıkışla kalır
ORTAM_KLIP = {}

def t(x):  # ASS zaman biçimi
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# ---- zaman çizelgesi ve altyazılar ----
pos = 0.0; subs = []; starts = {}
for ad, i, o, g, ss in EDL:
    starts.setdefault(ad, pos)
    for a, b, m in ss:
        a2 = max(a, i) - i + pos; b2 = min(b, o) - i + pos
        subs.append((a2, b2, m))
    pos += o - i
SON = pos            # donuk kare başlangıcı
TOPLAM = pos + DONUK

ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Alt,Inter SemiBold,40,&H00FFFFFF,&H00FFFFFF,&H00101010,&H78000000,0,0,0,0,100,100,0,0,1,2.6,0.8,2,120,120,500,1
Style: KutuKoyu,Inter ExtraBold,58,&H00ECF8FF,&H00ECF8FF,&H00141414,&H00141414,0,0,0,0,100,100,1,0,3,15,0,5,60,60,0,1
Style: KutuVurgu,Inter Black,90,&H00141414,&H00141414,&H003DB3F2,&H003DB3F2,0,0,0,0,100,100,1,0,3,17,0,5,60,60,0,1
Style: KutuVurguKucuk,Inter Black,40,&H00141414,&H00141414,&H003DB3F2,&H003DB3F2,0,0,0,0,100,100,3,0,3,12,0,5,60,60,0,1
Style: Sayac,Inter ExtraBold,36,&H00ECF8FF,&H00ECF8FF,&H00141414,&H00141414,0,0,0,0,100,100,1,0,3,11,0,5,60,60,0,1
Style: Baslik,Inter Black,128,&H00ECF8FF,&H00ECF8FF,&H00141414,&H78000000,0,0,0,0,100,100,2,0,1,6,2,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
p01 = EDL[0][2] - EDL[0][1]
POP = r"\fscx70\fscy70\t(0,140,\fscx106\fscy106)\t(140,220,\fscx100\fscy100)"
# açılış kancası (bölüm doğrudan P01 ile açılır)
ev.append((0.05, 3.0, "KutuKoyu", r"{\an5\pos(540,190)\frz2\fad(0,120)" + POP + r"}KÖYE 333 KİŞİ BAŞVURDU"))
ev.append((0.32, 3.0, "KutuVurgu", r"{\an5\pos(540,325)\frz-3\fad(0,120)" + POP + r"}EV SAYISI: 12"))
ev.append((3.1, 5.4, "KutuVurguKucuk", r"{\an7\pos(52,348)\frz-2\fad(0,140)" + POP + r"}SIFIR ŞEHİR · BÖLÜM 5"))
SA = 3.0
ODEME = starts["P05"] + 3.30 - 0.20          # ödeme sesi anı: kasa düşer
P_C = starts["P08"]                           # yeni başvurular
P_D = SON                                     # final
ev.append((ODEME, ODEME + 2.2, "KutuVurguKucuk", r"{\an7\pos(330,330)\frz-2\fad(0,200)" + POP + r"}−333.333,33 TL"))
ev.append((ODEME + 0.4, ODEME + 2.4, "KutuKoyu", r"{\an7\pos(330,400)\frz2\fad(0,200)" + POP + r"}BORÇ ÖDENDİ"))
PANELS = [("a", SA, ODEME), ("b", ODEME, P_C), ("c", P_C, P_D), ("d", P_D, TOPLAM + 1)]
for a, b, m in subs: ev.append((a, b, "Alt", m))
# kapanış: son kare donar; karartma ve yakınlaşma yok. Soru + takip çağrısı sırayla "pat" diye gelir.
ev.append((SON + 0.15, TOPLAM, "KutuKoyu", r"{\an5\pos(540,1290)\frz2" + POP + r"}İLK GELEN KİM?"))
ev.append((SON + 0.75, TOPLAM, "KutuVurguKucuk", r"{\an5\pos(540,1395)\frz-2" + POP + r"}TAHMİNİNİ YORUMA YAZ"))
ev.append((SON + 1.45, TOPLAM, "KutuVurgu", r"{\an5\pos(540,1505)\frz-3" + POP + r"\t(900,1100,\fscx108\fscy108)\t(1100,1300,\fscx100\fscy100)}TAKİP ET"))
for a, b, st, m in ev: ass += f"Dialogue: 0,{t(a)},{t(b)},{st},,0,0,0,,{m}\n"
open(f"{OUT}/B05.ass", "w", encoding="utf-8").write(ass)

# ---- ffmpeg ----
inp = []; fv = []; fa = []; lv = ""; la = ""
for n, (ad, i, o, g, ss) in enumerate(EDL):
    inp += ["-i", f"{SRC}/{ad}.mp4"]
    d = o - i
    v = f"[{n}:v]trim=start={i}:end={o},setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p"
    if n == len(EDL) - 1:   # son klip: son kare olduğu gibi donar (yakınlaşma, karartma yok; kullanıcı istemedi)
        v += f",tpad=stop_mode=clone:stop_duration={DONUK}"
    fv.append(v + f"[v{n}]")
    a = f"[{n}:a]atrim=start={i}:end={o},asetpts=PTS-STARTPTS,volume={g}dB"
    if ad in ORTAM_KLIP:
        a += f",volume={ORTAM_KLIP[ad]},afade=t=in:st=0:d=0.25,afade=t=out:st={d - 0.25}:d=0.25"
    else:
        # konuşma kapısı: yalnız replik aralıklarında klibin sesi açık, arada kısık
        ar = [(max(x, i) - i - PAY, min(y, o) - i + PAY) for x, y, _ in ss] + [(x - i, y - i) for x, y in EK_SES.get(ad, [])]
        w = "+".join(f"clip((t-{x - RAMPA:.3f})/{RAMPA},0,1)*clip(({y + RAMPA:.3f}-t)/{RAMPA},0,1)" for x, y in ar)
        a += f",volume='{KAPI}+{1 - KAPI}*min(1,{w})':eval=frame,afade=t=in:st=0:d=0.12,afade=t=out:st={d - 0.12}:d=0.12"
        for x, y in SUS.get(ad, []): a += f",volume='1-clip((t-{x - i:.3f})/0.06,0,1)*clip(({y - i:.3f}-t)/0.06,0,1)':eval=frame"
    if n == len(EDL) - 1: a += f",apad=pad_dur={DONUK}"
    fa.append(a + f"[a{n}]")
    lv += f"[v{n}]"; la += f"[a{n}]"
N = len(EDL)
fv.append(f"{lv}concat=n={N}:v=1:a=0[vc]")
fv.append(f"[vc]subtitles={OUT}/B05.ass:fontsdir=/usr/share/fonts/opentype/inter[vs]")
fa.append(f"{la}concat=n={N}:v=0:a=1[ac]")
# ortam yatağı: bölüm boyunca kesintisiz, yavaşça dalgalanan alçak frekanslı gürültü (yapay rüzgâr); kesmelerde ortam sesinin değişmesini örter
fa.append(f"anoisesrc=color=pink:sample_rate=48000:duration={TOPLAM}:seed=7,highpass=f=120,lowpass=f=2200,tremolo=f=0.13:d=0.45,volume={YATAK_DB}dB,afade=t=in:st=0:d=0.3,aformat=channel_layouts=stereo[bed]")
MUZIK = os.environ.get("MUZIK", "diziler/sifir-sehir/muzik/bitis_1.mp3")   # varsayılan: müzikli bitiş (kullanıcı tercihi); MUZIK= boş verilirse müziksiz
if MUZIK and not os.path.exists(MUZIK): MUZIK = None
_ = os.environ.get("MUZIK")   # verilirse bitişte çalar: son repliğin ardından girer, donuk karede öne çıkar
if MUZIK:
    inp += ["-i", MUZIK]; mi = len(EDL)
    MSURE = 11.4                 # müziğin kullanılan uzunluğu; son vuruş videonun sonuna denk gelir
    mb = TOPLAM - MSURE          # son repliklerin altında kısık başlar, donuk karede öne çıkar
    ac = SON - mb                # müzik zamanında donuk karenin başladığı an
    fa.append(f"[{mi}:a]atrim=0:{MSURE},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume='0.16+0.84*clip((t-{ac - 0.25:.2f})/0.35,0,1)':eval=frame,volume=-7dB,afade=t=in:st=0:d=0.4,adelay={mb * 1000:.0f}:all=1[mz]")
    fa.append(f"[ac][bed][mz]amix=inputs=3:normalize=0:duration=first,afade=t=out:st={TOPLAM - 0.25}:d=0.25[amix]")
else:
    fa.append(f"[ac][bed]amix=inputs=2:normalize=0:duration=first,afade=t=out:st={TOPLAM - 0.25}:d=0.25[amix]")

# ---- üst sayaç paneli (PNG, araclar/sayac_panel.py); durum değiştikçe yeni panel ----
X, Y = SAYAC_XY; prev = "vs"
for k, (ad, a0, b0) in enumerate(PANELS):
    png = f"{OUT}/sayac_{ad}.png"
    subprocess.run(["python3", "araclar/sayac_panel.py", png] + PANEL_CELLS[ad] + ["--vurgu=SON"], check=True, capture_output=True)
    ii = inp.count("-i"); inp += ["-loop", "1", "-framerate", str(FPS), "-t", f"{TOPLAM}", "-i", png]
    fade = f",fade=t=in:st={a0}:d=0.35:alpha=1" if k == 0 else ""
    fv.append(f"[{ii}:v]format=rgba{fade}[h{k}]")
    nxt = "vout" if k == len(PANELS) - 1 else f"vh{k}"
    fv.append(f"[{prev}][h{k}]overlay={X}:{Y}:enable='between(t,{a0:.2f},{b0:.2f})'[{nxt}]"); prev = nxt

def run(extra_a, out, vopts):
    cmd = ["ffmpeg", "-v", "error", "-y"] + inp + ["-filter_complex", ";".join(fv + fa + extra_a), "-map", "[vout]", "-map", "[aout]"] + vopts + ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-3000:])

# 1. geçiş: ses seviyesini ölç
cmd = ["ffmpeg", "-v", "info", "-y"] + inp + ["-filter_complex", ";".join(fa + ["[amix]loudnorm=print_format=summary[aout]"]), "-map", "[aout]", "-f", "null", "-"]
e = subprocess.run(cmd, capture_output=True, text=True).stderr
if "Input Integrated" not in e: sys.exit(e[-3000:])
olc = float(re.search(r"Input Integrated:\s+(-?[\d.]+)", e).group(1))
kazanc = HEDEF_LUFS - olc
# 2. geçiş: doğrusal kazanç + sınırlayıcı
cikti = f"{OUT}/B05_kurgu_{SURUM}.mp4"
run([f"[amix]volume={kazanc:.2f}dB,alimiter=limit=0.84:attack=3:release=60:level=disabled[aout]"], cikti,
    ["-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)])
e = subprocess.run(["ffmpeg", "-hide_banner", "-i", cikti, "-af", "loudnorm=print_format=summary", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
son = {k: re.search(k + r":\s+(-?[\d.]+)", e).group(1) for k in ("Input Integrated", "Input True Peak", "Input LRA")}
print(f"süre {TOPLAM:.2f} sn | ham {olc} LUFS, kazanç {kazanc:+.1f} dB | sonuç {son}")
print("klip başlangıçları:", {k: round(v, 2) for k, v in starts.items()})

# ---- kapaklı sürüm: kapak görseli videonun ilk karesi (tek kare) olur; Buffer gibi kapak seçtirmeyen araçlar için ----
kapak = f"{OUT}/B05_kapak.jpg"
if os.path.exists(kapak):
    k_out = f"{OUT}/B05_kurgu_{SURUM}_kapakli.mp4"
    kare = 1 / FPS
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{kare}", "-i", kapak, "-i", cikti,
        "-filter_complex", f"[0:v]scale=1080:1920,setsar=1,format=yuv420p,fps={FPS}[k];[1:v]fps={FPS},format=yuv420p[v];[k][v]concat=n=2:v=1:a=0[vout];[1:a]adelay={kare * 1000:.0f}:all=1[aout]",
        "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", k_out], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-2000:])
    print("kapaklı sürüm:", k_out)
