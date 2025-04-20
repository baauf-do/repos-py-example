# Dockerfile (đặt trong easia-green/)
FROM python:3.10-slim

# Cài đặt các gói hệ thống cần thiết (bỏ tesseract vì không sử dụng)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục app
WORKDIR /usr/src/app

# Copy toàn bộ mã nguồn
COPY . .

# Cài đặt thư viện Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r app/requirements.txt

# Mặc định chạy uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--workers", "1"]
