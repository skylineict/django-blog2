from django.urls import path
from .views import Editprofile, Profilepage

urlpatterns = [
    # path("register/", Registration.as_view(), name="register"),
    path("", Editprofile.as_view(), name="editprofile"),
    path('profile/<int:pk>', Profilepage.as_view(), name="show_profile")
    # path("contact/", Conactme.as_view(), name="contact")





]
