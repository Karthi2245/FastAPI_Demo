from database import base

from sqlalchemy import Column, String, Integer


class Inventory(base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    price = Column(Integer)
    brand = Column(String(255))



