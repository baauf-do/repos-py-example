from pathlib import Path

# ✅ Danh sách nhãn đúng sau khi loại bỏ các nhãn thừa
correct_classes = [
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


# 🔍 Load file classes.txt gốc
with open('store/labels_yolo/classes.txt', encoding='utf-8') as f:
  old_classes = [line.strip() for line in f.readlines()]

# ✅ Tạo ánh xạ old_class_id → new_class_id nếu hợp lệ
class_id_map = {old_id: correct_classes.index(name) for old_id, name in enumerate(old_classes) if name in correct_classes}

print('📌 Ánh xạ class_id cũ → mới:', class_id_map)

# 📂 Thư mục chứa các file YOLO .txt cần xử lý
label_folders = [Path('train/datasets/labels/train'), Path('train/datasets/labels/val')]

for folder in label_folders:
  for txt_path in folder.glob('*.txt'):
    new_lines = []
    with open(txt_path, 'r', encoding='utf-8') as f:
      for line in f:
        parts = line.strip().split()
        if not parts or not parts[0].isdigit():
          continue

        old_class_id = int(parts[0])

        # ✅ Bỏ nếu class_id vượt giới hạn danh sách cũ
        if old_class_id >= len(old_classes):
          print(f'⚠️ Bỏ dòng lỗi: {txt_path.name} → class_id={old_class_id} vượt giới hạn')
          continue

        old_label = old_classes[old_class_id]

        # ✅ Bỏ nếu là nhãn 'passport' (không còn dùng)
        if old_label == 'passport':
          print(f"⚠️ Bỏ nhãn 'passport' trong {txt_path.name}")
          continue

        # ✅ Ghi lại nếu nhãn hợp lệ
        if old_class_id in class_id_map:
          new_class_id = class_id_map[old_class_id]
          parts[0] = str(new_class_id)
          new_lines.append(' '.join(parts))
        else:
          print(f'⚠️ Bỏ nhãn không hợp lệ: {old_label} trong {txt_path.name}')

    # ✅ Ghi đè lại file
    with open(txt_path, 'w', encoding='utf-8') as f:
      if new_lines:
        f.write('\n'.join(new_lines) + '\n')
      else:
        f.write('')  # Xóa nội dung nếu không còn nhãn hợp lệ

print("✅ Hoàn tất sửa class_id và loại bỏ nhãn 'passport'")
# ✅ Ghi lại danh sách nhãn mới vào file classes.txt
with open('store/labels_yolo/classes_new.txt', 'w', encoding='utf-8') as f:
  for class_name in correct_classes:
    f.write(class_name + '\n')
print('✅ Ghi lại danh sách nhãn mới vào file classes_new.txt')
