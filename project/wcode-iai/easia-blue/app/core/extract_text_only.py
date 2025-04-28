import os
import pdfplumber
from app.models.export_utils import export_to_json
from app.services.contract_parser import ContractParser
from app.utils.decorator_logging import log_execution_time


class ExtractTextOnly:

  @staticmethod
  @log_execution_time
  def run(pdf_path: str, output_folder: str) -> dict:
    """
    Xử lý PDF chỉ chứa text.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
        text += page.extract_text() or ""

    parsed_data = ContractParser.parse(text)

    json_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".json"))
    export_to_json(parsed_data.dict(), json_path)

    return parsed_data.dict()
