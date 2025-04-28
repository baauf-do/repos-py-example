from fastapi import APIRouter
import os
from app.utils.logging_utils import log_debug  # Thêm log_debug

router = APIRouter()


@router.get("/uploaded-files/")
async def list_uploaded_files():
  """
  Trả về danh sách file đã upload trong store/input/
  """
  upload_folder = "store/input"
  try:
    files = [
      f for f in os.listdir(upload_folder)
      if os.path.isfile(os.path.join(upload_folder, f))
    ]
    log_debug(f"Listed uploaded files: found {len(files)} files", level="INFO")  # Ghi log thành công
    return {"files": files}

  except Exception as e:
    log_debug(f"Error listing uploaded files: {str(e)}", level="ERROR")  # Ghi log lỗi
    return {"error": str(e)}
