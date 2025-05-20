from fastapi import APIRouter, HTTPException
from app.services.contract_extractor import ContractExtractor
from app.services.storage_service import StorageService
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.post("/extract/")
async def extract(file_name: str):
  try:
    # Validate và lấy đúng file path
    pdf_path = StorageService.validate_uploaded_pdf(file_name)

    # Lấy output folder
    output_folder = StorageService.get_output_folder()

    # Thực hiện extract
    result = ContractExtractor.extract_contract(pdf_path, output_folder)

    log_debug(f"Extracted data from file: {file_name}", level="INFO")
    return {"status": "success", "data": result}

  except Exception as e:
    log_debug(f"Extraction failed for file {file_name}: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail="Failed to extract contract data.")
