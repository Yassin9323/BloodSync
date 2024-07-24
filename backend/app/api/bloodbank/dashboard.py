from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.core.database import get_db
from app.core import crud
from app.models.blood_banks import BloodBank
from app.models.bloodBanks_Inventory import BankInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction
from app.schemas import user
from app.utils import oauth2
from app.api.websockets import manager

router = APIRouter(prefix="/dashboard")

@router.get("/inventory")
async def inventory(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):
    """Get the bank inventory data and request counts for the dashboard."""
    cairo_bloodbank = crud.get_cairo_bloodbank(db)
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
    await manager.broadcast("inventory_update")
    return {"inventory": inventory_data}

@router.get("/inventory_total_units")
async def total_inventory(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):
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
    total_units = sum(item["available_units"] for item in inventory_data)
    await manager.broadcast("inventory_total_units_update")
    return {"total_units": total_units}

@router.get("/requests")
async def requests(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)): 
    pending_reqs = db.query(func.count(Request.id)).filter(Request.status == "pending").scalar()
    total_reqs = db.query(func.count(Request.id)).scalar()
    await manager.broadcast("requests_update")
    return {"requests": {"pending": pending_reqs, "total": total_reqs}}

@router.get("/transactions")
async def transactions(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)):  
    transactions = (
        db.query(Transaction)
        .options(joinedload(Transaction.requests).joinedload(Request.blood_types))
        .options(joinedload(Transaction.hospitals))
        .order_by(Transaction.created_at.desc())
        .limit(3)
        .all()
    )
    latest_transactions = [
        {"hospital_name": trns.hospitals.name, "req_num": trns.request_id, "blood_type": trns.requests.blood_types.type, "units": trns.units}
        for trns in transactions
    ]
    await manager.broadcast("transactions_update")
    return {"latest_transactions": latest_transactions}
