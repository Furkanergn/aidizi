#!/bin/bash
# B01 ham birleştirme: 15 klibi sırayla, işlem yapmadan birleştirir.
# Zincirlenen kliplerin (P06b, P07) ilk karesi önceki klibin son karesiyle aynı olduğu için atılır.
# Kullanım: bash araclar/b01_ham_birlestir.sh  (depo kökünden)
set -e
D=diziler/sifir-sehir/bolumler/B01/klipler/onayli
O=diziler/sifir-sehir/bolumler/B01/cikti; mkdir -p $O
ORDER="P01 P02 P03 P04 P05 P06a P06b P07 P08 P09 P10 P11 P12 P13 P14"
IN=""; F=""; i=0; L=""
for k in $ORDER; do
  IN="$IN -i $D/$k.mp4"
  if [ "$k" = "P06b" ] || [ "$k" = "P07" ]; then
    F="$F[$i:v]trim=start_frame=1,setpts=PTS-STARTPTS,fps=24,format=yuv420p[v$i];[$i:a]atrim=start=0.0417,asetpts=PTS-STARTPTS[a$i];"
  else
    F="$F[$i:v]setpts=PTS-STARTPTS,fps=24,format=yuv420p[v$i];[$i:a]asetpts=PTS-STARTPTS[a$i];"
  fi
  L="$L[v$i][a$i]"; i=$((i+1))
done
ffmpeg -v error -y $IN -filter_complex "${F}${L}concat=n=$i:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 21 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart $O/B01_ham_birlesik.mp4
ffprobe -v error -show_entries format=duration,size -of default=nw=1 $O/B01_ham_birlesik.mp4
