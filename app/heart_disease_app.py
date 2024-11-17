import joblib
import numpy as np

# Nạp mô hình và scaler
model = joblib.load('D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\logistic_regression_model.pkl')
scaler = joblib.load('D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\scaler.pkl')
categories = joblib.load('D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\categories.pkl')

chest_pain_categories, resting_ecg_categories, exercise_angina_categories, st_slope_categories = categories

# Các giá trị đầu vào tự động
age = int(input("Nhập tuổi: "))
sex = input("Nhập giới tính (1 (nam) / 0 (nữ)): ")
resting_bp = float(input("Nhập huyết áp lúc nghỉ (mmHg): "))
cholesterol = float(input("Nhập cholesterol (mg/dL): ")) 
fasting_bs =  int(input("Nhập fasting bs: "))
max_hr = float(input("Nhập nhịp tim tối đa (bpm): "))  
oldpeak = float(input("Nhập chênh lệch ST (Oldpeak): ")) 
chest_pain = input("Nhập loại đau ngực (ATA/NAP/ASY/TA): ").strip()
resting_ecg = input("Nhập điện tâm đồ (Normal/ST/LVH): ").strip()
exercise_angina = input("Đau thắt ngực khi vận động? (Y/N): ").strip().lower()
st_slope = input("Nhập độ dốc ST (Up/Flat/Down): ").strip() 

# Mã hóa các giá trị đầu vào
chest_pain_encoded = [1 if chest_pain == cp else 0 for cp in chest_pain_categories]
resting_ecg_encoded = [1 if resting_ecg == rec else 0 for rec in resting_ecg_categories]
exercise_angina_encoded = [1 if exercise_angina == ea else 0 for ea in exercise_angina_categories]
st_slope_encoded = [1 if st_slope == slope else 0 for slope in st_slope_categories]

# Kết hợp tất cả dữ liệu
input_data = [age, sex, resting_bp, cholesterol, fasting_bs, max_hr, oldpeak] + \
             chest_pain_encoded + resting_ecg_encoded + exercise_angina_encoded + st_slope_encoded

# Kiểm tra đặc trưng đầu vào
print(f"Input data features: {input_data}")

# Chuẩn hóa dữ liệu
input_data_scaled = scaler.transform([input_data])

# Dự đoán
prediction = model.predict(input_data_scaled)[0]
probability = model.predict_proba(input_data_scaled)[0][1]

# Hiển thị kết quả
if prediction == 1:
    print(f"Nguy cơ mắc bệnh tim cao! Xác suất: {probability:.2f}")
else:
    print(f"Nguy cơ mắc bệnh tim thấp! Xác suất: {probability:.2f}")