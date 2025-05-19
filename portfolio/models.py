"""
Models for the portfolio app.

Defines the Project model and Poll system, including voting restrictions.
"""

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    Represents a portfolio project showcased by a user.

    Attributes:
        title (str): The project's title.
        description (str): A detailed description of the project.
        image1 (ImageField, optional): First image representing the project.
        image2 (ImageField, optional): Second image representing the project.
        image3 (ImageField, optional): Third image representing the project.
        created_at (DateTimeField): Timestamp for when the project was added.
        updated_at (DateTimeField): Timestamp for the last modification.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    image2 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    image3 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp on save

    def __str__(self):
        return f"{self.title} (Added on {self.created_at.strftime('%Y-%m-%d')})"


class Poll(models.Model):
    """
    Represents a poll allowing users to vote on different choices.

    Attributes:
        question (str): The poll question presented to users.
        created_at (DateTimeField): Timestamp of when the poll was created.
        created_by (User, optional): The user who initiated the poll.
    """

    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    """
    Represents a selectable voting option within a poll.

    Attributes:
        poll (Poll): The associated poll.
        choice_text (str): The text label describing the choice.
        votes (int): The number of votes this choice has received.
    """

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    """
    Tracks user votes within a poll, ensuring each user votes only once.

    Attributes:
        poll (Poll): The poll being voted on.
        user (User): The user casting the vote.
        choice (Choice): The selected choice by the user.
    """

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "user")  # Restricts multiple votes from the same user

    def __str__(self):
        return f"{self.user.username} voted for '{self.choice}' in poll '{self.poll}'"



