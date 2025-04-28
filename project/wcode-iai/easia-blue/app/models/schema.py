from pydantic import BaseModel
from typing import Optional, List


class ContractData(BaseModel):
  company_name: str
  contract_number: str
  signed_date: Optional[str]
  total_value: Optional[str]
  terms: Optional[List[str]] = []
