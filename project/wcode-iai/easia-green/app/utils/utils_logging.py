import os
from datetime import datetime
import logging

# Tạo thư mục logs nếu chưa tồn tại
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Đường dẫn file log theo ngày
log_filename = os.path.join(LOG_DIR, f'log_{datetime.now().strftime("%Y%m%d")}.log')


def log_debug(message: str, level: str = 'INFO'):
  """
  Ghi log ra console và file log theo ngày, kèm cấp độ log.
  Chỉ chấp nhận level hợp lệ: INFO, DEBUG, WARNING, ERROR
  """
  allowed_levels = {'INFO', 'DEBUG', 'WARNING', 'ERROR'}
  if level not in allowed_levels:
    level = 'INFO'

  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  log_line = f'[{timestamp}] [{level}] {message}'
  print(log_line)

  with open(log_filename, 'a', encoding='utf-8') as f:
    f.write(log_line + '\n')


def configure_logging():
  """
  Cấu hình logging toàn cục cho ứng dụng.
  """
  logging.basicConfig(
    level=logging.INFO,  # Mức độ log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Định dạng log
    handlers=[
      logging.FileHandler(log_filename),  # Ghi log vào file
      logging.StreamHandler(),  # Ghi log ra console
    ],
  )
  return logging.getLogger(__name__)
