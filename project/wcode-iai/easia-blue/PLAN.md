## Kế hoạch phát triển dự án easia-blue

# 1. 🎯 Mục tiêu dự án

- Phát triển hệ thống backend **FastAPI**:
  - Tiếp nhận file PDF hợp đồng (text, scan, mixed).
  - Phân tích, extract dữ liệu thành JSON chuẩn hóa.
  - Đẩy dữ liệu JSON vào **SQL Server**.
  - Hỗ trợ **train YOLOv8** để detect vùng OCR cho file scan.
  - Xây dựng hệ thống dễ dàng bảo trì, mở rộng.

bây giờ tôi muốn tìm hiểu

tổng hợp giúp tôi các thư viện, models, các công cụ hỗ trợ phân tích văn bản thành các mục key-value để lưu vào json cho kiểu văn bản hợp đồng khách sạn đang sử dụng hiện nay

# 2. 🏗️ Cấu trúc tổng thể dự án

```
   easia-blue/
   │
   ├── app/
   │   ├── __init__.py
   │   ├── main.py                    # Khởi động FastAPI app
   │   │
   │   ├── api/                       # Các route API
   │   │   ├── __init__.py
   │   │   └── endpoints/
   │   │       ├── __init__.py
   │   │       ├── upload.py                        # API: upload file PDF
   │   │       ├── extract.py                       # API: extract data
   │   │       ├── extract.py                       # API: get all files in upload folder
   │   │       ├── database.py                      # API: push JSON vào SQL Server
   │   │       ├── process_pdf.py                   # API: Xử lý các file pdf
   │   │       ├── flow_upload_process_extract.py   # API: upload -> Process -> extract -> json
   │   │       └── status.py                        # API: kiểm tra server
   │   │
   │   ├── config/                   # Cấu hình hệ thống
   │   │   ├── base_settings.py    # Config chung
   │   │   ├── dev_settings.py     # Config cho development
   │   │   ├── prod_settings.py    # Config cho production
   │   │   ├── config.py             # Đọc biến môi trường từ .env
   │   │   ├── database.py           # Kết nối SQL Server
   │   │   └── __init__.py
   │   │
   │   ├── core/                     # Modular core: xử lý extract chi tiết theo text/scan/mixed – tuyệt vời
   │   │   ├── extract_text_only.py
   │   │   ├── extract_scan_only.py
   │   │   ├── extract_mixed.py
   │   │   └── __init__.py
   │   │
   │   ├── services/                 # Xử lý nghiệp vụ
   │   │   ├── __init__.py
   │   │   ├── pdf_processor.py      # Chuyển PDF thành ảnh
   │   │   ├── yolo_detector.py      # Detect vùng text bằng YOLOv8
   │   │   ├── ocr_reader.py         # OCR text bằng PaddleOCR
   │   │   ├── contract_parser.py    # Phân tích text thành JSON
   │   │   ├── storage_service.py    # Dịch vụ quản lý file trong hệ thống.
   │   │   └── contract_extractor.py # Điều hướng xử lý theo loại file
   │   │
   │   ├── models/                   # Định nghĩa dữ liệu, schema
   │   │   ├── __init__.py
   │   │   ├── schema.py             # Định nghĩa JSON hợp đồng
   │   │   └── export_utils.py       # Hàm export JSON, Excel
   │   │
   │   └── utils/                    # Các hàm tiện ích
   │       ├── __init__.py
   │       ├── logging_utils.py         # Quản lý cấu hình logging + log_debug
   │       ├── middleware_logging.py    # Middleware log request/response
   │       ├── decorator_logging.py     # Decorator log thời gian thực thi
   │       └── file_utils.py         # Kiểm tra file, move file, validate file
   │
   ├── frontend/                     # Giao diện hướng dẫn sử dụng, ghé api, các chính sách, thông tin
   │
   ├── store/                        # File vận hành trong runtime
   │   ├── input/                    # File PDF gốc
   │   ├── output/                   # File kết quả JSON/Excel
   │   ├── temp/                     # File tạm OCR, detect
   │   └── backup/                   # Backup file gốc
   │
   ├── notebooks/                    # Lưu các file jupyter notebook
   │
   ├── uploads/                      # Upload file template, rule, cấu hình tùy chỉnh
   │
   ├── train/                        # Dữ liệu training YOLOv8
   │   ├── images/                   # Ảnh dùng để train YOLO
   │   └── labels/                   # File label YOLO (.txt)
   │
   ├── test/                         # Dữ liệu test YOLOv8
   │   ├── images/                   # Ảnh dùng để test YOLO
   │   └── labels/                   # File label YOLO (.txt)
   │
   ├── .env                           # Biến môi trường
   ├── run.py                         # File run server nhanh (uvicorn)
   ├── requirements.txt               # Các package cần cài
   ├── setup.py                       # Cài đặt project package
   ├── Dockerfile                     # Docker build image
   ├── docker-compose.yml             # Docker-compose service
   ├── README.md                       # Tài liệu hướng dẫn
   ├── LoggingSetup.md                # Tài liệu hướng dẫn cai dat
   ├── README_API.md                   # Tài liệu hướng dẫn api
   └── PLAN.md                         # File kế hoạch phát triển
```

📋 Chi tiết cấu trúc:

| Mục                                                     | Nhận xét                                                                                      |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| app/                                                    | Rất gọn: tất cả code logic nằm gọn trong app/                                                 |
| api/endpoints/                                          | Tách endpoint rõ ràng, mỗi file 1 nghiệp vụ                                                   |
| config/                                                 | Đúng chuẩn: config.py (env loader) và database.py (kết nối DB) để riêng                       |
| core/                                                   | Modular core: xử lý extract chi tiết theo text/scan/mixed – tuyệt vời                         |
| services/                                               | Business logic tách riêng (PDFProcessor, YOLODetector, OCRReader...) đúng chuẩn Service Layer |
| models/                                                 | Đúng mô hình domain: schema định nghĩa cấu trúc dữ liệu                                       |
| utils/                                                  | Tiện ích chung: log, middleware, decorator, file_utils rất gọn                                |
| store/, upload/, train/, test/                          | Rõ folder runtime, dữ liệu lưu tách biệt                                                      |
| Các file .env, setup.py, Dockerfile, docker-compose.yml | Đầy đủ, sẵn sàng production                                                                   |
| README.md, PLAN.md, LoggingSetup.md, README_API.md      | Có tài liệu đầy đủ cho dev/frontend/devops – cực kỳ chuyên nghiệp                             |

```pwsh

                [ Client (Frontend, Postman, App) ]
                              ↓
                      [ FastAPI Server ]
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│                             app/                                   │
│                                                                    │
│ ┌───────────┬──────────────┬──────────────┬──────────────────────┐ │
│ │  api/     │  services/   │    core/     │       models/        │ │
│ │ (Routes)  │ (Business)   │ (Core logic) │  (Schemas & Export)  │ │
│ └───────────┴──────────────┴──────────────┴──────────────────────┘ │
│                                                                    │
│ Configs: config/config.py, config/database.py                      │
│ Utils: middleware_logging.py, decorator_logging.py, file_utils.py  │
└────────────────────────────────────────────────────────────────────┘
                              ↓
                       [ store/input/ ]
                      [ store/output/ ]
                       [ store/temp/ ]
                  [ upload/, train/, test/ ]

                              ↓
                    [ Database SQL Server ]

```

| Thành phần          | Chức năng                                                              |
|---------------------|------------------------------------------------------------------------|
| Client              | Frontend App, Mobile App hoặc dùng Postman test API                    |
| FastAPI Server      | Uvicorn chạy server API                                                |
| api/                | Định nghĩa các endpoint (upload, extract, push-db, status, files)      |
| services/           | Xử lý nghiệp vụ: PDFProcessor, YOLO detect, OCR reader, ContractParser |
| core/               | Các module phân tích file (text-only, scan-only, mixed)                |
| models/             | Định nghĩa schema dữ liệu + export JSON/Excel                          |
| config/             | Load biến môi trường .env, kết nối database                            |
| utils/              | Middleware log request, Decorator đo thời gian, Helper file_utils      |
| store/              | Lưu file PDF upload, JSON kết quả, file tạm                            |
| Database SQL Server | Lưu kết quả JSON đã phân tích                                          |

### 🎯 Dòng chảy chính của dữ liệu:
1. Người dùng upload file PDF ➔ /api/upload/
2. Server kiểm tra loại PDF (text-only, scan-only, mixed)
3. Điều hướng tới module xử lý tương ứng:
   - core/extract_text_only.py
   - core/extract_scan_only.py
   - core/extract_mixed.py
4. Kết quả phân tích text ➔ parse JSON theo schema
5. Lưu JSON/Excel vào store/output/
6. Nếu yêu cầu ➔ Đẩy dữ liệu vào SQL Server ➔ /api/push-db/
7. Ghi log toàn bộ quá trình vào folder logs/

### 📚 Ưu điểm của kiến trúc này:
✅ Mở rộng dễ: thêm API mới, module mới không ảnh hưởng code cũ.
✅ Dev team chia task dễ: mỗi module code riêng biệt, độc lập.
✅ Quản lý logs, error tracking chuẩn production.
✅ Có thể dễ dàng CI/CD và scaling hệ thống.
✅ Chuẩn hóa đường dẫn file, tài liệu rõ ràng.

# 3. 🧠 Flow xử lý file PDF

- Kiểm tra loại file PDF trước:

| Loại file           | Pipeline xử lý                                                                |
|---------------------|-------------------------------------------------------------------------------|
| Scan (chỉ ảnh)      | PDF ➔ Chuyển ảnh ➔ YOLO detect vùng ➔ PaddleOCR đọc text vùng ➔ Parse dữ liệu |
| Text (chỉ text)     | PDF ➔ Extract text ➔ Parse dữ liệu                                            |
| Mixed (text + scan) | PDF ➔ Extract text + Chuyển ảnh ➔ OCR ảnh ➔ Merge dữ liệu ➔ Parse JSON        |

# 4. ⚙️ Công nghệ sử dụng

| Thành phần       | Công nghệ                    |
|------------------|------------------------------|
| Backend API      | FastAPI                      |
| OCR Engine       | PaddleOCR                    |
| Object Detection | YOLOv8 (ultralytics)         |
| Database         | SQL Server (pyodbc, aioodbc) |
| PDF Text Extract | pdfplumber                   |
| Image Conversion | pdf2image                    |
| Docker & Compose | Đóng gói container           |

# 5. 📋 TODO List

- STT Việc cần làm Trạng thái

1. ✅ Hoàn thành cấu trúc project đầy đủ
2. ⬜ Viết check_pdf_type() phân loại PDF
3. ⬜ Xây dựng pdf_processor.py (chuyển ảnh)
4. ⬜ Xây dựng yolo_detector.py (detect vùng)
5. ⬜ Xây dựng ocr_reader.py (OCR vùng ảnh)
6. ⬜ Xây dựng contract_parser.py (phân tích text)
7. ⬜ Xây dựng contract_extractor.py (pipeline điều hướng)
8. ⬜ Viết các endpoint API (upload, extract, push-db)
9. ⬜ Setup train/test folder YOLO
10. ⬜ Tối ưu code, logging, validate file
11. ⬜ Viết tài liệu hướng dẫn sử dụng (README)
12. ⬜ Viết script hỗ trợ train YOLO nhanh (nếu cần)
13. ⬜ - nếu văn bản có thể trích xuất được, tiếp tục xử lý.
14. ⬜ Log sang hệ thống ngoài (ELK Stack, Grafana Loki...)
15. ⬜ Gửi cảnh báo khi lỗi nặng (ERROR) bằng email hoặc Slack
16. ⬜ Thêm versioning API

- kiểm tra định dạng file
  - sử dụng các thư viện như python-magic hoặc mimetypes để xác định loại file (PDF hoặc DOCX).
  - nếu file không phải là PDF hoặc DOCX, trả về lỗi cho người dùng.
- kiểm tra nội dung hợp đồng
  - sử dụng các thư viện như regex để kiểm tra xem nội dung hợp đồng có chứa các thông tin cần thiết hay không.
  - nếu không đủ thông tin, trả về lỗi cho người dùng.
- kiểm tra kích thước file
  - sử dụng os.path.getsize() để kiểm tra kích thước file.
  - nếu file quá lớn, trả về lỗi cho người dùng.

# 6. 🔥 Lưu ý quan trọng

- PaddleOCR cần cài paddlepaddle backend riêng (gợi ý dùng paddlepaddle-gpu nếu có GPU).
- YOLOv8 train cần chuẩn bị bộ dữ liệu ảnh + nhãn đúng format YOLO (txt).
- SQL Server phải kiểm tra driver ODBC trong Dockerfile (nên dùng ODBC Driver 17 hoặc 18).
- Cần bổ sung module logging để ghi log process trong thực tế.

# 7. 📈 Flow tổng thể (Call API ➔ Xử lý ➔ Kết quả)

## 1️⃣ Người dùng (client) Gửi request API lên FastAPI Server:

- API: POST /upload/ ➔ gửi file PDF.
- API: POST /extract/ ➔ yêu cầu extract nội dung từ file PDF đã upload.
- API: POST /push-db/ ➔ yêu cầu đẩy JSON đã extract vào database SQL Server.

## 2️⃣ FastAPI Endpoint nhận request:

* Tại app/api/endpoints/:
  - upload.py ➔ Nhận file PDF, lưu vào store/input/.
  - extract.py ➔ Gọi service contract_extractor.py xử lý file.
  - database.py ➔ Gọi core/database.py để insert vào SQL Server.

## 3️⃣ Chuyển request sang các Service tương ứng (app/services/):

Ví dụ với extract.py:

Nhận tên file PDF từ request.

Gọi contract_extractor.extract_contract(pdf_path):

Gọi pdf_processor.py kiểm tra loại file (text, scan, mixed).

Điều hướng sang:

Text ➔ Extract text ➔ Parse JSON.

Scan ➔ Convert ảnh ➔ Detect YOLO ➔ OCR vùng ➔ Parse JSON.

Mixed ➔ Combine cả 2 ➔ Parse JSON.

Kết quả JSON sau xử lý sẽ được lưu vào store/output/.

## 4️⃣ Xử lý chính trong các Service Layer

# 8. 📊 Logging

- Middleware: đã tự động log tất cả request/response rồi
- Decorator log_execution_time:
  - Áp dụng thêm vào các method bên trong các service classes (pdf_processor.py, yolo_detector.py, ocr_reader.py, contract_parser.py,
    contract_extractor.py...).
  - Giúp log tự động thời gian thực thi từng xử lý (ví dụ: thời gian detect vùng, OCR text, parse hợp đồng...).

# 9. Sơ đồ Modular Pipeline easia-blue

```pwsh
[ Upload API ]
      ↓
[ Check PDF Type ] -> text / scan / mixed
      ↓
+------------------+------------------+------------------+
|                  |                  |                  |
|                  |                  |                  |
v                  v                  v
[extract_text_only] [extract_scan_only] [extract_mixed]
|                  |                  |
v                  v                  v
[Parsed Contract Data (JSON)]
          ↓
[ Push to Database API ]
```

Giải thích sơ đồ:

Người dùng upload file.

Server check loại file (text/scan/mixed).

Điều hướng tới module extract phù hợp (ExtractTextOnly, ExtractScanOnly, ExtractMixed).

Parse data ra JSON chuẩn.

Đẩy vào Database SQL Server nếu cần.

✅ Sạch luồng, rõ module, dễ mở rộng thêm pipeline sau này (ví dụ: multi-lang OCR, version 2 contract rules, ...).

# 📄 Kết luận

- Cấu trúc hệ thống chuẩn, tách biệt rõ từng nhiệm vụ.
- Các module xử lý nghiệp vụ được tách biệt, dễ dàng thay thế hoặc mở rộng.
- Có thể dễ dàng tích hợp thêm các module mới như train YOLOv8, export JSON/Excel.
- TODO list rõ ràng, dễ follow từng bước làm.
- Dễ dàng mở rộng các module OCR mới, model detect mới.
- Triển khai nhanh chóng bằng Docker + docker-compose.

# PLAN.md - Project easia-blue - Development Plan

---

# 1. 🌟 Mục tiêu dự án

- Phát triển hệ thống backend **FastAPI**:
  - Tiếp nhận file PDF hợp đồng (text, scan, mixed).
  - Extract nội dung thành JSON chuẩn hóa.
  - Đẩy dữ liệu JSON vào **SQL Server**.
  - Hỗ trợ **train YOLOv8** cho vùng OCR.
  - Xây dựng hệ thống dễ dàng bảo trì, mở rộng.

---

# 2. 🏗️ Cấu trúc tổng thể dự án

```
easia-blue/
|
|├🔹 app/
|   |
|   |├🔹 api/
|   |   |
|   |   ├🔹 endpoints/
|   |       |
|   |       |├🔹 upload.py
|   |       |├🔹 extract.py
|   |       |├🔹 database.py
|   |       |└🔹 status.py
|   |
|   |├🔹 core/
|   |   |
|   |   |├🔹 config.py
|   |   |└🔹 database.py
|   |
|   |├🔹 services/
|   |   |
|   |   |├🔹 pdf_processor.py
|   |   |├🔹 yolo_detector.py
|   |   |├🔹 ocr_reader.py
|   |   |├🔹 contract_parser.py
|   |   |└🔹 contract_extractor.py
|   |
|   |├🔹 models/
|   |   |
|   |   |├🔹 schema.py
|   |   |└🔹 export_utils.py
|   |
|   |└🔹 utils/
|       |
|       |└🔹 file_utils.py
|
|├🔹 store/
|   |
|   |├🔹 input/
|   |├🔹 output/
|   |├🔹 temp/
|   |└🔹 backup/
|
|├🔹 upload/
|
|├🔹 train/
|   |
|   |├🔹 images/
|   |└🔹 labels/
|
|├🔹 test/
|   |
|   |├🔹 images/
|   |└🔹 labels/
|
|├🔹 .env
|├🔹 run.py
|├🔹 requirements.txt
|├🔹 setup.py
|├🔹 Dockerfile
|├🔹 docker-compose.yml
|├🔹 README.md
└🔹 PLAN.md
```

---

# 3. 🧐 Flow xử lý file PDF

| Loại file           | Pipeline xử lý                                    |
|:--------------------|:--------------------------------------------------|
| Chỉ Scan            | PDF ➔  Ảnh ➔ YOLO detect ➔ PaddleOCR ➔ Parse JSON |
| Chỉ Text            | PDF ➔ Extract Text ➔ Parse JSON                   |
| Mixed (text + scan) | PDF ➔ Extract Text + OCR Ảnh ➔ Merge ➔ Parse JSON |

---

# 4. ⚙️ Công nghệ sử dụng

| Thành phần       | Công nghệ                    |
|:-----------------|:-----------------------------|
| Backend API      | FastAPI                      |
| OCR Engine       | PaddleOCR                    |
| Object Detection | YOLOv8 (ultralytics)         |
| Database         | SQL Server (pyodbc, aioodbc) |
| PDF Text Extract | pdfplumber                   |
| Image Conversion | pdf2image                    |
| Docker & Compose | Đóng gói container           |

---

# 5. 📋 TODO List

| STT | Việc cần làm                             | Trạng thái |
|:----|:-----------------------------------------|:-----------|
| 1   | Cấu trúc project                         | ✅          |
| 2   | `check_pdf_type()` phân loại PDF         | ◻          |
| 3   | `pdf_processor.py` (convert PDF)         | ◻          |
| 4   | `yolo_detector.py` detect vùng           | ◻          |
| 5   | `ocr_reader.py` OCR PaddleOCR            | ◻          |
| 6   | `contract_parser.py` Parse text          | ◻          |
| 7   | `contract_extractor.py` pipeline manager | ◻          |
| 8   | API upload, extract, push-db             | ◻          |
| 9   | Setup train/test folder YOLO             | ◻          |
| 10  | Viết logging, handle error               | ◻          |
| 11  | Tối ưu pipeline xử lý                    | ◻          |

---

# 6. 🔥 Lưu ý quan trọng

- PaddleOCR cài đặc thêm `paddlepaddle` backend.
- SQL Server driver nên xác định rõ trong Dockerfile.
- Train YOLO với data format chuẩn YOLO (images/labels).
- Cần ghi log xử lý và exception trong production.

---

# 7. 💡 Flow chi tiết từ Call API ➔ Xử lý ➔ Trả về kết quả

## API Flow:

| API         | Flow                                                                    |
|:------------|:------------------------------------------------------------------------|
| `/upload/`  | Client upload file ➔ upload.py ➔ Lưu store/input/                       |
| `/extract/` | Client gửi filename ➔ extract.py ➔ contract_extractor.py ➔ Extract data |
| `/push-db/` | Client gửi filename ➔ database.py ➔ SQL Server insert                   |

### Quy trình extract chi tiết

```plaintext
Client ➔ FastAPI Endpoint ➔ Contract Extractor Service
    ➔ Check file type
    ➔ Text only: Extract text ➔ Parse JSON
    ➔ Scan only: Convert Ảnh ➔ YOLO detect ➔ OCR ➔ Parse JSON
    ➔ Mixed: Kết hợp text + scan ➔ Parse JSON
    ➔ Save output JSON file
    ➔ Return Response to client
```

### Response Ví dụ:

```json
{
  "status": "success",
  "filename": "abc_contract_2024.json",
  "data": {
    "company_name": "Công ty ABC",
    "contract_number": "HD12345",
    "signed_date": "2024-04-01",
    "total_value": "1,000,000,000 VND",
    "terms": [
      ...
    ]
  }
}
```

---

# 📅 Kết luận

- Kiến trúc tổng thể đã xây dựng rõ ràng.
- TODO rõ ràng cho các giai đoạn phát triển.
- Dễ dàng scale và deploy.
- Chuẩn bị cho các bước phát triển tiếp theo.

---

