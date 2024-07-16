from fastapi import APIRouter, HTTPException, Depends
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.hospitals_Inventory import HospitalInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction
from app.models.hospitals import Hospital


router = APIRouter(prefix="/{name}_hospital/dashboard", tags=["Hospital"])


@router.get("/inventory")
async def inventory(name, db: Session = Depends(get_db)):
    """Get the bank inventory data and request counts for the dashboard."""
    # Real time BloodBank inventory data
    # Fetch bank inventory data  
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
    
    return {"inventory": inventory_data}
    
@router.get("/inventory_total")
async def total_inventory(name, db: Session = Depends(get_db)):
    # Inventory part
    # Handle total units
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
    total_units = 0
    for item in inventory_data:
        total_units += item["available_units"]
        
    return {"total_units": total_units}
        
@router.get("/requests")
async def requests(name, db: Session = Depends(get_db)):  
    # Requests part    
    # Fetch request counts
    hospital = crud.get_hospital(name, db)
    pending_reqs = (
        db.query(func.count(Request.id)).
        filter(Request.hospital_id == hospital.id).
        filter(Request.status == "pending").scalar()
        )
    
    total_reqs = (
        db.query(func.count(Request.id)).
        filter(Request.hospital_id == hospital.id).scalar()
    )    
    return{"pending_requests": pending_reqs, "total_requests": total_reqs}


@router.get("/transactions")
async def transactions(name, db: Session = Depends(get_db)):  
    # Latest 3 Transactions Part
    # Fetch Hospital name , req.id, bloodtype, actual transfered units
    hospital = crud.get_hospital(name, db)
    transactions = (
        db.query(Transaction)
        .filter(Transaction.to_id == hospital.id)
        .options(joinedload(Transaction.requests).joinedload(Request.blood_types))
        .options(joinedload(Transaction.hospitals))
        .order_by(Transaction.created_at.desc())
        .limit(3)
        .all()
    )
    
    latest_transactions = [
        {"hospital name": trns.hospitals.name,
         "req.num": trns.request_id,
         "blood type": trns.requests.blood_types.type,
         "units": trns.units
         }
        for trns in transactions
    ]
    return {"latest_transactions": latest_transactions}
