from fastapi import APIRouter, HTTPException, Form
from app.api.hospital import dashboard, inventory, requests

router = APIRouter()
router.include_router(dashboard.router)
router.include_router(inventory.router)
router.include_router(requests.router)