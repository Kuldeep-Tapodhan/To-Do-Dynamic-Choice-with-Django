# 📋 To-Do Dynamic Choice with Django

A full-featured **task management application** built with Django, featuring a Kanban-style board with dynamic status columns, JWT authentication, role-based permissions, and a modern responsive UI with dark mode support.

🔗 **Live Demo:** [https://to-do-dynamic-choice-with-django.onrender.com](https://to-do-dynamic-choice-with-django.onrender.com)

---

## ✨ Features

### Core Functionality

- **Kanban Task Board** — Drag-free task cards organized by status columns (Unassigned → To Do → In Progress → Review → Done)
- **Dynamic Status Management** — Tasks can be moved between status columns via dropdown selectors
- **Inline Title Editing** — Click any task title to edit it in-place
- **Task Metadata** — Description, priority levels (Low / Medium / High), due dates, and completion tracking
- **Priority Color Coding** — Task cards are color-coded by priority: 🔴 High, 🟡 Medium, 🟢 Low

### Authentication & Authorization

- **Custom User Model** — Extended Django user with email (required, unique), phone, and bio fields
- **JWT Authentication** — Token-based auth for API clients using `djangorestframework-simplejwt`
- **Session Authentication** — Traditional session-based auth for template-rendered pages
- **Role-Based Permissions** — Superusers can view all normal users' tasks; normal users only see their own data
- **Object-Level Security** — Users cannot view, edit, or delete other users' tasks

### Superuser Features

- **User Selector Dropdown** — Superusers can switch between viewing any normal user's task board
- **Viewing Banner** — Clear indicator when viewing another user's data
- **User List API** — Superuser-only endpoint to list all registered users

### UI/UX

- **Dark/Light Theme Toggle** — Persisted via localStorage
- **Fully Responsive** — Mobile-first design with breakpoints at 768px, 380px
- **Modern Design** — Gradient headers, glassmorphism effects, smooth transitions
- **Rich Signup Form** — Grouped fields (Account Info / Personal Info) with validation

### API

- **RESTful API** — Full CRUD operations on tasks
- **JWT Token Endpoints** — Obtain, refresh, and verify tokens
- **API Registration** — Register via API and receive JWT tokens immediately
- **User Profile API** — Retrieve authenticated user's profile

---

## 🏗️ Tech Stack

| Layer            | Technology                             |
| ---------------- | -------------------------------------- |
| **Backend**      | Django 6.0, Django REST Framework      |
| **Auth**         | djangorestframework-simplejwt (JWT)    |
| **Database**     | PostgreSQL (Render production)         |
| **Static Files** | WhiteNoise                             |
| **Deployment**   | Render (Web Service + PostgreSQL)      |
| **Frontend**     | Vanilla HTML/CSS/JS (Django Templates) |

---

## 📁 Project Structure

```
To-Do-Dynamic-Choice-with-Django/
├── dynamic_choices/              # Django project configuration
│   ├── settings.py               #   Settings (DB, JWT, REST Framework)
│   ├── urls.py                   #   Root URL routing (auth + JWT endpoints)
│   └── wsgi.py                   #   WSGI entry point for production
│
├── core/                         # Main application
│   ├── models.py                 #   TimeStampedModel, CustomUser, Status, Task
│   ├── views.py                  #   TaskViewSet, RegisterView, UserProfileView, etc.
│   ├── serializers.py            #   User, Register, Task, Status serializers
│   ├── forms.py                  #   CustomUserCreationForm (signup)
│   ├── admin.py                  #   Enhanced admin for CustomUser, Task, Status
│   ├── urls.py                   #   App URLs (/api/tasks/, /api/register/, etc.)
│   └── migrations/               #   Database migrations + seed data
│
├── templates/
│   ├── core/
│   │   └── task_board.html       #   Main task board (Kanban UI)
│   └── registration/
│       ├── login.html            #   Login page
│       └── signup.html           #   Registration page
│
├── manage.py
├── requirements.txt
├── build.sh                      # Render build script
├── .env                          # Environment variables (not in git)
└── .gitignore
```

---

## 📊 Database Models

### TimeStampedModel (Abstract)

Provides `created_at` and `modified_at` fields to all models.

### CustomUser

Extends `AbstractUser` with:
| Field | Type | Notes |
| ---------- | ------------- | ------------------------ |
| `email` | EmailField | Required, unique |
| `phone` | CharField(20) | Optional |
| `bio` | TextField | Optional, max 500 chars |

### Status

| Field  | Type           | Notes  |
| ------ | -------------- | ------ |
| `name` | CharField(100) | Unique |

Default statuses (seeded via migration): `To Do`, `In Progress`, `Review`, `Done`

### Task

| Field          | Type            | Notes                            |
| -------------- | --------------- | -------------------------------- |
| `title`        | CharField(200)  | Required                         |
| `description`  | TextField       | Optional                         |
| `priority`     | CharField(10)   | Choices: `low`, `medium`, `high` |
| `due_date`     | DateField       | Optional                         |
| `is_completed` | BooleanField    | Default: `False`                 |
| `status`       | FK → Status     | Nullable (Unassigned)            |
| `user`         | FK → CustomUser | Owner of the task                |

---

## 🔌 API Endpoints

### Authentication (JWT)

| Method | Endpoint              | Auth | Description                    |
| ------ | --------------------- | ---- | ------------------------------ |
| POST   | `/api/token/`         | None | Get access + refresh tokens    |
| POST   | `/api/token/refresh/` | None | Refresh an access token        |
| POST   | `/api/token/verify/`  | None | Verify a token is valid        |
| POST   | `/api/register/`      | None | Register user + get JWT tokens |

### Tasks (CRUD)

| Method | Endpoint           | Auth     | Description                            |
| ------ | ------------------ | -------- | -------------------------------------- |
| GET    | `/api/tasks/`      | Required | List tasks (own tasks / all for admin) |
| POST   | `/api/tasks/`      | Required | Create a task                          |
| GET    | `/api/tasks/<id>/` | Required | Retrieve a task                        |
| PUT    | `/api/tasks/<id>/` | Required | Full update a task                     |
| PATCH  | `/api/tasks/<id>/` | Required | Partial update a task                  |
| DELETE | `/api/tasks/<id>/` | Required | Delete a task                          |

### User

| Method | Endpoint        | Auth      | Description                    |
| ------ | --------------- | --------- | ------------------------------ |
| GET    | `/api/profile/` | Required  | Get authenticated user profile |
| GET    | `/api/users/`   | Superuser | List all normal users          |

### Example: Login & Create Task

```bash
# 1. Get JWT token
curl -X POST https://to-do-dynamic-choice-with-django.onrender.com/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_user", "password": "your_pass"}'

# Response: {"access": "eyJ...", "refresh": "eyJ..."}

# 2. Create a task
curl -X POST https://to-do-dynamic-choice-with-django.onrender.com/api/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Task", "description": "Details", "priority": "high", "status": 1}'
```

---

## 🔐 Permissions & Security

| Role            | Can Do                                                          |
| --------------- | --------------------------------------------------------------- |
| **Normal User** | Create, read, update, delete **own tasks only**                 |
| **Superuser**   | View any normal user's tasks via dropdown, access user list API |

**Security measures:**

- Normal users get `403 Forbidden` if they attempt `?user_id=` URL manipulation
- Superusers cannot view other superuser accounts
- Task `user` field is read-only in the API (set automatically)
- `perform_update` prevents reassigning tasks to other users
- `perform_destroy` verifies ownership before deletion
- JWT tokens expire after 60 min (access) / 7 days (refresh), configurable via `.env`

---

## 🚀 Local Development Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- pip or uv

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kuldeep-Tapodhan/To-Do-Dynamic-Choice-with-Django.git
cd To-Do-Dynamic-Choice-with-Django

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cat > .env << 'EOF'
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Local PostgreSQL
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
EOF

# 5. Create database & run migrations
createdb todo_db
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/`

---

## 🌐 Render Deployment

### Environment Variables (Render Dashboard)

```
SECRET_KEY=<your-production-secret-key>
DEBUG=False
ALLOWED_HOSTS=to-do-dynamic-choice-with-django.onrender.com
DB_NAME=<render-db-name>
DB_USER=<render-db-user>
DB_PASSWORD=<render-db-password>
DB_HOST=<render-db-host>.oregon-postgres.render.com
DB_PORT=5432
DB_SSLMODE=require
```

### Build & Start Commands

| Setting           | Value                                       |
| ----------------- | ------------------------------------------- |
| **Build Command** | `./build.sh`                                |
| **Start Command** | `gunicorn dynamic_choices.wsgi:application` |

### `build.sh`

```bash
#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

---

## 📦 Dependencies

| Package                         | Purpose                      |
| ------------------------------- | ---------------------------- |
| `django`                        | Web framework                |
| `djangorestframework`           | REST API                     |
| `djangorestframework-simplejwt` | JWT authentication           |
| `gunicorn`                      | Production WSGI server       |
| `psycopg2-binary`               | PostgreSQL adapter           |
| `dj-database-url`               | Database URL parsing         |
| `whitenoise`                    | Static file serving          |
| `python-dotenv`                 | Environment variable loading |

---

## 🧪 Testing

```bash
python manage.py test
```

---

## 🐛 Troubleshooting

| Problem                                    | Solution                                                           |
| ------------------------------------------ | ------------------------------------------------------------------ |
| `ModuleNotFoundError: No module named ...` | `pip install -r requirements.txt`                                  |
| `Dependency on app with no migrations`     | `python manage.py makemigrations core && python manage.py migrate` |
| `Method Not Allowed (GET): /logout/`       | Django 5+ requires POST for logout (already handled in template)   |
| Static files not loading on Render         | `python manage.py collectstatic --noinput`                         |
| SSL error connecting to Render DB          | Add `DB_SSLMODE=require` to `.env`                                 |

---

## 👨‍💻 Author

**Kuldeep Tapodhan**

- GitHub: [@Kuldeep-Tapodhan](https://github.com/Kuldeep-Tapodhan)

---

## 📄 License

This project is licensed under the MIT License.

---

**Last Updated:** February 23, 2026

**Status:** ✅ Live on Render | ✅ JWT Auth | ✅ Role-Based Permissions | ✅ Mobile Responsive
