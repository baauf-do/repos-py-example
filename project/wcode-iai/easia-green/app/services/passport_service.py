# app/services/passport_service.py
from typing import Dict
from app.core.reader import extract_passport_info
from app.utils.utils_logging import configure_logging

# Cấu hình logging
logger = configure_logging()


class PassportService:
  @staticmethod
  def process_passport(file_name: str, file_bytes: bytes) -> Dict:
    """
    Xử lý trích xuất thông tin từ file hộ chiếu (ảnh/PDF), gọi tới core layer.
    """
    try:
      # log_debug(f'📂 [Service] Xử lý passport: {file_name}', level='INFO')
      logger.info(f'📂 [Service] Processing passport: {file_name}')
      result = extract_passport_info(file_name, file_bytes)
      # Nếu OCR thất bại, trả về thông báo lỗi
      if not result:
        logger.warning(f'⚠️ [Service] OCR failed for file: {file_name}')
        return {'error': 'Failed to extract passport information. Please try again with a clearer image.'}

      # log_debug(f'📤 [Service] Trích xuất hoàn tất: {result.get("passport_number", "UNKNOWN")}', level='INFO')
      logger.info(f'📤 [Service] Extraction completed: Passport Number - {result.get("passport_number", "UNKNOWN")}')
      return result
    except Exception as e:
      logger.error(f'❌ [Service] An unexpected error occurred: {str(e)}', exc_info=True)
      return {'error': f'An unexpected error occurred: {str(e)}'}
