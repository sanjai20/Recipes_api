import json
import os
import math
from sqlalchemy.orm import Session
from .models import Recipe
from .database import SessionLocal


# ✅ Path relative to THIS file (cloud-safe)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    CURRENT_DIR,
    "..",
    "US_recipes_null.Pdf.json"
)

DATA_PATH = os.path.abspath(DATA_PATH)


def clean_number(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def load_recipes(json_path: str):
    db: Session = SessionLocal()

    # ✅ Prevent duplicate loading (important for Render redeploys)
    if db.query(Recipe).first():
        print("⚠️ Recipes already loaded. Skipping insert.")
        db.close()
        return

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, json_path)

    print(f"📂 Loading JSON from: {file_path}")

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

    db: Session = SessionLocal()

    print("📂 Loading JSON from:", DATA_PATH)

    if not os.path.exists(DATA_PATH):
        raise Exception(f"JSON file not found at {DATA_PATH}")

    with open(DATA_PATH, "r", encoding="utf-8") as file:
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