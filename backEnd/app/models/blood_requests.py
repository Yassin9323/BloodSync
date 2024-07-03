#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Request(BaseModel, Base):
    __tablename__ = 'requests'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum('pending', 'approved', 'declined', 'redirected', name='request_statuses'), nullable=False, default='pending')
    units = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    hospital_id = Column(Integer, ForeignKey('hospitals.id'))
    blood_bank_id = Column(Integer, ForeignKey('blood_banks.id'))
    blood_type_id = Column(Integer, ForeignKey('blood_types.id'))
    
    hospital = relationship('Hospital')
    blood_bank = relationship('BloodBank')
    blood_type = relationship('BloodType')
