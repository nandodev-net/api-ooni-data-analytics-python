"""
This module contains the manager class for the CustomUser model.

The CustomUserManager class is responsible for creating and managing
instances of the CustomUser model, including the creation of regular
users and superusers.
"""

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifier for authentication instead of usernames."""

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            password (str, optional): The password of the user. Defaults to None.
            **extra_fields: Arbitrary keyword arguments.

        Returns:
            CustomUser: The created user instance.

        Raises:
            ValueError: If the username or email is not set.
        """
        if not username:
            raise ValueError("The Username must be set")
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.

        Args:
            username (str): The username of the superuser.
            email (str): The email of the superuser.
            password (str, optional): The password of the superuser. Defaults to None.
            **extra_fields: Arbitrary keyword arguments.

        Returns:
            CustomUser: The created superuser instance.

        Raises:
            ValueError: If the role is not set to SUPERADMIN or if is_staff or is_superuser are not True.
        """
        extra_fields.setdefault("role", "SUPERADMIN")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("role") != "SUPERADMIN":
            raise ValueError("Superuser must have role=SUPERADMIN.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)
