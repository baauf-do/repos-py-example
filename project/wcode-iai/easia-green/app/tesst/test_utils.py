# app/test/test_utils.py
from app.core.utils import is_valid_date


def test_valid_date():
  assert is_valid_date("650101")  # 1965-01-01
  assert is_valid_date("300101")  # 2030-01-01


def test_invalid_date():
  assert not is_valid_date("991331")  # ngày không hợp lệ
  assert not is_valid_date("650132")  # tháng không hợp lệ
