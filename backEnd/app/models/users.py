#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """ """
    __tablename__ = 'users'

    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    role = Column(Enum('hospital_admin', 'blood_bank_admin', name='user_roles'), nullable=False, default='hospital')
    hospital_id = Column(String(60), ForeignKey('hospitals.id'), nullable=False)
    blood_bank_id = Column(String(60), ForeignKey('blood_banks.id'), nullable=False)
