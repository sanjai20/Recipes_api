from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import recipes
from .database import engine
from .models import Base

# --------------------------------------------------
# Create FastAPI app
# --------------------------------------------------
app = FastAPI(title="Recipes API")

# ✅ Create database tables automatically
Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# Routers
# --------------------------------------------------
app.include_router(recipes.router)

# --------------------------------------------------
# Static & Templates (UI)
# --------------------------------------------------
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home():
    return {"message": "Recipes API Running"}