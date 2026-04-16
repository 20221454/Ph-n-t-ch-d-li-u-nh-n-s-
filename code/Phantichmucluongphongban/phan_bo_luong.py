from utils import load_data
import matplotlib.pyplot as plt

df = load_data()

plt.figure()
plt.hist(df["Luong"], bins=20)
plt.title("Phân bố lương nhân viên")
plt.xlabel("Lương")
plt.ylabel("Số lượng")
plt.tight_layout()
plt.savefig("output/phan_bo_luong.png")
plt.show()