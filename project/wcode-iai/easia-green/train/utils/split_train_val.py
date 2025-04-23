'''
Chia tập train thành tập train và val
Tạo thư mục val/images và val/labels
train/images/train/: còn 80% ảnh
train/images/val/: chứa 20% ảnh
labels/train/, labels/val/ tương ứng
'''

import os
import random
import shutil

# Đường dẫn ảnh gốc (đã gán nhãn)
image_dir = "train/images/train"
label_dir = "train/labels/train"

# Thư mục val
val_image_dir = "train/images/val"
val_label_dir = "train/labels/val"
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Tỉ lệ chia val (VD: 0.2 = 20%)
val_ratio = 0.2

# Lấy danh sách file ảnh
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".png"))]
random.shuffle(image_files)

# Tính số lượng ảnh đưa vào val
val_count = int(len(image_files) * val_ratio)
val_images = image_files[:val_count]

# Thực hiện di chuyển ảnh + nhãn tương ứng
for img in val_images:
    label = img.rsplit(".", 1)[0] + ".txt"

    shutil.move(os.path.join(image_dir, img), os.path.join(val_image_dir, img))
    shutil.move(os.path.join(label_dir, label), os.path.join(val_label_dir, label))

print(f"✅ Đã chia {val_count} ảnh vào thư mục validation.")
print("✅ Đã chia ảnh thành công.")
