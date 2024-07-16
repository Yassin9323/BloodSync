from fastapi import APIRouter
from app.api.bloodbank import dashboard, requests, inventory

router = APIRouter(prefix="/bloodbank", tags=["BloodBank"])

router.include_router(dashboard.router)
router.include_router(requests.router)
router.include_router(inventory.router)