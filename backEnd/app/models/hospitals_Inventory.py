#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class HospitalInventory(BaseModel, Base):
    __tablename__ = 'hospital_inventory'
    
    units = Column(Integer, nullable=False)
    hospital_id = Column(String(60), ForeignKey('hospitals.id'), unique=True, nullable=False)
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'), unique=True, nullable=False)

    transactions = relationship('Transaction', backref="hospital_inventory")

# 54f30789-af7f-4893-b4d6-e34b9f215bb2
# create HospitalInventory units=10 hospital_id="9a27b071-37eb-44de-ba54-1499729e6e85" blood_type_id="5c060dd2-25dc-424c-9356-addc789ee9f2"
""" 
Hospital --> HospitalInventory --> 
                                    |
                                    |BloodType  
                                    |
BloodBank --> BankInventory -----> 

"""