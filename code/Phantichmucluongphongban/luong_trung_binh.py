from utils import load_data
import matplotlib.pyplot as plt
import os

df = load_data()

salary_mean = df.groupby("PhongBan")["Luong"].mean()

print("\n=== LƯƠNG TRUNG BÌNH ===")
print(salary_mean)

os.makedirs("output", exist_ok=True)

plt.figure()
salary_mean.plot(kind="bar")
plt.title("Lương trung bình theo phòng ban")
plt.xlabel("Phòng ban")
plt.ylabel("Lương")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/luong_trung_binh.png")
plt.show()