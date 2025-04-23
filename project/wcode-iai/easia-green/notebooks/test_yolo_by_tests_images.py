from ultralytics import YOLO
import json
from pathlib import Path

# Load model đã huấn luyện
model_path = '../train/runs/passport_20250423_170321/weights/best.pt'
model = YOLO(model_path)

# Ảnh cần nhận diện
image_paths = ['../tests/images/visa-1.jpg', '../tests/images/visa-2.jpg']

# Thực hiện dự đoán
results = model(image_paths)

# Ghi kết quả ra file JSON
for result in results:
  output = {'image': Path(result.path).name, 'detections': []}

  if result.boxes:
    for box in result.boxes:
      cls_id = int(box.cls[0])
      conf = float(box.conf[0])
      label = model.names[cls_id]
      xyxy = box.xyxy[0].tolist()  # [x1, y1, x2, y2]

      output['detections'].append({'label': label, 'confidence': round(conf, 4), 'bbox': [round(coord, 2) for coord in xyxy]})
  else:
    print(f'⚠️ Không phát hiện được nhãn nào trong: {result.path}')

  # Ghi file JSON cùng tên
  json_path = Path(result.path).with_suffix('.json')
  with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
  print(f'✅ Đã ghi kết quả vào: {json_path}')
