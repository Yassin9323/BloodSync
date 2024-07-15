#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

class HospitalInventory(BaseModel, Base):
    __tablename__ = 'hospital_inventory'
    
    units = Column(Integer, nullable=False)
    hospital_id = Column(String(60), ForeignKey('hospitals.id'), nullable=False)
    blood_type_id = Column(String(60), ForeignKey('blood_types.id'), nullable=False)

    __table_args__ = (UniqueConstraint('hospital_id', 'blood_type_id', name='_hospital_blood_type_uc'),)

# 54f30789-af7f-4893-b4d6-e34b9f215bb2
# create class HospitalInventory units=12 hospital_id="37154c63-ef86-47e7-9079-9b8db4949ffb" blood_type_id="fef1d821-c2cc-41a9-85f1-9023ec62aa76"
""" 
Hospital --> HospitalInventory --> hos_inv = 8f50a5b9-0787-470c-acce-3ab734c5757f
                                    |
                                    |BloodType  
                                    |
BloodBank --> BankInventory -----> blood_id = 38b1ad42-db84-4eac-93fe-43a37a6fecb8
bank?_inv = 33d7b8bc-ed73-4841-8351-afa53fa53c83
request = 1cecc55a-13ff-4031-8393-eb23ec2db111
"""