from fastapi import APIRouter, HTTPException, Form, Depends, status
from app.core.database import get_db
from app.models.users import User
from app.models.blood_banks import BloodBank
from app.models.hospitals import Hospital
from app.utils.hashing import Hash
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core import crud
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordRequestForm
from app.utils import token


router = APIRouter(tags=["Authentication"])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"User with email '{request.username}' not found")
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Incorrect password")
    # print(user.role)
    # print(type(request))
    if user.role == "blood-bank-admin":
        place_name = "Cairo-BloodBank"
    else:
        hospital = db.query(Hospital).filter(Hospital.id == user.hospital_id).first()
        place_name = hospital.name
    print(place_name)
    access_token = token.create_access_token(data={"sub": user.email, "role": user.role, "place_name": place_name})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
async def create_user(
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...),
    place_name: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.check(User,"username", username, db)    #Check the username is Unique or not
    if user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    user = crud.check(User, 'email', email, db)        #Check the Email is Unique or not
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    hashed_password = Hash.bcrypt(password)
    print(role)
    print(place_name)
    # Get ID for the user
    if role == 'blood-bank-admin': 
        blood_bank_id = crud.id_by_role(role, place_name, db)
        hospital_id = None
    else: # hospital-admin
        hospital_id = crud.id_by_role(role, place_name, db)
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
        access_token = token.create_access_token(data={"sub": email, "role": role, "place_name": place_name})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/logout")
def logout():
    pass
