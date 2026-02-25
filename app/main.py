from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .routers import recipes
from .database import Base, engine

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipes API")

# include API router
app.include_router(recipes.router)

# templates
templates = Jinja2Templates(directory="app/templates")

# static files (CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# ---------- API HEALTH ----------
@app.get("/")
def home():
    return {"message": "Recipes API Running"}


# ---------- UI PAGE ----------
@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )