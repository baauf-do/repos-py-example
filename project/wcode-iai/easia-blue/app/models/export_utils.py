import pandas as pd


def text_to_dataframe(text):
  """
  Chuyển văn bản thành DataFrame.
  :param text: Chuỗi văn bản.
  :return: Pandas DataFrame.
  """
  lines = text.split("\n")
  return pd.DataFrame({"Content": lines})


def export_to_json(data: dict, output_path: str):
  """
  Xuất DataFrame ra file JSON.
  :param dict: Pandas DataFrame.
  :param output_path: Đường dẫn file JSON.
  """
  import json
  with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


def export_to_excel(data: dict, output_path: str):
  """
  Xuất DataFrame ra file Excel.
  :param dict: Pandas DataFrame.
  :param output_path: Đường dẫn file Excel.
  """
  df = pd.DataFrame([data])
  df.to_excel(output_path, index=False)
