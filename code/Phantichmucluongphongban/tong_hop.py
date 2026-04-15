import pandas as pd

df = pd.read_csv("dataset_cleaned.csv")


salary_stats = df.groupby("PhongBan")["Luong"].agg(
    mean="mean",
    max="max",
    min="min",
    median="median",
    std="std",
    count="count",
    sum="sum"
)

salary_stats.to_csv("salary_by_department.csv")

print("\n✅ Đã lưu file salary_by_department.csv")