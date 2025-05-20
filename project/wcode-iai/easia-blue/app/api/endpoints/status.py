from fastapi import APIRouter
from app.utils.logging_utils import log_debug

router = APIRouter()


@router.get("/status/")
async def server_status():
  log_debug("Health check - server status OK", level="INFO")
  return {"status": "running"}
