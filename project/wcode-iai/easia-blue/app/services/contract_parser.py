from app.models.schema import ContractData
from app.utils.decorator_logging import log_execution_time


class ContractParser:
  @staticmethod
  @log_execution_time
  def parse(text: str) -> ContractData:
    # TODO: Replace with actual parsing logic
    return ContractData(
      company_name="Công ty ABC",
      contract_number="HD123456",
      signed_date="2024-01-01",
      total_value="1,000,000,000 VND",
      terms=[]
    )
