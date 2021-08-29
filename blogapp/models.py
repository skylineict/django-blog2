from django.core.exceptions import ValidationError
from django.db import models
# from django.contrib.auth.models import AbstractUser, User
from datetime import datetime, date
from django.db.models.fields import related
from django.urls import reverse
# from .manager import*
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import *
from tinymce.models import HTMLField
from django.conf import settings

# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser, PermissionsMixin, )
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
User = settings.AUTH_USER_MODEL

# from django_quill.fields import QuillField
# from hitcount.settings import MODEL_HITCOUNT
# Create your models here.

massage = "image propertiy not all not allowed here"

# def blogpost_likes(request, pk):
# post = get_object_or_404()
#


def image_vailid(image):
    max_height = 1000
    max_width = 500
    height = image.height
    width = image.width
    if width > max_width and height > max_height:
        raise ValidationError(massage)


# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, user_name, first_name, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)

#         return self.create_user(email, user_name, first_name, password, **other_fields)

#     def create_user(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class Myusers(AbstractBaseUser, PermissionsMixin):
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
#     joindate = models.DateField(auto_now_add=True)

#     objects = Usermanager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['firstname', 'lastname']

#     # def has_perm(self, perm, obj=None):
#     #     return True

#     # def has_module_perms(self, app_label):
#     #     return True

#     def __str__(self):
#         return self.email


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    body = HTMLField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="image", validators=[image_vailid])
    likes = models.ManyToManyField(User, related_name="like_post")
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def numbers_of_likes(self):
        return self.likes.count()

    def current_hit_count(self):
        return self.hit_count_generic

    def __str__(self):
        return self.title + '| ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

        return reverse('info', args=[str(self.pk)])
