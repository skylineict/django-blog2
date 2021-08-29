from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class commentadmin(admin.ModelAdmin):
    list_display = ['name', 'your_comment', 'date', 'approve_comment']


# Register your models here.
