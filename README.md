# Chess Game Review — oyun sonrası analiz

Bitmiş bir satranç oyununun PGN'ini yapıştır; tarayıcıda çalışan Stockfish her hamleyi en iyi hamleyle karşılaştırsın,
hataları işaretlesin ve hamle başına harcanan süreyi göstersin. Sunucu yok, hesap yok: her şey tarayıcında çalışır.

*Paste the PGN of a finished game; Stockfish (running in your browser) compares every move with the engine's choice,
marks inaccuracies, mistakes and blunders, and charts the time spent per move. English below.*

> Bu araç yalnızca **bitmiş** oyunlar içindir. Süren bir oyunda motor yardımı almak chess.com dahil bütün sitelerin
> fair-play kurallarına aykırıdır; araç canlı oyunu okumaz.

## Ne yapar

- **Hamle değerlendirmesi:** en iyi / iyi / kusur (?!) / hata (?) / büyük hata (??) — kazanma şansındaki düşüşe göre (%10 / %20 / %30).
- **Motorun önerisi** tahtada yeşil okla; kayıp (piyon cinsinden) ve değerlendirme çubuğu.
- **Süre:** chess.com PGN'indeki `[%clk]` saatlerinden hamle başına harcanan süre, kalan saat ve süre grafiği.
- **Özet:** iki taraf için isabet yüzdesi, hata sayıları, ortalama kayıp, ortalama/en uzun düşünme süresi.
- **Derinlik 1–25** (yaklaşık 1000–3300 Elo; varsayılan 12 ≈ 2500), **Durdur** düğmesi.
- **Sesler** (taş, alma, şah, rok, terfi, mat) ve otomatik oynatma.
- Klavye: `←` `→` hamle, `Home` `End`, `boşluk` otomatik oynat, `F` tahtayı çevir.

## Kullanım

**Hemen kullan:** https://ckilincer.github.io/chess-game-review/ — kurulum yok.

Kendi bilgisayarında çalıştırmak istersen:

Sayfa bir Web Worker çalıştırdığı için `index.html`'e çift tıklayarak (`file://`) açılmaz; klasörü herhangi bir statik
sunucuyla servis etmek gerekir. `--directory` ile **bu klasörün yolunu** ver; vermezsen komutu hangi klasörde çalıştırdıysan onu servis eder ve sayfa açılmaz:

```
python -m http.server 8000 --directory KLASORUN_YOLU
```

sonra tarayıcıda `http://localhost:8000/` adresini aç. Durum satırı "Hazır" demiyorsa sunucu `.js` dosyalarını yanlış
türle (`text/plain`) veriyordur — Windows'ta kayıt defterindeki `.js` kaydı buna yol açabilir; o durumda başka bir statik
sunucu kullan. Sonra → **PGN yükle** → chess.com'da oyunu aç, *Paylaş → PGN → Kopyala*, yapıştır → **Analiz et**.

### PGN'i komut satırından çekmek: `pgn_cek.py`

chess.com'un herkese açık API'sinden **bitmiş** oyunları çeker (yalnızca Python 3):

```
python pgn_cek.py KULLANICI_ADI          # son oyun: ekrana yazar + panoya kopyalar
python pgn_cek.py KULLANICI_ADI -n 5     # son 5 oyun -> oyunlar.pgn
```

Ağın HTTPS'i araya girip kendi sertifikasıyla inceliyorsa (antivirüs, kurum ağı) Python'un yerine işletim sisteminin
`curl`'üne düşer; `pip install truststore` da aynı işi görür. Sertifika doğrulaması kapatılmaz.

## Dosyalar

| Dosya | Ne |
|---|---|
| `index.html` | Uygulamanın tamamı (arayüz, analiz, sesler) |
| `stockfish.js` | Stockfish 10, asm.js derlemesi (npm `stockfish.js@10.0.2`) |
| `chess.js` | Hamle kuralları ve PGN (npm `chess.js@0.10.3`) |
| `pgn_cek.py` | chess.com'dan bitmiş oyun PGN'i çekme betiği |
| `test/ekran_testi.py` | Playwright duman testi (örnek oyun, üç ekran boyutu) |

## Lisans

Bu depodaki kendi kodumuz MIT lisanslıdır (`LICENSE`). Paketlenen üçüncü taraf bileşenler kendi lisanslarıyla gelir:

- **Stockfish** — GPL-3.0-or-later, `lisanslar/stockfish-GPL-3.0.txt`. Kaynak: https://github.com/official-stockfish/Stockfish , JS derlemesi: https://github.com/nmrugg/stockfish.js
- **chess.js** — BSD-2-Clause, `lisanslar/chess.js-BSD-2-Clause.txt`. https://github.com/jhlywa/chess.js
- **Taş çizimleri** — Colin M.L. Burnett ("cburnett"), CC BY-SA 3.0; `index.html` içine gömülü (lichess/chessground kopyasından).

`stockfish.js` GPL olduğundan, bu depoyu Stockfish ile birlikte dağıtan bütün, GPL-3.0 koşullarına uymalıdır.

---

## English

**Use it online:** https://ckilincer.github.io/chess-game-review/

A single-page, serverless post-game review tool. Paste a finished game's PGN; Stockfish 10 (asm.js, in a Web Worker)
evaluates every position at a fixed depth (1–25), classifies each move by win-probability drop, shows the engine's
best move as an arrow, and charts time spent per move from chess.com `[%clk]` comments. Serve the folder with any
static server (`python -m http.server`) — opening `index.html` from disk won't start the worker.
`pgn_cek.py` downloads finished games from the chess.com public API. For finished games only; it never reads a live game.
