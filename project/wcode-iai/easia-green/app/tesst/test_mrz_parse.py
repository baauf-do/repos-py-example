# app/test/test_mrz_parse.py
import pytest
from app.core.mrz_parse import parse_mrz_td3, compute_check_digit


def test_parse_valid_mrz():
  mrz_text = (
    "P<VNMNGUYEN<<VAN<A<<<<<<<<<<<<<<<<<<\n"
    "B01234567<8VNM6501019M3001017<<<<<<<<<<<<<<04"
  )
  result = parse_mrz_td3(mrz_text)
  assert result is not None
  assert result["surname"] == "NGUYEN"
  assert result["given_names"] == "VAN A"
  assert result["passport_number"] == "B01234567"
  assert result["birth_date"] == "650101"
  assert result["expiry_date"] == "300101"


def test_check_digit():
  assert compute_check_digit("B01234567") == "8"
  assert compute_check_digit("650101") == "9"
  assert compute_check_digit("300101") == "7"
