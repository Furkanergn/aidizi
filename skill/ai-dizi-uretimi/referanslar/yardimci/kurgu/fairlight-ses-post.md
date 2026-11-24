# Fairlight ses post akışı (DaVinci Resolve 20/21)
Kaynak: Blackmagic Design, "DaVinci Resolve 20 Fairlight Audio Post" kılavuzu (documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Fairlight-Audio-Post.pdf).
Not: Bu dosya hazırlanırken kılavuz Claude'un bulut ortamından indirilemedi; aşağıdakiler ikincil kaynaklardan ve bu projedeki denemelerden derlendi. Kullanıcı PDF'i yüklerse ilgili sayfa numaralarıyla güncellenmeli.

## İz düzeni (her bölümde aynı)
| İz | İçerik | Not |
|---|---|---|
| A1 DIA | Kaynak kliplerin sesi | Track FX: Voice Isolation (Studio), gerekirse Dialogue Leveler |
| A2 DIA-2 / ADR | Değiştirilen ya da ayrı üretilmiş replikler | |
| A3 AMB | Tek kesintisiz ambiyans yatağı | Kesmede yeniden başlatma yok |
| A4 FX/Foley | Senkron efektler | |
| A5 MUS | Müzik | Diyalog altında duck |
| A6 PRINT | Onaylı master (mix dışarıda yapıldıysa) | Bu durumda A1–A5 kapatılır |

## Araçlar
- **Voice Isolation:** konuşmayı çevredeki sesten ayırır. Yalnız Studio'da var. Track FX olarak kullanmak güvenilir (B01'de %85). İstenmeyen sesler maskeliyorsa kullan.
- **Dialogue Leveler:** yüksek repliği indirir, alçak repliği kaldırır. Free ve Studio'da var.
- Sıra: önce **clip gain** ile replikleri eşitle, sonra (gerekiyorsa) Voice Isolation, en son Leveler. İkisi de master loudness aracı değildir.
- Kesmelerde ses tıkırtısı olmaması için kısa fade/crossfade (2–10 ms ses düzeyinde; ambiyans geçişinde 0.5–1 sn).
- **Loudness:** Fairlight loudness meter'da standart seçilir (EBU R128 / BS.1770 / özel −14). Ölçüm tüm işlemlerden **sonra**, teslim edilen ana bus üzerinde yapılır. Meter sıfırlanıp tüm teslim aralığı çalınır. True peak ölçümü açılır.
- **Marker / cue:** MCP'nin uygulayamadığı Fairlight işlemi için zaman kodlu marker bırakılır (renk + not). Kullanıcı elle yapar veya onaylar.

## MCP ile yapılabilenler (bu projede doğrulandı)
- `timeline_item.set_voice_isolation_state` → kullanılabilir.
- `set_audio` Volume/Pan → **yok sayılıyor** (bilinen kısıt). Kazanç medyaya gömülür ya da dışarıda mixlenir.
- Stem almak: A1'i tek başına mov/lpcm render et.
- Master değiştirmek: media pool'da `replace_clip` → iki timeline birden güncellenir.

## Dinleme kuralı
Claude sesi duyamaz. Seviye, zarf ve LUFS ölçümleri teknik doğruluğu gösterir, estetik onayı göstermez. Sesle ilgili yorum kararı (müzik yeri, susturma, efekt, yankı) kullanıcıya A/B ön izleme olarak dinletilir; onay gelmeden uygulanmaz.
