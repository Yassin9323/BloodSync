from fastapi import APIRouter, HTTPException, Form
from app.core.database import DBStorage
from app.models.users import User
from app.schemas.user import UserBase
from app.utils.hashing import hash_password, verify_password
from fastapi.responses import RedirectResponse


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
def create_user(request: UserBase):
    if request:
        hashed_password = hash_password(request.password)
        new_user = User(
            email=request.email,
            username=request.username,
            password=hashed_password,
            role=request.role
        )
        db_storage.save(new_user) # Add, commit, and refresh the new user in one step
        return {"message": "Registration successful."}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/logout")
def logout():
    pass
