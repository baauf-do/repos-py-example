from fastapi import APIRouter, HTTPException
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.post("/push-db/")
async def push_to_db(file_name: str):
  try:
    # TODO: đọc JSON và insert vào SQL Server
    log_debug(f"Pushed JSON {file_name} to database.", level="INFO")
    return {"status": "success", "message": f"Inserted {file_name} into database"}

  except Exception as e:
    log_debug(f"Push to DB failed for file {file_name}: {str(e)}", level="ERROR")
    raise HTTPException(status_code=500, detail="Failed to insert into database.")
