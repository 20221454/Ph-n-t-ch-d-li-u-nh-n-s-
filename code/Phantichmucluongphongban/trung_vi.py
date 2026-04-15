import pandas as pd

df = pd.read_csv("dataset_cleaned.csv")

median_salary = df.groupby("PhongBan")["Luong"].median()

print("\n=== TRUNG VỊ LƯƠNG ===")
print(median_salary)