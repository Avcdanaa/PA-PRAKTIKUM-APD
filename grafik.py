import os
import matplotlib.pyplot as plt
from datetime import datetime
from utils import clear_screen
from data import produk, penjualan

def tampilkan_grafik_penjualan():
    """Menampilkan grafik batang jumlah penjualan per produk."""
    if not penjualan or all(jumlah == 0 for jumlah in penjualan.values()):
        print("\nBelum ada data penjualan untuk ditampilkan.")
        input("Tekan Enter untuk kembali...")
        return

    nama_produk = [produk[id_prod]["nama"] for id_prod in penjualan]
    jumlah_terjual = list(penjualan.values())

    plt.figure(figsize=(10, 6))
    plt.bar(nama_produk, jumlah_terjual, color='skyblue', edgecolor='black')
    plt.title("Grafik Penjualan Produk", fontsize=16)
    plt.xlabel("Produk", fontsize=12)
    plt.ylabel("Jumlah Terjual", fontsize=12)
    plt.ylim(0, max(jumlah_terjual) + 1)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    try:
        plt.show()
    except Exception:
        # Jika environment tidak mendukung GUI (headless), simpan grafik ke file
        nama_file = f"grafik_penjualan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(nama_file)
        print(f"\nTidak dapat menampilkan jendela grafik. Grafik disimpan di: {nama_file}")
        try:
            # Coba buka file otomatis di Windows
            os.startfile(nama_file)
        except Exception:
            pass
    finally:
        plt.close()