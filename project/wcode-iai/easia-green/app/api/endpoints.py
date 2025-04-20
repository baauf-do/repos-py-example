# app/api/endpoints.py
# Nó chứa route chính /api/extract-passport và gọi hàm extract_passport_info(...) từ pipeline.
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.passport_service import PassportService

router = APIRouter()


@router.post("/extract-passport")
async def extract_passport(file: UploadFile = File(...)):
  if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".pdf")):
    raise HTTPException(status_code=400, detail="Unsupported file format")

  try:
    contents = await file.read()
    result = PassportService.process_passport(file.filename, contents)
    return JSONResponse(content=result)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
