import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

perf_analysis = df.groupby("NghiViec")["HieuSuat"].mean()

print("\n=== HIỆU SUẤT THEO TRẠNG THÁI NGHỈ VIỆC ===")
print(perf_analysis)

plt.figure()
perf_analysis.plot(kind="bar")
plt.title("Ảnh hưởng của hiệu suất đến nghỉ việc")
plt.xlabel("Trạng thái nghỉ việc")
plt.ylabel("Hiệu suất trung bình")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/attrition_performance.png")
plt.show()