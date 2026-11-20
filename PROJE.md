# Chess Game Review — proje

**Güncelleme:** 2026-11-20

## Ne bu, ne için
Bitmiş chess.com oyunlarını Stockfish ile hamle hamle inceleyen sayfa: hataları, motorun önerisini ve hamle başına harcadığın süreyi gösterir. Ayrıca chess.com'dan bitmiş oyunların PGN'ini çeken küçük bir betik (`pgn_cek.py`).

## Nasıl kurulu
Kod `D:\REPOS\Chess\oyun-analiz` klasöründe, GitHub'da `ckilincer/chess-game-review`. Kullanmak için claude.ai'deki artifact bağlantısını açman yeterli; yerelde açmak için klasörde `python -m http.server 8000` çalıştırıp `http://localhost:8000` adresine git.

## Geliştirme planı
1. ✓ Oyun sonrası analiz sayfası (Stockfish, hata sınıflama, süre grafiği)
2. ✓ chess.com görünümlü tahta, derinlik 1–25
3. ✓ Tahta + yan analiz + sağda notasyon düzeni, hamle sesleri
4. ✓ PGN çekme betiği
5. ✓ GitHub'a ilk gönderim
6. → Sesleri ve düzeni senin geri bildirimine göre ayarlama

## Şu an
- 2026-11-20: Kod GitHub'da: github.com/ckilincer/chess-game-review (herkese açık), yerel ile aynı.
- 2026-11-20: Analiz sayfası yeni düzen ve seslerle claude.ai'de yayında.

## Senin yapacakların
1. Analiz sayfasında sesleri dinleyip yeni düzenin ekranında nasıl durduğunu söyle.

## Sıradaki işler
- Değişiklikleri `revizyon.bat` ile gönder.
- Geri bildirime göre ses tınısı ve düzen ayarı.
