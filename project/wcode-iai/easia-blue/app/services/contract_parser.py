from app.core.extractors.contract_info_extractor import ContractInfoExtractor
from app.core.extractors.room_rates_extractor import RoomRatesExtractor
from app.core.extractors.special_policies_extractor import SpecialPoliciesExtractor


class ContractParser:

  @staticmethod
  def parse(text: str) -> dict:
    """
    Gọi lần lượt từng extractor, assemble kết quả
    """
    contract_info = ContractInfoExtractor.extract(text)
    room_rates = RoomRatesExtractor.extract(text)
    special_policies = SpecialPoliciesExtractor.extract(text)

    return {
      "contract_info": contract_info,
      "room_rates": room_rates,
      "special_policies": special_policies
    }
