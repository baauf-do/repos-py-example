# Structure of the project
```
├── easia/                                  # .NET Core app (ví dụ: backend cho giao diện người dùng, quản lý)
│   ├── src/                                # Thư mục chứa mã nguồn .NET Core
│   │   ├── easia/                          # Thư mục chứa project .NET Core (API hoặc UI)
│   │   │   ├── Controllers/                # Thư mục chứa các controllers
│   │   │   │   └── ContractController.cs   # Điều khiển xử lý hợp đồng
│   │   │   ├── Models/                     # Mô hình dữ liệu (có thể chứa class cho hợp đồng)
│   │   │   │   └── Contract.cs
│   │   │   ├── Program.cs                  # Điểm bắt đầu cho ứng dụng .NET Core
│   │   │   ├── Startup.cs                  # Cấu hình ứng dụng (services, middlewares, v.v.)
│   │   │   ├── easia.csproj                # File dự án .NET Core
│   │   │   └── Dockerfile                  # Dockerfile để containerize .NET Core service
│   │   └── README.md                       # Mô tả repo .NET Core
│   │
│   └── easia.sln                           # File solution của dự án .NET Core (nếu có)
```
# Chi tiết các thư mục và file trong cấu trúc:
- .NET Core ứng dụng chính. Có thể là một API để kết nối với các dịch vụ FastAPI, hoặc là giao diện quản lý cho người dùng.
  - src/: Thư mục chứa mã nguồn của ứng dụng .NET Core.
    - Controllers/: Các controller xử lý các API endpoints của .NET Core.
    - Models/: Các lớp dữ liệu mà bạn sử dụng trong ứng dụng (ví dụ: hợp đồng).
    - Program.cs: Điểm bắt đầu của ứng dụng .NET Core.
    - Startup.cs: Cấu hình các dịch vụ và middleware cho ứng dụng .NET Core.
    - Dockerfile: Định nghĩa cách containerize ứng dụng .NET Core.


