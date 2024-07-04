#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class Request(BaseModel, Base):
    __tablename__ = 'requests'
    
    status = Column(Enum('pending', 'approved', 'declined', 'redirected', name='request_statuses'), nullable=False, default='pending')
    units = Column(Integer, nullable=False)
    hospital_id = Column(String(60), ForeignKey('hospitals.id'))
    blood_bank_id = Column(String(60), ForeignKey('blood_banks.id'))
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'))

    hospital = relationship('Hospital', back_populates='requests')
    blood_bank = relationship('BloodBank', back_populates='requests')
    blood_type = relationship('BloodType', back_populates='requests')
    transactions = relationship('Transaction', back_populates='request')
