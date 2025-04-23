# ✅ app/services/data_loader.py

import os
import pandas as pd
from app.core.config import EXCEL_FOLDER


def load_all_excel_data():
  all_data = []
  for file_name in os.listdir(EXCEL_FOLDER):
    if file_name.endswith('.xlsx'):
      file_path = os.path.join(EXCEL_FOLDER, file_name)
      try:
        df = pd.read_excel(file_path)
        all_data.extend(df.to_dict(orient='records'))
      except Exception as e:
        print(f'Error loading {file_name}: {e}')
  return all_data


def load_excel_data(file_path: str):
  try:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')  # Trả về danh sách dict
  except Exception as e:
    print(f'Error loading Excel: {e}')
    return []
