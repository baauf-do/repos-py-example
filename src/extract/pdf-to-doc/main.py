# Khai báo thư viện sử dung
from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os


def convert_pdf_to_word(pdf_path, docx_path, lang="vie"):
  # Kiểm tra đường dẫn có tồn tại không? False là sai đường dẫn hoặc file không tồn tại
  if not os.path.exists(pdf_path):
    print("False là sai đường dẫn hoặc file không tồn tại")
    return

  # True là đúng đường dẫn hoặc file tồn tại
  else:
    print("True là đúng đường dẫn hoặc file tồn tại")
    # Chỉ định đường dẫn đến tesseract nếu bạn dùng Windows (bỏ dòng này nếu trên Linux/macOS)
    pytesseract.pytesseract.tesseract_cmd = (
      r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
    print(f"🔄 Đang chuyển đổi: {pdf_path}")
    try:
      # Chuyển PDF thành ảnh (mỗi trang là 1 ảnh)
      images = convert_from_path(pdf_path, dpi=300)
    except Exception as e:
      print(f"❌ Lỗi khi chuyển PDF sang ảnh: {e}")
      return

    # Tạo một file Word mới
    doc = Document()

    # OCR từng ảnh để trích xuất văn bản
    for i, image in enumerate(images):
      print(f"📄 OCR trang {i + 1}...")
      try:
        text = pytesseract.image_to_string(image, lang=lang)
      except Exception as e:
        print(f"⚠️ Lỗi OCR trang {i + 1}: {e}")
        continue

      doc.add_paragraph(text)
      doc.add_page_break()

    # Lưu file Word
    doc.save(docx_path)
    print(f"✅ Hoàn tất! File Word đã lưu tại: {docx_path}")


if __name__ == "__main__":
  input_pdf = os.path.join("data", "input", "cay-thuoc-an-giang_full.pdf")
  output_docx = os.path.join("data", "output", "cay-thuoc-an-giang_full.docx")

  convert_pdf_to_word(input_pdf, output_docx)
