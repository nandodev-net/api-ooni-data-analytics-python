"""
This module contains the models for the users application.

The CustomUser model extends Django's AbstractBaseUser and PermissionsMixin
to create a custom user model with additional roles and fields. It also includes
properties to check the role of a user.
"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.users.manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser model that extends AbstractBaseUser and PermissionsMixin.

    This model is used to represent a user in the application with different roles.
    """

    class Role(models.TextChoices):
        """Role choices for the CustomUser model."""

        SUPERADMIN = "SUPERADMIN", "Superadmin"
        ADMIN = "ADMIN", "Admin"
        ANALYST = "ANALYST", "Analyst"
        EDITOR = "EDITOR", "Editor"
        GUEST = "GUEST", "Guest"

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField("email address", unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.GUEST)
    raw_pss = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        """
        Return the string representation of the user.

        Returns:
            str: The email of the user.
        """
        return f"username: {self.username} - email: {self.email}"

    @property
    def is_superadmin(self):
        """
        Check if the user is an superadmin.

        Returns:
            bool: True if the user is an superadmin, False otherwise.
        """
        return self.role == self.Role.ADMIN

    @property
    def is_admin(self):
        """
        Check if the user is an admin.

        Returns:
            bool: True if the user is an admin, False otherwise.
        """
        return self.role == self.Role.ADMIN

    @property
    def is_analyst(self):
        """
        Check if the user is an analyst.

        Returns:
            bool: True if the user is an analyst, False otherwise.
        """
        return self.role == self.Role.ANALYST

    @property
    def is_editor(self):
        """
        Check if the user is an editor.

        Returns:
            bool: True if the user is an editor, False otherwise.
        """
        return self.role == self.Role.EDITOR

    @property
    def is_guest(self):
        """
        Check if the user is a guest.

        Returns:
            bool: True if the user is a guest, False otherwise.
        """
        return self.role == self.Role.GUEST
