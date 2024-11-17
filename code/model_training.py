from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from data_preprocessing import df
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

X = df.drop(columns=['HeartDisease'])
y = df['HeartDisease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Huấn luyện mô hình
logreg = LogisticRegression(class_weight='balanced')
logreg.fit(X_train, y_train)
y_pred_logreg = logreg.predict(X_test)
print(X_train)
print("Weights (w):", logreg.coef_)
print("Bias (w0):", logreg.intercept_)

# Đánh giá hiệu suất
print("Accuracy:", accuracy_score(y_test, y_pred_logreg))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_logreg))
print("Classification Report:\n", classification_report(y_test, y_pred_logreg))

# Lưu mô hình
joblib.dump(logreg, 'D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\logistic_regression_model.pkl')
joblib.dump(scaler, 'D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\scaler.pkl')

chest_pain_categories = ["ASY", "ATA", "NAP", "TA"]
resting_ecg_categories = ["LVH", "Normal", "ST"]
exercise_angina_categories = ["Y", "N"]
st_slope_categories = ["Down", "Flat", "Up"]

# Lưu vào file
joblib.dump(
    [chest_pain_categories, resting_ecg_categories, exercise_angina_categories, st_slope_categories],
    'D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\models\\categories.pkl'
)
