#!/usr/bin/env python3
"""Kurgu QC: tekrar kare, kesme sıçraması, luma adımı, siyah/sessiz bölgeler, loudness.
Kullanım: python qc.py RENDER.mp4 [--cuts 318,605,964] [--raw-diff 5.5,2.3,...]
Sonuçlar inceleme adayıdır; karar görüntü + sesle verilir."""
import argparse, subprocess, re, numpy as np
def frames(f,w=270,h=480):
    raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-vf',f'scale={w}:{h}','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w).astype(np.float32)
def main():
    p=argparse.ArgumentParser(); p.add_argument('input'); p.add_argument('--cuts',default=''); p.add_argument('--raw-diff',default='')
    p.add_argument('--fps',type=float,default=24)
    a=p.parse_args(); v=frames(a.input); n=len(v)
    d=np.abs(np.diff(v,axis=0)).mean((1,2)); L=v.mean((1,2))
    print(f'Kare sayısı: {n}  ({n/a.fps:.2f} sn)')
    dup=[i+1 for i in range(len(d)) if d[i]<0.15 and L[i]>8]
    print('Tekrar kare adayları (siyah hariç):',dup[:40] if dup else 'yok')
    big=[(int(i)+1,round(float(d[i]),1)) for i in np.argsort(d)[::-1][:12]]
    print('En büyük kare farkları (kesme/flaş adayı):',sorted(big))
    if a.cuts:
        cuts=[int(x) for x in a.cuts.split(',')]; raw=[float(x) for x in a.raw_diff.split(',')] if a.raw_diff else [None]*len(cuts)
        print('Birleşimler: kare | fark | komşu medyan | ham | luma adımı')
        for j,r in zip(cuts,raw):
            nb=float(np.median(np.r_[d[j-6:j-2],d[j+2:j+6]]))
            flag=' <-- kontrol' if (r and d[j-1]>r*1.3+0.5) or abs(L[j]-L[j-1])>2.5 else ''
            print(f'  {j:5d} | {d[j-1]:5.2f} | {nb:5.2f} | {r if r else "-"} | {L[j-1]:.1f}->{L[j]:.1f}{flag}')
    log=subprocess.run(['ffmpeg','-hide_banner','-i',a.input,'-vf','blackdetect=d=0.08:pic_th=0.98:pix_th=0.10',
        '-af','silencedetect=noise=-50dB:d=0.5,ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    print('Siyah bölgeler:',re.findall(r'black_start:([\d.]+) black_end:([\d.]+)',log) or 'yok')
    print('Sessiz bölgeler (>0.5 sn, -50 dB):',re.findall(r'silence_start: ([\d.]+)',log)[:20] or 'yok')
    m=re.search(r'Integrated loudness:\s+I:\s+([-\d.]+) LUFS.*?LRA:\s+([-\d.]+) LU.*?True peak:\s+Peak:\s+([-\d.]+) dBFS',log,re.S)
    if m: print(f'Loudness: {m.group(1)} LUFS, LRA {m.group(2)} LU, true peak {m.group(3)} dBTP  (hedef -14 / <= -1.5)')
if __name__=='__main__': main()
