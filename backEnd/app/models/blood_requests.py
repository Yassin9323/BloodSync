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
#blood_type_id="5c060dd2-25dc-424c-9356-addc789ee9f2"  units=5 hospital_id="9a27b071-37eb-44de-ba54-1499729e6e85" blood_bank_id="42ed083e-b389-4ee4-bba3-eec3a19ae693"
