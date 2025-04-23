# easia-blue
- trich xuat thong tin tu file pdf hop dong sang json
- tu du lieu json cap nhat vao database

## Structure of the project

```bash
easia-blue/                 # FastAPI service (ví dụ: xử lý hợp đồng PDF -> file .json)
├── app/                 # Thư mục chứa mã nguồn FastAPI
│   ├── __init__.py
│   ├── main.py          # File khởi tạo và định nghĩa API
│   ├── services/        # Các module xử lý logic (ví dụ: trích xuất dữ liệu PDF)
│   │   ├── __init__.py # File này có thể để trống
│   │   └── pdf_parser.py
│   ├── models/          # Các mô hình dữ liệu, có thể bao gồm các class để xử lý dữ liệu
│   │   ├── __init__.py # File này có thể để trống
│   │   └── contract.py
│   └── store/
│       ├── __init__.py # File này có thể để trống
│       ├── input
│       ├── output
│       └── temp
├── frontend/
│   ├── static/
│   └── templates/
│       └── index.html
├── models/
├── services/
├── store/
│   ├── input/
│   └── output/
├── tests/
├── uploads/
├── .env
├── requirements.txt # Các thư viện cần thiết cho FastAPI (pdfplumber, uvicorn, v.v.)
├── setup.py
├── Dockerfile            # Dockerfile để containerize FastAPI service
├── docker-compose.yml
├── README.md                 # Mô tả dịch vụ FastAPI
└── .gitignore                # Lọc các file không cần thiết khi dùng Git


```
## dua vao cau truc thu muc tao cac file va folder tuong ung bang bash
- Chạy các lệnh sau trong terminal:
```bash
mkdir -p easia-blue/app/services
mkdir -p easia-blue/app/models
mkdir -p easia-blue/app/store/input
mkdir -p easia-blue/app/store/output
mkdir -p easia-blue/app/store/temp
mkdir -p easia-blue/frontend/static
mkdir -p easia-blue/frontend/templates
mkdir -p easia-blue/models
mkdir -p easia-blue/services
mkdir -p easia-blue/store/input
mkdir -p easia-blue/store/output
mkdir -p easia-blue/tests
mkdir -p easia-blue/uploads
touch easia-blue/app/__init__.py
touch easia-blue/app/main.py
touch easia-blue/app/services/__init__.py
touch easia-blue/app/services/pdf_parser.py
touch easia-blue/app/models/__init__.py
touch easia-blue/app/models/contract.py
touch easia-blue/app/store/__init__.py
touch easia-blue/frontend/templates/index.html
touch easia-blue/.env
touch easia-blue/requirements.txt
touch easia-blue/setup.py
touch easia-blue/Dockerfile
touch easia-blue/docker-compose.yml
touch easia-blue/README.md
touch easia-blue/.gitignore

```

## Chi tiết các thư mục và file trong cấu trúc:

### easia-blue/

- FastAPI services xử lý các hợp đồng từ PDF và DOCX.
- app/: Chứa mã nguồn cho dịch vụ FastAPI.
  - main.py: Là file chính của FastAPI, nơi bạn sẽ khai báo các route và xử lý các yêu cầu.
  - services/: Chứa các module giúp xử lý logic (ví dụ: pdf_parser.py để trích xuất dữ liệu từ PDF và docx_parser.py để trích xuất dữ liệu
    từ DOCX).
  - models/: Chứa các mô hình dữ liệu để định nghĩa các cấu trúc dữ liệu bạn sử dụng trong API, chẳng hạn như mô hình hợp đồng.
  - requirements.txt: Liệt kê các thư viện cần thiết như fastapi, uvicorn, pdfplumber, python-docx, ...
  - Dockerfile: Định nghĩa cách containerize dịch vụ FastAPI.

### chạy file setup.py đầu tiên

- nó là file khởi tạo môi trường ảo cho dự án
- là file Setup environment for project tự động
  - here folder local path of project
  ```bash
  cd project/wcode-iai/easia-blue
  ```
  - run -> lựa chọn python version -> done
  ```bash
  py setup.py
  ```

### với file .env

- cấu hình trong đó
- sử dụng python-dotenv để load biến môi trường từ file .env vào ứng dụng FastAPI.



## flow - xử lý hơp đồng
1. Nhận file hợp đồng từ người dùng qua API.
2. Xác định loại file (PDF hoặc DOCX).
3. Sử dụng các module tương ứng để trích xuất dữ liệu từ file.
4. Xử lý dữ liệu đã trích xuất (ví dụ: lưu vào cơ sở dữ liệu, trả về cho người dùng, v.v.).
5. Trả về kết quả cho người dùng qua API.
6. Ghi log các hoạt động và lỗi (nếu có) để theo dõi và xử lý sau này.
7. Kiểm tra và xử lý các lỗi có thể xảy ra trong quá trình trích xuất dữ liệu.
8. Tối ưu hóa mã nguồn và cấu trúc thư mục để dễ dàng bảo trì và mở rộng trong tương lai.
9. Thực hiện kiểm thử để đảm bảo rằng các chức năng hoạt động đúng và không có lỗi.
10. Triển khai dịch vụ FastAPI lên môi trường sản xuất.
11. Cung cấp tài liệu hướng dẫn sử dụng API cho người dùng.
12. Theo dõi và bảo trì dịch vụ sau khi triển khai, bao gồm việc cập nhật mã nguồn, sửa lỗi và cải thiện hiệu suất.

- ide
  - sử dụng pycharm
  - cài đặt các plugin cần thiết cho FastAPI và Python.
  - cấu hình môi trường ảo trong PyCharm để dễ dàng quản lý các thư viện và phụ thuộc.
  - sử dụng terminal tích hợp trong PyCharm để chạy các lệnh như `uvicorn` hoặc `docker` mà không cần rời khỏi IDE.
  - sử dụng Git để quản lý mã nguồn và theo dõi các thay đổi trong dự án.

- ý tưởng thực hiện trích xuất hợp đồng để đưa vào database
  - kiểm tra nội dung văn bản
    - sử dụng các thư viện như pdfplumber hoặc python-docx để trích xuất văn bản từ file PDF hoặc DOCX.
    - nếu văn bản không thể trích xuất được, có khả năng đó là trang trắng hoặc .
