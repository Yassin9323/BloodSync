#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'
    
    units = Column(Integer, nullable=False)
    transaction_date = Column(TIMESTAMP, nullable=False)
    from_inventory_id = Column(String(60), ForeignKey('hospital_inventory.id'), nullable=False)
    to_inventory_id = Column(String(60), ForeignKey('bank_inventory.id'), nullable=False)
    request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)

    from_inventory = relationship('HospitalInventory')
    to_inventory = relationship('BankInventory')
    request = relationship('Request', back_populates='transactions')
