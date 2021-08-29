from django.contrib import admin
from django.db import models
from .models import Contactmeus
# Register your models here.


@admin.register(Contactmeus)
class Contactus(admin.ModelAdmin):
    pass
