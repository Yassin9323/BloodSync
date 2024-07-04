#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base


class BloodBank(BaseModel, Base):
    __tablename__ = 'blood_banks'

    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(50))

    users = relationship('User', back_populates='blood_bank')
    requests = relationship('Request', back_populates='blood_bank')
    blood_bank_inventory = relationship('BankInventory', back_populates='blood_bank')