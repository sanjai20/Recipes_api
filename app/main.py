from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .routers import recipes

app = FastAPI(
    title="Recipes Search UI",
    description="Recipe search with advanced filters",
    version="1.0"
)

# include API routes
app.include_router(recipes.router)

# templates + static
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# homepage UI
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )