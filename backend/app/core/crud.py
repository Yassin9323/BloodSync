# !/usr/bin/python3
from typing import Type
from app.models.hospitals import Hospital
from app.models.blood_banks import BloodBank
from app.models.blood_types import BloodType
from app.models.hospitals_Inventory import HospitalInventory
from app.models.bloodBanks_Inventory import BankInventory
from app.models.transactions import Transaction
from app.models.users import User
from app.models.blood_requests import Request
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from fastapi import APIRouter, HTTPException, Form, Depends


db = SessionLocal()

classes = {"Hospital": Hospital, "User": User,
        "BloodBank": BloodBank, "BloodType": BloodType, "HospitalInventory": HospitalInventory,
        "BankInventory": BankInventory, "Request": Request, "Transaction": Transaction}

def all(cls=None, db: Session = db):
    """Query on the current database session"""
    new_dict = {}
    try:
        if cls == None:
            for cls_2 in classes:
                objs = db.query(classes[cls_2]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        else:
            objs = db.query(classes[cls]).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                new_dict[key] = obj
        return new_dict
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()


def save(obj, db: Session = db):
    """Commit all changes of the current database session"""
    db.add(obj)
    db.commit()
    db.refresh(obj)


def get_object(cls, id, db: Session = db):
    """Get a specific object by class and ID"""
    instances = all(cls)
    for key, value in instances.items():
        key = key.split(".")
        if key[1] == id:
            return value
    return None


def count_of(cls=None, db: Session = db):
    """Count the number of objects in storage"""
    instances = all(cls)
    return len(instances)


def units_of(_type=None, db: Session = db):
    """Return the units of a specific bloodtype"""
    units = db.query(BloodType).filter(BloodType.type == _type)
    return len(units)


def check(cls, parm, value, db: Session = db):
    """return the object if it exists"""
    class_parm = getattr(cls, parm) #User.email
    user = db.query(cls).filter(class_parm == value).first()
    return user
    
def id_by_role(role, name, db: Session = db):
    """Return the ID of the user by role"""
    if role == 'blood-bank-admin':
        blood_bank = check(BloodBank, 'name', name, db)
        if blood_bank:
            blood_bank_id = blood_bank.id
            print (blood_bank_id)
            return blood_bank_id

    else: # hospital-admin
        hospital = check(Hospital, 'name', name, db)
        if hospital:
            hospital_id = hospital.id
            print (hospital_id)
            return hospital_id
    
def get_hospital(name, db: Session = db):
    h_name = name.capitalize()
    h_name = f"{h_name}-Hospital"
    hospital = db.query(Hospital).filter(Hospital.name == h_name).first()
    if not hospital:
        raise HTTPException(status_code=404, detail=f"{h_name} not found")
    return hospital

def get_cairo_bloodbank(db: Session = db):
    cairo_bloodbank = check(BloodBank, "name", "Cairo-BloodBank", db)
    if not cairo_bloodbank:
        raise HTTPException(status_code=404, detail="Cairo-BloodBank not found")
    return cairo_bloodbank
