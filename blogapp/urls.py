
from django.urls import path
from .views import (Home, Details, Addpost, blogpost_likes,
                    Editpost, Deletepost, Addcategory,
                    Catqegoryview, Categorylist,
                    )
from .views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('details/<int:pk>', Details.as_view(), name="info"),
    path('create', Addpost.as_view(), name="create"),
    path("edit/<int:pk>", Editpost.as_view(), name="edit"),
    path("delete/<int:pk>", Deletepost.as_view(), name="delete"),
    path("like/<int:pk>", blogpost_likes, name="bloglike"),

    # add category here on this page
    path('add', Addcategory.as_view(), name="addcate"),
    path("category/<str:cateme>/", Catqegoryview.as_view(), name="category"),
    path("category_list", Categorylist.as_view(), name="categorylist"),


]
