#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class BloodType(BaseModel, Base):
    __tablename__ = 'blood_types'
    
    type = Column(Enum('A+', 'B+', 'AB+', 'A-', 'B-', 'AB-', 'O+', 'O-', name='blood_types_enum'), nullable=False)

    requests = relationship('Request', back_populates='blood_type')
    hospital_inventory = relationship('HospitalInventory', back_populates='blood_type')
    bank_inventory = relationship('BankInventory', back_populates='blood_type')
