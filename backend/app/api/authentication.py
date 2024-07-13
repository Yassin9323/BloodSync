from fastapi import APIRouter, HTTPException, Form, Depends
from backend.app.core.database import get_db
from app.models.users import User
from app.models.hospitals import Hospital
from app.models.blood_banks import BloodBank
from app.utils.hashing import hash_password, verify_password
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session



router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == email).first()
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
    #Check the username is Unique or not
    existing_username = db.query(User).filter(User.username == username).first()
    print(existing_username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    #Check the Email is Unique or not
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed_password = hash_password(password)
    
    if role == 'hospital-admin':
        blood_bank_id = db.query(BloodBank).get(BloodBank.id).first()
        
    new_user = User(
        email=email,
        username=username,
        password=hashed_password,
        role=role,
        blood_bank_id = blood_bank_id
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
