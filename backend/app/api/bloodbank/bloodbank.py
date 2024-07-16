from fastapi import APIRouter
from app.api.bloodbank import dashboard, requests

router = APIRouter(prefix="/bloodbank", tags=["BloodBank"])

router.include_router(dashboard.router)
router.include_router(requests.router)