from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .database import Base, SessionLocal, engine
from .models import Recipe
from .parser import load_recipes
from .routers import recipes

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "US_recipes_null.Pdf.json"

app = FastAPI(
    title="Recipes Search UI",
    description="Recipe search with advanced filters",
    version="1.0"
)

# include API routes
app.include_router(recipes.router)

# templates + static
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        has_recipes = db.query(Recipe.id).first() is not None
    finally:
        db.close()

    if not has_recipes and DATA_FILE.exists():
        load_recipes(str(DATA_FILE))


# homepage UI
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
