#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class HospitalInventory(BaseModel, Base):
    __tablename__ = 'hospital_inventory'
    
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'), unique=True, nullable=False)
    hospital_id = Column(String(60), ForeignKey('hospitals.id'), unique=True, nullable=False)
    units = Column(Integer, nullable=False)

    blood_type = relationship('BloodType', back_populates='hospital_inventory')
    hospital = relationship('Hospital', back_populates='inventory')
