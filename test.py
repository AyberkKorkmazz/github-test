"""
📓 Basit Not Defteri Uygulaması
Notları ekle, listele, sil ve ara!
"""

import json
import os
from datetime import datetime


DOSYA = "notlar.json"


def notlari_yukle():
    """Notları dosyadan yükle."""
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def notlari_kaydet(notlar):
    """Notları dosyaya kaydet."""
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(notlar, f, ensure_ascii=False, indent=2)


def not_ekle(notlar, baslik, icerik):
    """Yeni bir not ekle."""
    not_item = {
        "id": len(notlar) + 1,
        "baslik": baslik,
        "icerik": icerik,
        "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notlar.append(not_item)
    notlari_kaydet(notlar)
    print(f"✅ Not eklendi: '{baslik}'")


def notlari_listele(notlar):
    """Tüm notları listele."""
    if not notlar:
        print("📭 Henüz hiç not yok.")
        return
    print(f"\n📓 Toplam {len(notlar)} not:\n" + "-" * 40)
    for n in notlar:
        print(f"[{n['id']}] {n['baslik']} ({n['tarih']})")
        print(f"    {n['icerik'][:60]}{'...' if len(n['icerik']) > 60 else ''}")
    print("-" * 40)


def not_sil(notlar, not_id):
    """ID'ye göre not sil."""
    for i, n in enumerate(notlar):
        if n["id"] == not_id:
            silinen = notlar.pop(i)
            notlari_kaydet(notlar)
            print(f"🗑️  Not silindi: '{silinen['baslik']}'")
            return
    print(f"❌ ID {not_id} bulunamadı.")


def not_ara(notlar, arama):
    """Başlık veya içerikte arama yap."""
    sonuclar = [
        n for n in notlar
        if arama.lower() in n["baslik"].lower() or arama.lower() in n["icerik"].lower()
    ]
    if sonuclar:
        print(f"\n🔍 '{arama}' için {len(sonuclar)} sonuç bulundu:")
        for n in sonuclar:
            print(f"  [{n['id']}] {n['baslik']}: {n['icerik'][:80]}")
    else:
        print(f"🔍 '{arama}' için sonuç bulunamadı.")


def menu():
    """Ana menü."""
    notlar = notlari_yukle()

    print("\n🌟 NOT DEFTERİ UYGULAMASI")

    while True:
        print("\n1. Not ekle")
        print("2. Notları listele")
        print("3. Not sil")
        print("4. Not ara")
        print("5. Çıkış")

        secim = input("\nSeçiminiz (1-5): ").strip()

        if secim == "1":
            baslik = input("Başlık: ").strip()
            icerik = input("İçerik: ").strip()
            if baslik and icerik:
                not_ekle(notlar, baslik, icerik)
            else:
                print("❗ Başlık ve içerik boş olamaz.")

        elif secim == "2":
            notlari_listele(notlar)

        elif secim == "3":
            notlari_listele(notlar)
            try:
                not_id = int(input("Silmek istediğiniz not ID: "))
                not_sil(notlar, not_id)
            except ValueError:
                print("❗ Geçerli bir ID girin.")

        elif secim == "4":
            arama = input("Arama terimi: ").strip()
            not_ara(notlar, arama)

        elif secim == "5":
            print("👋 Görüşmek üzere!")
            break

        else:
            print("❗ Geçersiz seçim, 1-5 arası bir sayı girin.")


if __name__ == "__main__":
    # Demo: direkt bazı notlar ekleyelim
    demo_notlar = []
    not_ekle(demo_notlar, "Alışveriş Listesi", "Süt, ekmek, yumurta, peynir, domates")
    not_ekle(demo_notlar, "Proje Fikirleri", "Python ile web scraper, ML modeli denemeleri, CLI araçları")
    not_ekle(demo_notlar, "Kitap Notları", "Clean Code: Fonksiyonlar küçük olmalı, tek iş yapmalı")

    print("\n--- Demo Mod ---")
    notlari_listele(demo_notlar)
    not_ara(demo_notlar, "python")

    # Gerçek uygulamayı çalıştırmak için aşağıdaki satırın yorumunu kaldır:
    # menu()