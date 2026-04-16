from utils import load_data
import matplotlib.pyplot as plt

df = load_data()

plt.figure()
df.boxplot(column="Luong", by="PhongBan")

plt.title("Boxplot lương theo phòng ban")
plt.suptitle("")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("output/boxplot_luong.png")
plt.show()