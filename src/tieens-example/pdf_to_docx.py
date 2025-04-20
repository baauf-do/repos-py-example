import os
from pdf2image import convert_from_path
import pytesseract
from docx import Document

# Cấu hình thư mục
# input_folder = r"C:\Users\tiendo\Documents\input_pdf"
# output_folder = r"C:\Users\tiendo\Documents\output_docx"
input_folder = r'data\input'
output_folder = r'data\output'
os.makedirs(output_folder, exist_ok=True)

# Lặp qua từng file PDF trong thư mục
for file_name in os.listdir(input_folder):
  if file_name.lower().endswith('.pdf'):
    print(f'🔍 Đang xử lý: {file_name}')
    pdf_path = os.path.join(input_folder, file_name)

    try:
      images = convert_from_path(pdf_path, dpi=300)
      doc = Document()

      for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='vie')
        doc.add_paragraph(text.strip())
        print(f'    Trang {i + 1}: {len(text.strip())} ký tự nhận được')

      output_name = os.path.splitext(file_name)[0] + '.docx'
      output_path = os.path.join(output_folder, output_name)
      doc.save(output_path)
      print(f'✅ Đã lưu DOCX: {output_path}\n')

    except Exception as e:
      print(f'❌ Lỗi khi xử lý {file_name}: {e}')
