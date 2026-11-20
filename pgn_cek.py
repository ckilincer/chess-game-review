#!/usr/bin/env python3
"""
chess.com'da BİTMİŞ oyunların PGN'ini herkese açık API'den çeker.

Kullanım:
    python pgn_cek.py KULLANICI_ADI            # son oyunu ekrana yazar, panoya kopyalar
    python pgn_cek.py KULLANICI_ADI -n 5       # son 5 oyunu oyunlar.pgn dosyasına kaydeder
    python pgn_cek.py KULLANICI_ADI -n 10 -o benim.pgn

Ek kurulum gerekmez (yalnızca Python 3).
"""
import argparse
import json
import platform
import shutil
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

# Kuruluysa, Python'un işletim sisteminin sertifika deposunu kullanmasını sağlar.
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

API = "https://api.chess.com/pub/player/{user}/games/archives"
HEADERS = {"User-Agent": "pgn-cek/1.0 (oyun sonrasi analiz)"}


def _ssl_hatasi_mi(e):
    return isinstance(getattr(e, "reason", e), ssl.SSLError) or isinstance(e, ssl.SSLError)


def _curl_ile(url):
    """Windows/macOS'taki curl, işletim sisteminin sertifika deposunu kullanır.
    Antivirüs veya şirket ağı HTTPS'i araya girip incelediğinde Python'un
    kendi listesi bu sertifikayı tanımaz ama işletim sistemi tanır."""
    curl = shutil.which("curl.exe") or shutil.which("curl")
    if not curl:
        return None
    r = subprocess.run([curl, "-sS", "-f", "-A", HEADERS["User-Agent"], url],
                       capture_output=True)
    if r.returncode != 0:
        mesaj = r.stderr.decode(errors="replace").strip()
        if "404" in mesaj:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        sys.exit(f"Bağlantı kurulamadı (curl): {mesaj}")
    return json.loads(r.stdout.decode("utf-8"))


def get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError:
        raise
    except (urllib.error.URLError, ssl.SSLError) as e:
        if not _ssl_hatasi_mi(e):
            sys.exit(f"Bağlantı kurulamadı: {getattr(e, 'reason', e)}")
        sonuc = _curl_ile(url)
        if sonuc is None:
            sys.exit("SSL sertifikası doğrulanamadı ve curl bulunamadı.\n"
                     "Çözüm: komut penceresinde  pip install truststore  çalıştırıp betiği tekrar dene.")
        return sonuc


def son_oyunlar(user, adet):
    """En yeni aylık arşivden geriye doğru giderek son `adet` bitmiş oyunu döndürür."""
    try:
        arsivler = get_json(API.format(user=user.lower()))["archives"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.exit(f"'{user}' adlı kullanıcı bulunamadı.")
        raise
    oyunlar = []
    for ay_url in reversed(arsivler):
        aylik = get_json(ay_url).get("games", [])
        # aylık liste eskiden yeniye sıralı; pgn alanı olmayanları atla
        aylik = [g for g in aylik if g.get("pgn")]
        aylik.sort(key=lambda g: g.get("end_time", 0), reverse=True)
        oyunlar.extend(aylik)
        if len(oyunlar) >= adet:
            break
    return oyunlar[:adet]


def panoya_kopyala(metin):
    sistem = platform.system()
    try:
        if sistem == "Windows":
            subprocess.run("clip", input=metin.encode("utf-16le"), check=True, shell=True)
        elif sistem == "Darwin":
            subprocess.run("pbcopy", input=metin.encode(), check=True)
        else:
            subprocess.run(["xclip", "-selection", "clipboard"], input=metin.encode(), check=True)
        return True
    except Exception:
        return False


def ozet(g):
    w, b = g["white"], g["black"]
    return (f'{w["username"]} ({w.get("rating", "?")}) - {b["username"]} ({b.get("rating", "?")})'
            f'  [{g.get("time_class", "")}, {g.get("time_control", "")}]  {g.get("url", "")}')


def main():
    ap = argparse.ArgumentParser(description="chess.com bitmiş oyun PGN'lerini çeker.")
    ap.add_argument("kullanici", help="chess.com kullanıcı adı")
    ap.add_argument("-n", "--adet", type=int, default=1, help="kaç oyun çekilsin (varsayılan 1)")
    ap.add_argument("-o", "--dosya", default=None, help="kaydedilecek dosya (varsayılan: n>1 ise oyunlar.pgn)")
    a = ap.parse_args()

    oyunlar = son_oyunlar(a.kullanici, max(1, a.adet))
    if not oyunlar:
        sys.exit("Hiç bitmiş oyun bulunamadı.")

    for i, g in enumerate(oyunlar, 1):
        print(f"{i}. {ozet(g)}")

    metin = "\n\n".join(g["pgn"].strip() for g in oyunlar) + "\n"
    dosya = a.dosya or ("oyunlar.pgn" if len(oyunlar) > 1 else None)

    if dosya:
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(metin)
        print(f"\n{len(oyunlar)} oyun '{dosya}' dosyasına kaydedildi.")
    if len(oyunlar) == 1:
        print("\n" + metin)
        if panoya_kopyala(metin):
            print("PGN panoya kopyalandı; analiz sayfasındaki kutuya yapıştırabilirsin.")


if __name__ == "__main__":
    main()
