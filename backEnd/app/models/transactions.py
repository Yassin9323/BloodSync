#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'

    units = Column(Integer)
    from_inv_id = Column(String(60), ForeignKey('hospital_inventory.id'), nullable=False)
    to_inv_id = Column(String(60), ForeignKey('bank_inventory.id'), nullable=False)
    request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)

# from_inv_id="9a27b071-37eb-44de-ba54-1499729e6e85" to_inv_id="42ed083e-b389-4ee4-bba3-eec3a19ae693" request_id="5c060dd2-25dc-424c-9356-addc789ee9f2"