# app/core/reader.py
# Đây là bộ điều phối chính của pipeline, xử lý cả ảnh và PDF, dùng PaddleOCR để OCR, gọi detect_mrz_region để tìm vùng MRZ, và parse_mrz_text để trích xuất thông tin cụ thể.

import os
import tempfile
from typing import Dict
from app.core.preprocess import preprocess_image
from app.core.pdf_utils import convert_pdf_to_images
from app.core.mrz_detect import detect_mrz_region
from app.core.mrz_parse import parse_mrz_text
from app.utils.utils_logging import log_debug

from paddleocr import PaddleOCR
from PIL import Image
import cv2
import numpy as np

ocr_model = PaddleOCR(use_angle_cls=True, lang='en')


def extract_passport_info(filename: str, file_bytes: bytes) -> Dict:
  """
  Hàm xử lý chính: từ file ảnh hoặc PDF, xử lý và trả thông tin MRZ
  """
  log_debug(f'📥 Bắt đầu xử lý file: {filename}', level='INFO')
  images = []

  if filename.lower().endswith('.pdf'):
    log_debug('📄 Nhận dạng là file PDF. Đang chuyển đổi sang ảnh...', level='INFO')
    images = convert_pdf_to_images(file_bytes)
  else:
    log_debug('🖼️ Nhận dạng là ảnh. Đang lưu tạm để xử lý...', level='INFO')
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[-1]) as tmp:
      tmp.write(file_bytes)
      tmp_path = tmp.name

    img = cv2.imread(tmp_path)
    images = [img]
    os.remove(tmp_path)

  for i, img in enumerate(images):
    log_debug(f'🔄 Đang xử lý ảnh trang {i + 1}/{len(images)}', level='INFO')
    preprocessed = preprocess_image(img)
    mrz_crop = detect_mrz_region(preprocessed, ocr_model)

    if mrz_crop is not None:
      log_debug('📦 Đã phát hiện vùng MRZ. Bắt đầu OCR...', level='INFO')
      text = ocr_image(mrz_crop, ocr_model)
      log_debug(f'🔡 Kết quả OCR MRZ:\n{text}', level='DEBUG')
      parsed = parse_mrz_text(text)
      if parsed:
        log_debug('✅ Trích xuất MRZ thành công.', level='INFO')
        return parsed
      else:
        log_debug('❌ MRZ không hợp lệ hoặc không parse được.', level='WARNING')
    else:
      log_debug('⚠️ Không phát hiện được vùng MRZ trên ảnh này.', level='WARNING')

  raise ValueError('Không thể trích xuất thông tin MRZ từ tài liệu này.')


def ocr_image(image: np.ndarray, ocr_model) -> str:
  """Chạy OCR với PaddleOCR trên ảnh MRZ"""
  pil_img = Image.fromarray(image)
  results = ocr_model.ocr(np.array(pil_img), cls=True)
  lines = [line[1][0] for line in results[0]]
  return '\n'.join(lines)
