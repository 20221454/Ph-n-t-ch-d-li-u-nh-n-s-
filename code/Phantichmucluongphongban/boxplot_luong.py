import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_cleaned.csv")

plt.figure()
df.boxplot(column="Luong", by="PhongBan")
plt.title("Boxplot lương theo phòng ban")
plt.suptitle("")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("boxplot_luong.png")
plt.show()
