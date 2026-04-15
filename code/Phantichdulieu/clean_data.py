import pandas as pd

# Đọc file
df = pd.read_csv("dataset_nhan_vien.csv")

# ========================
# 1. Xóa dữ liệu trùng
# ========================
df = df.drop_duplicates(subset="ID")

# ========================
# 2. Xử lý dữ liệu thiếu
# ========================
print(df.isnull().sum())

# Nếu có thiếu thì xử lý
df = df.dropna()

# ========================
# 3. Chuẩn hóa dữ liệu text
# ========================
df["Ten"] = df["Ten"].str.strip().str.title()
df["GioiTinh"] = df["GioiTinh"].str.strip()
df["PhongBan"] = df["PhongBan"].str.strip()

# ========================
# 4. Chuẩn hóa ngày
# ========================
df["NgayVaoLam"] = pd.to_datetime(df["NgayVaoLam"], errors='coerce')

# ========================
# 5. Lọc dữ liệu hợp lệ
# ========================
df = df[(df["HieuSuat"] >= 60) & (df["HieuSuat"] <= 100)]
df = df[df["Luong"] > 0]
df = df[df["Thuong"] >= 0]

# ========================
# 6. Tạo cột mới
# ========================
df["TongThuNhap"] = df["Luong"] + df["Thuong"]

# Thâm niên
current_year = 2026
df["ThamNien"] = current_year - df["NgayVaoLam"].dt.year

# ========================
# 7. Lưu file sạch
# ========================
df.to_csv("dataset_cleaned.csv", index=False)

print("Đã làm sạch dữ liệu xong!")