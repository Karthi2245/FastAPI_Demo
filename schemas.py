from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None  # optional one


# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[int] = None
#     brand: Optional[str] = None  # optional one
#
# class Inventory(BaseModel):
#     name = str
#     price = int
#     brand = str
#
#     class Config:
#         orm_mode = True
