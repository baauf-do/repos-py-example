from fastapi import APIRouter
from app.services.contract_extractor import ContractExtractor
from app.services.pdf_processor import PDFProcessor
from app.utils.logging_utils import log_debug

router = APIRouter()

"""Xử lý file chỉ text"""
@router.post("/process-text-pdf/")
async def process_text_pdf(file_name: str):
  """
  Xử lý PDF chỉ có text
  """
  try:
    pdf_path = f"store/input/{file_name}"
    output_folder = "store/output"

    pdf_type = PDFProcessor.check_pdf_type(pdf_path)
    if pdf_type != "text":
      return {"error": f"File {file_name} không phải PDF text thuần."}

    result = ContractExtractor.extract_text_only(pdf_path, output_folder)
    log_debug(f"Processed text-only PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing text-only PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}

"""Xử lý file chỉ scan"""
@router.post("/process-scan-pdf/")
async def process_scan_pdf(file_name: str):
  """
  Xử lý PDF chỉ có scan (ảnh)
  """
  try:
    pdf_path = f"store/input/{file_name}"
    output_folder = "store/output"

    pdf_type = PDFProcessor.check_pdf_type(pdf_path)
    if pdf_type != "scan":
      return {"error": f"File {file_name} không phải PDF scan."}

    result = ContractExtractor.extract_scan_only(pdf_path, output_folder)
    log_debug(f"Processed scan-only PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing scan-only PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}

"""Xử lý file mixed (text + scan)"""
@router.post("/process-mixed-pdf/")
async def process_mixed_pdf(file_name: str):
  """
  Xử lý PDF mixed (text + scan)
  """
  try:
    pdf_path = f"store/input/{file_name}"
    output_folder = "store/output"

    pdf_type = PDFProcessor.check_pdf_type(pdf_path)
    if pdf_type != "mixed":
      return {"error": f"File {file_name} không phải PDF mixed."}

    result = ContractExtractor.extract_mixed(pdf_path, output_folder)
    log_debug(f"Processed mixed-type PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing mixed-type PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}
