# app/services/passport_service.py
from typing import Dict
from core.reader import extract_passport_info
from core.utils import log_debug


class PassportService:
  @staticmethod
  def process_passport(file_name: str, file_bytes: bytes) -> Dict:
    """
    Xử lý trích xuất thông tin từ file hộ chiếu (ảnh/PDF), gọi tới core layer.
    """
    log_debug(f"📂 [Service] Xử lý passport: {file_name}", level="INFO")
    result = extract_passport_info(file_name, file_bytes)
    log_debug(f"📤 [Service] Trích xuất hoàn tất: {result.get('passport_number', 'UNKNOWN')}", level="INFO")
    return result
