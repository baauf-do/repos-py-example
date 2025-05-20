from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.storage_service import StorageService
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
  try:
    # Lấy đúng thư mục upload input
    upload_folder = StorageService.get_upload_folder()

    # Tạo file path đầy đủ
    file_path = upload_folder / file.filename

    # Save file upload
    with open(file_path, "wb") as buffer:
      content = await file.read()
      buffer.write(content)

    log_debug(f"Uploaded file: {file.filename}", level="INFO")
    return {"filename": file.filename}

  except Exception as e:
    log_debug(f"Upload failed: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail="Failed to upload file.")
