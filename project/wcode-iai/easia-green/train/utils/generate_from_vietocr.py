# generate_from_vietocr.py
# Viết lại từ SyntheticPassportGeneration.ipynb

import os
import json
import random
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
STORE_DIR = os.path.join(ROOT, 'store', 'VietOCR')
IMG_OUT_DIR = os.path.join(STORE_DIR, 'mutated_passports')
ANNOTATION_PATH = os.path.join(STORE_DIR, 'train', 'labels.json')

os.makedirs(IMG_OUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(ANNOTATION_PATH), exist_ok=True)

# Font thử nghiệm (nếu có sẵn)
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if not os.path.exists(FONT_PATH):
  FONT_PATH = None

IMG_WIDTH, IMG_HEIGHT = 600, 400
NUM_SAMPLES = 100

images, annotations = [], []
categories = [{'id': 1, 'name': 'passportid'}]
ann_id = 1

for i in range(NUM_SAMPLES):
  img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color='white')
  draw = ImageDraw.Draw(img)

  # Vẽ các vùng giả lập thông tin hộ chiếu
  name = f'NGUYEN VAN {random.randint(1, 99)}'
  passport_id = f'B{random.randint(10000000, 99999999)}'
  mrz = f'P<VNM{name.replace(" ", "<")}<<<<<<<<<<<<\n{passport_id}<9VNM8001019M3001017<<<<<<<<<<<<<<04'

  try:
    font = ImageFont.truetype(FONT_PATH, 18) if FONT_PATH else None
  except:
    font = None

  # Ghi MRZ vào gần cuối ảnh
  x, y = 40, IMG_HEIGHT - 60
  draw.text((x, y), mrz, font=font, fill=(0, 0, 0))

  # Ghi annotation bbox
  bbox_w = 520
  bbox_h = 50
  bbox = [x, y, bbox_w, bbox_h]

  filename = f'vietocr_{i:04d}.jpg'
  img.save(os.path.join(IMG_OUT_DIR, filename))

  images.append({'id': i, 'file_name': filename, 'width': IMG_WIDTH, 'height': IMG_HEIGHT})

  annotations.append({'id': ann_id, 'image_id': i, 'category_id': 1, 'bbox': bbox, 'area': bbox_w * bbox_h, 'iscrowd': 0})
  ann_id += 1

coco = {'images': images, 'annotations': annotations, 'categories': categories}

with open(ANNOTATION_PATH, 'w', encoding='utf-8') as f:
  json.dump(coco, f, indent=2)

print(f'✅ Đã tạo {NUM_SAMPLES} ảnh từ template VietOCR → {IMG_OUT_DIR}\n📝 Annotation lưu tại {ANNOTATION_PATH}')
