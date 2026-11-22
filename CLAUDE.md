# Chess Game Review — nasıl çalışılır

## BULUT OTURUMU — KULLANICI KURALLARI (önce bunu oku)

Bulut oturumları (claude.ai/code) `D:\REPOS\CLAUDE.md`'yi KENDİLİĞİNDEN OKUMAZ; bu oturumda yalnız bu depo vardır.
Ortak kurallar için `ckilincer/repos-meta` deposunu bağla (add_repo) ve onun `CLAUDE.md`'sini oku. En sık çiğnenen
kurallar burada da yazılı:

1. **Komut = Windows PowerShell 5.1.** Kullanıcının terminali `PS C:\Users\ckilincer>`. Verilen komutta `&&`, `||`,
   `cd /d` OLMAZ (ParserError). Klasör değiştirme yerine `git -C D:\REPOS\Chess\oyun-analiz pull`; iki adım gerekiyorsa
   `A; if ($?) { B }`. (D147)
2. **Tek komut, kod bloğunda yalnız komut.** Hata çıktısı, örnek, açıklama kod bloğuna konmaz.
3. **Senden bir şey isteniyorsa cevabın ilk satırında:** "Senden istediğim: …". İş yoksa bu cümle yazılmaz.
4. **Üç yer aynı:** iş bitince GitHub `main` ve `D:\REPOS\Chess\oyun-analiz` aynı commit'te olur (gönderim `revizyon.bat`).
5. **"Devam" yeter:** önce `STATUS.md`, sonra kaldığı yerden; kullanıcıya dosya adı söyletilmez.
6. Türkçe konuş; tek yol öner (alternatif sıralama); dar tablo.
7. Yazılan `.bat`'larda sonda `pause` olmaz.

## Proje

- Durum ve kullanıcı kararları: `STATUS.md` (önce oku) · sana hitaben özet: `PROJE.md`.
- Gönderim: `revizyon.bat` (SITE-PANEL id `chessgamereview`).
- Açılış adresi: http://127.0.0.1:7777/uygulama/chessgamereview/ (SITE-PANEL rotası) ve claude.ai artifact'ı; kullanıcıya `python -m http.server` tarifi verilmez.
- Yalnız bitmiş oyun (fair-play). Depo PUBLIC: sır, kişisel veri, chess.com logosu/sesi girmez; `lisanslar/` silinmez.
