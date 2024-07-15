#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'

    units = Column(Integer)
    from_id = Column(String(60), ForeignKey('blood_banks.id'), nullable=False)
    to_id = Column(String(60), ForeignKey('hospitals.id'), nullable=False)
    request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)

# from_inv_id="" to_inv_id="" request_id="" 