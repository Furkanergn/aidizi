# ffmpeg tarifleri (QC ve ses post)
Kaynak: FFmpeg Filters Documentation (ffmpeg.org/ffmpeg-filters.html). Seçenek adları ffmpeg 6.1 üzerinde `ffmpeg -h filter=<ad>` ile doğrulandı. Komutların hepsi örnek bir dosyada denendi.

## Teşhis (otomatik tespit = inceleme adayı, karar değil)
```bash
# Siyah kare: en az 2 kare (0.08 sn) siyah aralıklar
ffmpeg -i IN.mp4 -vf "blackdetect=d=0.08:pic_th=0.98:pix_th=0.10" -an -f null - 2>&1 | grep black_start
# Donuk kare: 2+ kare hareketsiz bölgeler (siyah, logo gibi bilinçli bölgeler de çıkar; gözle ayıkla).
# Tek tekrar kare için scripts/qc.py kullan (freezedetect tek kareyi kaçırır)
ffmpeg -i IN.mp4 -vf "freezedetect=n=0.0005:d=0.08" -an -f null - 2>&1 | grep freeze_
# Sahne değişimi skoru (beklenmeyen kesmeyi bulmak için)
ffmpeg -i IN.mp4 -vf "scdet=threshold=10" -an -f null - 2>&1 | grep lavfi.scd
# Sessizlik (replik boşlukları, kopuk ses)
ffmpeg -i IN.mp4 -af "silencedetect=noise=-45dB:d=0.4" -vn -f null - 2>&1 | grep silence_
# Loudness (EBU R128, true peak)
ffmpeg -i IN.mp4 -af "ebur128=peak=true" -vn -f null - 2>&1 | tail -14
ffmpeg -i IN.mp4 -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Integrated|True Peak|LRA"
```

## Kare çıkarma ve temas sayfası
```bash
# Belirli karenin tam görüntüsü (timeline karesi n)
ffmpeg -i IN.mp4 -vf "select=eq(n\,1131)" -vsync 0 -frames:v 1 kare_1131.png
# Kesme çevresi: n-3..n+3 yan yana
ffmpeg -i IN.mp4 -vf "select=between(n\,1128\,1134),scale=270:-1,tile=7x1" -vsync 0 -frames:v 1 kesme_1131.jpg
# 2 sn'de bir temas sayfası, zaman damgalı
ffmpeg -i IN.mp4 -vf "fps=1/2,scale=180:-1,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=9x6" -frames:v 1 temas.jpg
# Ses dalga resmi (kesme yerinde sıçrama kontrolü)
ffmpeg -ss 45 -t 6 -i IN.mp4 -filter_complex "showwavespic=s=1600x300:split_channels=1" -frames:v 1 dalga.png
```

## Ses işleme
```bash
# İki geçişli loudnorm (-14 LUFS / -1.5 dBTP). LRA hedefi girişin LRA'sından küçükse filtre "dynamic" moda düşer ve
# bilinçli sessizlikleri sıkıştırır. Çıktıdaki normalization_type mutlaka "linear" olmalı.
ffmpeg -i mix.wav -af loudnorm=I=-14:TP=-1.5:LRA=20:print_format=json -f null -          # 1. geçiş: ölç
ffmpeg -i mix.wav -af "loudnorm=I=-14:TP=-1.5:LRA=20:linear=true:measured_I=..:measured_TP=..:measured_LRA=..:measured_thresh=..:offset=..:print_format=summary" -ar 48000 -c:a pcm_s16le out.wav
# linear mümkün değilse: kazanç + 4x oversample limiter
ffmpeg -i mix.wav -af "volume=4.4dB,aresample=192000,alimiter=limit=0.83:attack=1:release=60:level=false,aresample=48000" -c:a pcm_s16le out.wav
# Müziği diyaloğa göre duck etme (sidechain): [0]=müzik [1]=diyalog
ffmpeg -i mus.wav -i dia.wav -filter_complex "[0][1]sidechaincompress=threshold=0.05:ratio=4:attack=20:release=400[d]" -map "[d]" mus_duck.wav
# Ses fade ve iki klip arası crossfade
ffmpeg -i a.wav -af "afade=t=in:st=0:d=0.5,afade=t=out:st=9.5:d=0.5" out.wav
ffmpeg -i a.wav -i b.wav -filter_complex "acrossfade=d=0.6:c1=qsin:c2=qsin" out.wav
# Hafif yankı ya da impulse response ile mekân
ffmpeg -i dia.wav -af "aecho=0.8:0.6:110:0.25" out.wav
ffmpeg -i dia.wav -i ir.wav -lavfi afir out.wav
# Uğultu/rüzgâr temizliği
ffmpeg -i dia.wav -af "highpass=f=80,lowpass=f=12000" out.wav
```

## Altyazı yakma ve teslim
```bash
ffmpeg -i nosub.mp4 -vf "ass=TR.ass:fontsdir=fonts" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -c:a copy -movflags +faststart TR.mp4
# Kare sayısı doğrulama
ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 OUT.mp4
```

## Uyarılar
- `-shortest` son kareleri kesebilir; kullanma, süreyi `-t` ya da kare sayısıyla ver.
- Etiketsiz (renk alanı unknown) kaynakları opencv ile işleyip bt709 etiketlemek renk kayması yaratır; ffmpeg ile işle, etiket ekleme.
- `xfade` (görüntü geçişi) Extend zincirinde **yasak**; yalnız ayrı sahneler arasında, kullanıcı onayıyla kullanılır.
