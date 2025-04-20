# app/core/mrz_parse.py
# Parse MRZ dạng TD3 (2 dòng, mỗi dòng 44 ký tự)
# Trích xuất các trường: document_type, issuing_country, surname, given_names, passport_number, dob, expiry_date, gender...
# Chuyển đổi ngày tháng sang định dạng YYYY-MM-DD
import re
from typing import Optional, Dict
from core.utils import log_debug


def parse_mrz_text(mrz_text: str) -> Optional[Dict]:
  """
  Parse MRZ dạng TD3 (2 dòng, mỗi dòng 44 ký tự)
  Trả về dict thông tin có cấu trúc
  """
  log_debug("📄 Bắt đầu phân tích MRZ text...", level="INFO")
  lines = mrz_text.strip().splitlines()
  if len(lines) != 2 or not all(len(l) >= 40 for l in lines):
    log_debug("❌ MRZ không đúng định dạng TD3 (2 dòng, >=40 ký tự mỗi dòng)", level="WARNING")
    return None

  line1, line2 = lines[0], lines[1]
  line1 = line1.ljust(44, '<')
  line2 = line2.ljust(44, '<')

  try:
    document_type = line1[0:2]
    issuing_country = line1[2:5]
    names_raw = line1[5:44].replace('<', ' ').strip()
    names = names_raw.split(' ', 1)

    passport_number = line2[0:9].replace('<', '')
    nationality = line2[10:13]
    birth_date = format_date(line2[13:19])
    gender = line2[20]
    expiry_date = format_date(line2[21:27])

    parsed_result = {
      "document_type": document_type,
      "issuing_country": issuing_country,
      "surname": names[0],
      "given_names": names[1] if len(names) > 1 else "",
      "passport_number": passport_number,
      "nationality": nationality,
      "date_of_birth": birth_date,
      "gender": gender,
      "expiration_date": expiry_date,
      "mrz": f"{line1}\n{line2}"
    }

    log_debug(f"✅ Parse MRZ thành công: {parsed_result}", level="DEBUG")
    return parsed_result
  except Exception as e:
    log_debug(f"❌ Lỗi khi parse MRZ: {e}", level="ERROR")
    return None


def format_date(yyMMdd: str) -> str:
  """Định dạng ngày từ yyMMdd sang yyyy-MM-dd"""
  if not re.match(r"\d{6}", yyMMdd):
    return ""
  year = int(yyMMdd[:2])
  year += 2000 if year < 50 else 1900
  return f"{year:04d}-{yyMMdd[2:4]}-{yyMMdd[4:6]}"


def parse_mrz_td3(mrz_text: str) -> Optional[Dict[str, str]]:
  """
  Parse MRZ dạng TD3 (2 dòng, mỗi dòng 44 ký tự) và trả về thông tin hộ chiếu.
  """
  lines = [line.strip() for line in mrz_text.splitlines() if line.strip()]
  if len(lines) != 2 or any(len(line) != 44 for line in lines):
    return None  # Không đúng chuẩn TD3

  line1, line2 = lines

  result = {
    "document_type": line1[0],
    "issuing_country": line1[2:5],
    "surname": line1[5:].split("<<")[0].replace("<", " ").strip(),
    "given_names": " ".join(line1[5:].split("<<")[1:]).replace("<", " ").strip(),
    "passport_number": line2[0:9].replace("<", "").strip(),
    "nationality": line2[10:13],
    "birth_date": line2[13:19],
    "sex": line2[20],
    "expiry_date": line2[21:27],
    "personal_number": line2[28:42].replace("<", "").strip(),
    "check_digits": {
      "passport_number_cd": line2[9],
      "birth_date_cd": line2[19],
      "expiry_date_cd": line2[27],
      "personal_number_cd": line2[42],
      "final_cd": line2[43],
    }
  }

  return result


def compute_check_digit(field: str) -> str:
  """
  Tính mã kiểm tra (check digit) cho chuỗi MRZ theo chuẩn ICAO 9303.
  """
  weights = [7, 3, 1]
  total = 0
  for i, char in enumerate(field):
    if char.isdigit():
      val = int(char)
    elif 'A' <= char <= 'Z':
      val = ord(char) - 55
    elif char == '<':
      val = 0
    else:
      val = 0
    total += val * weights[i % 3]
  return str(total % 10)
