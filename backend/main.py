from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from app.api import authentication
from app.api.bloodbank import bloodbank, websockets
from app.api.hospital import hospital
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import user
from app.utils import oauth2


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(bloodbank.router)
app.include_router(websockets.router)
app.include_router(hospital.router)


app.mount("/static", StaticFiles(directory="../frontend"), name="static")
templates = Jinja2Templates(directory="../frontend/public")


@app.get("/")
def index():
    return {"data": "index page"}

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    print("Sucessssssssss")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/bloodbank/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    print("BloodBank Dashboard Page")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    print("2")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/bloodbank/inventory", response_class=HTMLResponse)
async def bloodbank_inventory_page(request: Request):
    print("BloodBank inventory Page")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
