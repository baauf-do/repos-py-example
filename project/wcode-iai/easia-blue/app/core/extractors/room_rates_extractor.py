import re
from typing import List
from app.utils.decorator_logging import log_execution_time


class RoomRatesExtractor:

  @staticmethod
  @log_execution_time
  def extract(text: str) -> List[dict]:
    """
    Extract danh sách loại phòng và giá phòng từ raw text.
    """
    room_rates = []

    # TODO: Xác định block chứa bảng giá phòng (phần text trong hợp đồng)
    rates_block = RoomRatesExtractor.extract_rates_block(text)

    if rates_block:
      room_rates = RoomRatesExtractor.parse_rates_block(rates_block)

    return room_rates

  @staticmethod
  def extract_rates_block(text: str) -> str:
    """
    Tách riêng phần text chứa bảng giá phòng.
    """
    # Giả sử phần giá phòng nằm giữa 2 tiêu đề đặc trưng
    match = re.search(r"BẢNG GIÁ PHÒNG(.*?)(Chính sách trẻ em|Điều kiện thanh toán|Chính sách huỷ phòng|$)",
                      text, re.DOTALL | re.IGNORECASE)
    if match:
      return match.group(1)
    return ""

  @staticmethod
  def parse_rates_block(rates_block: str) -> List[dict]:
    """
    Parse từng dòng loại phòng trong bảng giá.
    """
    room_rates = []
    lines = rates_block.split("\n")

    for line in lines:
      # Cố gắng nhận dạng từng dòng giá phòng
      # (Ví dụ một dòng: Deluxe Room - 51m2 - King/Twin - 2.600.000/3.000.000 VND)

      match = re.search(
        r"(?P<room_type>.+?)\s*-\s*(?P<size>\d+)\s*m2\s*-\s*(?P<bed_type>.+?)\s*-\s*(?P<normal_price>[0-9\.]+)[/\\](?P<high_price>[0-9\.]+)",
        line
      )

      if match:
        room_type = match.group("room_type").strip()
        size_sqm = int(match.group("size"))
        bed_type = match.group("bed_type").strip()
        normal_season_rate = int(match.group("normal_price").replace(".", ""))
        high_season_rate = int(match.group("high_price").replace(".", ""))

        room = {
          "room_type": room_type,
          "quantity": None,  # Nếu có số lượng sẽ extract sau
          "size_sqm": size_sqm,
          "bed_type": bed_type,
          "normal_season_rate": normal_season_rate,
          "high_season_rate": high_season_rate,
          "festive_season_rate": None
        }
        room_rates.append(room)

    return room_rates
