import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_cleaned.csv")

salary_stats = df.groupby("PhongBan")["Luong"].mean()

print("\n=== LƯƠNG TRUNG BÌNH ===")
print(salary_stats)

plt.figure()
salary_stats.plot(kind="bar")
plt.title("Lương trung bình theo phòng ban")
plt.xlabel("Phòng ban")
plt.ylabel("Lương")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("luong_trung_binh.png")
plt.show()