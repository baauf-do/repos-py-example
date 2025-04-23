# app/core/mrz_detect.py
# Ưu tiên dùng YOLOv8 để crop vùng MRZ chính xác
# Nếu không có model hoặc không detect được, sẽ fallback sang PaddleOCR để dò text dòng MRZ (khoảng 2 dòng, ~44 ký tự)
# Sẽ được cache sau lần đầu tiên load
# Tách biệt phần quản lý model khỏi logic nhận diện MRZ
# Chuẩn hóa và dễ mở rộng nếu sau này bạn có nhiều model hơn
import numpy as np
import cv2  # noqa: F401
from typing import Optional
# from ultralytics import YOLO
from app.models.utils import load_yolo_model
from app.utils.utils_logging import log_debug

# Load YOLO model qua layer models/utils
YOLO_MODEL_PATH = "app/models/yolov8_mrz.pt"
yolo_model = load_yolo_model(YOLO_MODEL_PATH)


def detect_mrz_region(image: np.ndarray, ocr_model=None) -> Optional[np.ndarray]:
  """
  Phát hiện vùng MRZ từ ảnh đầu vào.
  Nếu có YOLO thì dùng YOLO, nếu không thì fallback bằng dò dòng OCR.
  Trả về ảnh đã crop vùng MRZ (nếu tìm thấy), hoặc None.
  """
  log_debug("🔍 Bắt đầu dò MRZ từ ảnh...", level="INFO")

  if yolo_model:
    log_debug("🤖 Sử dụng YOLOv8 để phát hiện vùng MRZ...", level="DEBUG")
    results = yolo_model(image)
    for box in results[0].boxes:
      x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
      conf = box.conf[0].item()
      log_debug(f"📦 YOLO phát hiện bbox: ({x1}, {y1}, {x2}, {y2}) - conf: {conf:.2f}", level="DEBUG")
      if conf > 0.5:
        return image[y1:y2, x1:x2]

  if ocr_model:
    log_debug("🧪 Fallback: Sử dụng PaddleOCR để dò dòng MRZ...", level="DEBUG")
    ocr_result = ocr_model.ocr(image, cls=True)
    lines = [line[1][0] for line in ocr_result[0]]
    mrz_lines = [line for line in lines if len(line) >= 40 and set(line).issubset(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<"))]
    log_debug(f"📄 Fallback MRZ lines: {len(mrz_lines)} dòng khớp", level="DEBUG")
    if len(mrz_lines) >= 2:
      return image  # fallback: trả nguyên ảnh để xử lý tiếp

  log_debug("⚠️ Không phát hiện được MRZ bằng bất kỳ phương pháp nào.", level="WARNING")
  return None
