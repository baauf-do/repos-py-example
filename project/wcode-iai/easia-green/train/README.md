# 🧠 Hướng dẫn huấn luyện mô hình YOLOv8 cho nhận diện MRZ

Thư mục `train/` này chứa toàn bộ mã nguồn và dữ liệu cần thiết để huấn luyện mô hình YOLOv8 nhận diện vùng MRZ (Machine Readable Zone) từ
ảnh hộ chiếu.

---

## ✅ 1. Cấu trúc thư mục chuẩn

```
train/
├── datasets/
│   └── mrz/
│       ├── images/
│       │   ├── train/         # Ảnh huấn luyện
│       │   └── val/           # Ảnh validation
│       └── labels/
│           ├── train/         # Nhãn YOLO tương ứng
│           └── val/
├── mrz.yaml                   # Cấu hình cho YOLO
├── train.py                   # Script huấn luyện
```

---

## ✍️ 2. Annotate dữ liệu

Bạn cần đánh dấu vùng MRZ trong mỗi ảnh.

### Công cụ đề xuất:

- [✅ Roboflow](https://roboflow.com) – online, trực quan
- [✅ LabelImg](https://github.com/tzutalin/labelImg) – local, open-source
- [✅ Label Studio](https://labelstud.io) – tùy biến mạnh

### Format file `.txt` (YOLO format):

Mỗi file `.txt` cùng tên với ảnh `.jpg`, chứa 1 dòng:

```
0 0.5 0.9 0.8 0.1
```

> `class_id x_center y_center width height` (toàn bộ giá trị là tỷ lệ 0-1)

---

## 📄 3. Tạo file `mrz.yaml`

```yaml
path: ./datasets/mrz
train: images/train
val: images/val
nc: 1
names: [ "mrz" ]
```

---

## 🚀 4. Huấn luyện mô hình

```bash
cd train
python train.py
```

Hoặc dùng trực tiếp từ YOLO CLI:

```bash
yolo task=detect mode=train \
  model=yolov8n.pt \
  data=mrz.yaml \
  epochs=100 \
  imgsz=640
```

> Nếu máy mạnh hơn, bạn có thể dùng `yolov8s.pt` hoặc `yolov8m.pt` thay vì `n`.

---

## 📦 5. Kết quả sau huấn luyện

YOLO sẽ tạo thư mục:

```
runs/detect/train/
├── weights/
│   └── best.pt    ✅ <-- file mô hình tốt nhất
```

Copy file `.pt` về app:

```bash
cp runs/detect/train/weights/best.pt ../app/models/yolov8_mrz.pt
```

---

## ✅ 6. Kiểm tra lại pipeline

Sau khi copy mô hình xong, chạy API hoặc test lại bằng notebook:

```
notebooks/demo_passport_reader.ipynb
```

---

## ❗ Gợi ý mở rộng

- Dữ liệu nên bao gồm ảnh mờ, nghiêng, chất lượng thấp
- Mix dữ liệu thực tế + ảnh scan chuẩn từ ICAO
- Kiểm tra thường xuyên bằng notebook hoặc API để tránh overfitting

---

Happy training! 💪📦
