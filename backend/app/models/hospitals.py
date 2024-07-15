#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base
from app.models.transactions import Transaction

class Hospital(BaseModel, Base):
    __tablename__ = 'hospitals'
    
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(50))

    hospital_inventory = relationship('HospitalInventory', backref='hospitals')
    users = relationship('User', cascade='all, delete, delete-orphan', backref='hospitals')
    requests = relationship('Request', backref='hospitals')
    transactions = relationship('Transaction', backref="hospitals")
