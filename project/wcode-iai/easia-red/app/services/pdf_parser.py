import pdfplumber

def extract_pdf_text(file):
  """Trích xuất văn bản từ file PDF."""
  with pdfplumber.open(file) as pdf:
    full_text = ""
    for page in pdf.pages:
      full_text += page.extract_text()
  return full_text
