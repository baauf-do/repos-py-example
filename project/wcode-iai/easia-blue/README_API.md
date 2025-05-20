# README_API.md - API Documentation for easia-blue

---

# 🔹 Tổng quan

Hệ thống cung cấp các API để xử lý file PDF hợp đồng:

- Upload file PDF.
- Extract dữ liệu hợp đồng.
- Đẩy dữ liệu JSON vào SQL Server.
- Kiểm tra trạng thái server.
- Liệt kê file đã upload.
- Xử lý riêng theo từng loại PDF: Text, Scan, Mixed.
- Upload + Process + Extract tự động chỉ với 1 API.

---

# 💡 Danh sách API

## 1. Upload file PDF

- **URL:** `/api/upload/`
- **Method:** `POST`
- **Input:** Upload file PDF (multipart/form-data)
- **Output:**

```json
{
  "filename": "contract_abc.pdf"
}
```

---

## 2. Extract dữ liệu từ file PDF (Auto detect loại file)

- **URL:** `/api/extract/`
- **Method:** `POST`
- **Input:**

```json
{
  "file_name": "contract_abc.pdf"
}
```

- **Output:**

```json
{
  "status": "success",
  "data": {
    "...parsed fields..."
  }
}
```

---

## 3. Đẩy JSON vào Database

- **URL:** `/api/push-db/`
- **Method:** `POST`
- **Input:**

```json
{
  "file_name": "contract_abc.json"
}
```

- **Output:**

```json
{
  "status": "success",
  "message": "Inserted contract_abc.json into database"
}
```

---

## 4. Check server status

- **URL:** `/api/status/`
- **Method:** `GET`
- **Output:**

```json
{
  "status": "running"
}
```

---

## 5. List file đã upload

- **URL:** `/api/uploaded-files/`
- **Method:** `GET`
- **Output:**

```json
{
  "files": [
    "contract_abc.pdf",
    "invoice_xyz.pdf"
  ]
}
```

---

# 🌐 API xử lý theo loại PDF

## 6. Xử lý file chỉ chứa text

- **URL:** `/api/process-text-pdf/`
- **Method:** `POST`
- **Input:**

```json
{
  "file_name": "contract_textonly.pdf"
}
```

- **Output:**

```json
{
  "status": "success",
  "data": {
    "...parsed fields..."
  }
}
```

---

## 7. Xử lý file chỉ chứa scan ảnh

- **URL:** `/api/process-scan-pdf/`
- **Method:** `POST`
- **Input:**

```json
{
  "file_name": "contract_scanonly.pdf"
}
```

- **Output:**

```json
{
  "status": "success",
  "data": {
    "...parsed fields..."
  }
}
```

---

## 8. Xử lý file mixed (text + scan)

- **URL:** `/api/process-mixed-pdf/`
- **Method:** `POST`
- **Input:**

```json
{
  "file_name": "contract_mixed.pdf"
}
```

- **Output:**

```json
{
  "status": "success",
  "data": {
    "...parsed fields..."
  }
}
```

---

## 9. Upload + Process + Extract tự động

- **URL:** `/api/upload-process-extract/`
- **Method:** `POST`
- **Input:** Upload file PDF (multipart/form-data)
- **Output:**

```json
{
  "status": "success",
  "filename": "contract_abc.pdf",
  "pdf_type": "text",
  "data": {
    "...parsed fields..."
  }
}
```

**Mô tả:**

- Upload file ➔ Detect PDF type ➔ Extract data ➔ Trả về JSON kết quả chỉ trong 1 lần gọi API.

---

# 🔹 Quy ước chung API

- Các API `POST` yêu cầu body dạng JSON nếu không upload file.
- Các lỗi sẽ trả về HTTP 400/500 + chi tiết lỗi trong field `error`.
- Các field trả về theo chuẩn hóa cấu trúc JSON đồng nhất.

---

# 📊 Ví dụ lỗi (Error Response)

```json
{
  "error": "File contract_abc.pdf not found."
}
```

---

# 🔹 Ghi chú thêm

- Tất cả file input PDF phải được upload vào folder `store/input/` trước.
- JSON output sẽ lưu ở `store/output/` cùng với file Excel nếu cần.
- API được chuẩn hóa để dễ dàng tích hợp vào bất kỳ dashboard hoặc frontend app nào.
- Log request/response đầy đủ theo từng bước xử lý.

---

# 👌 Done - Full API doc easia-blue chuẩn update mới nhất!
