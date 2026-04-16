from utils import load_data

df = load_data()

std = df.groupby("PhongBan")["Luong"].std()

print("\n=== ĐỘ LỆCH CHUẨN ===")
print(std)