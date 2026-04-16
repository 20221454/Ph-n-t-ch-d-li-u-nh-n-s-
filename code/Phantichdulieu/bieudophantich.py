import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

df["TrangThai"] = df["TrangThai"].str.strip()

df["y"] = df["TrangThai"].map({
    "Dang lam viec": 0,
    "Da nghi viec": 1
})

# ======================
# 1. PIE CHART
# ======================
plt.figure(figsize=(5,5))
df["y"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Đang làm", "Đã nghỉ"]
)
plt.title("Tỷ lệ nghỉ việc")
plt.ylabel("")
plt.show()

# ======================
# 2. LƯƠNG VS NGHỈ VIỆC
# ======================
plt.figure()
df.groupby("TrangThai")["Luong"].mean().plot(kind="bar")
plt.title("Lương vs nghỉ việc")
plt.show()

# ======================
# 3. HIỆU SUẤT VS NGHỈ VIỆC
# ======================
plt.figure()
df.groupby("TrangThai")["HieuSuat"].mean().plot(kind="bar")
plt.title("Hiệu suất vs nghỉ việc")
plt.show()

# ======================
# 4. SCATTER
# ======================
plt.figure()

colors = df["y"].map({0: "green", 1: "red"})

plt.scatter(df["Luong"], df["HieuSuat"], c=colors)

plt.title("Lương vs Hiệu suất")
plt.xlabel("Lương")
plt.ylabel("Hiệu suất")

plt.show()