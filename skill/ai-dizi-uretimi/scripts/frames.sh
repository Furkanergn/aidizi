#!/usr/bin/env bash
# Kesme/an çevresi kare şeridi: frames.sh VIDEO KARE [YARIÇAP=3] [ÇIKTI]
# Örnek: frames.sh bolum.mp4 1131 4 kesme_1131.jpg  -> 1127..1135 yan yana, kare numaralı
V=$1; N=$2; R=${3:-3}; O=${4:-kare_${N}.jpg}; A=$((N-R)); B=$((N+R)); C=$((2*R+1))
ffmpeg -v error -y -i "$V" -vf "select=between(n\,$A\,$B),scale=240:-1,drawtext=text='%{eif\:n+$A\:d}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=${C}x1" -vsync 0 -frames:v 1 "$O" && echo "$O"
