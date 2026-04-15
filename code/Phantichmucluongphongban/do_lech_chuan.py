import pandas as pd

df = pd.read_csv("dataset_cleaned.csv")

std_salary = df.groupby("PhongBan")["Luong"].std()

print("\n=== ĐỘ LỆCH CHUẨN ===")
print(std_salary)