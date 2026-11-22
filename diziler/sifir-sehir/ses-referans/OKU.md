# Ses referansları ve ses sabitleme planı (22 Kasım 2026)

`selin_referans.mp3`, `riza_referans.mp3`, `naci_referans.mp3`: B01 ve B02'nin onaylı kliplerinden, yalnızca o karakterin konuştuğu aralıklar kesilip birleştirildi (her biri 23–27 sn, −18 LUFS). Kullanıcının beğendiği Veo sesleri bunlar.

## Araştırma özeti
- Veo'da ses kimliği kilitlenemiyor; ses her klipte kareden ve yazılı tariften yeniden üretiliyor. Yaygın yöntem: tarifi her promptta kelimesi kelimesine aynı yazmak (bizde zaten var).
- Flow'a "ses malzemesi" (voice ingredient) eklendiği yazılıyor; yalnızca Ultra üyelikte, hazır ses listesinden seçmeli. Kullanıcı Pro'da. Doğrulanmadı.
- Üreticilerin kullandığı kesin çözüm kurguda: konuşma sesini ElevenLabs ses değiştiricisinden (speech-to-speech, `eleven_multilingual_sts_v2`) geçirip tek sese çevirmek. Oyunculuk ve zamanlama kaynaktan kalır, tını değişir.

## Plan
1. Önlem (bedava): sabit ses tarifi her promptta aynı; duygu ayrı katmanda (kural 18).
2. Garanti (gerekirse): bu üç referanstan ElevenLabs'ta karakter başına birer ses klonu; kurguda her replik kendi karakterinin klonuna çevrilir. Önce tek klipte denenir; kullanıcı kulağıyla onaylamadan bölüme uygulanmaz.
