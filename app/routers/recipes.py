from pathlib import Path

from fastapi import APIRouter, Query
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Recipe
from ..parser import extract_calories, load_recipes


# --------------------------------------------------
# CREATE ROUTER FIRST (VERY IMPORTANT)
# --------------------------------------------------
router = APIRouter(
    prefix="/api/recipes",
    tags=["Recipes"]
)

DATA_FILE = Path(__file__).resolve().parents[2] / "US_recipes_null.Pdf.json"


# --------------------------------------------------
# GET ALL RECIPES (Pagination)
# --------------------------------------------------
@router.get("/")
def get_recipes(page: int = 1, limit: int = 10):

    db: Session = SessionLocal()

    total = db.query(Recipe).count()

    recipes = (
        db.query(Recipe)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    db.close()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": recipes
    }


# --------------------------------------------------
# LOAD JSON DATA INTO DATABASE
# --------------------------------------------------
@router.post("/load-data")
def load_data():
    result = load_recipes(str(DATA_FILE))

    if result["skipped"]:
        return {"message": "Recipes already loaded", **result}

    return {"message": "Data loaded successfully", **result}


# --------------------------------------------------
# SEARCH RECIPES (DYNAMIC FILTER API)
# --------------------------------------------------
@router.get("/search")
def search_recipes(
    title: str | None = None,
    cuisine: str | None = None,
    min_rating: float | None = Query(None),
    max_time: int | None = Query(None),
    calories: int | None = Query(None),
    page: int = 1,
    limit: int = 10
):

    db: Session = SessionLocal()

    query = db.query(Recipe)

    # ---------- Filters ----------
    if title:
        query = query.filter(Recipe.title.ilike(f"%{title}%"))

    if cuisine:
        query = query.filter(Recipe.cuisine.ilike(f"%{cuisine}%"))

    if min_rating is not None:
        query = query.filter(Recipe.rating >= min_rating)

    if max_time is not None:
        query = query.filter(Recipe.total_time <= max_time)

    recipes = query.all()

    if calories is not None:
        filtered_recipes = []

        for recipe in recipes:
            recipe_calories = extract_calories(recipe.nutrients)
            if recipe_calories is not None and recipe_calories <= calories:
                filtered_recipes.append(recipe)

        recipes = filtered_recipes

    total = len(recipes)

    start = (page - 1) * limit
    end = start + limit
    recipes = recipes[start:end]

    db.close()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": recipes
    }
