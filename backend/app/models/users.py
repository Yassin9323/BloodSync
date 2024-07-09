#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """ """
    __tablename__ = 'users'

    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    role = Column(Enum('hospital-admin', 'blood-bank-admin', name='user_roles'), nullable=False, default='hospital')
    
    hospital_id = Column(String(60), ForeignKey('hospitals.id'))
    blood_bank_id = Column(String(60), ForeignKey('blood_banks.id'))

# username="Admin_AinShams" password="admin" email="Ain_shams@gmail.com" role="hospital-admin" hospital_id="9a27b071-37eb-44de-ba54-1499729e6e85"