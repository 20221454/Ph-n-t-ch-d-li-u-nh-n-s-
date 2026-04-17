import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

plt.figure()

df.boxplot(column="Luong", by="NghiViec")

plt.title("So sánh lương theo nghỉ việc")
plt.suptitle("")
plt.xlabel("Nghỉ việc")
plt.ylabel("Lương")

plt.tight_layout()
plt.savefig("output/attrition_boxplot.png")
plt.show()