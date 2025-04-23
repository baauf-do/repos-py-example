import os
from PIL import Image

# Đường dẫn
SOURCE_IMG_DIR = 'store/VietOCR/synthetic_passports'
ANNOTATION_FILE = 'store/VietOCR/extract/annotation.txt'
OUTPUT_IMG_DIR = 'train/images/train'
OUTPUT_LABEL_DIR = 'train/labels/train'

os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)
os.makedirs(OUTPUT_LABEL_DIR, exist_ok=True)

with open(ANNOTATION_FILE, 'r', encoding='utf-8') as f:
  lines = f.readlines()

for idx, line in enumerate(lines):
  line = line.strip()
  parts = line.split('\t')
  if len(parts) != 3:
    print(f'[Warning] Dòng {idx + 1} không hợp lệ (len={len(parts)}): {repr(line)}')
    continue  # bỏ qua dòng lỗi

  img_path, class_name, bbox = parts
  try:
    x1, y1, x2, y2 = map(int, bbox.split(','))
  except ValueError:
    print(f'[Warning] BBox lỗi tại dòng {idx + 1}: {bbox}')
    continue

  full_img_path = os.path.join('store/VietOCR', img_path)
  if not os.path.isfile(full_img_path):
    print(f'[Warning] Không tìm thấy ảnh: {full_img_path}')
    continue

  img = Image.open(full_img_path)
  w, h = img.size

  # YOLO format
  x_center = ((x1 + x2) / 2) / w
  y_center = ((y1 + y2) / 2) / h
  bbox_width = (x2 - x1) / w
  bbox_height = (y2 - y1) / h

  yolo_label = f'0 {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n'

  filename = os.path.basename(img_path)
  img.save(os.path.join(OUTPUT_IMG_DIR, filename))
  label_file = os.path.join(OUTPUT_LABEL_DIR, filename.replace('.png', '.txt'))

  with open(label_file, 'w') as out:
    out.write(yolo_label)
