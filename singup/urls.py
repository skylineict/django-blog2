from django.shortcuts import render
from .views import home
from django.urls import path


urlpatterns = [
    path("", home, name="index")



]


# Create your views here.
