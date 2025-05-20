# Roadmap Học Tập: Trích Xuất Hợp Đồng Từ File PDF, DOC, Excel

---

## 1. Python cơ bản & Xử lý file tài liệu
- Thành thạo Python cơ bản.
- Đọc, xử lý file PDF, Word, Excel.
- Công cụ:
  - PDF: PyPDF2, pdfplumber
  - Word: python-docx
  - Excel: openpyxl, pandas
- Project: Viết script đọc nội dung hợp đồng từ PDF, DOC, Excel.

## 2. OCR với PaddleOCR
- Sử dụng PaddleOCR để chuyển file scan hoặc ảnh hợp đồng thành text.
- Tìm hiểu cài đặt và sử dụng PaddleOCR.
- Project: OCR hợp đồng scan, xuất dữ liệu text thô với PaddleOCR.

## 3. Xử lý ngôn ngữ tự nhiên (NLP) - Trích xuất thông tin
- Tập trung trích xuất thông tin hợp đồng (tên bên, số hợp đồng, ngày tháng, điều khoản).
- Công cụ: spaCy, Hugging Face Transformers.
- Project: Dùng spaCy hoặc mô hình fine-tuned để nhận diện và trích xuất các trường quan trọng trong hợp đồng.

## 4. Machine Learning & Deep Learning nâng cao (Tùy chọn)
- Nâng cao mô hình trích xuất bằng các mô hình Transformer (BERT, RoBERTa...).
- Project: Fine-tune mô hình cho trích xuất thông tin hợp đồng.

## 5. Ứng dụng & Triển khai thực tế
- Tạo pipeline tự động đọc file hợp đồng, áp dụng OCR và NLP để trích xuất thông tin, lưu vào database.
- Có thể tích hợp PaddleOCR và mô hình NLP trong hệ thống xử lý tài liệu.

---

## Tham khảo tài liệu & khóa học

- Python & xử lý file:
  - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
  - [PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/latest/)
  - [python-docx Documentation](https://python-docx.readthedocs.io/en/latest/)
  - [pandas Documentation](https://pandas.pydata.org/docs/)
- OCR:
  - [PaddleOCR Github](https://github.com/PaddlePaddle/PaddleOCR)
  - [PaddleOCR Tutorial](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/installation_en.md)
- NLP & IE:
  - [spaCy NER Tutorial](https://spacy.io/usage/linguistic-features#named-entities)
  - [Hugging Face Course](https://huggingface.co/course/chapter1)
- ML/DL (Tùy chọn):
  - [Coursera NLP Specialization](https://www.coursera.org/specializations/natural-language-processing)
  - [Hugging Face Transformers Docs](https://huggingface.co/docs/transformers/index)

---

# TODO - Lộ trình học trích xuất hợp đồng

- [ ] Hoàn thiện Python cơ bản và xử lý file PDF, DOC, Excel
- [ ] Thử nghiệm OCR với PaddleOCR trên các file hợp đồng scan
- [ ] Xây dựng pipeline trích xuất text từ hợp đồng qua OCR và xử lý file
- [ ] Học và áp dụng NLP để nhận diện các trường dữ liệu quan trọng trong hợp đồng
- [ ] Tạo project mẫu trích xuất tự động các thông tin: tên bên, số hợp đồng, ngày ký, điều khoản
- [ ] (Tùy chọn) Fine-tune mô hình Transformer nâng cao trích xuất thông tin
- [ ] Triển khai pipeline tự động, lưu trữ dữ liệu vào database hoặc file có cấu trúc
- [ ] Viết tài liệu hướng dẫn và test case cho dự án
- [ ] Cập nhật, cải tiến hiệu quả và độ chính xác của pipeline theo phản hồi thực tế

