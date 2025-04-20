# app/test/test_passport_services.py
import os
import pytest
from app.services.passport_services import extract_info_from_passport


def test_extract_info_from_passport():
  img_path = "store/input/sample_passport.jpg"
  model_path = "app/models/yolov8_mrz.pt"

  if not os.path.exists(img_path) or not os.path.exists(model_path):
    pytest.skip("Thiếu ảnh mẫu hoặc model để test")

  result = extract_info_from_passport(img_path)
  assert isinstance(result, dict)
  assert "mrz_raw" in result
  assert "mrz_parsed" in result
  assert result["mrz_parsed"].get("passport_number")
