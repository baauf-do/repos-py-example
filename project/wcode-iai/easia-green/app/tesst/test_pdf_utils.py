# app/test/test_pdf_utils.py
import os
import pytest
from app.core.pdf_utils import pdf_to_images


def test_pdf_to_images():
  test_pdf = "store/input/sample_passport.pdf"
  if not os.path.exists(test_pdf):
    pytest.skip("Thiếu file sample_passport.pdf để test")

  images = pdf_to_images(test_pdf)
  assert isinstance(images, list)
  assert len(images) > 0
  assert images[0].mode in ["RGB", "L"]
