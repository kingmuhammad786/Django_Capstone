"""
Views for the portfolio app.

Handles authentication (login, logout, register), project listing,
and poll interactions.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Project, Poll, Choice, Vote


class CustomLoginView(LoginView):
    """
    Custom login view explicitly using 'portfolio/login.html'
    instead of the default 'registration/login.html'.
    """
    template_name = "portfolio/login.html"


def home(request):
    """Render the home page."""
    return render(request, "portfolio/home.html")


def about(request):
    """Render the about page."""
    return render(request, "portfolio/about.html")


def contact(request):
    """Render the contact page."""
    return render(request, "portfolio/contact.html")


def project_list(request):
    """
    Render the project list page.
    
    Retrieves all projects from the database.
    """
    projects = Project.objects.all()
    return render(request, "portfolio/project_list.html", {"projects": projects})


def project_detail(request, pk):
    """
    Render details of a single project.
    
    Retrieves a project by its primary key.
    """
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})


def register_view(request):
    """
    Handle user registration.
    
    Creates a new user if the username does not already exist.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if not username or not password:
            return render(
                request,
                "portfolio/register.html",
                {"error": "Username and password required."},
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "portfolio/register.html",
                {"error": "Username already exists."},
            )

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login")

    return render(request, "portfolio/register.html")


@login_required
@require_POST
def logout_view(request):
    """Handle user logout via a POST request."""
    logout(request)
    return redirect("home")


@login_required
def poll_list(request):
    """
    Display all available polls.
    
    Only logged-in users can view this page.
    """
    polls = Poll.objects.all()
    return render(request, "portfolio/poll_list.html", {"polls": polls})


@login_required
def poll_detail(request, poll_id):
    """
    Display the details of a specific poll.
    
    Includes a flag indicating whether the user has already voted.
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    user_has_voted = Vote.objects.filter(poll=poll, user=request.user).exists()
    return render(
        request,
        "portfolio/poll_detail.html",
        {"poll": poll, "user_has_voted": user_has_voted},
    )


@login_required
def vote(request, poll_id):
    """
    Handles voting for a poll.
    
    Ensures that each logged-in user can vote only once per poll.
    Validates that a choice is selected and that it belongs to the poll.
    """
    poll = get_object_or_404(Poll, pk=poll_id)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        if not choice_id:
            # No choice submitted; re-render with an error message.
            context = {
                "poll": poll,
                "user_has_voted": Vote.objects.filter(poll=poll, user=request.user).exists(),
                "error": "Please select a valid choice before voting.",
            }
            return render(request, "portfolio/poll_detail.html", context)

        # Ensure the choice belongs to the current poll.
        choice = get_object_or_404(Choice, pk=choice_id, poll=poll)

        # Prevent duplicate votes by the same user on a single poll.
        if Vote.objects.filter(poll=poll, user=request.user).exists():
            return redirect("poll_detail", poll_id=poll.pk)

        Vote.objects.create(poll=poll, user=request.user, choice=choice)
        # Optional: increment the vote count.
        choice.votes += 1
        choice.save()

        return redirect("poll_list")

    # Fallback for non-POST requests.
    return render(request, "portfolio/poll_detail.html", {"poll": poll})






