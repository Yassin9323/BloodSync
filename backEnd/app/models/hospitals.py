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
    users = relationship('User', cascade='all, delete, delete-orphan', back_populates='hospital')
    requests = relationship('Request', back_populates='hospital')
    hospital_inventory = relationship('HospitalInventory', back_populates='hospital')
