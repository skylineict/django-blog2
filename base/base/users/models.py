from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Usermanager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        email = self.normalize_email(email)

        user = self.model(email=email,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') != True:
            raise ValueError("is_staff not = True")

        if other_fields.get('is_superuser') != True:
            raise ValueError("is_superuser not = True")
        return self.create_user(email, password, **other_fields)


class Myusers(AbstractBaseUser):
    membersid = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(max_length=40, unique=True)
    phone = models.IntegerField(null=True, blank=True)
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=69)
    username = models.CharField(
        max_length=40, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=60, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    joindate = models.DateField(auto_now_add=True)

    objects = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
