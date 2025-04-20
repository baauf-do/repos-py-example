# app/core/preprocess.py
import cv2
import numpy as np
from core.utils import log_debug


def preprocess_image(image: np.ndarray) -> np.ndarray:
  """
  Tiền xử lý ảnh:
  - Chuyển grayscale
  - Resize về chiều rộng chuẩn (nếu cần)
  - Tăng tương phản bằng CLAHE
  - Lọc nhiễu và làm mượt ảnh bằng bộ lọc Bilateral để khử nhiễu
  """
  log_debug("🧼 Bắt đầu tiền xử lý ảnh...", level="INFO")

  # Resize nếu quá lớn
  max_width = 1000
  if image.shape[1] > max_width:
    scale = max_width / image.shape[1]
    image = cv2.resize(image, None, fx=scale, fy=scale)
    log_debug(f"📐 Resize ảnh về chiều rộng {max_width}px", level="DEBUG")

  # Chuyển grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  log_debug("🎨 Chuyển ảnh sang grayscale", level="DEBUG")

  # Tăng tương phản (CLAHE)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  enhanced = clahe.apply(gray)
  log_debug("🔆 Tăng tương phản bằng CLAHE", level="DEBUG")

  # Làm mượt để loại bỏ nhiễu nhỏ
  smoothed = cv2.bilateralFilter(enhanced, d=9, sigmaColor=75, sigmaSpace=75)
  log_debug("💧 Làm mượt ảnh bằng bilateral filter", level="DEBUG")

  return smoothed
