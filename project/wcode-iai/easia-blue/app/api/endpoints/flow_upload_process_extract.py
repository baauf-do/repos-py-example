"""
➡ Upload file PDF ➔
➡ Process phân loại file (text/scan/mixed) ➔
➡ Extract dữ liệu contract ➔
➡ Trả về kết quả JSON tất cả trong 1 API call duy nhất.
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.storage_service import StorageService
from app.services.pdf_processor import PDFProcessor
from app.services.contract_extractor import ContractExtractor
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.post("/upload-process-extract/")
async def upload_process_extract(file: UploadFile = File(...)):
  try:
    # 1. Upload file vào store/input
    upload_folder = StorageService.get_upload_folder()
    file_path = upload_folder / file.filename

    with open(file_path, "wb") as buffer:
      content = await file.read()
      buffer.write(content)

    log_debug(f"Uploaded file: {file.filename}", level="INFO")

    # 2. Validate file
    pdf_path = StorageService.validate_uploaded_pdf(file.filename)

    # 3. Phân loại PDF (text, scan, mixed)
    pdf_type = PDFProcessor.check_pdf_type(pdf_path)
    log_debug(f"Detected PDF type: {pdf_type} for {file.filename}", level="INFO")

    # 4. Extract contract dữ liệu
    output_folder = StorageService.get_output_folder()

    if pdf_type == "text":
      result = ContractExtractor.extract_text_only(pdf_path, output_folder)
    elif pdf_type == "scan":
      result = ContractExtractor.extract_scan_only(pdf_path, output_folder)
    elif pdf_type == "mixed":
      result = ContractExtractor.extract_mixed(pdf_path, output_folder)
    else:
      raise ValueError(f"Không xác định được loại file PDF: {pdf_type}")

    log_debug(f"Successfully extracted contract data from {file.filename}", level="INFO")

    # 5. Trả kết quả
    return {
      "status": "success",
      "filename": file.filename,
      "pdf_type": pdf_type,
      "data": result
    }

  except Exception as e:
    log_debug(f"Upload-Process-Extract failed for {file.filename}: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail=f"Failed to upload and extract contract data: {str(e)}")
