from .views import Commentview
from django.urls import path


urlpatterns = [
    path("post/<int:pk>/comment/", Commentview.as_view(), name="comment"),


]
