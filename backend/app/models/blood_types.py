#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class BloodType(BaseModel, Base):
    __tablename__ = 'blood_types'
    
    type = Column(Enum('A+', 'B+', 'AB+', 'A-', 'B-', 'AB-', 'O+', 'O-', name='blood_types_enum'), nullable=False)

    hospital_inventory = relationship('HospitalInventory', backref='blood_types')
    bank_inventory = relationship('BankInventory', backref='blood_types')
    requests = relationship('Request', backref='blood_types')
    
    
    
# create BloodType type="AB+" 