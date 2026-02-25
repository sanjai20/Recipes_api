import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# --------------------------------------------------
# Get absolute project directory (Render compatible)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database file path
DB_PATH = os.path.join(BASE_DIR, "recipes.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# --------------------------------------------------
# Engine
# --------------------------------------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# --------------------------------------------------
# Session
# --------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()