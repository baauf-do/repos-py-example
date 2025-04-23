# 📁 Cấu trúc project chatbot

# Cấu trúc thư mục (chuẩn hóa theo yêu cầu)

```bash
chatbot-project/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── chatbot.py
│   ├── services/
│   │   └── data_loader.py
│   ├── store/
│   │   └── data.xlsx         # ✅ Dữ liệu nội bộ (Excel)
│   └── main.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

# ✅ app/core/config.py

import os

# Đường dẫn đến file Excel nằm trong thư mục app/store
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "..", "store", "data.xlsx")

# ✅ README.md

# Chatbot Project with Python 3.10 + FastAPI + Ollama

## 🔧 Mục tiêu
- Xây dựng chatbot sử dụng dữ liệu nội bộ từ file Excel
- Gọi mô hình cộng đồng như Ollama (hoặc Claude/OpenAI)
- Cung cấp API qua FastAPI
- Chạy toàn bộ bằng Docker

## 📦 Cấu trúc thư mục

```bash
chatbot-project/
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── models/chatbot.py
│   ├── services/data_loader.py
│   ├── store/data.xlsx
│   └── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Cách chạy

1. Cài Docker & Ollama

```bash
ollama run llama3  # hoặc bất kỳ model nào đã pull
```

2. Build và chạy API:

```bash
docker-compose up --build
```

3. Gửi request:

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Xin chào, bạn là ai?"}'
```

## ✍️ Mô tả các file chính

- `data_loader.py`: đọc file Excel thành danh sách dict.
- `chatbot.py`: gửi prompt đến mô hình Ollama.
- `routes.py`: tạo endpoint `/api/chat`.
- `config.py`: cấu hình đường dẫn file Excel.
- `main.py`: khởi chạy FastAPI.

## 📌 Ghi chú
- Có thể thay Ollama bằng Claude hoặc GPT bằng cách chỉnh `chatbot.py`
- Đảm bảo file `data.xlsx` tồn tại để tránh lỗi khi load dữ liệu.
