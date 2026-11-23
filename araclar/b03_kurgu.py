#!/usr/bin/env python3
"""B03 kurgusu: kırpma, sıralama, altyazı ve ekran yazıları, seviye eşitleme, ortam yatağı.
Çalıştır: python3 araclar/b03_kurgu.py  (depo kökünden)
Çıktı: diziler/sifir-sehir/bolumler/B03/cikti/B03_kurgu_v1.mp4 ve B03.ass
"""
import subprocess, os, re, sys

B = "diziler/sifir-sehir/bolumler/B03"
SRC = f"{B}/klipler/onayli"
OUT = f"{B}/cikti"
SURUM = "v1"
FPS = 24
os.makedirs(OUT, exist_ok=True)

# Klip listesi: (ad, giriş sn, çıkış sn, ses kazancı dB, altyazılar[(başla, bitir, metin)] kaynak klip zamanıyla)
# Kazançlar: diyalog klipleri yaklaşık -18 LUFS'a çekilir (ölçülen değerler kayit.md içinde); ortam klipleri kısılır.
EDL = [
 ("P01",  0.30, 5.90,  0.0, []),   # klip gelince zamanlar ve altyazı ölçülecek
 ("P02a", 0.10, 1.70,  0.0, []),
 ("P02c", 0.50, 3.70, +5.0, [(1.80, 2.75, "Sayın Muhtar…")]),
 ("P03",  0.60, 3.00, +6.0, []),
 ("P04",  0.80, 7.93, -4.7, [(1.10, 1.75, "Rıza ben."), (2.85, 3.85, "Yeni ortağınız."), (4.35, 6.45, "Şalteri kapatıyoruz, tasarrufu paylaşıyoruz."), (6.55, 7.70, "Kazan kazan!")]),
 ("P05",  0.30, 5.90, +4.6, [(1.40, 3.20, "Öncekiler slayt getirmişti.")]),
 ("P06",  0.60, 5.90,  0.0, [(1.65, 2.80, "Bakın, fatura burada."), (3.20, 4.55, "Üç yüz otuz üç bin—")]),
 ("P07",  0.00, 3.60, +2.7, []),
 ("P09",  0.20, 5.90, -3.3, [(1.70, 3.20, "Koş Rıza, koş!"), (4.25, 5.20, "Yetişemez.")]),
 ("P08",  0.30, 5.60, -3.3, [(1.40, 2.50, "Sayın Muhtar!"), (2.90, 4.00, "Muhtar Bey!"), (4.40, 5.40, "Bir dakika!")]),
 ("P10",  0.60, 5.90,  0.0, [(3.05, 3.85, "Ver bakayım.")]),
 ("P11",  0.60, 7.60, -2.2, [(1.25, 2.10, "Sen kimsin?"), (3.00, 4.00, "Yeni… sahip…"), (4.10, 5.30, "Sahip mi?!")]),
 ("P12",  1.00, 5.90,  0.0, [(1.50, 2.75, "Şalter Muhtar'da."), (3.05, 4.05, "Muhtar bende."), (4.40, 5.50, "Anahtar da burada.")]),
 ("P13",  0.40, 5.90, +3.2, [(0.70, 1.55, "Verir misiniz?"), (3.15, 3.80, "Veririm."), (4.25, 5.00, "Bir şartla.")]),
]
EDL = [e for e in EDL if os.path.exists(f"{SRC}/{e[0]}.mp4")]   # eksik klip atlanır (ön izleme)
DONUK = 3.2          # son karenin dondurulduğu süre (bitiş yazısı)
HEDEF_LUFS = -15.0
YATAK_DB = -21       # ortam yatağı kaynağının seviyesi (dB); süzgeçlerden sonra bitmiş kurguda yaklaşık -44 dB
KAPI = 0.05          # replik dışındaki anlarda klibin kendi sesinin çarpanı (yaklaşık -26 dB)
RAMPA = 0.09         # kapının açılıp kapanma süresi (sn)
PAY = 0.14           # repliğin önüne ve arkasına bırakılan pay (sn)
# Replik olmayan ama korunması gereken sesler (kaynak klip zamanı)
EK_SES = {"P02c": [(0.80, 1.35)], "P05": [(0.3, 5.9)], "P06": [(4.7, 5.5)], "P07": [(0.0, 3.6)], "P08": [(0.3, 5.6)], "P09": [(0.2, 5.9)], "P10": [(0.6, 3.0)], "P11": [(5.3, 7.6)]}
# Replik içermeyen klipler: kendi sesleri bu çarpanla, yumuşak giriş-çıkışla kalır
ORTAM_KLIP = {"P02a": 0.0, "P03": 0.6}

def t(x):  # ASS zaman biçimi
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

# ---- zaman çizelgesi ve altyazılar ----
pos = 0.0; subs = []; starts = {}
for ad, i, o, g, ss in EDL:
    starts[ad] = pos
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
Style: Baslik,Inter Black,128,&H00ECF8FF,&H00ECF8FF,&H00141414,&H78000000,0,0,0,0,100,100,2,0,1,6,2,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
p01 = EDL[0][2] - EDL[0][1]
POP = r"\fscx70\fscy70\t(0,140,\fscx106\fscy106)\t(140,220,\fscx100\fscy100)"
# açılış kancası
ev.append((0.05, 3.3, "KutuKoyu", r"{\an5\pos(540,190)\frz2\fad(0,90)" + POP + r"}KOCAM KEÇİYLE"))
ev.append((0.32, 3.3, "KutuVurgu", r"{\an5\pos(540,325)\frz-3\fad(0,90)" + POP + r"}TOPLANTIYA GİRDİ"))
if "P03" in starts: ev.append((starts["P03"] + 0.15, starts["P03"] + 2.3, "KutuVurguKucuk", r"{\an5\pos(540,150)\frz-2\fad(0,140)" + POP + r"}SIFIR ŞEHİR · BÖLÜM 3"))
if "P10" in starts: ev.append((starts["P10"] + 2.6, starts["P10"] + 5.2, "KutuVurguKucuk", r"{\an5\pos(760,640)\frz-2\fad(0,140)" + POP + r"}EMİNE"))
for a, b, m in subs: ev.append((a, b, "Alt", m))
# kapanış: son kare donar ve yavaşça yaklaşır; karartma yok. Soru + takip çağrısı sırayla "pat" diye gelir.
ev.append((SON + 0.15, TOPLAM, "KutuKoyu", r"{\an5\pos(540,1290)\frz2" + POP + r"}EMİNE'NİN ŞARTI NE?"))
ev.append((SON + 0.75, TOPLAM, "KutuVurguKucuk", r"{\an5\pos(540,1395)\frz-2" + POP + r"}TAHMİNİNİ YORUMA YAZ"))
ev.append((SON + 1.45, TOPLAM, "KutuVurgu", r"{\an5\pos(540,1505)\frz-3" + POP + r"\t(900,1100,\fscx108\fscy108)\t(1100,1300,\fscx100\fscy100)}TAKİP ET"))
for a, b, st, m in ev: ass += f"Dialogue: 0,{t(a)},{t(b)},{st},,0,0,0,,{m}\n"
open(f"{OUT}/B03.ass", "w", encoding="utf-8").write(ass)

# ---- ffmpeg ----
inp = []; fv = []; fa = []; lv = ""; la = ""
for n, (ad, i, o, g, ss) in enumerate(EDL):
    inp += ["-i", f"{SRC}/{ad}.mp4"]
    d = o - i
    v = f"[{n}:v]trim=start={i}:end={o},setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p"
    if n == len(EDL) - 1:   # son klip: son kare donar, küçük bir sıçramayla yaklaşır ve yavaşça yaklaşmaya devam eder; karartma yok
        v += f",tpad=stop_mode=clone:stop_duration={DONUK},scale=w='2*trunc(540*(1+0.045*clip((t-{d})/0.18,0,1)+0.05*clip((t-{d})/{DONUK},0,1)))':h=-2:eval=frame:flags=bicubic,crop=1080:1920"
    fv.append(v + f"[v{n}]")
    a = f"[{n}:a]atrim=start={i}:end={o},asetpts=PTS-STARTPTS,volume={g}dB"
    if ad in ORTAM_KLIP:
        a += f",volume={ORTAM_KLIP[ad]},afade=t=in:st=0:d=0.25,afade=t=out:st={d - 0.25}:d=0.25"
    else:
        # konuşma kapısı: yalnız replik aralıklarında klibin sesi açık, arada kısık
        ar = [(max(x, i) - i - PAY, min(y, o) - i + PAY) for x, y, _ in ss] + [(x - i, y - i) for x, y in EK_SES.get(ad, [])]
        w = "+".join(f"clip((t-{x - RAMPA:.3f})/{RAMPA},0,1)*clip(({y + RAMPA:.3f}-t)/{RAMPA},0,1)" for x, y in ar)
        a += f",volume='{KAPI}+{1 - KAPI}*min(1,{w})':eval=frame,afade=t=in:st=0:d=0.03,afade=t=out:st={d - 0.04}:d=0.04"
    if n == len(EDL) - 1: a += f",apad=pad_dur={DONUK}"
    fa.append(a + f"[a{n}]")
    lv += f"[v{n}]"; la += f"[a{n}]"
N = len(EDL)
fv.append(f"{lv}concat=n={N}:v=1:a=0[vc]")
fv.append(f"[vc]subtitles={OUT}/B03.ass:fontsdir=/usr/share/fonts/opentype/inter[vout]")
fa.append(f"{la}concat=n={N}:v=0:a=1[ac]")
# ortam yatağı: bölüm boyunca kesintisiz, yavaşça dalgalanan alçak frekanslı gürültü (yapay rüzgâr); kesmelerde ortam sesinin değişmesini örter
fa.append(f"anoisesrc=color=pink:sample_rate=48000:duration={TOPLAM}:seed=7,highpass=f=120,lowpass=f=700,tremolo=f=0.13:d=0.45,volume={YATAK_DB}dB,afade=t=in:st=0:d=0.3,aformat=channel_layouts=stereo[bed]")
fa.append(f"[ac][bed]amix=inputs=2:normalize=0:duration=first,afade=t=out:st={TOPLAM - 0.25}:d=0.25[amix]")

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
cikti = f"{OUT}/B03_kurgu_{SURUM}.mp4"
run([f"[amix]volume={kazanc:.2f}dB,alimiter=limit=0.84:attack=3:release=60:level=disabled[aout]"], cikti,
    ["-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)])
e = subprocess.run(["ffmpeg", "-hide_banner", "-i", cikti, "-af", "loudnorm=print_format=summary", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
son = {k: re.search(k + r":\s+(-?[\d.]+)", e).group(1) for k in ("Input Integrated", "Input True Peak", "Input LRA")}
print(f"süre {TOPLAM:.2f} sn | ham {olc} LUFS, kazanç {kazanc:+.1f} dB | sonuç {son}")
print("klip başlangıçları:", {k: round(v, 2) for k, v in starts.items()})

# ---- kapaklı sürüm: kapak görseli videonun ilk karesi (tek kare) olur; Buffer gibi kapak seçtirmeyen araçlar için ----
kapak = f"{OUT}/B03_kapak.jpg"
if os.path.exists(kapak):
    k_out = f"{OUT}/B03_kurgu_{SURUM}_kapakli.mp4"
    kare = 1 / FPS
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{kare}", "-i", kapak, "-i", cikti,
        "-filter_complex", f"[0:v]scale=1080:1920,setsar=1,format=yuv420p,fps={FPS}[k];[1:v]fps={FPS},format=yuv420p[v];[k][v]concat=n=2:v=1:a=0[vout];[1:a]adelay={kare * 1000:.0f}:all=1[aout]",
        "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", k_out], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-2000:])
    print("kapaklı sürüm:", k_out)
