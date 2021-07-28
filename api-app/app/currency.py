from pydantic import BaseModel
from typing import List

# class Currency(BaseModel):
#     name: str
#     code: str
#     symbol: str
#     price: float

class Currency(BaseModel):
    name: str
    symbol: str

class CurrencyList(BaseModel):
    currencies: List[Currency] = None


