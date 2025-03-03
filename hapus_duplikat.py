import pandas as pd

def hapus_duplikat(df, subset=None, keep='first'):
    """
    Menghapus baris duplikat dari DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame yang ingin dibersihkan dari duplikat.
    subset (list, optional): Daftar nama kolom yang digunakan untuk mendeteksi duplikat. 
                             Default None (menggunakan semua kolom).
    keep (str, optional): 
        - 'first' (default) : Menyimpan duplikat pertama yang muncul.
        - 'last' : Menyimpan duplikat terakhir yang muncul.
        - False : Menghapus semua duplikat.

    Returns:
    pd.DataFrame: DataFrame yang sudah dihapus duplikatnya.
    """
    return df.drop_duplicates(subset=subset, keep=keep)

# Contoh penggunaan:
data = {
    'Nama': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Usia': [25, 30, 25, 35, 30],
    'Kota': ['Jakarta', 'Bandung', 'Jakarta', 'Surabaya', 'Bandung']
}

df = pd.DataFrame(data)

print("DataFrame sebelum menghapus duplikat:")
print(df)

# Menghapus duplikat berdasarkan semua kolom
df_cleaned = hapus_duplikat(df)

print("\nDataFrame setelah menghapus duplikat:")
print(df_cleaned)
