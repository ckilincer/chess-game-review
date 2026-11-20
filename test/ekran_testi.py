"""
Analiz sayfasının duman testi: sayfayı yerel sunucuda açar, örnek oyunu analiz eder,
üç ekran boyutunda ekran görüntüsü alır ve sayfa hatası olmadığını doğrular.

Gerekli:  pip install playwright  &&  playwright install chromium
Çalıştır: python test/ekran_testi.py
"""
import functools
import http.server
import pathlib
import sys
import threading

from playwright.sync_api import sync_playwright

KOK = pathlib.Path(__file__).resolve().parent.parent
PORT = 8765


def sunucu():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(KOK))
    s = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


def main():
    s = sunucu()
    hata = False
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w, h, ad in [(1440, 860, "genis"), (1100, 800, "orta"), (400, 850, "telefon")]:
            pg = b.new_page(viewport={"width": w, "height": h})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(f"http://127.0.0.1:{PORT}/index.html")
            pg.wait_for_function("document.getElementById('status').textContent==='Hazır'", timeout=60000)
            pg.click("#demo")
            pg.wait_for_function("document.getElementById('status').textContent==='Analiz tamam'", timeout=180000)
            pg.click("td.m >> text=Nxf7")
            etiket = pg.inner_text("#info")
            pg.screenshot(path=str(KOK / f"test-{ad}.png"))
            ok = not errs and "Büyük hata" in etiket
            print(f"{ad:8} {'OK' if ok else 'HATA'}  {errs if errs else ''}")
            hata |= not ok
            pg.close()
        b.close()
    s.shutdown()
    sys.exit(1 if hata else 0)


if __name__ == "__main__":
    main()
