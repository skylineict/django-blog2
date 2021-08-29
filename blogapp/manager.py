# from django.contrib.auth.models import BaseUserManager
# from django.utils.translation import gettext_lazy as _


# from django.contrib.auth.models import BaseUserManager


# class Usermanager(BaseUserManager):
#     def create_user(self, email, firstname, lastname, password, **other_fields):

#         email = self.normalize_email(email)
#         user = self.model(email=email, firstname=firstname,
#                           lastname=lastname, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

# creating supper users for admin
# def create_superuser(self, email, firstname, lastname, password, **other_fields):
#     other_fields.setdefault('is_staff', True)
#     other_fields.setdefault('is_superuser', True)
#     user = self.create_user(
#         email, firstname, lastname, password, **other_fields)
#     return user


# class CustomAccountManager(BaseUserManager):

#     def create_user(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, user_name, first_name, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         return self.create_user(email, user_name, first_name, password, **other_fields)
