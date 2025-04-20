import pdfplumber
import os
import pandas as pd
from datetime import datetime

# Định nghĩa đường dẫn file
dtnow = datetime.now()  # current date and time
pdf_path = os.path.join("data", "thong bao dmhc 1.1.2025.pdf")
xls_path = os.path.join("data", f"thong_bao_dmhc_clean-{dtnow.strftime("%Y%m%d%H%M%S")}.xlsx")


def extract_tables_from_pdf(pdf_path):
  """Trích xuất chỉ dữ liệu bảng từ PDF"""
  extracted_data = []
  with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
      tables = page.extract_tables()
      for table in tables:
        for row in table:
          # Lọc bỏ các dòng trống hoặc chứa toàn giá trị None
          if row and any(cell.strip() if cell else "" for cell in row):
            extracted_data.append(row)
  return extracted_data


def save_to_xls(data, xls_path):
  """Lưu dữ liệu bảng vào file Excel"""
  # Chuyển dữ liệu thành DataFrame
  df = pd.DataFrame(data)

  # Loại bỏ các dòng trùng lặp tiêu đề (nếu có)
  if not df.empty:
    header = df.iloc[0]  # Giả sử dòng đầu tiên là tiêu đề
    df_cleaned = df[~df.apply(lambda row: row.equals(header), axis=1)]
    df_cleaned = pd.concat([pd.DataFrame([header]), df_cleaned])  # Giữ lại tiêu đề
    # Lặp qua các cột và thay thế \n trong các cột kiểu chuỗi
    for col in df_cleaned.columns:
      if df_cleaned[col].dtype == "object":  # Kiểm tra kiểu dữ liệu của cột
        df_cleaned[col] = df_cleaned[col].str.replace(r"\n", " ", regex=True)
  else:
    df_cleaned = df

  # Lưu vào file Excel
  df_cleaned.to_excel(xls_path, index=False, header=False)
  print(f"Dữ liệu đã được lưu vào: {xls_path}")


def convert_pdf_to_excel():
  """Hàm chính để trích xuất dữ liệu từ PDF và lưu vào Excel"""
  # Kiểm tra xem file PDF có tồn tại không
  if not os.path.exists(pdf_path):
    print(f"File PDF không tồn tại: {pdf_path}")
    return

  # Đảm bảo thư mục lưu file Excel tồn tại
  os.makedirs(os.path.dirname(xls_path), exist_ok=True)

  print("Đang trích xuất dữ liệu từ các bảng trong PDF...")
  table_data = extract_tables_from_pdf(pdf_path)

  if table_data:
    save_to_xls(table_data, xls_path)
  else:
    print("Không tìm thấy bảng dữ liệu nào trong PDF.")


if __name__ == "__main__":
  convert_pdf_to_excel()
