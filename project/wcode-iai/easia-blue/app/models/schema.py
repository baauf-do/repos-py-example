from typing import List, Optional
from pydantic import BaseModel


class ValidityPeriod(BaseModel):
  start_date: Optional[str] = None  # yyyy-mm-dd
  end_date: Optional[str] = None


class PartyInfo(BaseModel):
  company_name: Optional[str] = None
  address: Optional[str] = None
  phone: Optional[str] = None
  tax_code: Optional[str] = None
  representative: Optional[str] = None
  title: Optional[str] = None


class ContractInfo(BaseModel):
  party_a: Optional[PartyInfo] = None
  party_b: Optional[PartyInfo] = None
  validity: Optional[ValidityPeriod] = None


class RoomRate(BaseModel):
  room_type: Optional[str] = None
  quantity: Optional[int] = None
  size_sqm: Optional[int] = None
  bed_type: Optional[str] = None
  normal_season_rate: Optional[float] = None
  high_season_rate: Optional[float] = None
  festive_season_rate: Optional[float] = None


class SpecialPolicies(BaseModel):
  children_policy: Optional[dict] = None
  cancellation_policy: Optional[dict] = None
  payment_terms: Optional[dict] = None
  bank_details: Optional[dict] = None
  check_in_out_policy: Optional[dict] = None
  special_offers: Optional[List[str]] = None


class ContractData(BaseModel):
  contract_info: Optional[ContractInfo] = None
  room_rates: Optional[List[RoomRate]] = None
  special_policies: Optional[SpecialPolicies] = None
