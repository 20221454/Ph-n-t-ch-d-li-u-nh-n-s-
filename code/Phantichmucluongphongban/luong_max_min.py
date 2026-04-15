import pandas as pd

df = pd.read_csv("dataset_cleaned.csv")

stats = df.groupby("PhongBan")["Luong"].agg(["min", "max"])

print("\n=== LƯƠNG CAO NHẤT & THẤP NHẤT ===")
print(stats)