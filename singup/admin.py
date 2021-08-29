from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.expressions import OrderBy
from .models import*
from django.contrib.auth.models import Group
from django.db.models import Avg
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .form import AdmincreateUser, Adminchangeuser
import math
from .form import UserChangeForm, UserCreationForm


User = get_user_model()
# Register your models here.


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', "lastname", "firstname",
                    'email', 'phone', 'Occupation')

    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', "lastname", "firstname", 'phone',
                                      'Occupation', 'Qualification', 'marital_status', 'location', 'image', 'about'
                                      )}),
        ('social media', {'fields': ('facebook', "twitter", "instagram", "youtube",
                                     )}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'username', 'surname', 'firstname', 'lastname', 'phone',
                       'Occupation', 'Qualification', 'marital_status', 'location', 'image', 'about',
                       'is_active', 'is_staff', 'facebook', "twitter", "instagram", "youtube"),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# The fields to be used in displaying the User model.
# These override the definitions on the base UserAdmin
# that reference specific fields on auth.User.
# list_display = ['email', 'admin']
# list_filter = ['admin']

# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
# overrides get_fieldsets to use this attribute when creating a user.


@admin.register(Course)
class course(admin.ModelAdmin):
    list_display = ('year', 'name')


@admin.register(Person)
class course(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'show_avarage')

    def show_avarage(self, pk):
        result = Grade.objects.filter(person=pk).aggregate(Avg('grade'))
        ouput = math.trunc(result['grade__avg'])
        return ouput
    show_avarage.short_description = "STUDENT SCORE"


@ admin.register(Grade)
class course(admin.ModelAdmin):

    list_display = ('person', 'grade', 'course')
