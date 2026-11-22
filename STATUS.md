# Chess Game Review (oyun-analiz) — durum

**Son güncelleme:** 2026-11-22 · ilk sürüm GitHub'da (`149796e`, public)

## Şu an
- Herkese açık adres: https://ckilincer.github.io/chess-game-review/ — GitHub Pages depoda zaten açıktı (`has_pages: true`); 2026-11-22 Chrome'da "Analiz tamam" ölçüldü. Paylaşılacak link budur; artifact yalnız sahibine açık.
- Açılış adresi (yerel): http://127.0.0.1:7777/uygulama/chessgamereview/ — SITE-PANEL `yerel_uygulama` rotası klasörü servis eder, `.js`'i `text/javascript` ile verir. Kullanıcının Chrome'unda denendi: motor "Hazır", örnek oyun "Analiz tamam" (2026-11-22).
- Tek sayfalık oyun sonrası analiz: `index.html` + `stockfish.js` (Stockfish 10 asm.js, Worker) + `chess.js` 0.10.3.
- Claude artifact olarak da yayında (yalnız sahibine açık): https://claude.ai/artifact/SkUwCsa8b64LccaRaxw6DQ — sürüm `1795181490-cc93`. Depodaki `index.html` ile aynı.
- `pgn_cek.py`: chess.com public API'den bitmiş oyun PGN'i; SSL hatasında Windows `curl`'üne düşer.

## Sırada
- Gönderimler `revizyon.bat` (id `chessgamereview`) ile; `ilk-kurulum.bat` bir kez çalıştı, tekrar gerekmez.
- Kullanıcıdan: yeni düzen ve seslerin gerçek ekranda/hoparlörde nasıl olduğu.

## Son oturumlar
- 2026-11-22: Kullanıcı panelde adresi bulamadı; README'deki `python -m http.server` tarifi onda çalışmadı (sebebi ölçülmedi: yanlış klasör ya da Windows'un `.js` MIME kaydı olası). Panel rotası + adres bloğu eklendi, PROJE/README düzeltildi.
- 2026-11-20 (2): Kod `D:\REPOS\Chess\oyun-analiz`'e taşındı; `ilk-kurulum.bat` ile `ckilincer/chess-game-review` (public) açıldı, `git ls-remote` = yerel `149796e` (ölçüldü). Panel kaydı `chessgamereview` eklendi. Kullanıcı betik sonundaki `pause`'dan ("press any key") rahatsız: kaldırıldı.
- 2026-11-20: Canlı hamle önerici isteği reddedildi (fair-play), yerine oyun sonrası analiz yapıldı. Sürümler: yeşil tahta + cburnett taşlar; derinlik 1–25 + Durdur; üç sütunlu düzen (tahta ekran yüksekliğinde, yanında analiz, sağda dar notasyon), oyuncu saatleri, WebAudio hamle sesleri, otomatik oynatma. Headless Chrome'da üç boyutta denendi (hata yok). Sesler dinlenemedi.
- 2026-11-20: `pgn_cek.py` kurum ağında çalışmadı: Python ve curl/schannel ikisi de UNTRUSTED_ROOT — kurum ağı chess.com'u engelleyip TLS'i kendi köküyle kesiyor (kullanıcı chess.com'a yalnız tarayıcıda VPN ile giriyor). Evde/mobil ağda denenmedi.

## Bilmeden dokunma
- Bu projede yazılan .bat'larda sonda `pause` yok: kullanıcı "press any key" istemiyor. Yalnız kullanıcı girdisi gerçekten beklenen adımda kalır.
- Canlı oyunu okuyan / süren oyunda öneri veren özellik eklenmez (fair-play). Kapsam yalnız bitmiş oyun.
- Taş CSS sınıfları `cw/cb` + `tp/tn/tb/tr/tq/tk` önekli: önek kaldırılırsa fil (`b`) ile siyah (`b`) çakışır, piyonlar fil görünür.
- Sınıflama ham cp ile değil kazanma şansı düşüşüyle: Stockfish 10 düşük derinlikte açılışta ±1 piyon dalgalanıyor, cp eşiği sahte "hata" üretiyordu.
- `index.html` `file://` ile açılmaz (Worker); yerel sunucu gerekir. Kullanıcıya verilecek adres panel rotasıdır, `python -m http.server` tarifi verilmez. Artifact sayfası dış `fetch` yapamaz → PGN elle yapıştırılır.
- Sesler sentezleniyor (chess.com ses dosyaları kullanılmaz); ~300 Hz altı vuruşlar hoparlörde duyulmaz (sure-uyarisi dersi).
- `stockfish.js` GPL-3.0: depo dağıtımı lisans dosyasıyla birlikte olmalı (`lisanslar/`).
- `pgn_cek.py` sertifika doğrulamasını kapatmaz; kapatma önerisi kabul edilmez.
