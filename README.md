# Heart Failure Diagnosis using Logistic Regression

## Tổng quan

Dự án này áp dụng mô hình **Hồi quy Logistic** để dự đoán khả năng mắc bệnh suy tim dựa trên các chỉ số sức khỏe của bệnh nhân. Bộ dữ liệu bao gồm các thông tin như tuổi tác, mức độ cholesterol, huyết áp, loại đau ngực và kết quả ECG.

Mục tiêu của dự án là xây dựng một mô hình phân loại hiệu quả, hỗ trợ chẩn đoán bệnh suy tim với độ chính xác cao.

---

## Các đặc trưng trong dữ liệu

### Các đặc trưng số (Numerical Features):

- **Age**: Tuổi của bệnh nhân (đã chuẩn hóa).
- **RestingBP**: Huyết áp khi nghỉ ngơi (mmHg).
- **Cholesterol**: Mức cholesterol trong máu (mm/dL).
- **MaxHR**: Nhịp tim tối đa đạt được.
- **Oldpeak**: Sự thay đổi của đoạn ST sau khi tập luyện (so với lúc nghỉ).

### Các đặc trưng phân loại (Categorical Features):

- **Sex**: Giới tính của bệnh nhân (0 = Nữ, 1 = Nam).
- **ChestPainType**: Loại đau ngực:
  - ASY (Asymptomatic): Không triệu chứng.
  - ATA (Atypical Angina): Đau thắt ngực không điển hình.
  - NAP (Non-Anginal Pain): Đau không liên quan đến tim.
  - TA (Typical Angina): Đau thắt ngực điển hình.
- **RestingECG**: Kết quả điện tâm đồ khi nghỉ ngơi:
  - Normal: Bình thường.
  - ST: Bất thường sóng ST-T.
  - LVH: Tăng gánh thất trái.
- **ExerciseAngina**: Đau thắt ngực khi vận động (0 = Không, 1 = Có).
- **ST_Slope**: Độ dốc đoạn ST:
  - Up: Đi lên.
  - Flat: Phẳng.
  - Down: Đi xuống.

### Biến mục tiêu (Target Variable):

- **HeartDisease**: Biến phân loại nhị phân:
  - 0: Không mắc bệnh.
  - 1: Mắc bệnh.

---

## Quy trình dự án

![Workflow Diagram](/images/project_%20process.png)

### 1. **Thu thập Dữ liệu**

Bộ dữ liệu được thu thập từ các bệnh nhân đã được chẩn đoán về bệnh suy tim. Dữ liệu bao gồm các cột:

- **Age**: Tuổi tác của bệnh nhân.
- **Sex**: Giới tính của bệnh nhân (1: Nam, 0: Nữ).
- **RestingBP**: Huyết áp lúc nghỉ.
- **Cholesterol**: Mức độ cholesterol.
- **FastingBS**: Mức đường huyết khi nhịn ăn.
- **MaxHR**: Nhịp tim tối đa đạt được trong bài kiểm tra.
- **Oldpeak**: Mức độ giảm của ST segment trên ECG.
- **HeartDisease**: Nhãn mục tiêu (1: Có suy tim, 0: Không có suy tim).

### 2. **Tiền Xử Lý Dữ liệu**

Trước khi sử dụng dữ liệu để huấn luyện mô hình, các bước tiền xử lý dữ liệu bao gồm:

- **Xử lý thiếu dữ liệu**: Các giá trị thiếu được xử lý bằng cách thay thế bằng giá trị trung bình hoặc loại bỏ dòng chứa giá trị thiếu.
- **Mã hóa các biến phân loại**: Các biến phân loại như giới tính và các loại đau ngực được mã hóa thành các giá trị số để mô hình có thể sử dụng.
- **Chuẩn hóa dữ liệu**: Các đặc trưng số được chuẩn hóa để đưa về cùng một phạm vi giá trị, giúp mô hình học tốt hơn.

### 3. **Huấn luyện Mô hình**

Sau khi dữ liệu được xử lý, mô hình hồi quy logistic sẽ được huấn luyện. Các bước huấn luyện bao gồm:

- **Chia dữ liệu**: Dữ liệu được chia thành tập huấn luyện và tập kiểm tra với tỷ lệ 80% - 20%.
- **Huấn luyện mô hình**: Sử dụng thuật toán hồi quy logistic để huấn luyện mô hình trên tập huấn luyện.
- **Tinh chỉnh mô hình**: Các siêu tham số như `C`, `solver` có thể được tối ưu hóa để cải thiện hiệu suất mô hình.

### 4. **Đánh giá Mô hình**

Sau khi huấn luyện xong, mô hình được đánh giá bằng các chỉ số hiệu suất như:

- **Accuracy**: Độ chính xác của mô hình trong việc phân loại đúng các bệnh nhân có và không có suy tim.
- **Precision, Recall, F1-Score**: Các chỉ số này đo lường hiệu suất mô hình với các lớp dữ liệu không cân bằng.

### 5. **Dự đoán và Ứng dụng**

Khi mô hình đã được huấn luyện và đánh giá, mô hình có thể được sử dụng để dự đoán khả năng mắc bệnh suy tim của bệnh nhân mới dựa trên các chỉ số đầu vào. Cách sử dụng mô hình:

1. Nhập các đặc trưng như tuổi, huyết áp, cholesterol, nhịp tim tối đa,... vào mô hình.
2. Mô hình trả về xác suất bệnh nhân có suy tim hay không.
