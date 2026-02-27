import json
import math
from sqlalchemy.orm import Session
from .models import Recipe
from .database import SessionLocal


# ---------- helper function ----------
def clean_number(value):
    """
    Convert NaN or invalid numbers into NULL
    (assessment requirement)
    """
    if value is None:
        return None

    if isinstance(value, float) and math.isnan(value):
        return None

    return value


# ---------- main parser ----------
def load_recipes(json_path: str):
    db: Session = SessionLocal()

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    inserted = 0

    for item in data.values():

        recipe = Recipe(
            cuisine=item.get("cuisine"),
            title=item.get("title"),
            rating=clean_number(item.get("rating")),
            prep_time=clean_number(item.get("prep_time")),
            cook_time=clean_number(item.get("cook_time")),
            total_time=clean_number(item.get("total_time")),
            description=item.get("description"),
            nutrients=item.get("nutrients"),
            serves=item.get("serves"),
        )

        db.add(recipe)
        inserted += 1

    db.commit()
    db.close()

    print(f"✅ Inserted {inserted} recipes successfully!")