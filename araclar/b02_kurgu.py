#!/usr/bin/env python3
"""B02 kurgusu: kırpma, sıralama, altyazı ve ekran yazıları, seviye eşitleme, ortam yatağı.
Çalıştır: python3 araclar/b02_kurgu.py  (depo kökünden)
Çıktı: diziler/sifir-sehir/bolumler/B02/cikti/B02_kurgu_v1.mp4 ve B02.ass
"""
import subprocess, os, re, sys

B = "diziler/sifir-sehir/bolumler/B02"
SRC = f"{B}/klipler/onayli"
OUT = f"{B}/cikti"
SURUM = "v1"
FPS = 24
os.makedirs(OUT, exist_ok=True)

# Klip listesi: (ad, giriş sn, çıkış sn, ses kazancı dB, altyazılar[(başla, bitir, metin)] kaynak klip zamanıyla)
# Kazançlar: diyalog klipleri yaklaşık -18 LUFS'a çekilir (ölçülen değerler kayit.md içinde); ortam klipleri kısılır.
EDL = [
 ("P01", 0.45, 5.50, +4.5, [(0.70, 2.05, "Rıza. Kaç para?"), (2.70, 3.25, "Üç…"), (3.95, 4.75, "Üç bin mi?")]),
 ("P02", 0.70, 5.90, +5.0, [(1.05, 2.40, "Üç yüz otuz üç bin…"), (3.05, 4.75, "üç yüz otuz üç lira, hayatım.")]),
 ("P03", 0.70, 3.90, +3.5, [(1.10, 2.70, "Otuz üç de kuruşu var.")]),
 ("P04", 0.50, 5.97, +4.4, [(0.90, 3.15, "Amca, burada üç kişi yaşıyorsunuz."), (3.85, 5.75, "Bu kadar elektriği kim yaktı ya?")]),
 ("P05", 0.50, 5.97, -0.5, [(0.90, 2.25, "Meydandaki lambalar."), (2.90, 4.30, "On iki senedir yanıyor."), (4.75, 5.85, "Gerisi faiz.")]),
 ("P06", 0.30, 3.30, +6.0, []),
 ("P07", 0.30, 5.60, +3.7, [(0.65, 1.90, "Ya tamam, sorun yok!"), (2.10, 3.15, "Kapatırız, biter."), (3.55, 4.75, "Şalter nerede amca?")]),
 ("P08", 0.70, 3.30, +4.0, [(1.25, 2.20, "Muhtarda.")]),
 ("P09", 0.60, 5.30, +2.0, [(1.00, 1.60, "Süper!"), (2.20, 4.20, "Hemen bir toplantı ayarlayalım muhtarla.")]),
 ("P10", 0.50, 3.60, +3.0, [(1.00, 2.50, "Kendisi şurada.")]),   # klip gelince zamanlar ölçülüp düzeltilecek
 ("P11", 0.40, 3.60, -3.0, []),
 ("P12", 0.80, 5.97, +5.0, [(1.25, 3.10, "Rıza… bu muhtar keçi."), (3.75, 5.60, "Demokratik bir süreç olmuştur aşkım.")]),
 ("P13", 0.70, 2.75,  0.0, [(1.05, 2.35, "Üç oyla seçildi.")]),   # 2.75'ten sonra Naci kameraya dönüyor
 ("P14", 0.30, 5.97, +5.4, [(0.60, 1.50, "Hadi git konuş."), (1.85, 2.85, "Keçiyle mi ya?"), (3.55, 5.05, "Muhtarla, hayatım.")]),
]
EDL = [e for e in EDL if os.path.exists(f"{SRC}/{e[0]}.mp4")]   # eksik klip atlanır (ön izleme)
DONUK = 2.8          # son karenin dondurulduğu süre (bitiş yazısı)
HEDEF_LUFS = -15.0
YATAK_DB = -21       # ortam yatağı kaynağının seviyesi (dB); süzgeçlerden sonra bitmiş kurguda yaklaşık -44 dB
KAPI = 0.05          # replik dışındaki anlarda klibin kendi sesinin çarpanı (yaklaşık -26 dB)
RAMPA = 0.09         # kapının açılıp kapanma süresi (sn)
PAY = 0.14           # repliğin önüne ve arkasına bırakılan pay (sn)
# Replik olmayan ama korunması gereken sesler (kaynak klip zamanı)
EK_SES = {}
# Replik içermeyen klipler: kendi sesleri bu çarpanla, yumuşak giriş-çıkışla kalır
ORTAM_KLIP = {"P06": 0.6, "P11": 0.6}

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
# açılış kancası: iki eğik kutu, sırayla "pat" diye açılır (marka imzası; kapakla aynı dil)
ev.append((0.05, 3.3, "KutuKoyu", r"{\an5\pos(540,190)\frz2\fad(0,90)" + POP + r"}KOCAMIN ALDIĞI ŞEHİR"))
ev.append((0.32, 3.3, "KutuVurgu", r"{\an5\pos(540,325)\frz-3\fad(0,90)" + POP + r"}BORCUYLA GELDİ"))
# bölüm etiketi: P03 boyunca, küçük kutu (yakın planda yüzü kapatmasın diye başlık yok)
ev.append((starts["P03"] + 0.15, starts["P03"] + 3.1, "KutuVurguKucuk", r"{\an5\pos(540,150)\frz-2\fad(0,140)" + POP + r"}SIFIR ŞEHİR · BÖLÜM 2"))
# keçinin adı
if "P11" in starts: ev.append((starts["P11"] + 0.35, starts["P11"] + 3.15, "KutuVurgu", r"{\an5\pos(540,420)\frz-3\fad(0,120)" + POP + r"}MUHTAR"))
for a, b, m in subs: ev.append((a, b, "Alt", m))
# kapanış: son kare donar, takip çağrısı (kancayla aynı dil)
ev.append((SON + 0.30, TOPLAM - 0.05, "KutuKoyu", r"{\an5\pos(540,262)\frz2\fad(0,250)" + POP + r"}DEVAMI İÇİN"))
ev.append((SON + 0.60, TOPLAM - 0.05, "KutuVurgu", r"{\an5\pos(540,408)\frz-3\fad(0,250)" + POP + r"}TAKİP ET"))
for a, b, st, m in ev: ass += f"Dialogue: 0,{t(a)},{t(b)},{st},,0,0,0,,{m}\n"
open(f"{OUT}/B02.ass", "w", encoding="utf-8").write(ass)

# ---- ffmpeg ----
inp = []; fv = []; fa = []; lv = ""; la = ""
for n, (ad, i, o, g, ss) in enumerate(EDL):
    inp += ["-i", f"{SRC}/{ad}.mp4"]
    d = o - i
    v = f"[{n}:v]trim=start={i}:end={o},setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p"
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
fv.append(f"[vc]subtitles={OUT}/B02.ass:fontsdir=/usr/share/fonts/opentype/inter[vout]")
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
cikti = f"{OUT}/B02_kurgu_{SURUM}.mp4"
run([f"[amix]volume={kazanc:.2f}dB,alimiter=limit=0.84:attack=3:release=60:level=disabled[aout]"], cikti,
    ["-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)])
e = subprocess.run(["ffmpeg", "-hide_banner", "-i", cikti, "-af", "loudnorm=print_format=summary", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
son = {k: re.search(k + r":\s+(-?[\d.]+)", e).group(1) for k in ("Input Integrated", "Input True Peak", "Input LRA")}
print(f"süre {TOPLAM:.2f} sn | ham {olc} LUFS, kazanç {kazanc:+.1f} dB | sonuç {son}")
print("klip başlangıçları:", {k: round(v, 2) for k, v in starts.items()})
