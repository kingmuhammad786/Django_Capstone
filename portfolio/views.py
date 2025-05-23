from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Project, Poll, Choice, Vote


class CustomLoginView(LoginView):
    """
    Custom login view using 'portfolio/login.html' instead of the default template.
    
    This view provides authentication functionality while ensuring users log in 
    using a designated template.
    """
    template_name = "portfolio/login.html"


def home(request):
    """Render the homepage displaying an overview of the portfolio."""
    return render(request, "portfolio/home.html")


def about(request):
    """Render the 'About' page with information about the portfolio."""
    return render(request, "portfolio/about.html")


def contact(request):
    """Render the 'Contact' page for user inquiries and messages."""
    return render(request, "portfolio/contact.html")


def project_list(request):
    """
    Render a page displaying all available projects.

    Retrieves and displays all projects stored in the database, allowing 
    users to browse project details.
    """
    projects = Project.objects.all()
    return render(request, "portfolio/project_list.html", {"projects": projects})


def project_detail(request, pk):
    """
    Render details for a specific project.

    Fetches a project instance using its primary key and presents details 
    including title, description, and related content.
    """
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})


def register_view(request):
    """
    Handle user registration by creating a new account.

    Ensures unique usernames and password validation before storing 
    user credentials securely in the database.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if not username or not password:
            return render(
                request,
                "portfolio/register.html",
                {"error": "Username and password are required."},
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "portfolio/register.html",
                {"error": "Username already exists. Please choose another."},
            )

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login")

    return render(request, "portfolio/register.html")


@login_required
@require_POST
def logout_view(request):
    """
    Handle user logout via a secure POST request.

    Logs out the currently authenticated user and redirects them to the homepage.
    """
    logout(request)
    return redirect("home")


@login_required
def poll_list(request):
    """
    Display all available polls for authenticated users.

    Retrieves polls from the database and renders them for user participation.
    """
    polls = Poll.objects.all()
    return render(request, "portfolio/poll_list.html", {"polls": polls})


@login_required
def poll_detail(request, poll_id):
    """
    Display detailed information about a selected poll.

    Checks whether the logged-in user has already voted on the poll 
    and prevents duplicate voting.
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
    Handle user voting for a specific poll.

    - Validates that users select a choice before submitting their vote.
    - Ensures users cannot vote more than once per poll.
    - Records the vote in the database while updating the choice count.
    """
    poll = get_object_or_404(Poll, pk=poll_id)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        if not choice_id:
            context = {
                "poll": poll,
                "user_has_voted": Vote.objects.filter(poll=poll, user=request.user).exists(),
                "error": "Please select a valid choice before voting.",
            }
            return render(request, "portfolio/poll_detail.html", context)

        choice = get_object_or_404(Choice, pk=choice_id, poll=poll)

        if Vote.objects.filter(poll=poll, user=request.user).exists():
            return redirect("poll_detail", poll_id=poll.pk)

        Vote.objects.create(poll=poll, user=request.user, choice=choice)
        choice.votes += 1
        choice.save()

        return redirect("poll_list")

    return render(request, "portfolio/poll_detail.html", {"poll": poll})








