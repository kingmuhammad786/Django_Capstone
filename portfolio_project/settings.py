"""
Django settings for portfolio_project.

This module configures the Django project settings, encompassing:

- Core application setup (INSTALLED_APPS)
- Middleware pipeline configuration (MIDDLEWARE)
- Template engine settings (TEMPLATES)
- Database connection details (DATABASES)
- Static and media file management (STATIC_URL, MEDIA_URL)
- User authentication and authorization (AUTHENTICATION_BACKENDS, LOGIN_URL)
- Internationalization and localization (LANGUAGE_CODE, TIME_ZONE)
- Security settings (SECRET_KEY, ALLOWED_HOSTS)
"""

import os
from pathlib import Path

# Base directory of the project. This is used to resolve paths relative to the project.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key used for cryptographic signing. **IMPORTANT:** Keep this secret in production!
SECRET_KEY = "your-secure-secret-key"

# Debug mode. Set to `False` in production to disable detailed error pages.
DEBUG = True

# Allowed hosts for this Django application.  Required for security reasons in deployment.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# List of installed Django applications. These provide various functionalities to the project.
INSTALLED_APPS = [
    "django.contrib.admin",  # Administrative interface for managing the site.
    "django.contrib.auth",   # Authentication and authorization framework.
    "django.contrib.contenttypes", # Framework for handling content types.
    "django.contrib.sessions", # Session management.
    "django.contrib.messages",  # Support for displaying messages to users.
    "django.contrib.staticfiles", # Management of static files (CSS, JavaScript, images).
    "portfolio",            # Your portfolio application.
]

# Middleware defines the request/response cycle of the Django application.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware", # Common utilities.
    "django.middleware.csrf.CsrfViewMiddleware", # Cross-Site Request Forgery protection.
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Associates users with requests.
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware", # Clickjacking protection.
]

# Root URL configuration for the entire project.
ROOT_URLCONF = "portfolio_project.urls"

# Template engine configuration. Specifies how Django finds and renders templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Directories where Django should look for templates.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",  # Makes the 'user' variable available in templates.
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application used to serve the Django application.
WSGI_APPLICATION = "portfolio_project.wsgi.application"

# Database configuration.  In this case, it's SQLite (suitable for development).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3", # Path to the SQLite database file.
    }
}

# Settings for serving media files (user-uploaded files).
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Settings for serving static files (CSS, JavaScript, images).
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Internationalization settings.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True  # Enable translation.
USE_TZ = True   # Enable timezone support.

# Default primary key field type for automatically generated models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication URLs
LOGIN_URL = "/login/"  # URL for the login page
LOGIN_REDIRECT_URL = "/"  # URL to redirect to after successful login
LOGOUT_REDIRECT_URL = "/"  # URL to redirect to after logout

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"] #Default Django authentication backend