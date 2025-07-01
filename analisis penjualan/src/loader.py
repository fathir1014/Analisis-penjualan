import pandas as pd

def load_data(filepath):
    """
    Membaca file Excel multi-sheet dan menggabungkan semua sheet jadi satu DataFrame.
    Menambahkan kolom 'Cabang' berdasarkan nama sheet.
    """
    all_sheets = pd.read_excel(filepath, sheet_name=None)
    df_list = []

    for sheet_name, df in all_sheets.items():
        df["Cabang"] = sheet_name
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df
