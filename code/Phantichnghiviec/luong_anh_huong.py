import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

# Nhóm theo trạng thái nghỉ việc
salary_analysis = df.groupby("NghiViec")["Luong"].mean()

print("\n=== LƯƠNG TRUNG BÌNH THEO TRẠNG THÁI NGHỈ VIỆC ===")
print(salary_analysis)

plt.figure()
salary_analysis.plot(kind="bar")
plt.title("Ảnh hưởng của lương đến nghỉ việc")
plt.xlabel("Trạng thái nghỉ việc")
plt.ylabel("Lương trung bình")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/attrition_salary.png")
plt.show()