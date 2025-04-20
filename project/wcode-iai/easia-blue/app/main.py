import os
from services.pdf_processor import PDFProcessor
from models.export_utils import text_to_dataframe, export_to_json, export_to_excel
from datetime import datetime

dtnow = datetime.now()  # current date and time


def main():
  input_dir = "store/input"
  output_dir = "store/output"
  temp_dir = "store/temp"

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  processor = PDFProcessor(input_dir, temp_dir)

  for file_name in os.listdir(input_dir):
    if file_name.endswith(".pdf"):
      pdf_path = os.path.join(input_dir, file_name)
      print(f"Đang xử lý file: {file_name}")

      # Tùy chọn phương pháp xử lý
      method = "text"  # Hoặc "image"
      text = processor.process_pdf(pdf_path, method=method)

      # Chuyển văn bản thành DataFrame
      df = text_to_dataframe(text)

      print(df)
      # Xuất dữ liệu
      json_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}-{dtnow.strftime('%Y%m%d%H%M%S')}.json")
      excel_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}-{dtnow.strftime('%Y%m%d%H%M%S')}.xlsx")
      export_to_json(df, json_path)
      export_to_excel(df, excel_path)

      print(f"Đã xuất dữ liệu: {json_path}, {excel_path}")


if __name__ == "__main__":
  main()
