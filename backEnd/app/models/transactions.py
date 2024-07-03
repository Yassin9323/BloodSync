#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'
    
    units = Column(Integer, nullable=False)
    transaction_date = Column(TIMESTAMP, nullable=False)
    from_inventory_id = Column(Integer, ForeignKey('hospital_inventory.id'), nullable=False)
    to_inventory_id = Column(Integer, ForeignKey('bank_inventory.id'), nullable=False)
    request_id = Column(Integer, ForeignKey('requests.id'), nullable=False)
    
    from_inventory = relationship('HospitalInventory', foreign_keys=[from_inventory_id])
    to_inventory = relationship('BankInventory', foreign_keys=[to_inventory_id])
    request = relationship('Request')
