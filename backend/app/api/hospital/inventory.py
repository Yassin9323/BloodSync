from fastapi import APIRouter, HTTPException, Depends
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.hospitals_Inventory import HospitalInventory
from app.models.hospitals import Hospital
from app.schemas import user
from app.utils import oauth2

router = APIRouter(prefix="/{name}_hospital/inventory", tags=["Hospital"])

@router.get("/")
async def hospital_inventory(name, db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):
    """ get the inventory for specific hospital """
    hospital = crud.get_hospital(name, db)
    hospital_inventories = (
        db.query(HospitalInventory)
        .filter(HospitalInventory.hospital_id == hospital.id)
        .options(joinedload(HospitalInventory.blood_types))
        .all()
    )
    
    inventory_data = [
        {"blood_type": inv.blood_types.type, "available_units": inv.units}
        for inv in hospital_inventories
    ]
    h_name = hospital.name
    
    return {"inventory":{
        "name": h_name,
        "inventory_data": inventory_data}        
    }
