from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import Usermanager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

occupation = [('student', 'Student'), ('Working class', 'Working class'),
              ('Programmer', 'Programmer')

              ]

qualification = [("WAEC", "WAEC"), ("HND", "HND"),
                 ("MASTER", "MASTER")
                 ]
marriage = [("Single", "Single"), ("Married", "Married")

            ]
# Create your models here.


class Registration(AbstractBaseUser, PermissionsMixin):
    surname = models.CharField(max_length=30, null=True)
    firstname = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=30, unique=True)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    Occupation = models.CharField(
        choices=occupation, max_length=40, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    Qualification = models.CharField(
        choices=qualification, null=True, max_length=30, blank=True)
    marital_status = models.CharField(
        choices=marriage, max_length=30, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    username = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to="profile",)
    about = models.TextField(max_length=600, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    object = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Person(models.Model):
    last_name = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name_plural = "People"


class Course(models.Model):
    name = models.CharField(max_length=30, null=True)
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year", )

    def __str__(self):
        return self.name


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['person']

    def __str__(self):
        return str(self.person)
