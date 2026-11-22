#!/usr/bin/env python3
"""B01 kurgusu: kırpma, sıralama, altyazı ve ekran yazıları, seviye eşitleme, ortam yatağı.
Çalıştır: python3 araclar/b01_kurgu.py  (depo kökünden)
Çıktı: diziler/sifir-sehir/bolumler/B01/cikti/B01_kurgu_v1.mp4 ve B01.ass
"""
import subprocess, os, re, sys

B = "diziler/sifir-sehir/bolumler/B01"
SRC = f"{B}/klipler/onayli"
OUT = f"{B}/cikti"
SURUM = "v2"
FPS = 24
os.makedirs(OUT, exist_ok=True)

# Klip listesi: (ad, giriş sn, çıkış sn, ses kazancı dB, altyazılar[(başla, bitir, metin)] kaynak klip zamanıyla)
# Kazançlar: diyalog klipleri yaklaşık -18 LUFS'a çekilir (ölçülen değerler kayit.md içinde); ortam klipleri kısılır.
EDL = [
 ("P01", 0.90, 3.92, +3.4, [(1.50, 3.92, "Rıza… bunun neresi şehir?")]),
 ("P02", 0.30, 3.30,  0.0, []),
 ("P03", 0.10, 5.97, +1.6, [(0.35, 2.00, "Şehir merkezi burası aşkım!"), (2.00, 3.55, "Bak, tabelası bile var."), (3.95, 5.60, "Tabelayı keçi yiyor, Rıza.")]),
 ("P04", 0.50, 3.00, -4.0, []),
 ("P05", 0.10, 7.40, +2.9, [(0.40, 3.90, "On iki ev, bir depo, bir değirmen…"), (4.20, 4.95, "Nüfus: üç."), (4.95, 5.85, "Üç bin mi?"), (6.25, 7.00, "Üç.")]),
 ("P06a", 0.60, 5.97, +5.6, [(1.10, 2.15, "Kimin parasıyla?"), (2.95, 3.95, "Dedemden kalan…"), (4.65, 5.60, "biraz da birikim.")]),
 ("P06b", 0.0417, 5.60, +5.9, [(0.55, 1.45, "Biraz dediğin?"), (3.55, 4.95, "Ev için ayırdığımız kadar.")]),
 ("P07", 0.60, 3.00,  0.0, []),
 ("P08", 0.60, 5.97, +1.7, [(1.10, 2.40, "Ama potansiyele bak!"), (2.40, 4.85, "Şuraya kafe, şuraya ortak çalışma alanı—")]),
 ("P09", 0.10, 3.20, -4.0, []),
 ("P10", 0.20, 5.97, +2.0, [(0.60, 2.30, "Yeni sahipler siz misiniz?"), (3.80, 5.75, "Öncekiler de böyle heyecanlıydı.")]),
 ("P11", 0.70, 3.30, +4.3, [(1.30, 2.30, "Öncekiler mi?")]),
 ("P12", 0.70, 3.40, -0.9, [(1.30, 2.70, "Üç gün dayandılar.")]),
 ("P13", 0.20, 5.97, +2.1, [(0.55, 1.30, "Bu arada…"), (1.70, 3.15, "köyün elektrik borcu."), (4.25, 5.20, "Artık sizin.")]),
 ("P14", 1.20, 5.97, +7.0, [(2.80, 3.40, "Rıza."), (4.60, 5.30, "Kaç?")]),
]
DONUK = 2.8          # son karenin dondurulduğu süre (bitiş yazısı)
HEDEF_LUFS = -15.0
YATAK_DB = -21       # ortam yatağı kaynağının seviyesi (dB); süzgeçlerden sonra bitmiş kurguda yaklaşık -44 dB
KAPI = 0.05          # replik dışındaki anlarda klibin kendi sesinin çarpanı (yaklaşık -26 dB)
RAMPA = 0.09         # kapının açılıp kapanma süresi (sn)
PAY = 0.14           # repliğin önüne ve arkasına bırakılan pay (sn)
# Replik olmayan ama korunması gereken sesler (kaynak klip zamanı): P08'de kadraj dışı metal gürültüsü
EK_SES = {"P08": [(5.02, 5.97)]}
# Replik içermeyen klipler: kendi sesleri bu çarpanla, yumuşak giriş-çıkışla kalır
ORTAM_KLIP = {"P02": 0.5, "P04": 0.6, "P07": 0.0, "P09": 0.6}

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
p01 = EDL[0][2] - EDL[0][1]; p02 = EDL[1][2] - EDL[1][1]
POP = r"\fscx70\fscy70\t(0,140,\fscx106\fscy106)\t(140,220,\fscx100\fscy100)"
# açılış kancası: iki eğik kutu, sırayla "pat" diye açılır (marka imzası; kapakla aynı dil)
ev.append((0.05, p01 - 0.04, "KutuKoyu", r"{\an5\pos(540,238)\frz2\fad(0,90)" + POP + r"}KOCAM BÜTÜN BİRİKİMİMİZLE"))
ev.append((0.32, p01 - 0.04, "KutuVurgu", r"{\an5\pos(540,385)\frz-3\fad(0,90)" + POP + r"}BİR ŞEHİR SATIN ALDI"))
# başlık
ev.append((p01 + 0.20, p01 + p02 - 0.08, "Baslik", r"{\an5\pos(540,300)\fad(160,140)}SIFIR ŞEHİR"))
ev.append((p01 + 0.45, p01 + p02 - 0.08, "KutuVurguKucuk", r"{\an5\pos(540,430)\frz-2\fad(0,140)" + POP + r"}BÖLÜM 1"))
for a, b, m in subs: ev.append((a, b, "Alt", m))
# kapanış: son kare donar, takip çağrısı (kancayla aynı dil)
ev.append((SON + 0.30, TOPLAM - 0.05, "KutuKoyu", r"{\an5\pos(540,262)\frz2\fad(0,250)" + POP + r"}DEVAMI İÇİN"))
ev.append((SON + 0.60, TOPLAM - 0.05, "KutuVurgu", r"{\an5\pos(540,408)\frz-3\fad(0,250)" + POP + r"}TAKİP ET"))
for a, b, st, m in ev: ass += f"Dialogue: 0,{t(a)},{t(b)},{st},,0,0,0,,{m}\n"
open(f"{OUT}/B01.ass", "w", encoding="utf-8").write(ass)

# ---- ffmpeg ----
inp = []; fv = []; fa = []; lv = ""; la = ""
for n, (ad, i, o, g, ss) in enumerate(EDL):
    inp += ["-i", f"{SRC}/{ad}.mp4"]
    d = o - i
    v = f"[{n}:v]trim=start={i}:end={o},setpts=PTS-STARTPTS,fps={FPS},format=yuv420p"
    if n == len(EDL) - 1:   # son klip: son kareyi dondur, hafif karart, siyaha geç
        v += f",tpad=stop_mode=clone:stop_duration={DONUK},eq=brightness='if(gt(t,{d}),-0.07,0)':eval=frame,fade=t=out:st={d + DONUK - 0.3}:d=0.3"
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
fv.append(f"[vc]subtitles={OUT}/B01.ass:fontsdir=/usr/share/fonts/opentype/inter[vout]")
fa.append(f"{la}concat=n={N}:v=0:a=1[ac]")
# ortam yatağı: bölüm boyunca kesintisiz, yavaşça dalgalanan alçak frekanslı gürültü (yapay rüzgâr); kesmelerde ortam sesinin değişmesini örter
fa.append(f"anoisesrc=color=pink:sample_rate=48000:duration={TOPLAM}:seed=7,highpass=f=120,lowpass=f=700,tremolo=f=0.13:d=0.45,volume={YATAK_DB}dB,afade=t=in:st=0:d=0.3,aformat=channel_layouts=stereo[bed]")
fa.append(f"[ac][bed]amix=inputs=2:normalize=0:duration=first,afade=t=out:st={TOPLAM - 0.5}:d=0.5[amix]")

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
cikti = f"{OUT}/B01_kurgu_{SURUM}.mp4"
run([f"[amix]volume={kazanc:.2f}dB,alimiter=limit=0.84:attack=3:release=60:level=disabled[aout]"], cikti,
    ["-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)])
e = subprocess.run(["ffmpeg", "-hide_banner", "-i", cikti, "-af", "loudnorm=print_format=summary", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
son = {k: re.search(k + r":\s+(-?[\d.]+)", e).group(1) for k in ("Input Integrated", "Input True Peak", "Input LRA")}
print(f"süre {TOPLAM:.2f} sn | ham {olc} LUFS, kazanç {kazanc:+.1f} dB | sonuç {son}")
print("klip başlangıçları:", {k: round(v, 2) for k, v in starts.items()})
