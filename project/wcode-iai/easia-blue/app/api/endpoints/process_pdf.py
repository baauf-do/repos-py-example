from fastapi import APIRouter
from app.services.contract_extractor import ContractExtractor
from app.services.pdf_processor import PDFProcessor
from app.services.storage_service import StorageService
from app.utils.logging_utils import log_debug

router = APIRouter()

"""Xử lý file chỉ text"""


@router.post("/process-text-pdf/")
async def process_text_pdf(file_name: str):
  try:
    # Validate file
    pdf_path = StorageService.validate_uploaded_pdf(file_name)

    # Kiểm tra loại file
    pdf_type = PDFProcessor.check_pdf_type(str(pdf_path))
    if pdf_type != "text":
      return {"error": f"File {file_name} không phải PDF text thuần."}

    output_folder = StorageService.get_output_folder()
    result = ContractExtractor.extract_text_only(str(pdf_path), str(output_folder))
    log_debug(f"Processed text-only PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing text-only PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}


"""Xử lý file chỉ scan"""


@router.post("/process-scan-pdf/")
async def process_scan_pdf(file_name: str):
  try:
    pdf_path = StorageService.validate_uploaded_pdf(file_name)

    pdf_type = PDFProcessor.check_pdf_type(str(pdf_path))
    if pdf_type != "scan":
      return {"error": f"File {file_name} không phải PDF scan."}

    output_folder = StorageService.get_output_folder()
    result = ContractExtractor.extract_scan_only(str(pdf_path), str(output_folder))
    log_debug(f"Processed scan-only PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing scan-only PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}


"""Xử lý file mixed (text + scan)"""


@router.post("/process-mixed-pdf/")
async def process_mixed_pdf(file_name: str):
  try:
    pdf_path = StorageService.validate_uploaded_pdf(file_name)

    pdf_type = PDFProcessor.check_pdf_type(str(pdf_path))
    if pdf_type != "mixed":
      return {"error": f"File {file_name} không phải PDF mixed."}

    output_folder = StorageService.get_output_folder()
    result = ContractExtractor.extract_mixed(str(pdf_path), str(output_folder))
    log_debug(f"Processed mixed-type PDF: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Error processing mixed-type PDF: {str(e)}", level="ERROR")
    return {"error": str(e)}
