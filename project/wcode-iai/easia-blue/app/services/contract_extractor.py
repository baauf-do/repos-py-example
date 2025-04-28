from app.core.extract_text_only import ExtractTextOnly
from app.core.extract_scan_only import ExtractScanOnly
from app.core.extract_mixed import ExtractMixed

class ContractExtractor:

  @staticmethod
  def extract_text_only(pdf_path: str, output_folder: str):
    return ExtractTextOnly.run(pdf_path, output_folder)

  @staticmethod
  def extract_scan_only(pdf_path: str, output_folder: str):
    return ExtractScanOnly.run(pdf_path, output_folder)

  @staticmethod
  def extract_mixed(pdf_path: str, output_folder: str):
    return ExtractMixed.run(pdf_path, output_folder)
