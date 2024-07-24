from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import os
from app.api import authentication
from app.api.bloodbank import bloodbank
from app.api.hospital import hospital
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import user
from app.utils import oauth2
from app.api import websockets


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
    print("Login Page")
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    print("Register page")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/{place_name}/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, place_name):
    place_name = place_name.capitalize()
    print(f"{place_name} Dashboard Page")
    return templates.TemplateResponse("dashboard.html", {"request": request, "place_name": place_name})

@app.get("/{place_name}/inventory", response_class=HTMLResponse)
async def bloodbank_inventory_page(request: Request, place_name):
    place_name = place_name.capitalize()
    print(f"{place_name} inventory Page")
    return templates.TemplateResponse("inventory.html", {"request": request, "place_name": place_name})

@app.get("/{place_name}/requests", response_class=HTMLResponse)
async def bloodbank_requests_page(request: Request, place_name):
    place_name = place_name.capitalize()
    print(f"{place_name} requests Page")
    return templates.TemplateResponse("requests.html", {"request": request, "place_name": place_name})

@app.get("/{place_name}/request_form", response_class=HTMLResponse)
async def hospital_req_form(request: Request, place_name):
    place_name = place_name.capitalize()
    print(f"{place_name} requests Page")
    return templates.TemplateResponse("req_form.html", {"request": request, "place_name": place_name})

@app.get("/inventory")
async def get_url_inventory():
    # Here you can do any processing you need, for example querying a database
    new_url = "/x/inventory"  # The URL you want to redirect to
    return JSONResponse(content={"new_url": new_url})
