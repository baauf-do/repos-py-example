import pdfplumber
import io

from app.models.contract import extract_structured_data_from_text


def parse_contract(file_bytes: bytes) -> dict:
  text = ""
  with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
    for page in pdf.pages:
      text += page.extract_text() + "\n"

  contract_data = extract_structured_data_from_text(text)
  return contract_data
