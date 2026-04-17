import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

os.makedirs("output", exist_ok=True)

dept_attrition = df.groupby("PhongBan")["NghiViec"].mean()

print("\n=== TỶ LỆ NGHỈ VIỆC THEO PHÒNG BAN ===")
print(dept_attrition)

plt.figure()
dept_attrition.plot(kind="bar")
plt.title("Tỷ lệ nghỉ việc theo phòng ban")
plt.xlabel("Phòng ban")
plt.ylabel("Tỷ lệ nghỉ việc")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/attrition_department.png")
plt.show()