"""
URL configuration for the portfolio app.

Defines routes for portfolio pages, projects, authentication, and polls.
"""

from django.urls import path
from .views import (
    poll_list,
    poll_detail,
    vote,
    CustomLoginView,
    register_view,
    logout_view,
)
from . import views

urlpatterns = [
    # Core pages
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Project-related URLs
    path("projects/", views.project_list, name="project_list"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),

    # Authentication routes
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),

    # Polling system routes (login required)
    path("polls/", poll_list, name="poll_list"),
    path("polls/<int:poll_id>/", poll_detail, name="poll_detail"),
    path("polls/<int:poll_id>/vote/", vote, name="vote"),
]