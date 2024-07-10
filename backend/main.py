from fastapi import FastAPI, Request
from app.api.authentication import router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os


app = FastAPI()
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the static files and templates
static_files_path = os.path.join(current_dir, 'frontend/public')
app.mount("/static", StaticFiles(directory="public"), name="static")
templates = Jinja2Templates(directory="frontend/src/pages/html")
# Include the router from the auth module
app.include_router(router)


@app.get("/")
def index():
    return {"data": "index page"}

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    print("Sucessssssssss")
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    return templates.TemplateResponse("errorpage.html", {"request": request})