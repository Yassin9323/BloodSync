#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class Request(BaseModel, Base):
    __tablename__ = 'requests'
    
    status = Column(Enum('pending', 'approved', 'declined', 'redirected', name='request_statuses'), nullable=False, default='pending')
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'))
    units = Column(Integer, nullable=False)
    hospital_id = Column(String(60), ForeignKey('hospitals.id'), nullable=False)
    blood_bank_id = Column(String(60), ForeignKey('blood_banks.id'), nullable=False)

    transactions = relationship('Transaction', backref='requests')
