import pdfplumber
import xlwt
import os

# Định nghĩa đường dẫn file
pdf_path = os.path.join("data", "thong bao dmhc 1.1.2025.pdf")
xls_path = os.path.join("data", "thong_bao_dmhc.xls")


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
    """Lưu dữ liệu bảng vào file XLS"""
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")

    for row_idx, row in enumerate(data):
        for col_idx, cell in enumerate(row):
            sheet.write(row_idx, col_idx, cell if cell else "")

    workbook.save(xls_path)


def convert_pdf_to_excel():
    print("Đang trích xuất dữ liệu từ các bảng trong PDF...")
    table_data = extract_tables_from_pdf(pdf_path)

    if table_data:
        save_to_xls(table_data, xls_path)
        print(f"Dữ liệu đã được lưu vào: {xls_path}")
    else:
        print("Không tìm thấy bảng dữ liệu nào trong PDF.")


if __name__ == "__main__":
    convert_pdf_to_excel()
