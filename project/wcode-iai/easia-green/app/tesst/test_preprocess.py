# app/test/test_preprocess.py
import os
import pytest
from PIL import Image
from app.core.preprocess import preprocess_image


def test_preprocess_image():
  img_path = "store/input/sample_passport.jpg"
  if not os.path.exists(img_path):
    pytest.skip("Thiếu file sample_passport.jpg để test")

  processed = preprocess_image(img_path)
  assert isinstance(processed, Image.Image)
  assert processed.size[0] > 0 and processed.size[1] > 0
