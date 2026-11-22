# Chess Game Review — proje

**Güncelleme:** 2026-11-22

## Ne bu, ne için
Bitmiş chess.com oyunlarını Stockfish ile hamle hamle inceleyen sayfa: hataları, motorun önerisini ve hamle başına harcadığın süreyi gösterir. Ayrıca chess.com'dan bitmiş oyunların PGN'ini çeken küçük bir betik (`pgn_cek.py`).

## Nasıl kurulu
Kod `D:\REPOS\Chess\oyun-analiz` klasöründe, GitHub'da `ckilincer/chess-game-review`. Açmak için adresler (SITE-PANEL'de bu projenin sekmesinin en üstünde de yazılı):
- **Herkese açık — arkadaşına gönder:** **https://ckilincer.github.io/chess-game-review/** (hesap gerekmez).
- Bu bilgisayarda: **http://127.0.0.1:7777/uygulama/chessgamereview/** — panel arka planda hep açık olduğu için ek bir şey çalıştırman gerekmez.
- claude.ai artifact'ı: https://claude.ai/artifact/SkUwCsa8b64LccaRaxw6DQ (yalnız sana açık, başkasına gönderme).

## Geliştirme planı
1. ✓ Oyun sonrası analiz sayfası (Stockfish, hata sınıflama, süre grafiği)
2. ✓ chess.com görünümlü tahta, derinlik 1–25
3. ✓ Tahta + yan analiz + sağda notasyon düzeni, hamle sesleri
4. ✓ PGN çekme betiği
5. ✓ GitHub'a ilk gönderim
6. → Sesleri ve düzeni senin geri bildirimine göre ayarlama

## Şu an
- 2026-11-22: Herkese açık adres: https://ckilincer.github.io/chess-game-review/ (GitHub Pages; kullanıcının Chrome'unda örnek oyun analiz edildi).
- 2026-11-22: Sayfa artık panelden açılıyor: http://127.0.0.1:7777/uygulama/chessgamereview/ (eski `python -m http.server` tarifi sende çalışmamıştı).
- 2026-11-20: Kod GitHub'da: github.com/ckilincer/chess-game-review (herkese açık), yerel ile aynı.
- 2026-11-20: Analiz sayfası yeni düzen ve seslerle claude.ai'de yayında.

## Senin yapacakların
1. Analiz sayfasında sesleri dinleyip yeni düzenin ekranında nasıl durduğunu söyle.

## Sıradaki işler
- Değişiklikleri `revizyon.bat` ile gönder.
- Geri bildirime göre ses tınısı ve düzen ayarı.
