
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Usermanager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        if not email:
            raise ValueError("emaill will not be none")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        user = self.create_user(
            email=email, username=username, password=password, **other_fields)
        return user
