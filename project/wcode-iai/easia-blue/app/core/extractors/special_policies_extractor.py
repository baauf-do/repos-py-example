import re
from typing import Dict
from app.utils.decorator_logging import log_execution_time


class SpecialPoliciesExtractor:

  @staticmethod
  @log_execution_time
  def extract(text: str) -> Dict:
    """
    Extract tất cả các chính sách đặc biệt từ raw text hợp đồng.
    """
    children_policy = SpecialPoliciesExtractor.extract_children_policy(text)
    cancellation_policy = SpecialPoliciesExtractor.extract_cancellation_policy(text)
    payment_terms = SpecialPoliciesExtractor.extract_payment_terms(text)
    bank_details = SpecialPoliciesExtractor.extract_bank_details(text)
    check_in_out_policy = SpecialPoliciesExtractor.extract_check_in_out_policy(text)
    special_offers = SpecialPoliciesExtractor.extract_special_offers(text)

    return {
      "children_policy": children_policy,
      "cancellation_policy": cancellation_policy,
      "payment_terms": payment_terms,
      "bank_details": bank_details,
      "check_in_out_policy": check_in_out_policy,
      "special_offers": special_offers
    }

  @staticmethod
  def extract_children_policy(text: str) -> Dict:
    """
    Extract chính sách trẻ em.
    """
    policy = {}
    match = re.search(r"Chính sách trẻ em(.*?)(Chính sách huỷ phòng|Điều kiện thanh toán|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      policy["content"] = match.group(1).strip()
    return policy

  @staticmethod
  def extract_cancellation_policy(text: str) -> Dict:
    """
    Extract chính sách huỷ phòng.
    """
    policy = {}
    match = re.search(r"Chính sách huỷ phòng(.*?)(Điều kiện thanh toán|Chính sách khác|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      policy["content"] = match.group(1).strip()
    return policy

  @staticmethod
  def extract_payment_terms(text: str) -> Dict:
    """
    Extract điều kiện thanh toán.
    """
    terms = {}
    match = re.search(r"Điều kiện thanh toán(.*?)(Thông tin tài khoản|Chính sách khác|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      terms["content"] = match.group(1).strip()
    return terms

  @staticmethod
  def extract_bank_details(text: str) -> Dict:
    """
    Extract thông tin tài khoản ngân hàng.
    """
    details = {}
    match = re.search(r"Thông tin tài khoản(.*?)(Chính sách khác|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      block = match.group(1)

      bank_name_match = re.search(r"Ngân hàng.*?:\s*(.+)", block, re.IGNORECASE)
      if bank_name_match:
        details["bank_name"] = bank_name_match.group(1).strip()

      account_name_match = re.search(r"Tên tài khoản.*?:\s*(.+)", block, re.IGNORECASE)
      if account_name_match:
        details["account_name"] = account_name_match.group(1).strip()

      account_number_match = re.search(r"Số tài khoản.*?:\s*(.+)", block, re.IGNORECASE)
      if account_number_match:
        details["account_number"] = account_number_match.group(1).strip()

      swift_code_match = re.search(r"Swift Code.*?:\s*(.+)", block, re.IGNORECASE)
      if swift_code_match:
        details["swift_code"] = swift_code_match.group(1).strip()

    return details

  @staticmethod
  def extract_check_in_out_policy(text: str) -> Dict:
    """
    Extract chính sách check-in / check-out.
    """
    policy = {}
    match = re.search(r"Chính sách check-in/check-out(.*?)(Chính sách khác|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      policy["content"] = match.group(1).strip()
    return policy

  @staticmethod
  def extract_special_offers(text: str) -> list:
    """
    Extract các ưu đãi đặc biệt (special offers).
    """
    offers = []
    match = re.search(r"Ưu đãi đặc biệt(.*?)(Chính sách khác|$)", text, re.DOTALL | re.IGNORECASE)
    if match:
      offers_block = match.group(1).strip()
      # Split từng dòng nếu có nhiều ưu đãi
      lines = offers_block.split("\n")
      for line in lines:
        line = line.strip("- ").strip()
        if line:
          offers.append(line)
    return offers
