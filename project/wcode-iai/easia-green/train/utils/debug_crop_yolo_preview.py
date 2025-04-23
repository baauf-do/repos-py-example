import os
import cv2
from ultralytics import YOLO

# Cấu hình
MODEL_PATH = 'C:/repos/vs-code/baauf-do/repos-py-example/runs/detect/train22/weights/best.pt'
SOURCE_DIR = 'C:/repos/vs-code/baauf-do/repos-py-example/project/wcode-iai/easia-green/tests/images'
SAVE_CROP_DIR = 'C:/repos/vs-code/baauf-do/repos-py-example/project/wcode-iai/easia-green/tests/outputs/crops'

os.makedirs(SAVE_CROP_DIR, exist_ok=True)

# Load YOLO model
model = YOLO(MODEL_PATH)
class_names = model.names

# Dự đoán ảnh
results = model.predict(SOURCE_DIR, conf=0.5)

# Lưu vùng crop
for result in results:
  image_path = result.path
  image_name = os.path.splitext(os.path.basename(image_path))[0]
  image = cv2.imread(image_path)
  h, w = image.shape[:2]

  for i, box in enumerate(result.boxes):
    cls_id = int(box.cls[0])
    label = class_names[cls_id]

    # Lấy toạ độ pixel từ box
    x_center, y_center, bw, bh = [float(v) for v in box.xywh[0]]
    x1 = max(int(x_center - bw / 2), 0)
    y1 = max(int(y_center - bh / 2), 0)
    x2 = min(int(x_center + bw / 2), w)
    y2 = min(int(y_center + bh / 2), h)

    # Crop và lưu thử
    cropped = image[y1:y2, x1:x2]
    out_path = os.path.join(SAVE_CROP_DIR, f'{image_name}_{label}_{i}.jpg')
    cv2.imwrite(out_path, cropped)
    print(f'✅ Đã lưu: {out_path}')
