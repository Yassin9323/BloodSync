from fastapi import APIRouter, HTTPException, Depends
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.blood_banks import BloodBank
from app.models.blood_types import BloodType
from app.models.bloodBanks_Inventory import BankInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction


router = APIRouter()

@router.get("/dashboard")
async def dashboard(db: Session = Depends(get_db)):
    """Get the bank inventory data and request counts for the dashboard."""
    # Real time BloodBank inventory data
    # Fetch bank inventory data
    cairo_bloodbank = crud.check(BloodBank, "name", "Cairo-BloodBank", db)
    if not cairo_bloodbank:
        raise HTTPException(status_code=404, detail="Cairo-BloodBank not found")
    
    bank_inventories = (
        db.query(BankInventory)
        .filter(BankInventory.bank_id == cairo_bloodbank.id)
        .options(joinedload(BankInventory.blood_types))
        .all()
    )
    
    inventory_data = [
        {"blood_type": inv.blood_types.type, "available_units": inv.units}
        for inv in bank_inventories
    ]
    
    
    # Inventory part
    # Handle total units 
    total_units = 0
    for item in inventory_data:
        total_units += item["available_units"]
        
        
    # Requests part    
    # Fetch request counts
    pending_reqs = db.query(func.count(Request.id)).filter(Request.status == "pending").scalar()
    total_reqs = db.query(func.count(Request.id)).scalar()
    
    
    # Latest 3 Transactions Part
    # Fetch Hospital name , req.id, bloodtype, actual transfered units
    transactions = (
        db.query(Transaction)
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
    
    
    return {
        "inventory": inventory_data,
        "requests": {
            "pending": pending_reqs,
            "total": total_reqs
        },
        "total_units":total_units,
        "latest_transactions": latest_transactions
    }
