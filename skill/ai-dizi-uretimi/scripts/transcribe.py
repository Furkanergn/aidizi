#!/usr/bin/env python3
"""faster-whisper ile kelime düzeyinde replik zamanlaması.
Kullanım: python transcribe.py GİRDİ [--lang tr] [--model large-v3] [--fps 24] [--offset-frames 0] [--out sonuc]
Çıktı: sonuc.json (segment + kelime, saniye ve kare), sonuc.srt (taslak altyazı).
--offset-frames: klibin timeline'daki kayıt başlangıcı (kare) - kaynak IN karesi; timeline karesi hesaplanır.
Kurulum: pip install faster-whisper   (model ilk çalıştırmada Hugging Face'ten iner)"""
import argparse, json, sys
def tc(s):
    h=int(s//3600); m=int(s%3600//60); sec=s%60
    return f"{h:02d}:{m:02d}:{int(sec):02d},{int(round((sec-int(sec))*1000)):03d}"
def main():
    p=argparse.ArgumentParser()
    p.add_argument('input'); p.add_argument('--lang',default='tr'); p.add_argument('--model',default='large-v3')
    p.add_argument('--fps',type=float,default=24.0); p.add_argument('--offset-frames',type=int,default=0)
    p.add_argument('--device',default='auto'); p.add_argument('--out',default='transcript')
    p.add_argument('--min-silence-ms',type=int,default=500)
    a=p.parse_args()
    from faster_whisper import WhisperModel
    dev=a.device
    if dev=='auto':
        try:
            import ctranslate2; dev='cuda' if ctranslate2.get_cuda_device_count()>0 else 'cpu'
        except Exception: dev='cpu'
    model=WhisperModel(a.model,device=dev,compute_type='float16' if dev=='cuda' else 'int8')
    segs,info=model.transcribe(a.input,language=a.lang,beam_size=5,word_timestamps=True,
                               vad_filter=True,vad_parameters=dict(min_silence_duration_ms=a.min_silence_ms),
                               condition_on_previous_text=False)
    segs=list(segs)   # generator: transkripsiyon burada çalışır
    fr=lambda s: int(round(s*a.fps))+a.offset_frames
    out={'input':a.input,'language':info.language,'fps':a.fps,'offset_frames':a.offset_frames,'segments':[]}
    srt=[]
    for i,s in enumerate(segs,1):
        out['segments'].append({'start':round(s.start,3),'end':round(s.end,3),'start_frame':fr(s.start),'end_frame':fr(s.end),
            'text':s.text.strip(),'words':[{'w':w.word.strip(),'start':round(w.start,3),'end':round(w.end,3),
            'start_frame':fr(w.start),'end_frame':fr(w.end),'p':round(w.probability,3)} for w in (s.words or [])]})
        srt.append(f"{i}\n{tc(s.start)} --> {tc(s.end)}\n{s.text.strip()}\n")
    json.dump(out,open(a.out+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    open(a.out+'.srt','w',encoding='utf-8').write('\n'.join(srt))
    for s in out['segments']: print(f"[{s['start']:7.2f}-{s['end']:7.2f}] kare {s['start_frame']}-{s['end_frame']}  {s['text']}")
    low=[w for s in out['segments'] for w in s['words'] if w['p']<0.5]
    if low: print('Düşük güvenli kelimeler (karede/dudakta doğrula):',', '.join(f"{w['w']}@{w['start']}" for w in low[:30]))
if __name__=='__main__': main()
