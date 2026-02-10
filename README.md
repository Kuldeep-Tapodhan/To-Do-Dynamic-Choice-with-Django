# To-Do Dynamic Choice with Django

## 📋 Project Overview
A comprehensive Django-based to-do list application with dynamic choice fields and modern web interface. This project is fully deployed on Render and features real-time task management capabilities.

---

## 📁 Project Structure

```
To-Do-Dynamic-Choice-with-Django/
├── dynamic_choices/           # Django project configuration
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration for deployment
│   ├── settings.py           # Project settings & configurations
│   ├── urls.py               # URL routing configuration
│   └── wsgi.py               # WSGI configuration for production
│
├── core/                      # Main Django application
│   ├── migrations/           # Database migration files
│   ├── __init__.py
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── tests.py              # Unit tests
│   ├── urls.py               # App-level URL routing
│   ├── views.py              # View logic & request handlers
│   └── templates/            # HTML templates
│
├── templates/                 # Global templates directory
│   ├── base.html
│   └── index.html
│
├── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── build.sh                   # Build script for Render deployment
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## ✨ Features

- ✅ **Dynamic To-Do List** - Create, read, update, and delete tasks in real-time
- ✅ **Dynamic Choice Fields** - Use dropdown menus with dynamic options
- ✅ **User Authentication** - Secure user login and registration
- ✅ **User Authorization** - Role-based access control
- ✅ **RESTful API** - Full CRUD operations via API endpoints
- ✅ **Responsive Design** - Mobile-friendly interface
- ✅ **Database Integration** - SQLite (development) / PostgreSQL (production)
- ✅ **Render Deployment** - Ready for production deployment

---

## 📦 Dependencies

```
Django >= 3.2
djangorestframework >= 3.10
django-cors-headers >= 3.5
gunicorn >= 20.0
python-decouple >= 3.4
psycopg2-binary >= 2.8  # For PostgreSQL
```

View the complete list in [requirements.txt](requirements.txt)

---

## 🚀 Installation Instructions

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kuldeep-Tapodhan/To-Do-Dynamic-Choice-with-Django.git
   cd To-Do-Dynamic-Choice-with-Django
   ```

2. **Create a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file for environment variables:**
   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - Main Application: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📖 Usage Guide

### Dashboard
- Navigate to the homepage to view your to-do list
- Tasks are displayed with their status, priority, and due date

### Creating Tasks
1. Click the "Add New Task" button
2. Fill in task details:
   - Task title
   - Description
   - Due date
   - Priority level (using dynamic choice field)
   - Category
3. Click "Save" to create the task

### Managing Tasks
- **Edit**: Click the edit icon to modify task details
- **Complete**: Mark tasks as complete with the checkbox
- **Delete**: Remove tasks with the delete button
- **Filter**: Filter tasks by status, priority, or category

### Admin Panel
- Access at `/admin/`
- Manage users, tasks, and system settings
- View application logs and analytics

---

## 🔌 API Endpoints

### Tasks Management
```
GET    /api/tasks/              - Retrieve all tasks
POST   /api/tasks/              - Create a new task
GET    /api/tasks/<id>/         - Retrieve a specific task
PUT    /api/tasks/<id>/         - Update a task
PATCH  /api/tasks/<id>/         - Partially update a task
DELETE /api/tasks/<id>/         - Delete a task
```

### Authentication
```
POST   /api/auth/login/         - User login
POST   /api/auth/logout/        - User logout
POST   /api/auth/register/      - User registration
GET    /api/auth/profile/       - Get user profile
```

### Example API Request
```bash
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🌐 Render Deployment Guide

### Prerequisites
- Render account (free at [render.com](https://render.com))
- GitHub repository connected to Render

### Deployment Steps

1. **Create Environment Variables on Render:**
   - Go to your service settings on Render
   - Add the following environment variables:
     ```
     SECRET_KEY=your_production_secret_key
     DEBUG=False
     DATABASE_URL=your_postgres_database_url
     ALLOWED_HOSTS=your-app-name.onrender.com
     PYTHON_VERSION=3.10.12
     ```

2. **Configure Build Command:**
   ```bash
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```

3. **Configure Start Command:**
   ```bash
   gunicorn dynamic_choices.wsgi:application --bind 0.0.0.0:$PORT
   ```

4. **Deploy:**
   - Push your code to GitHub
   - Render will automatically deploy on every push to the main branch

5. **Database Setup:**
   - Create a PostgreSQL database on Render
   - Update the `DATABASE_URL` environment variable

6. **Access Your Application:**
   - Your app will be available at `https://your-app-name.onrender.com`

### Monitoring & Logs
- View deployment logs in the Render dashboard
- Check application logs in real-time
- Monitor resource usage and performance metrics

---

## 🔧 Configuration

### Django Settings
Key settings in `dynamic_choices/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 📝 Database Models

### Task Model
```python
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'django'`**
- Solution: Install dependencies with `pip install -r requirements.txt`

**Issue: `django.core.exceptions.ImproperlyConfigured`**
- Solution: Check your environment variables and `settings.py` configuration

**Issue: Database migration errors**
- Solution: Run `python manage.py migrate` and check database connection

**Issue: Static files not loading on Render**
- Solution: Run `python manage.py collectstatic` and check STATIC_URL and STATIC_ROOT

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Render Documentation](https://render.com/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Kuldeep Tapodhan**
- GitHub: [@Kuldeep-Tapodhan](https://github.com/Kuldeep-Tapodhan)
- Email: djtapodhan143@gmail.com

---

## 🎉 Acknowledgments

- Django community for the excellent framework
- Render for seamless deployment
- Contributors and users

---

**Last Updated:** February 10, 2026

**Status:** ✅ Deployed on Render | ✅ Production Ready
