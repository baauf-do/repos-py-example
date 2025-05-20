# =========================================
# Stage 1: Build base image + install deps
# =========================================
FROM python:3.10-slim AS builder

# Cài các thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y gcc libpq-dev unixodbc-dev curl && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Tạo virtualenv riêng biệt trong build image
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# =========================================
# Stage 2: Create final runtime image
# =========================================
FROM python:3.10-slim

# Cài thư viện hệ thống tối thiểu (runtime only)
RUN apt-get update && apt-get install -y unixodbc curl && rm -rf /var/lib/apt/lists/*

# Copy virtualenv từ builder stage
COPY --from=builder /venv /venv

# Copy code project vào
COPY app /app/app
COPY store /app/store
COPY upload /app/upload
COPY train /app/train
COPY test /app/test
COPY run.py /app/run.py
COPY .env /app/.env

# Chạy bằng user không phải root (nếu muốn bảo mật hơn)
# RUN adduser --disabled-password appuser
# USER appuser

WORKDIR /app

# Export path virtualenv
ENV PATH="/venv/bin:$PATH"

# Expose port
EXPOSE 8901

# Lệnh mặc định khi container run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8901"]
