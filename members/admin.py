from django.contrib import admin
from .models import Contactus


class Adminuser(admin.ModelAdmin):
    list_display = ["full_name", 'phone', 'purpose', 'comment', "contact_by"]


# Register your models here.
admin.site.register(Contactus, Adminuser)
