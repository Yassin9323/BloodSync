from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from app.api import authentication
from app.api.bloodbank import bloodbank, websockets
from app.api.hospital import hospital


app = FastAPI()


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

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    print("2")
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
