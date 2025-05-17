"""
Django settings for portfolio_project.

Includes configurations for authentication, static files, database setup, and media file handling.
"""

import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key (ensure this is kept secret in production)
SECRET_KEY = "your-secure-secret-key"

# Debug mode (set to False in production)
DEBUG = True

# Allowed Hosts (Required for Deployment)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Installed applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",  # Your portfolio app
]

# Middleware Configuration
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Root URL Configuration
ROOT_URLCONF = "portfolio_project.urls"

# Templates Configuration (Ensuring Authentication Context Is Passed)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Ensures templates are recognized
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",  # Ensures `user.is_authenticated` works correctly
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Authentication Settings (Forcing Django to Use Custom Login Template)
LOGIN_URL = "/login/"  # Redirects users to our custom login page
LOGIN_REDIRECT_URL = "/"  # Sends users to the home page after login
LOGOUT_REDIRECT_URL = "/"  # Sends users to the home page after logout
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

# WSGI Application Reference
WSGI_APPLICATION = "portfolio_project.wsgi.application"

# Database Configuration (SQLite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Media settings (Required for serving uploaded images)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static files configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
