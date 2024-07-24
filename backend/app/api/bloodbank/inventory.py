from fastapi import APIRouter, HTTPException, Depends, Form
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.blood_banks import BloodBank
from app.models.hospitals import Hospital
from app.models.bloodBanks_Inventory import BankInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction
from app.models.hospitals_Inventory import HospitalInventory
from app.schemas import user
from app.utils import oauth2
from app.api.websockets import manager

router = APIRouter(prefix="/inventory")


@router.get("/")
async def bloodbank_inventory(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):
    """Get BloodBank Inventory"""
    cairo_bloodbank = crud.get_cairo_bloodbank(db)
    bloodbank_inventories = db.query(BankInventory).filter(BankInventory.bank_id == cairo_bloodbank.id).all()
    
    inventory_data = [
        {"blood_type": inv.blood_types.type, "available_units": inv.units}
        for inv in bloodbank_inventories
    ]
    name2 =  cairo_bloodbank.name
    
    await manager.broadcast("inventory_update")
    return {"inventory":{
        "name": name2,
        "inventory_data": inventory_data}        
    }

@router.get("/{hospital_name}_inventory")
async def get_hospital_inventory(hospital_name: str, db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):
    hospital = crud.get_hospital(hospital_name, db)

    hospital_inventories = db.query(HospitalInventory).filter(HospitalInventory.hospital_id == hospital.id).all()
    
    inventory_data = [
        {"blood_type": inv.blood_types.type, "available_units": inv.units}
        for inv in hospital_inventories
    ]
    
    await manager.broadcast("inventory_hospital_update")
    return {"details":{
        "name": hospital.name,
        "inventory": inventory_data
    }
    }

