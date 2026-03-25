import json
import math
import re
from pathlib import Path

from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Recipe


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


def extract_calories(nutrients):
    """
    Extract the numeric calories value from the nutrients payload.
    The dataset stores calories as strings like "389 kcal".
    """
    if not nutrients or not isinstance(nutrients, dict):
        return None

    calories = nutrients.get("calories")

    if calories is None:
        return None

    if isinstance(calories, (int, float)):
        return None if isinstance(calories, float) and math.isnan(calories) else float(calories)

    if not isinstance(calories, str):
        return None

    match = re.search(r"(\d+(?:\.\d+)?)", calories)
    if not match:
        return None

    return float(match.group(1))


# ---------- main parser ----------
def load_recipes(json_path: str):
    db: Session = SessionLocal()

    existing_count = db.query(Recipe).count()
    if existing_count > 0:
        db.close()
        print(f"Recipes already loaded: {existing_count}")
        return {"inserted": 0, "skipped": True, "total": existing_count}

    file_path = Path(json_path)
    with open(file_path, "r", encoding="utf-8") as file:
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

    print(f"Inserted {inserted} recipes successfully!")
    return {"inserted": inserted, "skipped": False, "total": inserted}
