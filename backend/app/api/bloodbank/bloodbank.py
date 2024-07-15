from fastapi import APIRouter
from app.api.bloodbank import dashboard

router = APIRouter(prefix="/blood-bank", tags=["BloodBank"])

router.include_router(dashboard.router)  