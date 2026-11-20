@echo off
REM Chess Game Review - TEK SEFERLIK ilk kurulum: git deposu + GitHub deposu (public) + ilk gonderim.
REM Sonraki gonderimler: revizyon.bat
setlocal
cd /d "%~dp0"
set REPO=ckilincer/chess-game-review

if not exist .git (
  git init -b main || goto :hata
)
git add -A || goto :hata
git diff --cached --quiet || git commit -m "Chess Game Review: ilk surum (oyun sonrasi analiz + pgn_cek.py)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || goto :hata

git remote get-url origin >nul 2>&1 && goto :gonder

where gh >nul 2>&1
if %errorlevel%==0 (
  echo GitHub deposu gh ile aciliyor: %REPO%
  gh repo create %REPO% --public --source=. --remote=origin --description "Post-game chess review in the browser: Stockfish move classification and time-per-move from chess.com PGN" || goto :hata
) else (
  echo.
  echo gh bulunamadi. Tarayicida GitHub'in yeni depo sayfasi aciliyor.
  echo Ad: chess-game-review  -  Public  -  README/LICENSE EKLEME, bos birak  -  Create repository
  start "" "https://github.com/new?name=chess-game-review&visibility=public"
  echo Depoyu olusturduktan sonra bu pencereye donup bir tusa bas.
  pause >nul
  git remote add origin https://github.com/%REPO%.git || goto :hata
)

:gonder
git push -u origin main || goto :hata

for /f %%a in ('git rev-parse HEAD') do set YEREL=%%a
for /f %%a in ('git ls-remote origin refs/heads/main') do set UZAK=%%a
echo.
if "%YEREL%"=="%UZAK%" (
  echo SONUC YESIL: GitHub ile yerel ayni ^(%YEREL:~0,7%^). https://github.com/%REPO%
) else (
  echo SONUC KIRMIZI: uzak=%UZAK% yerel=%YEREL%
)
exit /b 0

:hata
echo.
echo SONUC KIRMIZI: bir adim basarisiz oldu, yukaridaki mesaja bak.
exit /b 1
