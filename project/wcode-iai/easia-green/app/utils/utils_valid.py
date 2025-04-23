# app/core/utils.py
import re
from datetime import datetime
from app.utils.utils_logging import log_debug


def is_valid_date(date_str: str) -> bool:
  """
  Kiểm tra xem chuỗi ngày có hợp lệ theo định dạng YYYY-MM-DD hay không.
  """
  log_debug(f'🔍 Kiểm tra ngày hợp lệ: {date_str}', level='INFO')
  try:
    datetime.strptime(date_str, '%Y-%m-%d')
    log_debug(f'✅ Ngày hợp lệ: {date_str}', level='DEBUG')
    return True
  except ValueError:
    log_debug(f'❌ Ngày không hợp lệ: {date_str}', level='WARNING')
    return False


def clean_text(text: str) -> str:
  """
  Làm sạch chuỗi văn bản OCR, chỉ giữ lại ký tự chữ hoa, số, và ký tự đặc biệt '<'.
  """
  cleaned = re.sub(r'[^A-Z0-9< ]', '', text.upper()).strip()
  log_debug(f"🧹 Làm sạch OCR: '{text}' -> '{cleaned}'", level='DEBUG')
  if not cleaned:
    log_debug(f"⚠️ Kết quả làm sạch OCR rỗng từ đầu vào: '{text}'", level='WARNING')
  return cleaned
