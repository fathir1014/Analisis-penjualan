import pandas as pd

def tambah_kolom_omzet(df):
    df["Omzet"] = df["Harga"] * df["Jumlah"]
    return df

def tambah_kolom_waktu(df):
    df["Tanggal"] = pd.to_datetime(df["Tanggal"])
    df["Bulan"] = df["Tanggal"].dt.strftime("%B")
    df["BulanNum"] = df["Tanggal"].dt.month
    df["Tahun"] = df["Tanggal"].dt.year
    return df

def ringkasan_omzet_per_bulan(df):
    return df.groupby(["Tahun", "Bulan", "BulanNum"])["Omzet"].sum().reset_index()

def ringkasan_omzet_per_kategori(df):
    return df.groupby("Kategori")["Omzet"].sum().reset_index()

def ringkasan_status_pengiriman(df):
    return df.groupby("Status").size().reset_index(name="Jumlah")
