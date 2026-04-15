import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_cleaned.csv")

total_salary = df.groupby("PhongBan")["Luong"].sum()

print("\n=== TỔNG QUỸ LƯƠNG ===")
print(total_salary)

plt.figure()
total_salary.plot(kind="bar")
plt.title("Tổng quỹ lương theo phòng ban")
plt.xlabel("Phòng ban")
plt.ylabel("Tổng lương")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("tong_quy_luong.png")
plt.show()