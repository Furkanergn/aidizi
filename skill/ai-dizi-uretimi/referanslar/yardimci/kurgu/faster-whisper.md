# faster-whisper ile replik zamanlaması
Kaynak: github.com/SYSTRAN/faster-whisper (README).

## Kurulum
```
pip install faster-whisper
```
- Python 3.9+. FFmpeg gerekmez; ses PyAV ile çözülür (PyAV FFmpeg kütüphanelerini içerir).
- GPU: CUDA 12 için cuBLAS ve cuDNN 9 gerekir (güncel ctranslate2 yalnızca CUDA 12 + cuDNN 9 destekler).
- CPU: `device="cpu", compute_type="int8"`.
- Modeller ilk çalıştırmada Hugging Face'ten indirilir. **Claude'un bulut ortamında huggingface.co engelli olabilir.** Bu durumda:
  - script kullanıcının PC'sinde çalıştırılır, ya da
  - kullanıcı claude.ai ayarlarında huggingface.co alan adına izin verir.

## Model seçimi
- `large-v3`: en doğru, Türkçe için önerilen.
- `turbo`: hızlı, batched pipeline ile.
- `distil-large-v3`: hızlı ama İngilizce odaklı; TR için kullanma.

## Kullanım (scripts/transcribe.py)
```
python transcribe.py <video_veya_ses> --lang tr --model large-v3 --out sonuc
```
Çıktılar:
- `sonuc.json`: segment ve kelime başlangıç/bitiş saniyeleri, timeline karesi (fps ile).
- `sonuc.srt`: ham altyazı. Taslaktır; ASS stiline (KURGU_KURALLARI §4) göre yeniden satırlanır.

Önemli API notları:
- `transcribe()` bir **generator** döner; transkripsiyon ancak üzerinde dolaşıldığında çalışır (`list(segments)`).
- Kelime zamanı için `word_timestamps=True`. Segment alanları: `segment.start`, `segment.end`, `segment.text`. Kelime alanları: `word.start`, `word.end`, `word.word`.
- `vad_filter=True` sessizliği atar. Varsayılan yalnız 2 sn'den uzun sessizliği kaldırır; replik arası için `vad_parameters=dict(min_silence_duration_ms=500)`.
- Dili sabitle (`language="tr"` / `"en"`). Dil tahmini kısa kliplerde yanılabilir.

## Kurguda kullanımı
1. Her kaynak klibin (veya diyalog stem'inin) transkriptini çıkar. Replik IN/OUT'unu kaynak zamanı olarak kesme kaydına yaz.
2. Timeline zamanı = klibin kayıt başlangıcı + (kaynak saniye × fps − kaynak IN karesi).
3. Altyazı cue'ları kelime zamanlarından üretilir. Kritik replikte karede ve dudakta doğrula.
4. Senaryo metniyle karşılaştır: eksik, tekrar veya yanlış replik → QC adayı.
5. Whisper yalnızca konuşmayı bulur; kimin konuştuğunu söylemez. Konuşmacıyı görüntüden doğrula.
