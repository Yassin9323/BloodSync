#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base


class BloodBank(BaseModel, Base):
    __tablename__ = 'blood_banks'

    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(50))
    
    blood_bank_inventory = relationship('BankInventory', backref='blood_banks')
    users = relationship('User', backref='blood_banks')
    requests = relationship('Request', backref='blood_banks')
    transactions = relationship('Transaction', backref="blood_banks")
