from sqlalchemy.orm import Session
from .models import Recipe


def get_recipes(db: Session, page: int = 1, limit: int = 10):

    offset = (page - 1) * limit

    total = db.query(Recipe).count()

    recipes = (
        db.query(Recipe)
        .order_by(Recipe.rating.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": recipes,
    }