import pdfplumber
import json

def extract_pdf_text(file):
  """Trích xuất văn bản từ file PDF."""
  with pdfplumber.open(file) as pdf:
    full_text = ""
    for page in pdf.pages:
      full_text += page.extract_text()
  return full_text

def extract_pdf_scan_image_text(pdf_file):
  """
  Trích xuất văn bản từ file PDF.
  """
  with pdfplumber.open(pdf_file) as pdf:
    text = ""
    for page in pdf.pages:
      text += page.extract_text() + "\n"
  return text.strip()


def convert_to_json(text):
  """
  Chuyển đổi văn bản thuần thành JSON.
  """
  return {"content": text}


def convert_to_ndjson(text):
  """
  Chuyển đổi văn bản thuần thành NDJSON (mỗi dòng là một đối tượng JSON).
  """
  lines = text.split("\n")
  ndjson = [json.dumps({"line": line}) for line in lines if line.strip()]
  return "\n".join(ndjson)
