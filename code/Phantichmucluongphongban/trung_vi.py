from utils import load_data

df = load_data()

median = df.groupby("PhongBan")["Luong"].median()

print("\n=== TRUNG VỊ LƯƠNG ===")
print(median)