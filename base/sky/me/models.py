from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class Usermanager(BaseUserManager):
#     def create_user(self, email, username, phone, lastname, firstname, state, gender, password=None):

#         email = self.normalize_email(email)
#         if not email:
#             raise ValueError("email most not be nill")

#         user = self.model(email=email, username=username, phone=phone,
#                           lastname=lastname, firstname=firstname, state=state, gender=gender)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staff(self, email, username, phone, lastname, firstname, state, gender, password=None):
#         user = self.create_user(
#             email=email, username=username, phone=phone,
#             lastname=lastname, firstname=firstname, state=state, gender=gender, password=password)
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, phone, lastname, firstname, state, gender, password=None):

#         user = self.create_user(email=email, username=username, phone=phone,
#                                 lastname=lastname, firstname=firstname, state=state, gender=gender, password=password)
#         user.is_staff = True
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class Myusers(AbstractBaseUser):
#     membersid = models.CharField(max_length=10, unique=True, null=True)
#     email = models.EmailField(max_length=40, unique=True)
#     phone = models.IntegerField(null=True, blank=True)
#     firstname = models.CharField(max_length=30, null=True, blank=True)
#     lastname = models.CharField(max_length=69)
#     username = models.CharField(
#         max_length=40, unique=True, null=True, blank=True)
#     gender = models.CharField(max_length=50, null=True, blank=True)
#     state = models.CharField(max_length=60, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     joindate = models.DateField(auto_now_add=True)

#     objects = Usermanager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):
#         return '%s %s %s %s' % (self.firstname, self.lastname, self.gender, self.email)

#     def get_short_name(self):
#         return '%s %s' % (self.username, self.membersid, self.email)

#     def __str__(self):
#         return self.email

#     def is_staff(self):
#         return self.staff

#     def is_admin(self):
#         return self.admin


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
