from utils import load_data

df = load_data()

stats = df.groupby("PhongBan")["Luong"].agg(["min", "max"])

print("\n=== LƯƠNG MIN - MAX ===")
print(stats)