#!/usr/bin/env python3
"""B01_paket.md dosyasını mevcut prompt dosyalarından yeniden kurar. Klasörlere dokunmaz.
Çalıştır: python3 araclar/b01_paket_md.py (depo kökünden)"""
import os
B="diziler/sifir-sehir/bolumler/B01"
PLAN=[("P01","SB01",4),("P02","SB02",4),("P03","SB03",6),("P04","SB04",4),("P05","SB05",8),("P06a","SB06",6),("P06b","P06a'nın son karesi",6),("P07","SB01",4),("P08","SB08",6),("P09","SB09",4),("P10","SB10",6),("P11","SB11",4),("P12","SB12",4),("P13","SB10",6),("P14","SB14",6)]
o=["# B01 üretim paketi — klipler","",
"Flow ayarı her klip için aynı: **kareden videoya · Veo 3.1 Lite · 9:16**. Başlangıç karesi olarak yalnızca aşağıda yazan kareyi yükle; karakter sayfası, ifade sayfası ya da plaka ekleme.","",
"| Klip | Başlangıç karesi | Süre | Durum |","|---|---|---|---|"]
def kare(k,sb):
    d=f"{B}/klipler/{k}"
    f=[x for x in os.listdir(d) if x.endswith(".jpg")] if os.path.isdir(d) else []
    return f[0] if f else None
for k,sb,s in PLAN:
    f=kare(k,sb); o.append(f"| {k} | {sb} | {s} sn | {'Hazır' if f else 'Kare bekleniyor'} |")
o.append("")
for k,sb,s in PLAN:
    f=kare(k,sb)
    o+=[f"## {k}","",f"**Başlangıç karesi:** {sb} · **Süre:** {s} sn",""]
    o+=[f"Dosya: `klipler/{k}/{f}`","",f"![{sb}](klipler/{k}/{f})",""] if f else ["Kare henüz hazır değil.",""]
    o+=["Prompt:","","```",open(f"{B}/videolar/{k}.txt",encoding="utf-8").read().strip(),"```",""]
open(f"{B}/B01_paket.md","w",encoding="utf-8").write("\n".join(o))
print("yazıldı")
