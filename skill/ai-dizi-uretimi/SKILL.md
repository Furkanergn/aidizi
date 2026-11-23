---
name: ai-dizi-uretimi
description: AI ile üretilen dikey kısa dizi, mini dizi, Reels/TikTok/Shorts bölümü, animasyon skeç ya da karakterli seri video projelerini baştan sona yürütür - senaryo, mizansen, karakter ve ifade sayfaları, storyboard (başlangıç) karesi promptları, Veo/Flow video promptları, klip kalite kontrolü, ffmpeg kurgusu, kapak ve yayın metni. Kullanıcı "bölüm yaz", "sıradaki bölümü yap", "storyboard promptu", "video promptu", "karakter tutarlılığı", "Türkçe konuşan AI video", "Veo", "Flow", "kareden videoya", "klip kontrolü", "kurgu yap" dediğinde ya da görsel ve video üretim araçlarıyla (ChatGPT görsel, Nano Banana, Veo, Kling, Seedance) karakterli hikâye anlatan bir seri kurmak istediğinde bu skill'i MUTLAKA kullan; kullanıcı "dizi" demese bile, aynı karakterlerin birden çok klipte konuştuğu her iş buraya girer.
---

# AI dizi üretimi

Bu skill, aynı karakterlerin konuştuğu çok klipli AI video işlerini (dikey kısa dizi, skeç serisi) yürütme yöntemidir. Bir Türkçe animasyon dizisinin üç bölümünde yapılan hatalardan çıkarıldı; her kuralın yanında hangi hatayı önlediği yazar. Kuralı anlamadan uygulama: sebebi bilirsen kuralın kapsamadığı durumda da doğru kararı verirsin.

## Çalışma biçimi

- **Depo tek doğruluk kaynağıdır.** Karar, kural, senaryo, prompt, kayıt dosyada durur; sohbet geçicidir. Proje kökünde bir `CLAUDE.md` tut: durum, kilitli kararlar, kurallar. Her oturumun sonunda güncelle ve commit et.
- **Kullanıcı bir hata yakalarsa aynı turda kurala çevir.** Önce sebebi bul (çoğu zaman model değil, prompt), sonra kuralı "ne oldu, neden oldu, bundan sonra ne yapılır" biçiminde yaz. Aynı hata ikinci kez yaşanmamalı.
- **Promptları elle değil betikle üret.** Bir Python dosyasında karakter tarifleri sabit değişken, her plan bir kayıt olsun; betik klasörleri, numaralı referansları ve prompt dosyalarını yazsın. Tarif tek yerde düzelir, 14 prompt birden düzelir.
- **Kontrol etmediğin çıktıyı gösterme, duyamadığın şeyi övme.** Görüntüyü kareye dökerek, konuşmayı yazıya dökerek kontrol et. Sesi duyamazsın: tonlama, ses benzerliği ve "kulağa iyi geliyor mu" kullanıcıya sorulur ve bunu açıkça söylersin.
- **Kredi harcamadan önce fiyatı öğren ve sor.** Kullanıcı bölüm başına bir tavan vermediyse her harcama için onay al. Her üretimi kayıt dosyasına yaz: tarih, ne, model, referanslar, kredi, sonuç.
- **Yapamadığını açıkça söyle.** Bir araca erişemiyorsan (kullanıcının tarayıcısı, sınırsız üretim hakkı) nedenini ve kullanıcının ne yapabileceğini yaz, sonra erişim gerektirmeyen kısmı yap.
- **Kullanıcıya kısa ve sonuçtan başlayarak yaz.** Ne oldu, ne lazım, sıradaki adım.

## Üretim hattı

Her aşamanın bir kapısı var; kapıdan geçmeyen iş sonraki aşamaya girmez.

| # | Aşama | Kapı |
|---|---|---|
| 1 | Senaryo | Kanca, gülme anları, bitiş sorusu, üretilebilirlik (aşağıda) |
| 2 | Mizansen tablosu | Her planda kamera, kim nerede, hareket ve bakış yönü |
| 3 | Varlıklar | Karakter sayfası, ifade sayfaları, jest sayfaları, mekân plakaları |
| 4 | Başlangıç kareleri | Yüz ve kıyafet sayfayla aynı, duygu planın ilk anı, mizansene uygun |
| 5 | Video klipleri | Yazıya döküm senaryoyla aynı, eller ve nesneler sabit, kameraya bakan yok |
| 6 | Kurgu | Seviye, altyazı, ortam sesi sürekliliği |
| 7 | Yayın paketi | Kapak, metin, kapaklı sürüm |

Dosya düzeni: `diziler/<dizi>/varliklar/`, `diziler/<dizi>/bolumler/Bxx/{senaryo.md, kayit.md, kareler/SBxx/, klipler/Pxx/, cikti/}`, `diziler/<dizi>/mekan-krokisi.md`, `araclar/`.

## 1. Senaryo

- İlk 2 saniyede kanca (hareket ya da çarpıcı replik + ekran yazısı), sonda soru. "Devamı sonraki bölümde" deme; son kare donar, takip çağrısı gelir.
- Önceki bölümün verdiği sözü öde (yorumlara sorulan soru, eksik kalan cevap).
- Bölüm başına tek yeni tanışma, üç-dört tekrar eden şaka.
- Replikler gündelik konuşma ağzıyla yazılır; karakterler arasındaki ilişki (karı koca samimiyeti, hitaplar) replikte duyulur.
- Mantık denetimi: bir sayı ya da olay izleyiciyi "öyle olur mu" diye durduruyorsa tek cümlelik bir açıklama replik olarak eklenir.
- Kalite kapısı: ilk 2 saniye sessiz izleyeni durdurur mu; 10. saniyede durum anlaşılır mı; en az üç gülme anı karakterden mi geliyor; ana karakter bir karar alıyor mu; bitiş soru mu; her plan üretilebilir mi; arkadaşa gönderilecek bir an var mı.

## 2. Mizansen: önce kroki, sonra prompt

Bu aşama atlandığında kareler tek tek güzel ama birlikte anlamsız çıkar: karakterin taburesi boş kalır, kamera ters tarafa geçer, koşan karakter yanlış kenardan girer.

- Her mekân için bir kroki yaz: sabit noktalar (kim nerede durur, hangi nesne nerede), yönler, ve kodlanmış kamera konumları (C1, C2…) ile her konumun hangi referans görselle eşleştiği.
- Her bölüm için mizansen tablosu yaz: plan, kamera kodu, her karakterin yeri (kadrajda olmayanlar dâhil), arka planda kim görünüyor, hareket yönü, giriş-çıkış kenarı, bakış kenarı.
- Kadrajda olmayan karakterin yeri promptta yazılır ("kameranın arkasında") ya da arka planda küçük gösterilir. O karaktere ait yer boş bırakılmaz.
- Sahnenin ilk planı izleyicinin zaten bildiği yönden kurulur. Karakter bir yere gidiyorsa önce geldiği yerden, arkadan ve geniş gösterilir; hedefteki nesneler önceki bölümlerde durdukları yerdedir. Yüz için ters açıya ancak bundan sonra geçilir ve ters açıda sahnenin bir işareti kadrajda kalır.
- Kamera eksenin tek yanında kalır: karakterlerin sağ-sol yeri plandan plana değişmez. Hareketin ekran yönü kesmeler boyunca korunur.
- Yeni bir şey, daha önce gösterilmiş mekâna sonradan eklenmez; yeni mekâna konur.

## 3. Varlıklar (referans görseller)

- Karakter başına: tam boy karakter sayfası, en az iki ifade sayfası (biri kısık, biri güçlü duygular: kahkaha, bağırma, sitem, şok), elleri boş tam boy jest sayfası. Hayvan ve hareketli nesneler için hareket sayfası.
- Mekân başına: bir geniş plaka ve gereken ters açı. Nesneler ayrı görsellerdir ve birbirine göre ölçekli değildir; gerçek boyut her promptta sözle verilir ("ön kolu uzunluğunda").
- **Karakter tarifini yazmadan önce sayfaya bak.** Yanlış bir kelime (midi etek yerine mini) üretimi sayfadan uzaklaştırır; model yazıya uyar.
- Tarif sabit bloktur: yaş, saç, yüz, kıyafet parçaları, ayakkabı, vücut oranı, boy farkı. "İnceltme, gençleştirme, güzelleştirme" yasağını açıkça yaz.
- Farklı kaynaklı karakterler aynı stil düzeyine çekilir: bir karakterin sayfası fazla gerçekçiyse, başka bir karakterin sayfası yalnızca stil örneği olarak eklenir ve "bu kişi görselde yer almaz" denir.
- Türetilmiş sayfalarda yüz kayabilir (daha yaşlı, daha kırışık). Yüz için asıl sayfa esas alınır; türetilmişler yalnızca ifade ve poz örneğidir.

Görsel üretimini kullanıcı başka bir araçta yapıyorsa `referanslar/gorsel-uretim-adimi.md` kalıbını kullan.

## 4. Başlangıç kareleri

- Her klip onaylı bir başlangıç karesinden üretilir; video modeline yalnızca kare ve prompt verilir.
- Kare, planın ilk anındaki duyguyu ve jesti taşır. Karede nötr duran karakter ilk saniyede coşkulu oynatılamaz.
- Aynı kare bir bölümde en çok iki klipte kullanılır; önceki bölümün kareleri yeniden kullanılmaz (aynı ana devam eden ilk plan hariç). Aksi hâlde bölümler birbirinin aynısı görünür.
- Kareyi doğrudan hedef oranda (9:16) iste; sonradan kırpmak el ve nesneleri kadraj dışına atar.
- Her kare için ayrı sohbet ve yalnızca o karenin referansları: aynı pakette başka karakterin görseli varsa model onu da kareye koyar. Görmediğimiz bir mekân için başka mekânın görselini referans verme; kopyalar.
- Bir karakterin tek başına olduğu kare video modelinin filtresine takılıyorsa (yüz, stil ya da telif benzerliği) o karakterin planlarını ikili kur; aynı isteği en çok bir kez yinele.

Kalıp: `referanslar/kare-promptu.md`.

## 5. Video promptları

Kalıp ve tam örnek: `referanslar/video-promptu.md`. Özü:

- **Dil:** prompt İngilizce, replikler tırnak içinde hedef dilde ve o dilin harfleriyle. "Native speakers, speak ONLY <dil>" ve zor kelimeler için okunuş notu yazılır. Her klibin konuşması yazıya dökülüp senaryoyla karşılaştırılır.
- **Her saniye yazılır.** Boş bırakılan süreyi model kendi doldurur: karakter yürür gider, kameraya bakar, kıyafet değişir. Replik 5 saniyeyse klip 6 saniye seçilir ve son saniyeye sessiz bir eylem yazılır.
- **Oyunculuk tarifi.** Her replik için duygu ve şiddeti, yüz, adıyla bir jest ve ses (ton, hız, yükseklik, vurgulanan kelime). "flat, calm, deadpan, makes no gestures" varsayılan olarak yazılmaz; yazarsan karakter dümdüz oynar ve bu modelin değil promptun hatasıdır.
- **Es ve tepki.** İki replik arasında yazılı bir es (elini indirir, başını çevirir, burnundan güler); son 1,5–2 saniye sözsüz bir kapanış jesti; dinleyen karakter de tepki verir. 8 saniyede en çok iki replik.
- **Eller ve nesneler.** Nesne tutmak varsayılan değildir; jest yapacak karakterin elleri boş tasarlanır, nesne başka birine ya da bir yere bırakılır. Nesne tutuluyorsa hangi elde olduğu ve plan boyunca orada kaldığı yazılır. Hareket yasaklanmaz, adıyla yazılır.
- **Sabit bölümler:** kamera (kilitli ya da bilerek tek bir hareket), başlangıç karesinin tarifi, eller ve nesneler, sesler, saniye saniye oyun, son kare, bakışlar ("kimse kameraya bakmaz"), yüz ve kıyafet sabiti, okunuş, ses katmanı ("müzik yok, altyazı yok").
- **Hareket.** Bölümün en az üçte biri bel üstü ya da boy plandır; en az iki planda karakter yer değiştirir ve başlangıç-bitiş konumu yazılır.
- **Ses iki katmandır.** Sabit katman (kimin sesi: yaş, tını) her klipte kelimesi kelimesine aynıdır; duygu her replikte ayrı yazılır. Video modelinde ses kilitlenemez; kayma duyulursa kurguda her karakterin replikleri, o karakterin beğenilen sesinden yapılmış klona ses dönüştürmeyle çevrilir. Kullanıcı tek klipte kulağıyla onaylamadan bölüme uygulanmaz.
- **İki denemede geçmeyen planı üçüncü kez üretme; yeniden tasarla** (açıyı değiştir, planı böl, hareketi kadraj dışına al ve sonucunu göster).

## 6. Klip kontrolü

Her klip için: saniyede iki kareden kontak sayfası, son kare, konuşmanın yazıya dökümü, yarım saniyelik ses seviyesi, toplam LUFS. Bakılacaklar:

- Döküm senaryoyla kelime kelime aynı mı, replik sırası doğru mu?
- Eller ve nesneler baştan sona yerinde mi; nesne belirip kayboluyor mu?
- Kameraya bakan, yürüyüp giden, kıyafeti ya da yüzü değişen var mı?
- Yanlış prompt yapıştırılmış olabilir mi (başka karakterin repliği)?
- Çözünürlük: klipler düşük çözünürlükte inmiş olabilir; yüksek olanı iste.
- Zincirleme planlarda bir klibin son karesi sonrakinin başlangıç karesidir; çıkarıp sonraki klibin klasörüne koy ve promptu kareye göre güncelle.

Küçük kusur kurguda kesilerek çözülür (replikten sonra kameraya dönen karakter); klip yeniden üretilmez.

## 7. Kurgu (ffmpeg)

- Kurgu bir betikle yapılır: klip listesi (giriş, çıkış, kazanç, altyazılar) veri olarak durur, betik her seferinde aynı sonucu üretir. Video dosyaları depoya girmez.
- Diyalog klipleri aynı seviyeye çekilir; son çıktı −15 LUFS civarı, tepe sınırlayıcıyla.
- **Ortam sesi sürekliliği:** video modeli her klibe farklı bir arka plan sesi üretir ve kesmeler duyulur. Her klibin kendi sesi replik aralıklarının dışında kısılır (konuşma kapısı), altına bölüm boyunca kesintisiz tek bir ortam yatağı konur.
- Altyazı küçük ve sade; açılış kancası ve bitiş çağrısı gösterişli ve markanın görsel diliyle. Yazılar yüzü kapatmaz.
- Farklı çözünürlükteki klipler tek boyuta ölçeklenir.
- Kapak ayrı bir betikle, dizinin bir karesi üstüne üretilir. Kapak seçtirmeyen yayın araçları için kapağı videonun ilk karesi (tek kare) yapan ikinci bir sürüm de verilir.

## 8. Teslim

Her teslimde: neyin onaylandığı, neyin kontrol edilemediği (ses), bilinen kusurlar, harcanan kredi, kullanıcının yapacağı sıradaki tek adım. Yayın metni, sabitlenecek yorum ve paylaşım adımları bir dosyada durur.

## Sık yapılan hatalar ve sebepleri

| Belirti | Sebep | Çözüm |
|---|---|---|
| Karakter dümdüz konuşuyor | Promptta "flat/calm", eller nesneye kilitli, "never loud" | Oyunculuk tarifi, serbest eller, duygu katmanı |
| Nesne havada kalıyor, büyüyüp küçülüyor | Nesneyi tutan el yazılmamış, karakter iki eliyle jest yapıyor | Nesneyi başkasına ver ya da tutan eli sabit yaz |
| Klibin sonunda karakter yürüyüp gidiyor, kameraya bakıyor | Son saniyeler yazılmamış | Her saniyeyi yaz, kapanış jesti ekle |
| Kıyafet ya da vücut sayfadan farklı | Tarif sayfaya bakılmadan yazılmış | Sayfaya bak, tarifi düzelt, oran yasağını ekle |
| Karede yanlış kişi var | Pakette başka karenin referansı var | Kare başına ayrı sohbet, yalnızca kendi referansları |
| Yeni mekân eski mekânın kopyası | Eski mekân referans verilmiş | Referanssız, yalnızca yazıdan üret |
| Bölüm öncekinin aynısı görünüyor | Kareler yeniden kullanılmış | Kare başına en çok iki klip, yeni bölümde yeni kareler |
| Sahnede kim nerede anlaşılmıyor | Mizansen tablosu yok, sahne ters açıdan açılmış | Kroki, tablo, ilk plan bilinen yönden |
| Kesmelerde arka plan sesi değişiyor | Kliplerin kendi ortam sesleri | Konuşma kapısı ve sürekli yatak |
| Yabancı aksan, yanlış okunan isim | Dil talimatı ve okunuş notu yok | Dil satırı, okunuş notu, yazıya dökerek doğrulama |
