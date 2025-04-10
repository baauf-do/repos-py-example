import xlrd
import pandas as pd
import os

# Đọc file .xls
xls_output_path = os.path.join("../data", "thong_bao_dmhc.xls")
workbook = xlrd.open_workbook(xls_output_path)
sheet = workbook.sheet_by_index(0)

# Chuyển sang DataFrame
data = [sheet.row_values(row) for row in range(sheet.nrows)]
df = pd.DataFrame(data)

# Giả sử dòng tiêu đề bị lặp lại có cùng nội dung, ví dụ giống dòng đầu tiên
header = df.iloc[0]
df_cleaned = df[~df.apply(lambda row: row.equals(header), axis=1)]

# Ghi ra file mới
# df_cleaned.to_excel("data/thong_bao_dmhc_clean.xlsx", index=False, header=False)
# print(df_cleaned)

# Lặp qua các cột và thay thế \n trong các cột kiểu chuỗi
for col in df_cleaned.columns:
    if df_cleaned[col].dtype == "object":  # Kiểm tra kiểu dữ liệu của cột
        df_cleaned[col] = df_cleaned[col].str.replace(r"\n", " ", regex=True)

# Hiển thị DataFrame đã được xử lý
print(df_cleaned)
# df_cleaned.to_excel("data/thong_bao_dmhc_clean_done.xlsx", index=False, header=False)
