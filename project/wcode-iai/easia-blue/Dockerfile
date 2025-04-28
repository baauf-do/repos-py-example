FROM python:3.10-slim

# 1. Cài các thư viện cơ bản
RUN apt-get update && apt-get install -y \
    gcc g++ unixodbc-dev libpq-dev curl \
    logrotate cron \
    && rm -rf /var/lib/apt/lists/*

# 2. Thiết lập thư mục làm việc
WORKDIR /app

# 3. Copy toàn bộ code vào container
COPY . .

# 4. Cài thư viện Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Tạo file cronjob cho logrotate
RUN echo "0 0 * * * /usr/sbin/logrotate /etc/logrotate.d/easia-blue" > /etc/cron.d/logrotate-easia-blue

# 6. Phân quyền và active cron
RUN chmod 0644 /etc/cron.d/logrotate-easia-blue
RUN crontab /etc/cron.d/logrotate-easia-blue

# 7. Expose port
EXPOSE 8901

# 8. Command start cả app và cron service
CMD service cron start && uvicorn app.main:app --host 0.0.0.0 --port 8901 --reload
