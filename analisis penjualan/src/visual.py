import matplotlib.pyplot as plt

def plot_omzet_per_bulan(df_ringkasan, output_path):
    df_ringkasan = df_ringkasan.sort_values(["Tahun", "BulanNum"])
    label = df_ringkasan["Bulan"] + " " + df_ringkasan["Tahun"].astype(str)

    plt.figure(figsize=(10, 6))
    plt.bar(label, df_ringkasan["Omzet"])
    plt.title("Omzet per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Total Omzet")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_status_pengiriman(df_status, output_path):
    plt.figure(figsize=(6, 6))
    plt.pie(df_status["Jumlah"], labels=df_status["Status"], autopct="%1.1f%%", startangle=90)
    plt.title("Status Pengiriman")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
