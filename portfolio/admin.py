"""
Admin configuration for the portfolio app.

Defines how the Project, Poll, Choice, and Vote models are displayed in the Django admin panel.
"""

from django.contrib import admin
from .models import Project, Poll, Choice, Vote


class ProjectAdmin(admin.ModelAdmin):
    """
    Custom admin settings for the Project model.
    """
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('description',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """
    Custom admin settings for the Poll model.
    """
    list_display = ('question', 'created_at', 'created_by')
    search_fields = ('question',)
    ordering = ('-created_at',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """
    Custom admin settings for the Choice model.
    """
    list_display = ('poll', 'choice_text', 'votes')
    list_filter = ('poll',)
    search_fields = ('choice_text',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """
    Custom admin settings for the Vote model.
    """
    list_display = ('poll', 'user', 'choice')
    list_filter = ('poll', 'user')





