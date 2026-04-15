import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_cleaned.csv")

plt.figure()
plt.hist(df["Luong"], bins=20)
plt.title("Phân bố lương")
plt.xlabel("Luong")
plt.ylabel("Số lượng")
plt.tight_layout()
plt.savefig("phan_bo_luong.png")
plt.show()