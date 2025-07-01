from src.loader import load_data
from src.analisis import (
    tambah_kolom_omzet,
    tambah_kolom_waktu,
    ringkasan_omzet_per_bulan,
    ringkasan_omzet_per_kategori,
    ringkasan_status_pengiriman,
)
from src.visual import plot_omzet_per_bulan, plot_status_pengiriman
from src.exporter import simpan_ke_excel
from src.utils import pastikan_folder_output

def main():
    filepath = "analisis penjualan/data/penjualan.xlsx"
    df = load_data(filepath)
    df = tambah_kolom_omzet(df)
    df = tambah_kolom_waktu(df)

    df_bulanan = ringkasan_omzet_per_bulan(df)
    print(df_bulanan)
    df_kategori = ringkasan_omzet_per_kategori(df)
    df_status = ringkasan_status_pengiriman(df)

    while True:
        print("\n=== MENU INTERAKTIF ===")
        print("1. Lihat ringkasan omzet per bulan")
        print("2. Lihat ringkasan omzet per kategori")
        print("3. Lihat status pengiriman")
        print("4. Simpan semua ke Excel")
        print("5. Buat grafik dan simpan PNG")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            print("\n--- Omzet per Bulan ---")
            print(df_bulanan)
        elif pilihan == "2":
            print("\n--- Omzet per Kategori ---")
            print(df_kategori)
        elif pilihan == "3":
            print("\n--- Status Pengiriman ---")
            print(df_status)
        elif pilihan == "4":
            simpan_ke_excel(df_bulanan, df_kategori, df_status, "analisis penjualan/output/laporan_penjualan.xlsx")
            pastikan_folder_output('output')
            print("✅ File Excel berhasil disimpan di analisis penjualan/output/laporan_penjualan.xlsx")
        elif pilihan == "5":
            plot_omzet_per_bulan(df_bulanan, "analisis penjualan/output/omzet_bulanan.png")
            plot_status_pengiriman(df_status, "analisis penjualan/output/status_pengiriman.png")
            pastikan_folder_output('output')
            print("✅ Grafik berhasil disimpan di folder output/")
        elif pilihan == "6":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("⚠️ Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
