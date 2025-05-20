from fastapi import APIRouter, HTTPException
from app.services.storage_service import StorageService
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.get("/uploaded-files/")
async def list_uploaded_files():
  try:
    files = StorageService.list_uploaded_files()
    log_debug(f"Listed uploaded files: found {len(files)} files", level="INFO")
    return {"files": files}
  except Exception as e:
    log_debug(f"Error listing uploaded files: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail="Failed to list uploaded files.")
