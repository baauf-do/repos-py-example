import os
import json
import pdfplumber
from app.models.export_utils import export_to_json
from app.services.contract_parser import ContractParser
from app.utils.decorator_logging import log_execution_time
from app.utils.logging_utils import log_debug


class ExtractTextOnly:

  @staticmethod
  @log_execution_time
  def run(pdf_path: str, output_folder: str) -> dict:
    """
    2-step pipeline:
    1. Extract raw text from PDF.
    2. Parse structured JSON data.
    """
    # Step 1: Extract raw text
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
        extracted = page.extract_text()
        if extracted:
          text += extracted + "\n"

    if not text.strip():
      raise ValueError("Không trích xuất được text từ file PDF.")

    # Save raw text vào file JSON
    raw_folder = "store/temp"
    os.makedirs(raw_folder, exist_ok=True)
    raw_filename = os.path.basename(pdf_path).replace(".pdf", "_raw.json")
    raw_path = os.path.join(raw_folder, raw_filename)

    with open(raw_path, "w", encoding="utf-8") as f:
      json.dump({"raw_text": text}, f, ensure_ascii=False, indent=2)

    log_debug(f"Saved raw text to {raw_path}", level="INFO")

    # Step 2: Parse structured JSON từ raw
    parsed_data = ContractParser.parse(text)

    # Nếu parsed_data là dict rồi thì không dùng .dict()
    if isinstance(parsed_data, dict):
      parsed_dict = parsed_data
    else:
      parsed_dict = parsed_data.dict()

    # Save final structured JSON
    final_filename = os.path.basename(pdf_path).replace(".pdf", ".json")
    final_path = os.path.join(output_folder, final_filename)
    export_to_json(parsed_dict, final_path)

    log_debug(f"Exported parsed data to {final_path}", level="INFO")

    return parsed_dict
