#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Hospital(BaseModel, Base):
    __tablename__ = 'hospitals'
    
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(50))