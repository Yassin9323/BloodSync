from fastapi import FastAPI, Request
from app.api.authentication import router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")
# Include the router from the auth module
app.include_router(router)


@app.get("/")
def index():
    return {"data": "index page"}

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    print("Sucessssssssss")
    return templates.TemplateResponse("login.html", {"request": request})

