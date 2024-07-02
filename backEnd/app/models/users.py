#!/usr/bin/python3

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """ """
    __tablename__ = 'users'

    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    cities = relationship("City", cascade='all, delete-orphan', backref="state")

    
