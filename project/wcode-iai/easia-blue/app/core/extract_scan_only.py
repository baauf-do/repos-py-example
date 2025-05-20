import os
from app.services.pdf_processor import PDFProcessor
from app.services.yolo_detector import YoloDetector
from app.services.ocr_reader import OCRReader
from app.models.export_utils import export_to_json
from app.services.contract_parser import ContractParser
from app.utils.decorator_logging import log_execution_time


class ExtractScanOnly:

  @staticmethod
  @log_execution_time
  def run(pdf_path: str, output_folder: str) -> dict:
    """
    Xử lý PDF chỉ chứa ảnh scan.
    """
    images = PDFProcessor.pdf_to_images(pdf_path, output_folder)
    detector = YoloDetector()
    reader = OCRReader()
    extracted_texts = []

    for img_path in images:
      boxes = detector.detect(img_path)
      for box in boxes:
        # TODO: Crop vùng box ảnh và OCR vùng đó
        extracted_texts.append("Detected text from region")

    text = " ".join(extracted_texts)
    parsed_data = ContractParser.parse(text)

    # Nếu parsed_data là dict rồi thì không dùng .dict()
    if isinstance(parsed_data, dict):
      parsed_dict = parsed_data
    else:
      parsed_dict = parsed_data.dict()

    json_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".json"))
    export_to_json(parsed_dict, json_path)

    return parsed_dict
