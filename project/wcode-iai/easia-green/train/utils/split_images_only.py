'''
Đây là một script hoàn chỉnh giúp bạn chia ngẫu nhiên ảnh từ train/images/train/ sang train/images/val/ theo tỷ lệ 80/20, không cần đụng đến file label nếu bạn chưa có label.
Chú ý: Script này chỉ di chuyển ảnh, không tạo nhãn cho ảnh trong thư mục val. Nếu bạn cần tạo nhãn cho ảnh trong thư mục val, bạn có thể sử dụng một script khác để làm điều đó.
'''
import os
import random
import shutil

# 📁 Thư mục chứa toàn bộ ảnh trước khi chia (ban đầu)
source_dir = 'train/images/train'

# 📁 Thư mục chứa ảnh validation sau khi chia
val_dir = 'train/images/val'
os.makedirs(val_dir, exist_ok=True)

# ✅ Tỷ lệ ảnh dùng cho val
val_ratio = 0.2  # 20%

# 📋 Lấy danh sách tất cả ảnh
image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.png'))]
random.shuffle(image_files)

# 📦 Tính số lượng ảnh cần đưa vào val
val_count = int(len(image_files) * val_ratio)
val_images = image_files[:val_count]

# 🔁 Di chuyển ảnh sang val
for img in val_images:
  src_path = os.path.join(source_dir, img)
  dest_path = os.path.join(val_dir, img)
  shutil.move(src_path, dest_path)

print(f'✅ Đã chia {val_count}/{len(image_files)} ảnh vào thư mục validation.')
print('✅ Đã chia ảnh thành công.')
