# Structure of the project
```
easia-red/
├── app/
│   ├── __init__.py
│   ├── main.py               # Khởi tạo FastAPI và định nghĩa các endpoint
│   ├── services/             # Logic xử lý trích xuất dữ liệu từ PDF
│   │   └── pdf_parser.py     # Module trích xuất văn bản từ file PDF
│   ├── models/               # Các mô hình dữ liệu (ví dụ: Contract)
│   │   └── contract.py       # Mô hình dữ liệu của hợp đồng
│   ├── requirements.txt      # Các thư viện cần thiết cho FastAPI
│   └── Dockerfile            # Dockerfile để containerize FastAPI service
├── README.md                 # Mô tả dịch vụ FastAPI
└── .gitignore                # Lọc các file không cần thiết khi dùng Git
```

# Chi tiết các thư mục và file trong cấu trúc:
## easia-red/
- FastAPI services xử lý các hợp đồng từ PDF và DOCX.
- app/: Chứa mã nguồn cho dịch vụ FastAPI.
  - main.py: Là file chính của FastAPI, nơi bạn sẽ khai báo các route và xử lý các yêu cầu.
  - services/: Chứa các module giúp xử lý logic (ví dụ: pdf_parser.py để trích xuất dữ liệu từ PDF và docx_parser.py để trích xuất dữ liệu từ DOCX).
  - models/: Chứa các mô hình dữ liệu để định nghĩa các cấu trúc dữ liệu bạn sử dụng trong API, chẳng hạn như mô hình hợp đồng.
  - requirements.txt: Liệt kê các thư viện cần thiết như fastapi, uvicorn, pdfplumber, python-docx, ...
  - Dockerfile: Định nghĩa cách containerize dịch vụ FastAPI.

# Setup
1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

# Run the FastAPI application:

```bash
uvicorn app.main:app --reload
```
