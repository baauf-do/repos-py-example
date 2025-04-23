# 📄 Passport Reader API - EASIA GREEN

Hệ thống trích xuất thông tin từ hộ chiếu (passport) từ ảnh và PDF, trả kết quả dưới dạng JSON. API có thể chạy độc lập, hỗ trợ Docker, dễ
dàng tích hợp vào ứng dụng .NET Framework 4.8 hoặc bất kỳ hệ thống backend nào.

---

## 🚀 Mục tiêu

- Tự động nhận diện và trích xuất thông tin MRZ từ ảnh hộ chiếu hoặc file PDF.
- Hỗ trợ ảnh chụp kém chất lượng.
- Có thể tích hợp vào hệ thống quản lý người dùng, nhập cảnh, CRM...
- API dễ mở rộng (auth, logging, tracking...)

---

## 🧠 Công nghệ sử dụng

| Công nghệ              | Mô tả                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------|
| Python 3.10            | Ngôn ngữ chính                                                                                                |
| FastAPI                | Xây dựng REST API                                                                                             |
| PaddleOCR              | OCR chính xác cao                                                                                             |
| YOLOv8 (Ultralytics)   | Nhận diện vùng MRZ                                                                                            |
| OpenCV                 | Xử lý ảnh                                                                                                     |
| pdf2image / PyMuPDF    | Xử lý PDF                                                                                                     |
| Docker                 | Đóng gói và triển khai API                                                                                    |
| pytest                 | Kiểm thử tự động                                                                                              |
| PyTorch                | (GPU hỗ trợ CUDA 11.8)                                                                                        |
| Albumentations         | Thư viện tăng cường dữ liệu mạnh mẽ, hỗ trợ các kỹ thuật như xoay, làm mờ, thay đổi độ sáng, thêm nhiễu, v.v. |
| imgaug                 | (tùy chọn): Thư viện tăng cường dữ liệu linh hoạt, hỗ trợ nhiều phép biến đổi ảnh.                            |
| Pillow                 | Xử lý ảnh cơ bản                                                                                              |
| opencv-python-headless | Xử lý ảnh không cần GUI, Xử lý ảnh (xoay, chỉnh sửa)                                                          |
| scikit-image           | Xử lý ảnh nâng cao                                                                                            |
| scikit-learn           | Xử lý ảnh nâng cao                                                                                            |
| numpy                  | Xử lý dữ liệu                                                                                                 |
| pandas                 | Xử lý dữ liệu                                                                                                 |
| matplotlib             | Trực quan hóa dữ liệu                                                                                         |
| torch                  | Thư viện học sâu                                                                                              |
| torchvision            | Thư viện học sâu, Hỗ trợ xử lý ảnh cho PyTorch                                                                |
| tqdm                   | Hiển thị tiến trình trong terminal                                                                            |
| faker                  | Tạo dữ liệu giả cho test, Tạo dữ liệu ngẫu nhiên (tên, ngày sinh, v.v.)                                       |
| regex                  | Xử lý chuỗi, tìm kiếm và thay thế chuỗi theo mẫu                                                              |

---

## 🔄 Flow xử lý

```text
main.py
  └── FastAPI khởi chạy app
      └── /api/extract-passport (endpoints.py)
            └── PassportService.process_passport()
                  └── extract_passport_info() từ core/reader.py
                        ├── Xử lý ảnh/pdf
                        ├── Phát hiện MRZ (YOLOv8 hoặc OCR)
                        ├── Trích xuất văn bản (PaddleOCR)
                        └── Parse thông tin MRZ (mrz_parse)
```

## 📁 Cấu trúc thư mục

```
easia-green/
├── app/                            # Ứng dụng chính
│   ├── main.py                     # Entry point khởi chạy FastAPI
│   ├── api/                        # Định nghĩa các route API
│   ├── core/                       # Xử lý OCR, MRZ, preprocess...
│   │   ├── mrz_detect.py           # Hàm chính điều phối toàn pipeline
│   │   ├── mrz_detect.py           # Dò vùng MRZ bằng YOLO hoặc OCR
│   │   ├── mrz_parse.py            # Parse MRZ text thành structured fields
│   │   ├── preprocess.py           #  xử lý ảnh: resize, contrast, làm mượt, v.v.
│   │   ├── pdf_utils.py            # chuyển PDF thành ảnh
│   │   └── utils.py                # (tuỳ chọn – validate ngày, logging, helper nhỏ)
│   ├── services/                   # Xử lý nghiệp vụ (dùng core + models)
│   │   └── passport_services.py    # Xử lý nghiệp vụ passport
│   ├── models/                     # Trained YOLOv8 models
│   │   ├── yolov8_mrz.pt           # Model YOLOv8 đã train
│   │   └── paddleocr/             # Model PaddleOCR
│   │       ├── ocr_system/         # Model OCR
│   │       ├── ocr_system.py        # Hàm chính gọi OCR
│   │       └── ocr_system_config.py # Cấu hình cho OCR
│   ├── test/                       # Unit test
│   │   ├── test_mrz_detect.py        # Test dò vùng MRZ
│   │   ├── test_mrz_parse.py         # Test parse MRZ
│   │   ├── test_preprocess.py         # Test xử lý ảnh
│   │   ├── test_pdf_utils.py          # Test chuyển PDF thành ảnh
│   │   ├── test_utils.py              # Test các hàm tiện ích
│   │   ├── test_reader.py             # Test trích xuất ảnh sang text
│   │   └── test_passport_services.py  # Test dịch vụ passport
│   ├── utils/                          # Chứa các hàm tiện ích dùng chung
│   │   ├── utils_logging.py            # Tiện ích ghi log
│   │   └── utils_valid.py              # Tiện ích validate dữ liệu
│   ├── requirements.txt            # Các thư viện phụ thuộc
│   └── Dockerfile                  # Docker hóa ứng dụng
│
├── store/                          # Lưu dữ liệu test, ảnh input/output
│   ├── input/
│   └── output/
│
├── notebooks/                      # Jupyter notebook dùng để thử nghiệm
│   └── demo_passport_reader.ipynb  # Demo cách sử dụng API
│
├── logs/                           # Lưu log hệ thống
│   └── log_YYYYMMDD.log            # Log hệ thống
│
├── train/                          # Dùng để train mô hình YOLOv8 riêng
│   ├── datasets/
│   │   ├── images/
│   │   │   ├── train/         # Ảnh huấn luyện
│   │   │   │   ├── img001.jpg
│   │   │   │   └── ...
│   │   │   └── val/           # Ảnh validation
│   │   │       └── img099.jpg
│   │   └── labels/
│   │       ├── train/         # Nhãn YOLO tương ứng
│   │       │   ├── img001.txt
│   │       │   └── ...
│   │       └── val/
│   │           └── img099.txt
│   ├── data.yaml                   # Cấu hình cho YOLO
│   └── train.py                   # Script huấn luyện
│
├── run_tests.py       # Script chạy toàn bộ test ✅
│
└── README.md



```

## 🔁 Luồng xử lý chính

```
main.py → API endpoint → services → core (detect, OCR, parse)
```

## ✅ Cách chạy test toàn bộ

```bash
python run_tests.py
```

- Script sẽ chạy tất cả các test trong `app/test/`
- Log kết quả và cảnh báo nếu thiếu file mẫu (`sample_passport.jpg`, `sample_passport.pdf`, ...)

> 📦 Đảm bảo bạn đã có các file mẫu test trong thư mục `store/input/` để tránh bị skip.

---

---

## ⚙️ Cách chạy local

```bash
cd app
python -m venv .venv
type .venv/Scripts/activate     # Windows
source .venv/bin/activate       # Unix
pip install -r requirements.txt
python main.py
```

> API sẽ chạy tại `http://localhost:8000/api/extract-passport`

---

## 🐳 Chạy với Docker

```bash
cd app
docker build -t easia-green-api .
docker run -p 8000:8000 easia-green-api
```

---

## 🧪 Gọi thử API

```bash
curl -X POST http://localhost:8000/api/extract-passport \
  -F "file=@store/input/passport.jpg"
```

Kết quả trả về dạng JSON:

```json
{
  "passport_number": "B1234567",
  "surname": "NGUYEN",
  "given_names": "VAN A",
  "nationality": "VNM",
  "date_of_birth": "1990-01-01",
  "expiration_date": "2030-01-01",
  "gender": "M"
}
```

---

## Annotate dữ liệu

Bạn cần đánh dấu vùng MRZ trong mỗi ảnh.

### Công cụ đề xuất:

- [✅ Roboflow](https://roboflow.com) – online, trực quan
- [✅ LabelImg](https://github.com/tzutalin/labelImg) – local, open-source
- [✅ Label Studio](https://labelstud.io) – tùy biến mạnh

### Format file `.txt` (YOLO format):

Mỗi file `.txt` cùng tên với ảnh `.jpg`, chứa 1 dòng: 0 0.5 0.9 0.8 0.1

> `class_id x_center y_center width height` (toàn bộ giá trị là tỷ lệ 0-1)

## 🧠 Huấn luyện lại YOLOv8 cho MRZ

1. Chuẩn bị dữ liệu:

```
train/datasets/mrz/
├── images/train, val
├── labels/train, val    # file .txt YOLO format
```

- chú thích
  - Tạo thư mục `datasets/mrz/` trong thư mục `train/`.
  - `images/train/` và `images/val/` chứa ảnh huấn luyện và validation.
  - `labels/train/` và `labels/val/` chứa nhãn tương ứng với ảnh.
  - Mỗi ảnh có 1 file nhãn `.txt` cùng tên, chứa tọa độ vùng MRZ.
  - Tạo 2 thư mục `train` và `val` trong `datasets/mrz/images/` và `datasets/mrz/labels/`.
  - Chia dữ liệu thành 2 phần: 80% cho train và 20% cho val.
  - Tạo file `mrz.yaml` trong thư mục `train/` để định nghĩa cấu hình cho YOLOv8.
  - Chạy script huấn luyện YOLOv8.
  - Sau khi huấn luyện xong, copy file mô hình tốt nhất vào thư mục `app/models/`.
  - Format file `.txt` (YOLO format):

Mỗi file `.txt` cùng tên với ảnh `.jpg`, chứa 1 dòng: 0 0.5 0.9 0.8 0.1

> `class_id x_center y_center width height` (toàn bộ giá trị là tỷ lệ 0-1)

2. File `mrz.yaml`:

```yaml
path: ./datasets/mrz
train: images/train
val: images/val
nc: 1
names: [ "mrz" ]
```

3. Huấn luyện mô hình

```bash
cd train
python train.py
```

- Hoặc dùng trực tiếp từ YOLO CLI:

```bash
cd train
yolo task=detect mode=train model=yolov8n.pt data=mrz.yaml epochs=100 imgsz=640

- hoac
yolo task=detect mode=train \
  model=yolov8n.pt \
  data=mrz.yaml \
  epochs=100 \
  imgsz=640
```

> Nếu máy mạnh hơn, bạn có thể dùng yolov8s.pt hoặc yolov8m.pt thay vì n.

4. Kết quả sau huấn luyện.
   4.1 YOLO sẽ tạo thư mục:

```bash
runs/detect/train/
├── weights/
│   └── best.pt    ✅ <-- file mô hình tốt nhất
```

4.2 Copy file .pt về app:

```bash
cp runs/detect/train/weights/best.pt ../app/models/yolov8_mrz.pt
```

4.3 Sau huấn luyện, copy model tốt nhất vào app:

```bash
cp train/runs/detect/train/weights/best.pt app/models/yolov8_mrz.pt
```

5. Kiểm tra lại pipeline

- Sau khi copy mô hình xong, chạy API hoặc test lại bằng notebook:

---

## 📌 Ghi chú

- PaddleOCR hỗ trợ tốt cả ảnh scan, ảnh bị nghiêng hoặc mờ nhẹ.
- MRZ được detect bằng PaddleOCR hoặc YOLO tùy vào cấu hình.
- Mọi xử lý ảnh, detect, trích xuất đều có thể tinh chỉnh.
- Các log xử lý được ghi tự động vào `logs/log_YYYYMMDD.log`
- Dịch vụ nghiệp vụ được xử lý ở tầng `services/` tách biệt với `core/`
- Có thể thêm auth middleware vào `api/endpoints.py`.

---

## ✅ Hướng dẫn sử dụng:

Build và chạy container:
docker compose up --build

Truy cập API tại: http://localhost:8000
Swagger UI:         http://localhost:8000/docs
Kiểm tra log:       docker logs -f easia-green-api
Kiểm tra container: docker ps

## ✨ TODO mở rộng (tuỳ chọn)

- [ ] Viết file `endpoints.py` xử lý API `/extract-passport`
- [ ] Viết `reader.py` để điều phối pipeline (load ảnh, detect MRZ, OCR, parse)
- [ ] Viết `mrz_detect.py`: PaddleOCR hoặc YOLO detect vùng MRZ
- [ ] Viết `mrz_parse.py`: tách dòng MRZ và phân tích thành thông tin structured
- [ ] Xử lý ảnh từ PDF trong `pdf_utils.py`
- [ ] Viết `Dockerfile` cho app
- [ ] Viết test mẫu cho pipeline chính
- [ ] Tối ưu hóa pipeline xử lý ảnh mờ/nghiêng
- [ ] Thêm kiểm thử đầu vào (validate file, định dạng ảnh, xử lý lỗi OCR)
- [ ] Viết thêm unit test cho `services/passport_service.py`
- [ ] Xử lý bất thường trong MRZ, fallback OCR nhiều vùng
- [ ] Tích hợp phần xác thực (auth) hoặc phân quyền
- [ ] Tách ảnh chân dung và crop vùng chữ ký
- [ ] Tự động log hệ thống và gửi lỗi ra email/Slack
- [ ] Tự động hóa đánh nhãn ảnh MRZ
- [ ] Tối ưu inference multi-GPU
- [ ] Tích hợp xác thực số hộ chiếu bằng checksum
- [ ] Export model sang ONNX để deploy cross-platform
-

---


🚀 Cách sử dụng
1. Chạy mặc định:
   ```bash
   python train/train.py
   ```
2. Chạy với thông số tùy chỉnh:
   ```bash
   python train/train.py --model yolov8s.pt --epochs 50 --imgsz 640 --batch 8 --lr 0.0005 --run_name pas
   ```





# Auth

🚀 *by Easia-Project teams!*
**baauf**

