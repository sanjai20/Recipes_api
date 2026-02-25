from fastapi import APIRouter, Query
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Recipe
from ..parser import load_recipes


# --------------------------------------------------
# CREATE ROUTER FIRST (VERY IMPORTANT)
# --------------------------------------------------
router = APIRouter(
    prefix="/api/recipes",
    tags=["Recipes"]
)


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
    load_recipes("US_recipes_null.Pdf.json")
    return {"message": "Data loaded successfully"}


# --------------------------------------------------
# SEARCH RECIPES (DYNAMIC FILTER API)
# --------------------------------------------------
@router.get("/search")
def search_recipes(
    title: str | None = None,
    cuisine: str | None = None,
    min_rating: float | None = Query(None),
    max_time: int | None = Query(None),
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

    if min_rating:
        query = query.filter(Recipe.rating >= min_rating)

    if max_time:
        query = query.filter(Recipe.total_time <= max_time)

    # ---------- Pagination ----------
    total = query.count()

    recipes = (
        query
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