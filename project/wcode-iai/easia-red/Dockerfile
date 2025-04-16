FROM python:3.10-slim

WORKDIR /app

COPY app .

# ✨ Thêm PYTHONPATH chỉ ra thư mục gốc chứa app/
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
