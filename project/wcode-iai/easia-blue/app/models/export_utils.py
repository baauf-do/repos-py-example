import pandas as pd
import os


def text_to_dataframe(text):
  """
  Chuyển văn bản thành DataFrame.
  :param text: Chuỗi văn bản.
  :return: Pandas DataFrame.
  """
  lines = text.split("\n")
  return pd.DataFrame({"Content": lines})


def export_to_json(df, output_path):
  """
  Xuất DataFrame ra file JSON.
  :param df: Pandas DataFrame.
  :param output_path: Đường dẫn file JSON.
  """
  df.to_json(output_path, orient="records", force_ascii=False)


def export_to_excel(df, output_path):
  """
  Xuất DataFrame ra file Excel.
  :param df: Pandas DataFrame.
  :param output_path: Đường dẫn file Excel.
  """
  df.to_excel(output_path, index=False)
