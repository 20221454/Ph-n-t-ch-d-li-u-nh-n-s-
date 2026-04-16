import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv(r"D:\Quản lý nhân sự\data\dataset_cleaned.csv")
df.columns = df.columns.str.strip()

# =========================
# 2. XỬ LÝ DỮ LIỆU
# =========================

# Chuẩn hóa text
df["TrangThai"] = df["TrangThai"].str.strip()

# Tạo label
df["y"] = df["TrangThai"].map({
    "Dang lam viec": 0,
    "Da nghi viec": 1
})

# =========================
# 3. FEATURE ENGINEERING
# =========================

# Xử lý ngày
df["NgayVaoLam"] = pd.to_datetime(df["NgayVaoLam"], errors='coerce')
df["NamVaoLam"] = df["NgayVaoLam"].dt.year

# Số năm làm việc (giả sử hiện tại là 2025)
df["SoNamLamViec"] = 2025 - df["NamVaoLam"]

# Feature mới
df["TyLeThuong"] = df["Thuong"] / (df["Luong"] + 1)
df["LuongTrenNam"] = df["Luong"] / (df["ThamNien"] + 1)
df["HieuSuatTrenNam"] = df["HieuSuat"] / (df["ThamNien"] + 1)

# =========================
# 4. LOẠI BỎ CỘT KHÔNG CẦN
# =========================
drop_cols = [
    "ID", "Ten", "SoDienThoai", "Email",
    "TrangThai", "NgayVaoLam"
]

df = df.drop(columns=drop_cols, errors='ignore')

# =========================
# 5. ENCODE DỮ LIỆU
# =========================
df = pd.get_dummies(df, drop_first=True)

# =========================
# 6. TÁCH X, y
# =========================
X = df.drop("y", axis=1)
y = df["y"]

# =========================
# 7. TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 8. TRAIN MODEL (TỐI ƯU)
# =========================
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=12,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# 9. DỰ ĐOÁN (TỐI ƯU RECALL)
# =========================s
y_prob = model.predict_proba(X_test)[:, 1]

# Điều chỉnh threshold (QUAN TRỌNG)
threshold = 0.4
y_pred = (y_prob > threshold).astype(int)

# =========================
# 10. ĐÁNH GIÁ
# =========================
print("===== KẾT QUẢ =====")
print("\n📊 Độ chính xác:")
print("Accuracy =", accuracy_score(y_test, y_pred))

print("\n📋 Báo cáo chi tiết:")
print(classification_report(y_test, y_pred))

# =========================
# 11. CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
plt.imshow(cm, cmap='viridis')

for i in range(len(cm)):
    for j in range(len(cm[0])):
        plt.text(j, i, cm[i, j], ha='center', va='center')

plt.title("Confusion Matrix - Dự đoán nghỉ việc")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.tight_layout()
plt.show()

# =========================
# 12. FEATURE IMPORTANCE
# =========================
importance = pd.Series(model.feature_importances_, index=X.columns)

importance.sort_values().tail(10).plot(kind="barh")
plt.title("Top yếu tố ảnh hưởng nghỉ việc")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()