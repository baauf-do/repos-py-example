import re


def extract_structured_data_from_text(text: str) -> dict:
  data = {}

  # Ngày ký
  match = re.search(r'Hợp đồng.*ngày\s+(\d{2}/\d{2}/\d{4})', text)
  data["sign_date"] = match.group(1) if match else None

  # Bên A
  data["party_a"] = {}
  match = re.search(r'BÊN A:?\s*(.*?)\n', text)
  data["party_a"]["name"] = match.group(1).strip() if match else None

  match = re.search(r'BÊN A.*?\n.*?\n(.*?)\n', text)
  data["party_a"]["address"] = match.group(1).strip() if match else None

  match = re.search(r'MST\s*[:\-]?\s*(\d+)', text)
  data["party_a"]["tax_code"] = match.group(1) if match else None

  match = re.search(r'\b(\u00d4ng|Bà)\s+([A-ZÀ-\u1ef9][\w\s\.-]+)\s*-\s*(.*?)\n', text)
  if match:
    data["party_a"]["representative"] = match.group(2).strip()
    data["party_a"]["position"] = match.group(3).strip()

  # Bên B (placeholder)
  data["party_b"] = {"name": "Khách sạn XYZ"}

  # Trích bảng giá (giả định đơn giản)
  table_match = re.search(r'GIÁ PHÒNG(.*?)BỬa ĂN BẮT BUỘC', text, re.DOTALL)
  if table_match:
    data["price_table_raw"] = table_match.group(1).strip()

  return data
