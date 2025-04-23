# synthetic_data_generator.py
import os
import json
import random
from PIL import Image, ImageDraw

# Luôn đảm bảo lưu ảnh ra đúng store/VietOCR tại gốc project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SAVE_DIR = os.path.join(ROOT_DIR, 'store', 'VietOCR')
IMAGE_DIR = os.path.join(SAVE_DIR, 'mutated_passports')
LABEL_FILE = os.path.join(SAVE_DIR, 'train', 'labels.json')

# Cấu hình dữ liệu sinh ra
NUM_SAMPLES = 100
IMAGE_SIZE = (640, 400)

# Đảm bảo thư mục tồn tại
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LABEL_FILE), exist_ok=True)

images = []
annotations = []
categories = [
  {'id': 1, 'name': 'passportid'},
]

ann_id = 1
for i in range(NUM_SAMPLES):
  img = Image.new('RGB', IMAGE_SIZE, color=(255, 255, 255))
  draw = ImageDraw.Draw(img)

  # Vẽ một vùng MRZ ngẫu nhiên ở cuối ảnh
  x = random.randint(30, 80)
  y = IMAGE_SIZE[1] - random.randint(60, 80)
  w = random.randint(400, 520)
  h = random.randint(30, 50)
  draw.rectangle([x, y, x + w, y + h], outline='black', width=2)

  filename = f'sample_{i:04d}.jpg'
  filepath = os.path.join(IMAGE_DIR, filename)
  img.save(filepath)

  images.append(
    {
      'id': i,
      'file_name': filename,
      'width': IMAGE_SIZE[0],
      'height': IMAGE_SIZE[1],
    }
  )

  annotations.append({'id': ann_id, 'image_id': i, 'category_id': 1, 'bbox': [x, y, w, h], 'area': w * h, 'iscrowd': 0})
  ann_id += 1

coco = {'images': images, 'annotations': annotations, 'categories': categories}

with open(LABEL_FILE, 'w', encoding='utf-8') as f:
  json.dump(coco, f, indent=2)

print(f'✅ Đã sinh {NUM_SAMPLES} ảnh hộ chiếu và lưu annotation tại {LABEL_FILE}')
