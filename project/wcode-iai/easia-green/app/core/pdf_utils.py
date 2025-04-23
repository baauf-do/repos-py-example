# app/core/pdf_utils.py
import fitz  # PyMuPDF
import numpy as np
import cv2
from typing import List
from io import BytesIO  # noqa: F401
from app.utils.utils_logging import log_debug


def convert_pdf_to_images(pdf_bytes: bytes) -> List[np.ndarray]:
  """
  Chuyển PDF bytes thành danh sách ảnh (mỗi trang 1 ảnh)
  Trả về list ảnh numpy array (BGR)
  """
  log_debug('📄 Đang chuyển đổi PDF thành ảnh...', level='INFO')
  images = []

  try:
    pdf = fitz.open(stream=pdf_bytes, filetype='pdf')
  except Exception as e:
    log_debug(f'❌ Không thể mở file PDF: {e}', level='ERROR')
    return images

  for page_num in range(len(pdf)):
    try:
      page = pdf[page_num]
      pix = page.get_pixmap(dpi=300)
      img_data = pix.tobytes('ppm')
      img_array = np.frombuffer(img_data, dtype=np.uint8)
      img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
      if img is not None:
        images.append(img)
        log_debug(f'📎 Đã chuyển trang {page_num + 1} thành ảnh ({img.shape})', level='DEBUG')
      else:
        log_debug(f'⚠️ Không đọc được ảnh từ trang {page_num + 1}', level='WARNING')
    except Exception as e:
      log_debug(f'❌ Lỗi xử lý trang {page_num + 1}: {e}', level='ERROR')

  log_debug(f'✅ Tổng số ảnh chuyển được từ PDF: {len(images)}', level='INFO')
  return images
