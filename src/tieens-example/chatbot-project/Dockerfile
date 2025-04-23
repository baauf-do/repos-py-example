# Base image với Python 3.10
FROM python:3.10-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Sao chép toàn bộ project vào container
COPY . .

# Cài đặt các thư viện từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port cho FastAPI
EXPOSE 8000

# Lệnh chạy app bằng uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
