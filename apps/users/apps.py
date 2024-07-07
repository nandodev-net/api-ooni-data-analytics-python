"""
Apps module for the users application.

This module defines the configuration for the users application.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for the users application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
