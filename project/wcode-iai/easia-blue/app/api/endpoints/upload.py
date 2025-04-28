from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
  try:
    file_path = os.path.join("store/input", file.filename)
    with open(file_path, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)

    log_debug(f"Uploaded file: {file.filename}", level="INFO")
    return {"filename": file.filename}

  except Exception as e:
    log_debug(f"Upload failed: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail="Failed to upload file.")
