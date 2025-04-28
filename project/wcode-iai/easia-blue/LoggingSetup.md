# Logging Setup.md - easia-blue Project

---

# 1. 📅 Mục tiêu

- Quản lý logs chính xác, an toàn, tách biệt theo ngày, theo loại log (request, error, debug, info).
- Tự động xóa log cũ sau 30 ngày.
- Hỗ trợ deploy trên server và trong Docker.

---

# 2. 🔹 Cấu trúc logs

```bash
logs/
├🔹 20240428/
│   ├🔹 request.log
│   ├🔹 error.log
│   ├🔹 debug.log
│   └🔹 info.log
├🔹 20240429/
    ├🔹 request.log
    ├🔹 error.log
    ├🔹 debug.log
    └🔹 info.log
```

---

# 3. 🔹 Cài đặt Logging trong code

- Sử dụng `app/utils/logging_utils.py`
- Sử dụng `log_debug(message, level)` để ghi log nhanh.
- Tự động config log theo ngày, tạo nhiều file log.

---

# 4. 🔹 Triển khai Logrotate

- File config: `/etc/logrotate.d/easia-blue`

```bash
/home/your_username/easia-blue/logs/*/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    copytruncate
}
```

- Xoay log ngay lần đầu:
```bash
sudo logrotate -f /etc/logrotate.d/easia-blue
```

---

# 5. 🔹 Sử dụng trong FastAPI

- Middleware: log request/response.
- Decorator: log execution time function.


---

# Dockerfile - Tối ưu Logging

```Dockerfile
FROM python:3.10-slim

# Cài đặt các package cần thiết
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt logrotate
RUN apt-get update && apt-get install -y logrotate

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy code
COPY ../easia-green .

# Cài package Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8901

# Chạy logrotate theo cron (nếu muốn)
# COPY cronfile /etc/cron.d/logrotate-cron
# RUN chmod 0644 /etc/cron.d/logrotate-cron
# RUN crontab /etc/cron.d/logrotate-cron

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8901", "--reload"]
```

---

# docker-compose.yml - Tối ưu Logging

```yaml
version: "3.9"

services:
  easia-blue:
    build: .
    container_name: easia-blue-app
    ports:
      - "8901:8901"
    volumes:
      - .:/app
      - ./logs:/app/logs
    environment:
      - HOST=0.0.0.0
      - PORT=8901
    restart: always
```

- Volume mount `./logs` ra host server.
- Log vẫn quay bên host qua logrotate.

---

# 6. 🔹 Ghi nhớ quan trọng

- Mỗi ngày server sinh folder log mới theo ngày.
- Giữ 30 ngày log, sau đó tự động nén và xóa.
- Tất cả request, error, debug, info log chia file riêng.
- Monitoring log bằng ELK/Grafana Loki có thể dễ dàng.

---

# 🔗 Done!

- Project easia-blue đã có hệ thống Logging chuẩn sẵn sàng production!

