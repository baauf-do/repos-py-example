# import os
import json
import cv2
from pathlib import Path
from paddleocr import PaddleOCR

# 📁 Cấu hình thư mục
IMAGE_DIR = Path('../tests/images')
JSON_DIR = IMAGE_DIR
OUTPUT_DIR = Path('../tests/outputs/extracted_json')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 🔧 Khởi tạo OCR - CPU mode (an toàn)
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)

# 📋 Các trường cần trích xuất (ưu tiên theo confidence nếu trùng)
field_order = [
  'fullname',
  'dob',
  'sex',
  'passportid',
  'passportid2',
  'nationality',
  'pob',
  'cmnd',
  'date_of_issue',
  'date_of_expiry',
  'place_of_issue',
  'mrz',
]

# 🔁 Quét từng file .json kết quả từ YOLO
for json_file in JSON_DIR.glob('*.json'):
  with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

  image_path = IMAGE_DIR / data.get('image', '')
  if not image_path.exists():
    print(f'⚠️ Ảnh không tồn tại: {image_path}')
    continue

  image = cv2.imread(str(image_path))
  if image is None:
    print(f'❌ Không đọc được ảnh: {image_path}')
    continue

  h, w = image.shape[:2]
  result_dict = {field: '' for field in field_order}

  for item in data.get('detections', []):
    label = item.get('label')
    if label not in field_order:
      continue

    x1, y1, x2, y2 = map(int, item.get('bbox', []))
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w, x2), min(h, y2)

    crop = image[y1:y2, x1:x2]
    if crop.size == 0:
      print(f'⚠️ Crop rỗng cho nhãn {label} trong {image_path.name}')
      continue

    ocr_result = ocr.ocr(crop, cls=True)
    if ocr_result and len(ocr_result[0]) > 0:
      text = ocr_result[0][0][1][0].strip()
      if not result_dict[label]:  # chỉ lấy nếu chưa có giá trị
        result_dict[label] = text

  # 💾 Ghi ra file JSON
  out_path = OUTPUT_DIR / json_file.name
  with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, indent=2, ensure_ascii=False)

  print(f'✅ Trích xuất xong: {out_path}')
