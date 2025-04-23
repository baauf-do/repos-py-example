import os
# from PIL import Image

# Cấu hình layout (center_x, center_y, width, height) theo tỉ lệ ảnh
layout_classes = {
  0: (0.43, 0.23, 0.45, 0.06),  # fullname
  1: (0.32, 0.39, 0.20, 0.05),  # dob
  2: (0.32, 0.46, 0.15, 0.05),  # sex
  3: (0.76, 0.22, 0.20, 0.05),  # passportid
  4: (0.21, 0.88, 0.20, 0.05),  # passportid2 (MRZ)
  5: (0.73, 0.29, 0.20, 0.05),  # nationality
  6: (0.73, 0.36, 0.25, 0.05),  # pob
  7: (0.73, 0.46, 0.20, 0.05),  # cmnd
  8: (0.34, 0.58, 0.20, 0.05),  # date_of_issue
  9: (0.74, 0.58, 0.20, 0.05),  # date_of_expiry
  10: (0.50, 0.64, 0.60, 0.05),  # place_of_issue
  11: (0.50, 0.95, 1.00, 0.10),  # mrz
}


def auto_label(image_dir, label_dir):
  os.makedirs(label_dir, exist_ok=True)
  for img_name in os.listdir(image_dir):
    if not img_name.lower().endswith(('.jpg', '.png')):
      continue

    label_lines = []
    for class_id, (x, y, w, h) in layout_classes.items():
      line = f'{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n'
      label_lines.append(line)

    label_filename = os.path.splitext(img_name)[0] + '.txt'
    label_path = os.path.join(label_dir, label_filename)

    with open(label_path, 'w') as f:
      f.writelines(label_lines)
    print(f'✅ Gán nhãn cho: {img_name}')


# Chạy cho train và val
if __name__ == '__main__':
  auto_label('train/images/train', 'train/labels/train')
  auto_label('train/images/val', 'train/labels/val')
