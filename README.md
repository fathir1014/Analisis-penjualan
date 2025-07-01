# 📊 Analisis Penjualan Modular – Multi-Cabang

Sistem Python modular untuk analisis penjualan dari file Excel multi-sheet (Cabang_A, Cabang_B, Cabang_C). Proyek ini menghitung omzet, merangkum data penjualan bulanan, serta menampilkan grafik batang dan pie chart untuk kebutuhan analisis bisnis secara visual.

---

## 🚀 Fitur

- 📥 Membaca file Excel dengan beberapa sheet
- 🧮 Menghitung omzet per produk, kategori, dan bulan
- 📊 Membuat visualisasi bar chart dan pie chart
- 📤 Menyimpan hasil analisis ke Excel dan PNG
- 🧩 Struktur kode modular: loader, analisis, visual, exporter, utils

---

## 📁 Struktur Folder

📂 analisis_penjualan/
├── 📂 data/
│ └── penjualan.xlsx # Input file (multi-sheet Excel)
│
├── 📂 output/
│ ├── laporan_penjualan.xlsx # Ringkasan data
│ ├── omzet_bulanan.png # Grafik omzet per bulan
│ └── status_pengiriman.png # Pie chart status pengiriman
│
├── 📂 src/
│ ├── loader.py # Load data dari Excel
│ ├── analisis.py # Hitung omzet & ringkasan
│ ├── visual.py # Grafik & visualisasi
│ ├── exporter.py # Simpan file Excel + PNG
│ ├── utils.py # Cek folder & tools tambahan
│
├── main.py # Interface CLI interaktif
└── requirements.txt


---

## ▶️ Cara Menjalankan

1. Pastikan `penjualan.xlsx` berada di folder `data/`.
2. Buka terminal di folder proyek.
3. Jalankan:

```bash
python src/main.py

🛠️ Teknologi

Python
Pandas
Matplotlib
OpenPyXL
