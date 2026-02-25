import json
import os
import math
from sqlalchemy.orm import Session
from .models import Recipe
from .database import SessionLocal


# ✅ ALWAYS resolve project root safely
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def clean_number(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def load_recipes(json_filename: str):

    db: Session = SessionLocal()

    # ✅ FULL ABSOLUTE PATH (Render safe)
    file_path = os.path.join(BASE_DIR, json_filename)

    print("📂 Looking for file at:", file_path)

    if not os.path.exists(file_path):
        raise Exception(f"JSON file not found at {file_path}")

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

    print(f"✅ Inserted {inserted} recipes successfully!")