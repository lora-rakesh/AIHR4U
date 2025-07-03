# AIHR4U Backend (Django + DRF) 

This is the backend API for **AIHR4U**, built with Django and Django REST Framework. It includes company verification APIs and is deployed on Render with PostgreSQL as the database.

---

##  Live API

- **Base URL**: https://aihr4u.onrender.com
- **Verify Company Endpoint**: `api/verify-company/`  
  Example: `POST https://aihr4u.onrender.com/api/verify-company/`

---

##  Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- PostgreSQL (via Render)
- `django-cors-headers`
- Render.com (deployment)
- Gunicorn + Whitenoise for static hosting

---

##  Local Development Setup

### 1. Clone the repository

```bash
git init
git clone https://github.com/lora-rakesh/AIHR4U.git

## Installation and Setup Instructions

1. **Create Project Directory**
   ```bash
   mkdir HR4U
   cd HR4U

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows

3. **Install all project dependencies**

   ```bash
   pip install \
   django \
   djangorestframework \
   djangorestframework-simplejwt \
   psycopg2-binary \
   python-decouple \
   python-dotenv \
   dj-database-url \
   whitenoise \
   django-cors-headers\

4. **Create Django Project and App**
   ```bash
   django-admin startproject project
   cd project
   python manage.py startapp app

5. **Make changes in settings.py**
   - Add 
    'rest_framework',
    'rest_framework_simplejwt',
    'app',
    'corsheaders', to the INSTALLED_APPS list.
   - Add
    'corsheaders.middleware.CorsMiddleware', 
     'whitenoise.middleware.WhiteNoiseMiddleware', as well. 
   - Configure Database in settings.py ( Via Render)

6. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. **Final Setup and Run**
   ```bash
   python manage.py createsuperuser  # Create Superuser for admin panel
   python manage.py runserver   # Run the Development Server
   pip freeze > requirements.txt  # Create Requirements File


8. **Folder Structure**
   ```bash
   HR4U/
   ├── project/                      # Main Django project (settings and configuration)
   │   ├── __init__.py
   │   ├── settings.py               # Global settings
   │   ├── urls.py                   # Root URL configuration
   │   ├── wsgi.py                   # WSGI entry-point for deployment
   │   └── asgi.py                   # ASGI entry-point for async support
   │
   ├── app/                          # Core Django app (business logic)
   ├── __init__.py
   │   ├── admin.py                  # Admin panel configuration
   │   ├── apps.py
   │   ├── models.py                 # Models
   │   ├── serializers.py            # Data validation & transformation
   │   ├── urls.py                   # App-level routing
   │   ├── utils.py                  # Utility functions (OTP, helper logic)
   │   └── views.py                  # Business logic & API views
   │                 
   │
   │
   ├── migrations/                   # Django model migrations
   │
   ├── .env                          # Environment variables (not committed)
   ├── .gitignore                    # Files/folders to exclude from Git
   ├── manage.py                     # Django management utility
   ├── render.yaml                   # MAIN deployment config
   ├── requirements.txt              # Python dependencies
   └── README.md                     # Project documentation


🔒 CSRF Protection
This project uses session authentication and CSRF protection.

To get CSRF token:
GET /get-csrf/ → returns { "message": "CSRF cookie set" } and sets the cookie.

POST requests should include the X-CSRFToken header with the token from the csrftoken cookie.



✅ Company Verification API


POST /api/verify-company/
Request JSON:

json
{
  "company_name": "LoRa IT Innovations Pvt Ltd"
}
Response (if company exists in DB):

json
{
  "message": "✅ Company Verified"
}
Response (if company not found):

json
{
  "message": "❌ Company Not Found"
}