#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base
from app.models.transactions import Transaction

class BankInventory(BaseModel, Base):
    __tablename__ = 'bank_inventory'

    units = Column(Integer, nullable=False)
    bank_id = Column(String(60), ForeignKey('blood_banks.id'), unique=True, nullable=False)
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'), unique=True, nullable=False)

    transactions = relationship('Transaction', backref="bank_inventory")

# create BankInventory units=30 bank_id="42ed083e-b389-4ee4-bba3-eec3a19ae693" blood_type_id="5c060dd2-25dc-424c-9356-addc789ee9f2"
