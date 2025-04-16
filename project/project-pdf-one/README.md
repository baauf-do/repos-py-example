# ⚙️ Cách dùng:
1. Cài các thư viện:
```bash
pip install paddleocr
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
pip install pdf2image python-docx pillow
```
2. Đặt file PDF vào thư mục pdf/ và chạy:


```bash
python paddleocr_ocr.py
```


3. Cau truc thư mục dự án dạng cây
```bash
project_pdf/
├── pdf/                          # 📂 File PDF gốc
│   └── full_700_pages.pdf
├── images/                       # 📂 Ảnh từng trang sau khi convert
│   └── page_0001.jpg
│   └── ...
├── output/                       # 📂 Kết quả xuất ra (Word & text)
│   ├── cay_thuoc_part1.docx
│   ├── cay_thuoc_part2.docx
│   ├── ...
│   └── cay_thuoc_ocr_full.txt
├── tesseract/                    # (Tuỳ chọn) nếu cần tesseract hỗ trợ thêm
├── paddleocr_ocr.py              # 🧠 Script xử lý OCR nâng cao với PaddleOCR
└── README.md                     # (Tuỳ chọn) hướng dẫn cài đặt/chạy
```

4. Cài setuptools vào Python environment của bạn
```bash
pip install setuptools
```
