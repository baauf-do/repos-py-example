# TODO.md: Phát triển Hệ thống Trích Xuất Thông Tin Hợp Đồng Khách Sạn

**Mục tiêu:** Xây dựng một hệ thống có khả năng trích xuất thông tin chính xác và đáng tin cậy từ các file PDF hợp đồng khách sạn, bao gồm cả các file text-based và scan/mixed.

**Flow tổng quan:**

1.  **Input: File PDF Hợp Đồng**
    * 1.1.  Kiểm tra tính hợp lệ của file PDF.
    * 1.2.  Upload và lưu trữ file PDF.
2.  **Xác Định Loại PDF và Tiền Xử Lý:**
    * 2.1.  Xác định loại PDF (text-based hoặc scan/mixed).
    * 2.2.  Xử lý Text-based PDF (trích xuất văn bản).
    * 2.3.  Xử lý Scan/Mixed PDF (chuyển đổi sang ảnh).
    * 2.4.  (Tùy chọn) Tiền xử lý ảnh nâng cao.
3.  **Trích Xuất Văn Bản (OCR):**
    * 3.1.  Sử dụng văn bản đã trích xuất (nếu là text-based PDF).
    * 3.2.  Trích xuất văn bản từ ảnh bằng OCR (nếu là scan/mixed PDF).
    * 3.3.  Hậu xử lý OCR (sửa lỗi chính tả, chuẩn hóa văn bản).
4.  **Phân Tích và Trích Xuất Thông Tin:**
    * 4.1.  Điều hướng xử lý (theo loại PDF).
    * 4.2.  Trích xuất thông tin nâng cao:
        * 4.2.1. Rule-based Extraction với Ngữ cảnh.
        * 4.2.2. NLP-based Extraction (tinh chỉnh NER, quan hệ thực thể, xử lý điều khoản phức tạp).
        * 4.2.3. Xử lý bảng nâng cao.
        * 4.2.4. Xử lý đa ngôn ngữ.
        * 4.2.5. Xác thực dữ liệu.
    * 4.3.  Lưu trữ dữ liệu trích xuất.
5.  **Tạo JSON:**
    * 5.1.  Định dạng dữ liệu nâng cao (cấu trúc JSON phức tạp, metadata).
    * 5.2.  Tạo chuỗi JSON.
6.  **Lưu Trữ Kết Quả:**
    * 6.1.  Lưu JSON vào file (tổ chức thư mục, kiểm soát phiên bản).
    * 6.2.  (Tùy chọn) Đẩy dữ liệu vào SQL Server (ánh xạ dữ liệu phức tạp, xử lý giao dịch).
    * 6.3.  Trả về kết quả qua API.
7.  **Xử Lý Lỗi và Logging:**
    * 7.1.  Logging (level logging, contextual logging, monitoring).
    * 7.2.  Xử lý lỗi (phân loại lỗi, retry mechanism, fallback mechanism, thông báo lỗi chi tiết).
8.  **API Flow:**
    * 8.1.  Tham số tùy chọn.
    * 8.2.  Xử lý bất đồng bộ.
    * 8.3.  Kết quả chi tiết.

**TODO List (Trước khi viết xử lý):**

**1. Phân tích chi tiết các mẫu hợp đồng:**

* \[x]   Liệt kê các trường thông tin cần trích xuất (key-value pairs) từ các mẫu hợp đồng.
    * Ví dụ: `ten_khach_san`, `dia_chi`, `thoi_gian_nhan_phong`, `thoi_gian_tra_phong`, `so_luong_khach`, `tong_gia`, `ngay_ky_hop_dong`, thông tin các bên liên quan, các điều khoản cụ thể.
* \[x]   Xác định các mẫu định dạng thông tin (ngày tháng, số tiền, địa chỉ, v.v.).
* \[x]   Phân tích cấu trúc của các bảng (nếu có).
* \[x]   Xác định các biến thể về ngôn ngữ (nếu có).
* \[x]   Xác định các trường thông tin bắt buộc và tùy chọn.
* \[x]   Phân loại các loại hợp đồng (nếu có thể).

**2. Lựa chọn và cấu hình thư viện/công cụ:**

* \[x]   Xác định các thư viện Python cần thiết cho từng bước (PyPDF2/pdfminer.six, PyMuPDF, PaddleOCR, spaCy/NLTK, regex, json, v.v.).
* \[x]   Cài đặt và cấu hình các thư viện.
* \[x]   (Nếu cần) Tinh chỉnh các mô hình (ví dụ: mô hình NER).

**3. Thiết kế schema JSON:**

* \[x]   Xác định cấu trúc JSON để biểu diễn thông tin trích xuất.
* \[x]   Xác định kiểu dữ liệu cho từng trường.
* \[x]   (Nếu cần) Thiết kế cấu trúc JSON phức tạp để biểu diễn các mối quan hệ.

**4. Thiết kế API (nếu cần):**

* \[x]   Xác định các API endpoint cần thiết.
* \[x]   Xác định các tham số đầu vào và đầu ra của API.
* \[x]   Xác định các định dạng dữ liệu (request/response).

**5. Lập kế hoạch xử lý lỗi và logging:**

* \[x]   Xác định các loại lỗi có thể xảy ra.
* \[x]   Lựa chọn thư viện logging và cấu hình.
* \[x]   Quyết định các thông tin cần log.

**6. Lập kế hoạch kiểm thử:**

* \[x]   Xác định các trường hợp kiểm thử (test cases).
* \[x]   Chuẩn bị dữ liệu kiểm thử (các file PDF mẫu).
* \[x]   Xác định các tiêu chí đánh giá (độ chính xác, thời gian xử lý).

**Ghi chú:**

* Các task được đánh dấu \[x] là các task cần hoàn thành trước khi bắt đầu viết mã xử lý chi tiết.
* Các task có thể được thực hiện song song hoặc theo thứ tự ưu tiên.
* Cần có sự trao đổi và thống nhất giữa các thành viên trong nhóm để đảm bảo tính nhất quán và hiệu quả.

---


