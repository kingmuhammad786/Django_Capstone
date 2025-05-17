"""
Models for the portfolio app.

Defines the Project model and Poll system, including voting restrictions.
"""

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    Represents a portfolio project.

    Attributes:
        title (str): The project's title.
        description (str): A detailed description of the project.
        image1 (ImageField): First optional image representing the project.
        image2 (ImageField): Second optional image representing the project.
        image3 (ImageField): Third optional image representing the project.
        created_at (DateTimeField): Timestamp for when the project was added.
        updated_at (DateTimeField): Timestamp for when the project was last updated.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    image2 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    image3 = models.ImageField(upload_to="project_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Automatically sets creation time
    updated_at = models.DateTimeField(auto_now=True)  # ✅ Auto-updates timestamp on changes

    def __str__(self):
        return f"{self.title} (Added: {self.created_at.strftime('%Y-%m-%d')})"


class Poll(models.Model):
    """
    Represents a poll with multiple choices.

    Attributes:
        question (str): The poll question.
        created_at (DateTimeField): Timestamp of when the poll was created.
        created_by (User): Optional reference to the creator of the poll.
    """
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Automatically sets timestamp
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    """
    Represents a selectable option in a poll.

    Attributes:
        poll (Poll): The poll to which this choice belongs.
        choice_text (str): The text representing the choice.
        votes (int): Count of votes for this choice.
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    """
    Represents a user's vote on a poll.

    Attributes:
        poll (Poll): The poll being voted on.
        user (User): The user casting the vote.
        choice (Choice): The selected choice.
    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "user")  # ✅ Prevents users from voting multiple times

    def __str__(self):
        return f"{self.user.username} voted for '{self.choice}' in poll '{self.poll}'"


