from fastapi import FastAPI
from app.api.authentication import router

app = FastAPI()

# Include the router from the auth module
app.include_router(router)


@app.get("/")
def index():
    return {"data": "index page"}
