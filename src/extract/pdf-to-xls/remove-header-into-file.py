import xlrd
import pandas as pd
import os

# Đọc file .xls
xls_input_path = os.path.join("data", "thong_bao_dmhc.xls")
workbook = xlrd.open_workbook(xls_input_path)
sheet = workbook.sheet_by_index(0)

# Chuyển sang DataFrame
data = [sheet.row_values(row) for row in range(sheet.nrows)]
df = pd.DataFrame(data)

# Giả sử dòng tiêu đề bị lặp lại có cùng nội dung, ví dụ giống dòng đầu tiên
header = df.iloc[0]
df_cleaned = df[~df.apply(lambda row: row.equals(header), axis=1)]

# Ghi ra file mới
df_cleaned.to_excel("data/thong_bao_dmhc_clean.xlsx", index=False, header=False)
