import os
import logging
from datetime import datetime

# Base logs directory
BASE_LOG_DIR = "logs"

# Sub-folder theo ngày
today_str = datetime.now().strftime("%Y%m%d")
TODAY_LOG_DIR = os.path.join(BASE_LOG_DIR, today_str)

# Tạo folder ngày nếu chưa có
os.makedirs(TODAY_LOG_DIR, exist_ok=True)

# Định nghĩa path từng loại log file
LOG_FILES = {
  "request": os.path.join(TODAY_LOG_DIR, "request.log"),
  "error": os.path.join(TODAY_LOG_DIR, "error.log"),
  "debug": os.path.join(TODAY_LOG_DIR, "debug.log"),
  "info": os.path.join(TODAY_LOG_DIR, "info.log"),
}


# Hàm cấu hình logger
def configure_logging():
  logger = logging.getLogger("easia-blue")
  logger.setLevel(logging.DEBUG)

  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

  # Handler cho từng loại log
  request_handler = logging.FileHandler(LOG_FILES["request"], encoding="utf-8")
  request_handler.setLevel(logging.INFO)
  request_handler.setFormatter(formatter)

  error_handler = logging.FileHandler(LOG_FILES["error"], encoding="utf-8")
  error_handler.setLevel(logging.ERROR)
  error_handler.setFormatter(formatter)

  debug_handler = logging.FileHandler(LOG_FILES["debug"], encoding="utf-8")
  debug_handler.setLevel(logging.DEBUG)
  debug_handler.setFormatter(formatter)

  info_handler = logging.FileHandler(LOG_FILES["info"], encoding="utf-8")
  info_handler.setLevel(logging.INFO)
  info_handler.setFormatter(formatter)

  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)
  console_handler.setLevel(logging.DEBUG)

  # Nếu logger chưa có handler thì add
  if not logger.handlers:
    logger.addHandler(request_handler)
    logger.addHandler(error_handler)
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(console_handler)

  return logger


# Tạo logger sẵn
logger = configure_logging()


# Hàm ghi log nhanh
def log_debug(message: str, level: str = "INFO"):
  if level == "DEBUG":
    logger.debug(message)
  elif level == "WARNING":
    logger.warning(message)
  elif level == "ERROR":
    logger.error(message)
  else:
    logger.info(message)
