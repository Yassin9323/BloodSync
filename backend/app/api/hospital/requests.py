from fastapi import APIRouter, HTTPException, Depends, Form
from app.core.database import get_db
from app.core import crud
from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from app.models.hospitals_Inventory import HospitalInventory
from app.models.hospitals import Hospital
from app.models.blood_requests import Request
from app.models.blood_banks import BloodBank
from app.models.blood_types import BloodType


router = APIRouter(prefix="/{name}_hospital/requests", tags=["Hospital"])

@router.get("/pending")
async def pending_hospital_requests(name, db: Session = Depends(get_db)):
    """pending requests """
    hospital = crud.get_hospital(name, db)
    pending_reqs = (
        db.query(Request).
        filter(Request.hospital_id == hospital.id).
        filter(Request.status == "pending").
        options(joinedload(Request.hospitals)).
        options(joinedload(Request.blood_types))
        )
    pending_requests = [
        {"hospital name": req.hospitals.name,
         "req.num": req.id,
         "blood type": req.blood_types.type,
         "units": req.units,
         "status": req.status
         }
        for req in pending_reqs
    ]
    return {"pending_requests": pending_requests}    


@router.get("/total")
async def total_hospital_requests(name, db: Session = Depends(get_db)):
    """total requests """
    hospital = crud.get_hospital(name, db)

    total_reqs = (
        db.query(Request).
        filter(Request.hospital_id == hospital.id).
        options(joinedload(Request.hospitals)).
        options(joinedload(Request.blood_types))
        )

    total_requests = [
        {"hospital name": req.hospitals.name,
         "req.num": req.id,
         "blood type": req.blood_types.type,
         "units": req.units,
         "status": req.status
         }
        for req in total_reqs
    ]
    return {"total_requests": total_requests}    

    
@router.post("")
async def create_request(
    name: str,
    blood_type: str = Form(...),
    requested_units: int = Form(...),
    db: Session = Depends(get_db),
    ):
    """Create Blood Request to the BloodBank"""
    hospital = crud.get_hospital(name, db)
    
    # Get BloodBank ID
    cairo_bloodbank = crud.check(BloodBank, "name", "Cairo-BloodBank", db)
    if not cairo_bloodbank:
        raise HTTPException(status_code=404, detail="Cairo-BloodBank not found")
    
    # Get BloodType ID
    blood_type_obj = db.query(BloodType).filter(BloodType.type == blood_type).first()

    # Create Request
    new_request = Request(
        blood_type_id = blood_type_obj.id,
        units = requested_units,
        hospital_id = hospital.id,
        blood_bank_id = cairo_bloodbank.id,
    )
    
    # Save Request
    crud.save(new_request, db)
    
    return {"detail": "Request created", "request_id": new_request.id}