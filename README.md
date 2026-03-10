# 🍽 Recipes API & Dashboard

A full-stack Recipe Data API built using **FastAPI**, **SQLite**, and a lightweight **HTML/CSS dashboard UI**.

This project parses a large JSON dataset of recipes, stores it in a database, and exposes REST APIs with filtering, pagination, and search capabilities. A simple dashboard UI allows users to explore recipes visually.

---

# 🚀 Features

### Backend API

* Parse recipe JSON dataset
* Store structured data in SQLite database
* REST API built using FastAPI
* Pagination support
* Search & filtering
* Sorted by rating
* Handles NaN values safely

### Frontend Dashboard

* Interactive recipe table
* Star rating display ⭐
* Search filters
* Pagination controls
* Click row to view recipe details
* Nutrition information panel
* Responsive UI

---

# 🛠 Tech Stack

Backend

* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

Frontend

* HTML
* CSS
* JavaScript

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── routers/
│   │   └── recipes.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── static/
│   │   └── style.css
│   │
│   ├── models.py
│   ├── database.py
│   ├── crud.py
│   ├── parser.py
│   └── main.py
│
├── requirements.txt
├── US_recipes_null.Pdf.json
└── README.md
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/sanjai20/Recipes_api.git
cd Recipes_api
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```
python -m uvicorn app.main:app --reload
```

Server will run at

```
http://127.0.0.1:8000
```

---

# 🌐 Application URLs

### Dashboard UI

```
http://127.0.0.1:8000
```

### API Documentation (Swagger)

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## Get All Recipes

```
GET /api/recipes?page=1&limit=10
```

Returns paginated recipes sorted by rating (descending).

Example request

```
http://127.0.0.1:8000/api/recipes?page=1&limit=10
```

Example response

```
{
 "page":1,
 "limit":10,
 "total":8451,
 "data":[
   {
     "title":"Sweet Potato Pie",
     "cuisine":"Southern Recipes",
     "rating":4.8,
     "prep_time":15,
     "cook_time":100,
     "total_time":115
   }
 ]
}
```

---

## Search Recipes

```
GET /api/recipes/search
```

Query Parameters

| Parameter  | Description            |
| ---------- | ---------------------- |
| title      | Search by recipe title |
| cuisine    | Filter by cuisine      |
| min_rating | Minimum rating         |
| max_time   | Maximum total time     |
| calories   | Filter by calories     |

Example request

```
http://127.0.0.1:8000/api/recipes/search?title=pie&min_rating=4
```

Example response

```
{
 "data":[
  {
   "title":"Sweet Potato Pie",
   "cuisine":"Southern Recipes",
   "rating":4.8,
   "total_time":115
  }
 ]
}
```

---

# 🗄 Database Schema

The database contains a table named **recipes**.

| Column      | Type                  |
| ----------- | --------------------- |
| id          | Integer (Primary Key) |
| title       | VARCHAR               |
| cuisine     | VARCHAR               |
| rating      | FLOAT                 |
| prep_time   | INTEGER               |
| cook_time   | INTEGER               |
| total_time  | INTEGER               |
| description | TEXT                  |
| nutrients   | JSON                  |
| serves      | VARCHAR               |

The schema is implemented using **SQLAlchemy ORM** in:

```
app/models.py
```

The database is automatically created when the application starts.

---

# 🧪 API Testing

You can test the API using:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

Swagger provides an interactive interface to:

* Test endpoints
* Provide query parameters
* View responses

---

### Example Curl Request

Get recipes

```
curl "http://127.0.0.1:8000/api/recipes?page=1&limit=10"
```

Search recipes

```
curl "http://127.0.0.1:8000/api/recipes/search?title=pie&min_rating=4"
```

---

# 📊 Dataset

The project uses the provided dataset:

```
US_recipes_null.Pdf.json
```

During parsing:

* NaN values are converted to `NULL`
* Nutrients are stored as JSON
* Data is inserted into SQLite database

---

# 🖥 UI Features

The dashboard provides:

* Recipe table view
* Star rating visualization
* Row click to view detailed recipe
* Nutrition information panel
* Search filters
* Pagination (15 / 25 / 50 results)
* No-results fallback screen

---

# 👨‍💻 Author

Sanjai Prashad

GitHub
https://github.com/sanjai20

---

# 📌 Notes

This project was developed as part of the **Recipe Data Collection and API Development Assessment**.

It demonstrates:

* Backend API design
* Database modeling
* Data parsing
* REST API development
* Frontend integration
