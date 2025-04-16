# Structure folder cho dự án WCode IAI

```
wcode-iai/                    # Thư mục gốc cho toàn bộ dự án
│
├── easia-red/              # FastAPI service 1 (ví dụ: xử lý hợp đồng PDF)
│   ├── app/                # Thư mục chứa mã nguồn FastAPI
│   │   ├── __init__.py     # File này có thể để trống
│   │   ├── main.py         # File khởi tạo và định nghĩa API
│   │   ├── services/       # Các module xử lý logic (ví dụ: trích xuất dữ liệu PDF)
│   │   │   ├── __init__.py # File này có thể để trống
│   │   │   └── pdf_parser.py
│   │   ├── models/         # Các mô hình dữ liệu, có thể bao gồm các class để xử lý dữ liệu
│   │   │   ├── __init__.py # File này có thể để trống
│   │   │   └── contract.py
│   │   ├── requirements.txt  # Các thư viện cần thiết cho FastAPI (pdfplumber, uvicorn, v.v.)
│   │   └── Dockerfile       # Dockerfile để containerize FastAPI service
│   ├── .venv-red/          # Môi trường ảo (đã được tạo và cài đặt thư viện)
│   │
│   └── README.md           # Mô tả repo FastAPI service 1
│
├── easia-blue/             # FastAPI service 2 (ví dụ: xử lý hợp đồng DOCX)
│   ├── app/                # Thư mục chứa mã nguồn FastAPI
│   │   ├── __init__.py     # File này có thể để trống
│   │   ├── main.py         # File khởi tạo và định nghĩa API
│   │   ├── services/       # Các module xử lý logic (ví dụ: trích xuất dữ liệu DOCX)
│   │   │   ├── __init__.py # File này có thể để trống
│   │   │   └── docx_parser.py
│   │   ├── models/         # Các mô hình dữ liệu, có thể bao gồm các class để xử lý dữ liệu
│   │   │   ├── __init__.py # File này có thể để trống
│   │   │   └── contract.py
│   │   ├── requirements.txt  # Các thư viện cần thiết cho FastAPI (python-docx, uvicorn, v.v.)
│   │   └── Dockerfile       # Dockerfile để containerize FastAPI service
│   ├── .venv-red/          # Môi trường ảo (đã được tạo và cài đặt thư viện)
│   │
│   └── README.md           # Mô tả repo FastAPI service 2
│
├── easia/             # .NET Core app (ví dụ: backend cho giao diện người dùng, quản lý)
│   ├── src/                # Thư mục chứa mã nguồn .NET Core
│   │   ├── easia/     # Thư mục chứa project .NET Core (API hoặc UI)
│   │   │   ├── Controllers/  # Thư mục chứa các controllers
│   │   │   │   └── ContractController.cs  # Điều khiển xử lý hợp đồng
│   │   │   ├── Models/         # Mô hình dữ liệu (có thể chứa class cho hợp đồng)
│   │   │   │   └── Contract.cs
│   │   │   ├── Program.cs    # Điểm bắt đầu cho ứng dụng .NET Core
│   │   │   ├── Startup.cs    # Cấu hình ứng dụng (services, middlewares, v.v.)
│   │   │   ├── easia.csproj  # File dự án .NET Core
│   │   │   └── Dockerfile    # Dockerfile để containerize .NET Core service
│   │   └── README.md        # Mô tả repo .NET Core
│   │
│   └── easia.sln       # File solution của dự án .NET Core (nếu có)
│
├── docker-compose.yml      # File cấu hình Docker Compose để orchestrate các dịch vụ
└── README.md               # Tài liệu mô tả tổng quan về toàn bộ dự án
```

# information

- Lợi ích của cấu trúc này:
  1. Tách biệt dịch vụ: Mỗi dịch vụ được tách biệt rõ ràng, giúp dễ dàng bảo trì, triển khai và mở rộng.
  2. Quản lý độc lập: Các dịch vụ FastAPI và .NET Core có thể phát triển độc lập, dễ dàng thay đổi mà không ảnh hưởng đến
     các dịch vụ còn lại.
  3. Triển khai dễ dàng: Với Docker, bạn có thể containerize từng dịch vụ và triển khai chúng trên bất kỳ nền tảng nào
     (AWS, Google Cloud, Azure, v.v.).
  4. Dễ dàng mở rộng: Nếu cần thêm dịch vụ nào khác trong tương lai (ví dụ: một dịch vụ khác để xử lý hợp đồng Excel), bạn chỉ cần thêm một
     thư mục dịch vụ mới mà không cần thay đổi cấu trúc hiện tại.

# Setup

- Cài python 3.10.
  - Python 3.10.10 - Feb. 8, 2023
  - Download Windows installer (64-bit)
  - https://www.python.org/downloads/release/python-31010/
- Cài đặt Docker và Docker Compose.
- Cài đặt các thư viện cần thiết cho FastAPI chạy trong môi trường ảo:
  - Tạo môi trường ảo cho FastAPI: đứng ở thư mục `easia-red` hoặc `easia-blue` và chạy lệnh sau:

```bash
py -3.10 -m venv .venv
```

- chạy các cài đặt bằng pip

```bash
py -m pip install --upgrade pip
```

- cài đặt các thư viện cần thiết cho FastAPI:

```bash
pip install "fastapi[standard]"
pip install .\app\requirements.txt
```

- chạy FastAPI:

```bash
fastapi dev .\app\main.py
```

hoặc

```bash
uvicorn app.main:app --reload
```

## Errors khi chạy fastapi/uvicorn

- Nếu gặp lỗi sau khi chạy FastAPI/uvicorn:

  - Tìm và dừng tiến trình Uvicorn thủ công
    - a. Tìm PID của tiến trình Uvicorn
      - Mở một terminal mới (hoặc sử dụng terminal hiện tại).
      - Chạy lệnh sau để tìm tiến trình Uvicorn:
      ```bash
        tasklist | findstr uvicorn
      ```
      > Lệnh này sẽ hiển thị danh sách các tiến trình liên quan đến Uvicorn, cùng với PID (Process ID).
    - b. Dừng tiến trình bằng PID
      - Dừng tiến trình Uvicorn bằng lệnh:
      ```bash
        taskkill /PID <PID> /F
      ```
      > Thay <PID> bằng số PID của tiến trình Uvicorn.

- dừng tất cả các tiến trình python/uvicorn/fastapi đang chạy:

```bash
taskkill /IM python.exe /F
taskkill /IM uvicorn.exe /F
taskkill /IM fastapi.exe /F
```

# Reference

- https://github.com/NguyenDucQuan12/Fast_API_server
