# Structure of the project
```
easia-blue/                 # FastAPI service 1 (ví dụ: xử lý hợp đồng PDF)
   ├── app/                 # Thư mục chứa mã nguồn FastAPI
   │   ├── __init__.py
   │   ├── main.py          # File khởi tạo và định nghĩa API
   │   ├── services/        # Các module xử lý logic (ví dụ: trích xuất dữ liệu PDF)
   │   │   └── pdf_parser.py
   │   ├── models/          # Các mô hình dữ liệu, có thể bao gồm các class để xử lý dữ liệu
   │   │   └── contract.py
   │   ├── requirements.txt # Các thư viện cần thiết cho FastAPI (pdfplumber, uvicorn, v.v.)
   │   └── Dockerfile       # Dockerfile để containerize FastAPI service
   │
   └── README.md            # Mô tả repo FastAPI service 1
```
# Chi tiết các thư mục và file trong cấu trúc:
## easia-blue/
- FastAPI services xử lý các hợp đồng từ PDF và DOCX.
- app/: Chứa mã nguồn cho dịch vụ FastAPI.
  - main.py: Là file chính của FastAPI, nơi bạn sẽ khai báo các route và xử lý các yêu cầu.
  - services/: Chứa các module giúp xử lý logic (ví dụ: pdf_parser.py để trích xuất dữ liệu từ PDF và docx_parser.py để trích xuất dữ liệu từ DOCX).
  - models/: Chứa các mô hình dữ liệu để định nghĩa các cấu trúc dữ liệu bạn sử dụng trong API, chẳng hạn như mô hình hợp đồng.
  - requirements.txt: Liệt kê các thư viện cần thiết như fastapi, uvicorn, pdfplumber, python-docx, ...
  - Dockerfile: Định nghĩa cách containerize dịch vụ FastAPI.
