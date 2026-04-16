import pandas as pd

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

df["TrangThai"] = df["TrangThai"].str.strip()

df["y"] = df["TrangThai"].map({
    "Dang lam viec": 0,
    "Da nghi viec": 1
})

print("=== THỐNG KÊ DỮ LIỆU ===")
print(df.describe())

print("\n=== TỶ LỆ NGHỈ VIỆC ===")
print(df["y"].value_counts(normalize=True))

print("\n=== LƯƠNG THEO TRẠNG THÁI ===")
print(df.groupby("TrangThai")["Luong"].mean())

print("\n=== HIỆU SUẤT THEO TRẠNG THÁI ===")
print(df.groupby("TrangThai")["HieuSuat"].mean())