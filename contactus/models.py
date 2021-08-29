from django.db import models

# Create your models here.


class Contactmeus(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=20)
    Email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    subject = models.TextField(max_length=400)
