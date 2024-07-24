from fastapi import APIRouter, HTTPException, Depends, Form
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.blood_banks import BloodBank
from app.models.bloodBanks_Inventory import BankInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction
from app.models.hospitals_Inventory import HospitalInventory
from app.schemas import user
from app.utils import oauth2
from app.api.websockets import manager


router = APIRouter(prefix="/requests")


@router.get("/pending")
async def requests(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)): 
    # Requests part    
    # Fetch request counts    
    pending_reqs = (
        db.query(Request).
        filter(Request.status == "pending").
        options(joinedload(Request.hospitals)).
        options(joinedload(Request.blood_types))
        )
    pending_requests = [
        {"hospital_name": req.hospitals.name,
         "req_num": req.id,
         "blood_type": req.blood_types.type,
         "units": req.units,
         "status": req.status
         }
        for req in pending_reqs
    ]
    
    await manager.broadcast("pending_reqs_update")
    return {"pending_requests": pending_requests}


@router.get("/total")
async def requests(db: Session = Depends(get_db), current_user: user.User = Depends(oauth2.get_current_user)): 
    # Requests part    
    # Fetch request counts    
    total_reqs = (
        db.query(Request).
        options(joinedload(Request.hospitals)).
        options(joinedload(Request.blood_types))
        )
    total_requests = [
        {"hospital_name": req.hospitals.name,
         "req_num": req.id,
         "blood_type": req.blood_types.type,
         "units": req.units,
         "status": req.status
         }
        for req in total_reqs
    ]
    
    await manager.broadcast("total_reqs_update")
    return {"total_requests": total_requests}

# Define a Pydantic model


@router.post("/update_status")
async def update_request_status(
    x: user.UpdateRequestStatus,  # Use the Pydantic model here
    db: Session = Depends(get_db),
    current_user: user.User = Depends(oauth2.get_current_user)
):
    print("Update Status \n\n\n")
    """Update the status of a blood request"""
    request = db.query(Request).filter(Request.id == x.request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    if x.action not in ["approve", "decline", "redirect"]:
        raise HTTPException(status_code=400, detail="Invalid action")
    
    if request.status != "pending":
        raise HTTPException(status_code=400, detail="action had been taken before")

    hospital_inv = (db.query(HospitalInventory).
        filter(HospitalInventory.blood_type_id == request.blood_type_id).
        filter(HospitalInventory.hospital_id == request.hospital_id).first()
        )
    # request.status = action
    if x.action == "approve":
        bloodbank_inv = db.query(BankInventory).filter(BankInventory.blood_type_id == request.blood_type_id).first()
        request.status = "approved"
        if bloodbank_inv.units < request.units:
            raise HTTPException(status_code=400, detail="not enough units in BloodBank_Inventory (try redirect)")
        else:
            bloodbank_inv.units = bloodbank_inv.units - request.units 
            hospital_inv.units = hospital_inv.units + request.units
               
    elif x.action == "decline":
        request.status = "declined"

    else:
        hospital_invs = (db.query(HospitalInventory).
        filter(HospitalInventory.blood_type_id == request.blood_type_id).all()
        )
        for inv in hospital_invs:
            if inv.units > request.units:
                inv.units = inv.units - request.units
                hospital_inv.units = hospital_inv.units + request.units
                request.status = "redirected"

    db.commit()
    db.refresh(request)
    db.refresh(bloodbank_inv)
    db.refresh(hospital_inv)

    await manager.broadcast("update_status_update")
    return {"details":{
            "status": request.status,
            "request_id": request.id
    }
    }