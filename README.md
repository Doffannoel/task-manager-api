# 📝 Task Management API

A simple and scalable backend API built with Django REST Framework for managing tasks with categories, priorities, and deadlines. This project is part of a technical internship assessment.

---

## 🚀 Features

- ✅ CRUD Tasks (Create, Read, Update, Delete)
- 🏷️ Task attributes: title, description, category, priority, deadline
- 📅 Filtering by category, priority, deadline range
- 📊 Sorting by creation date, priority, deadline
- 🔒 Input validation
- 📄 Auto-generated Swagger API documentation
- 🧪 Unit-tested business logic

---

## 🏗️ Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- django-filter
- gunicorn (for later production deployment)

---

## 📂 Project Structure

```
taskmanager/
├── manage.py
├── taskmanager/         # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/               # Main app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
├── requirements.txt
├── Procfile
└── .gitignore
```

---

## 🧪 Installation & Local Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Doffannoel/task-manager-api.git
   cd <repo-name>
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start server:**
   ```bash
   python manage.py runserver
   ```

---

## 📌 API Endpoints

| Method | Endpoint        | Description               |
|--------|------------------|---------------------------|
| POST   | `/tasks/`         | Create a task             |
| GET    | `/tasks/`         | List all tasks            |
| GET    | `/tasks/<id>/`    | Get specific task         |
| PUT    | `/tasks/<id>/`    | Update task               |
| DELETE | `/tasks/<id>/`    | Delete task               |

### ✅ Filtering
- `/tasks/?priority=High`
- `/tasks/?category=Work`
- `/tasks/?ordering=deadline`

---

## 📄 API Documentation (Swagger)

Explore your API interactively via:

- Swagger UI: [`/swagger/`](http://localhost:8000/swagger/)
- Redoc UI: [`/redoc/`](http://localhost:8000/redoc/)
- JSON Schema: [`/swagger.json`](http://localhost:8000/swagger.json)

---

## ✅ Validation Rules

- `title`: cannot be empty
- `deadline`: must be a future date
- `priority`: must be `Low`, `Medium`, or `High`

---

## 🧪 Run Unit Tests

```bash
python manage.py test
```

> Example test included for `POST /tasks/`. Additional tests recommended for full coverage.

---

## 👤 Author

- Doffannoel Sihotang  
- Email: noelsihotang2004@gmail.com  
- Project Date: July 2025

---

## 📄 License

This project is licensed under the MIT License.
