# app/core/utils.py
import os
import re
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def is_valid_date(date_str: str) -> bool:
  from .utils import log_debug
  log_debug("🔍 Kiểm tra ngày hợp lệ: {}".format(date_str), level="INFO")
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    log_debug(f"✅ Ngày hợp lệ: {date_str}", level="DEBUG")
    return True
  except ValueError:
    log_debug(f"❌ Ngày không hợp lệ: {date_str}", level="WARNING")
    return False


def clean_text(text: str) -> str:
  from .utils import log_debug
  cleaned = re.sub(r"[^A-Z0-9< ]", "", text.upper()).strip()
  log_debug(f"🧹 Làm sạch OCR: '{text}' -> '{cleaned}'", level="DEBUG")
  if not cleaned:
    log_debug(f"⚠️ Kết quả làm sạch OCR rỗng từ đầu vào: '{text}'", level="WARNING")
  return cleaned


def log_debug(message: str, level: str = "INFO"):
  """
  Ghi log ra console và file log theo ngày, kèm cấp độ log.
  Chỉ chấp nhận level hợp lệ: INFO, DEBUG, WARNING, ERROR
  """
  allowed_levels = {"INFO", "DEBUG", "WARNING", "ERROR"}
  if level not in allowed_levels:
    level = "INFO"

  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  log_line = f"[{timestamp}] [{level}] {message}"
  print(log_line)

  log_filename = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y%m%d')}.log")
  with open(log_filename, "a", encoding="utf-8") as f:
    f.write(log_line + "\n")
