import re
from typing import Dict
from app.utils.decorator_logging import log_execution_time


class ContractInfoExtractor:

  @staticmethod
  @log_execution_time
  def extract(text: str) -> Dict:
    """
    Extract thông tin Bên A, B và thời gian hiệu lực hợp đồng từ raw text.
    """
    party_a = ContractInfoExtractor.extract_party_info(text, side="A")
    party_b = ContractInfoExtractor.extract_party_info(text, side="B")
    validity = ContractInfoExtractor.extract_validity(text)

    return {
      "party_a": party_a,
      "party_b": party_b,
      "validity": validity
    }

  @staticmethod
  def extract_party_info(text: str, side: str = "A") -> Dict:
    """
    Extract thông tin của một bên (A hoặc B).
    """
    party_info = {
      "company_name": None,
      "address": None,
      "phone": None,
      "tax_code": None,
      "representative": None,
      "title": None
    }

    # Tìm theo dấu mốc Bên A / Bên B
    pattern = rf"BÊN {side}.*?(?=BÊN [A|B]|$)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if match:
      block = match.group()

      # Tên công ty
      name_match = re.search(r"Công ty.*?:\s*(.+)", block, re.IGNORECASE)
      if name_match:
        party_info["company_name"] = name_match.group(1).strip()

      # Địa chỉ
      address_match = re.search(r"Địa chỉ.*?:\s*(.+)", block, re.IGNORECASE)
      if address_match:
        party_info["address"] = address_match.group(1).strip()

      # Điện thoại
      phone_match = re.search(r"Điện thoại.*?:\s*(.+)", block, re.IGNORECASE)
      if phone_match:
        party_info["phone"] = phone_match.group(1).strip()

      # Mã số thuế
      tax_code_match = re.search(r"Mã số thuế.*?:\s*(.+)", block, re.IGNORECASE)
      if tax_code_match:
        party_info["tax_code"] = tax_code_match.group(1).strip()

      # Người đại diện
      rep_match = re.search(r"Người đại diện.*?:\s*(.+)", block, re.IGNORECASE)
      if rep_match:
        party_info["representative"] = rep_match.group(1).strip()

      # Chức danh
      title_match = re.search(r"Chức danh.*?:\s*(.+)", block, re.IGNORECASE)
      if title_match:
        party_info["title"] = title_match.group(1).strip()

    return party_info

  @staticmethod
  def extract_validity(text: str) -> Dict:
    """
    Extract thời gian hiệu lực hợp đồng (start date, end date).
    """
    validity = {
      "start_date": None,
      "end_date": None
    }

    # Tìm theo format ngày
    date_match = re.search(
      r"Có hiệu lực từ ngày\s*(\d{2}/\d{2}/\d{4})\s*đến ngày\s*(\d{2}/\d{2}/\d{4})",
      text, re.IGNORECASE
    )

    if date_match:
      start_raw = date_match.group(1)
      end_raw = date_match.group(2)

      # Đổi từ dd/mm/yyyy ➔ yyyy-mm-dd
      validity["start_date"] = ContractInfoExtractor.format_date(start_raw)
      validity["end_date"] = ContractInfoExtractor.format_date(end_raw)

    return validity

  @staticmethod
  def format_date(date_str: str) -> str:
    """Chuyển đổi dd/mm/yyyy ➔ yyyy-mm-dd"""
    parts = date_str.strip().split("/")
    if len(parts) == 3:
      return f"{parts[2]}-{parts[1]}-{parts[0]}"
    return date_str
