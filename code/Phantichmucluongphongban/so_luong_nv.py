import pandas as pd

df = pd.read_csv("dataset_cleaned.csv")

count = df.groupby("PhongBan")["Luong"].count()

print("\n=== SỐ LƯỢNG NHÂN VIÊN ===")
print(count)