# from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db import models
from django.contrib import admin
from .models import Post, Category

# User = get_user_model()


# @admin.register(User)
# class Useradmin(admin.ModelAdmin):
#     pass


class Detials(admin.ModelAdmin):
    list_display = ['title', 'body', 'author', 'date']

#     # def formatted_hit_count(self, obj):
#     # return obj.current_hit_count if obj.current_hit_count > 0 else '-'
#     # formatted_hit_count.admin_order_field = 'hit_count'
#     # formatted_hit_count.short_description = 'Hits'

#     # def save_model(self, request,  Post,  form, change):
#     # if not Post.author:
#     # Post.author = request.user.username
#     # Post.save
#     # return super().save_model(request, obj, form, change)


class Cate(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Post, Detials)
admin.site.register(Category, Cate)


admin.site.site_header = "professional Blog"
