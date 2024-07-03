#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class BloodType(BaseModel, Base):
    __tablename__ = 'blood_types'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum('A+', 'B+', 'AB+', 'A-', 'B-', 'AB-', 'O+', 'O-', name='blood_types_enum'), nullable=False)
