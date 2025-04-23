from ultralytics import YOLO
import os

# Đây là một script hoàn chỉnh giúp bạn chạy YOLOv8 để dự đoán ảnh trong một thư mục và lưu kết quả vào một thư mục khác.
# Chú ý: Script này chỉ chạy dự đoán cho ảnh, không tạo nhãn cho ảnh trong thư mục test. Nếu bạn cần tạo nhãn cho ảnh trong thư mục test, bạn có thể sử dụng một script khác để làm điều đó.
# ROOT_FILE = os.path.dirname(os.path.abspath(__file__))  # Đường dẫn đến thư mục chứa script này
ROOT_PATH_PROJECT = 'C:/repos/vs-code/baauf-do/repos-py-example/project/wcode-iai/easia-green/'  # Đường dẫn đến thư mục gốc của dự án
ROOT_PATH_REPOS = 'C:/repos/vs-code/baauf-do/repos-py-example/'  # Đường dẫn đến thư mục gốc của dự án
# 📁 Đường dẫn đến mô hình đã huấn luyện
MODEL_PATH = ROOT_PATH_REPOS + 'runs/detect/train22/weights/best.pt'  # 🔁 sửa lại đúng trainXX của bạn

# 📁 Thư mục chứa ảnh test
TEST_IMAGES_DIR = ROOT_PATH_PROJECT + 'tests/images'

# 📁 Nơi YOLO lưu kết quả ảnh (tự động)
OUTPUT_DIR = ROOT_PATH_REPOS + 'runs/detect/test_batch'

# Load mô hình YOLOv8
model = YOLO(MODEL_PATH)

# Chạy predict cho cả thư mục ảnh
results = model.predict(source=TEST_IMAGES_DIR, save=True, project=OUTPUT_DIR, name='test_batch', conf=0.5)

# Hiển thị kết quả từng ảnh (tuỳ chọn)
for result in results:
  print(f'📸 Ảnh: {result.path}')
  for box in result.boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    label = model.names[cls_id]
    print(f'🔹 Class: {label} | Conf: {conf:.2f}')
  print('-----')
