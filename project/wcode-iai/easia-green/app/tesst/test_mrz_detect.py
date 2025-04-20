# app/test/test_mrz_detect.py
import os
import pytest
from app.core.mrz_detect import detect_mrz_yolo


def test_detect_mrz_yolo():
  img_path = "store/input/sample_passport.jpg"
  model_path = "app/models/yolov8_mrz.pt"

  if not os.path.exists(img_path) or not os.path.exists(model_path):
    pytest.skip("Thiếu ảnh mẫu hoặc model YOLOv8 để test")

  result = detect_mrz_yolo(img_path, model_path)
  assert result is not None
  assert isinstance(result, dict)
  assert "image" in result and result["image"] is not None
