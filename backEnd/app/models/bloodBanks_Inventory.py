#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base
from app.models.transactions import Transaction

class BankInventory(BaseModel, Base):
    __tablename__ = 'bank_inventory'
    
    bank_id = Column(String(60), ForeignKey('blood_banks.id'), unique=True, nullable=False)
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'), unique=True, nullable=False)
    units = Column(Integer, nullable=False)

    blood_bank = relationship('BloodBank', back_populates='inventory')
    blood_type = relationship('BloodType', back_populates='bank_inventory')
