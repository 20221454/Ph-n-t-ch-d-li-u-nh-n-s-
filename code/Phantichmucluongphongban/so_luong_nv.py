from utils import load_data

df = load_data()

count = df.groupby("PhongBan")["Luong"].count()

print("\n=== SỐ LƯỢNG NHÂN VIÊN ===")
print(count)