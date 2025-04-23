import os
import cv2
import json
from ultralytics import YOLO
from paddleocr import PaddleOCR

# 📁 Cấu hình
MODEL_PATH = 'C:/repos/vs-code/baauf-do/repos-py-example/runs/detect/train22/weights/best.pt'
SOURCE_DIR = 'C:/repos/vs-code/baauf-do/repos-py-example/project/wcode-iai/easia-green/tests/images'
SAVE_JSON_DIR = 'C:/repos/vs-code/baauf-do/repos-py-example/project/wcode-iai/easia-green/tests/outputs/json'
os.makedirs(SAVE_JSON_DIR, exist_ok=True)

# Khởi tạo PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # nếu có tiếng Việt thì dùng lang='en' vẫn ổn vì MRZ dùng Latin

# Load model YOLO
model = YOLO(MODEL_PATH)
class_names = model.names

# Predict ảnh
results = model.predict(SOURCE_DIR, conf=0.5)

# Xử lý từng ảnh
for result in results:
  image_path = result.path
  image_name = os.path.basename(image_path)
  image = cv2.imread(image_path)
  h, w = image.shape[:2]

  info = {}
  for box in result.boxes:
    cls_id = int(box.cls[0])
    label = class_names[cls_id]

    # Tọa độ pixel
    x_center, y_center, bw, bh = box.xywh[0]
    x1 = int((x_center - bw / 2))
    y1 = int((y_center - bh / 2))
    x2 = int((x_center + bw / 2))
    y2 = int((y_center + bh / 2))

    cropped = image[y1:y2, x1:x2]
    result_ocr = ocr.ocr(cropped, cls=True)

    # Lấy kết quả OCR dòng đầu tiên (nếu có)
    text = ''
    if result_ocr and len(result_ocr[0]) > 0:
      text = result_ocr[0][0][1][0].strip()

    info[label] = text

  # Ghi ra file JSON
  json_path = os.path.join(SAVE_JSON_DIR, image_name.replace('.jpg', '.json').replace('.png', '.json'))
  with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

  print(f'✅ Trích xong: {json_path}')
