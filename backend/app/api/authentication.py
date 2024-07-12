from fastapi import APIRouter, HTTPException, Form, Depends
from app.core.database import DBStorage
from app.core.database__2 import get_db
from app.models.users import User
from app.models.hospitals import Hospital
from app.models.blood_banks import BloodBank
from app.schemas.user import UserBase
from app.utils.hashing import hash_password, verify_password
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session



router = APIRouter(tags=["Authentication"])
db_storage = DBStorage()

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    user = db_storage.get_by_email(email)
    print(user)
    if user:
        if verify_password(password, user.password):
            return RedirectResponse(url="/dashboard", status_code=303)
            # return {"message": "Login successful"}

    print("Login failed: Invalid credentials")
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/register")
def create_user(
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_username = db.query(User).filter(User.username == username).first()
    print(existing_username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed_password = hash_password(password)
    
    if role == 'hospital-admin':
        bank_id = db.query(BloodBank).get(BloodBank.id).all()
        blood_bank_id = bank_id

    new_user = User(
        email=email,
        username=username,
        password=hashed_password,
        role=role,
        blood_bank_id = bank_id
    )

    try:
        db.add(new_user)
        db.commit()
        return {"message": "Registration successful."}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@router.get("/logout")
def logout():
    pass
