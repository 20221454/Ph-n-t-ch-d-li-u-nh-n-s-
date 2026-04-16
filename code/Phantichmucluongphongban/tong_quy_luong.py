from utils import load_data
import matplotlib.pyplot as plt
import os

df = load_data()

total = df.groupby("PhongBan")["Luong"].sum()

print("\n=== TỔNG QUỸ LƯƠNG ===")
print(total)

os.makedirs("output", exist_ok=True)

plt.figure()
total.plot(kind="bar")
plt.title("Tổng quỹ lương theo phòng ban")
plt.xlabel("Phòng ban")
plt.ylabel("Tổng lương")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/tong_quy_luong.png")
plt.show()