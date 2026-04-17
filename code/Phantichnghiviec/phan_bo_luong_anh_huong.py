import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

# chuẩn hóa text
df["TrangThai"] = df["TrangThai"].str.strip()

# map sang số
df["TrangThai_num"] = df["TrangThai"].map({
    "Dang lam viec": 0,
    "Da nghi viec": 1
})

# bỏ dữ liệu lỗi
df = df.dropna(subset=["TrangThai_num", "Luong"])

# tách nhóm
stay = df[df["TrangThai_num"] == 0]["Luong"]
leave = df[df["TrangThai_num"] == 1]["Luong"]

print("Số đang làm:", len(stay))
print("Số đã nghỉ:", len(leave))

# BIỂU ĐỒ
plt.figure(figsize=(10,6))

plt.hist(stay, bins=20, alpha=0.6, label="Đang làm việc", color="green")
plt.hist(leave, bins=20, alpha=0.6, label="Đã nghỉ việc", color="red")

plt.title("Ảnh hưởng của phân bố lương đến nghỉ việc")
plt.xlabel("Mức lương")
plt.ylabel("Số lượng nhân viên")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()