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


def save(obj=None, db: Session = db):
    """Commit all changes of the current database session"""
    if not db.object_session(obj):
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


def check_email(email, db: Session = db):
    try:
        user = db.query(User).filter(User.email == email).first()
        return user
    except OperationalError as op_err:
        # Handle operational errors like lost connection
        db.rollback()
        raise op_err
    except ProgrammingError as prog_err:
        # Handle programming errors like commands out of sync
        db.rollback()
        raise prog_err
    except Exception as e:
        # General error handling
        db.rollback()
        raise e
    finally:
        db.close()
