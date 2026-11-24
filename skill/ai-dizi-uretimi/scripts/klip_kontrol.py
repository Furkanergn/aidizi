#!/usr/bin/env python3
"""Klip kontrolü: kontak sayfası (2 kare/sn), konuşmanın yazıya dökümü, yarım saniyelik ses seviyesi, son kare.
Kullanım: python3 araclar/klip_kontrol.py <çıktı_klasörü> <AD=dosya.mp4> [AD=dosya.mp4 ...]
Gerekir: ffmpeg, sherpa-onnx, soundfile; model yolu SHERPA_MODEL ortam değişkeninden (sherpa-onnx-whisper-small klasörü)."""
import sys, os, subprocess, re
import numpy as np, soundfile as sf, sherpa_onnx
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
d=os.environ.get("SHERPA_MODEL","/tmp/claude-0/-home-user-aidizi/3e2bd430-f3f5-517c-86c8-dde8953d429f/scratchpad/models/sherpa-onnx-whisper-small")+"/"
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+"small-encoder.int8.onnx",decoder=d+"small-decoder.int8.onnx",tokens=d+"small-tokens.txt",language="tr",task="transcribe",num_threads=4)
def tr(a,sr):
    st=r.create_stream(); st.accept_waveform(sr,a); r.decode_stream(st); return st.result.text.strip()
for arg in sys.argv[2:]:
    n,f=arg.split("=",1)
    p=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration:stream=width,height","-of","csv=p=0",f],capture_output=True,text=True).stdout.split()
    dur=float(p[-1]); cols=8; rows=int(np.ceil(dur*2/cols))
    subprocess.run(["ffmpeg","-v","error","-y","-i",f,"-vf",f"fps=2,scale=270:480,drawtext=text='{n} %{{pts\\:hms}}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile={cols}x{rows}","-frames:v","1","-q:v","3",f"{out}/{n}_sheet.jpg"])
    subprocess.run(["ffmpeg","-v","error","-y","-sseof","-0.08","-i",f,"-frames:v","1","-update","1","-q:v","1",f"{out}/{n}_son_kare.jpg"])
    w=f"{out}/{n}.wav"; subprocess.run(["ffmpeg","-v","error","-y","-i",f,"-ac","1","-ar","16000",w])
    a,sr=sf.read(w,dtype="float32")
    e=subprocess.run(["ffmpeg","-hide_banner","-i",f,"-af","loudnorm=print_format=summary","-vn","-f","null","-"],capture_output=True,text=True).stderr
    lufs=re.search(r"Input Integrated:\s+(-?[\d.]+)",e).group(1)
    rms=[20*np.log10(np.sqrt((a[int(i*.5*sr):int((i+1)*.5*sr)]**2).mean())+1e-9) for i in range(int(dur*2))]
    print(f"== {n}: {p[0]} {dur:.2f}s {lufs} LUFS")
    print("   tümü :",tr(a,sr))
    # sessizliklere göre parçala (RMS < -40 dB)
    segs=[];s=None
    for i,v in enumerate(rms+[-99]):
        if v>-40 and s is None: s=i
        if v<=-40 and s is not None: segs.append((s*.5,i*.5)); s=None
    for s0,e0 in segs:
        if e0-s0>=0.5: print(f"   {s0:.1f}-{e0:.1f}s:",tr(a[int(max(0,s0-.2)*sr):int((e0+.2)*sr)],sr))
    print("   rms  :"," ".join(f"{v:.0f}" for v in rms))
    os.remove(w)
