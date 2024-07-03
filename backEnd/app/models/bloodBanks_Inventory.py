#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class BankInventory(BaseModel, Base):
    __tablename__ = 'bank_inventory'
    
    bank_id = Column(Integer, ForeignKey('blood_banks.id'), unique=True, nullable=False)
    blood_type_id = Column(Integer, ForeignKey('blood_types.id'), unique=True, nullable=False)
    units = Column(Integer, nullable=False)
    
    blood_bank = relationship('BloodBank')
    blood_type = relationship('BloodType')
