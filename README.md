# 🍲 Recipes API — FastAPI Backend

A high-performance REST API built using **FastAPI** for managing and searching recipe data with filtering, pagination, and structured database storage.

---

## 🚀 Features

✅ Load large recipe dataset (8,000+ recipes)
✅ Pagination support
✅ Advanced search filters
✅ SQLite database integration
✅ Clean modular architecture
✅ Swagger API documentation
✅ Production-style FastAPI structure

---

## 🧠 Tech Stack

* **FastAPI**
* **Python 3.10**
* **SQLAlchemy**
* **SQLite**
* **Uvicorn**
* **Jinja2**
* **REST API Design**

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── routers/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── database.py
│   ├── crud.py
│   ├── parser.py
│   └── main.py
│
├── requirements.txt
└── US_recipes_null.Pdf.json
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sanjai20/Recipes_api.git
cd Recipes_api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI included.

---

## 🔍 API Endpoints

### Get Recipes (Pagination)

```
GET /api/recipes?page=1&limit=10
```

### Load Dataset

```
POST /api/recipes/load-data
```

### Search Recipes

```
GET /api/recipes/search
```

Filters supported:

* title
* cuisine
* min_rating
* max_time

---

## 📊 Dataset

Contains **8000+ recipes** including:

* Recipe title
* Cuisine type
* Cooking time
* Rating
* Nutrition information

---

## 👨‍💻 Author

**Sanjai**
Cybersecurity Student | Backend Developer

---

## ⭐ Future Improvements

* Docker support
* PostgreSQL migration
* Authentication (JWT)
* Cloud deployment (Render / AWS)
* Frontend dashboard
