import pandas as pd

def simpan_ke_excel(df_bulanan, df_kategori, df_status, output_path):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df_bulanan.to_excel(writer, sheet_name="OmzetBulanan", index=False)
        df_kategori.to_excel(writer, sheet_name="OmzetKategori", index=False)
        df_status.to_excel(writer, sheet_name="StatusPengiriman", index=False)
