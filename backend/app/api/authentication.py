from fastapi import APIRouter, HTTPException, Form, Depends
from app.core.database import get_db
from app.models.users import User
from app.models.blood_banks import BloodBank
from app.models.hospitals import Hospital
from app.utils.hashing import hash_password, verify_password
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core import crud
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr


router = APIRouter(tags=["Authentication"])

class LoginForm(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
def login(email: EmailStr = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.check(User,"email", email, db)
    if user:
        if verify_password(password, user.password):
            return JSONResponse(content={"success": True, "message": "Login successful"})

    return JSONResponse(content={"success": False, "message": "Invalid credentials"}, status_code=401)


@router.post("/register")
async def create_user(
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.check(User,"username", username, db)    #Check the username is Unique or not
    if user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    user = crud.check(User, 'email', email, db)        #Check the Email is Unique or not
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    hashed_password = hash_password(password)
    
    # Get ID for the user
    if role == 'blood-bank-admin': 
        blood_bank_id = crud.id_by_role(role, db)
        hospital_id = None
    else: # hospital-admin
        hospital_id = crud.id_by_role(role, db)
        blood_bank_id = None
        
    new_user = User(
        email=email,
        username=username,
        password=hashed_password,
        role=role,
        blood_bank_id = blood_bank_id,
        hospital_id = hospital_id
    )
    try:
        crud.save(new_user, db)
        return {"message": "Successful Registration"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/logout")
def logout():
    pass
