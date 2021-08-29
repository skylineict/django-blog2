
from django.urls import path
from members.views import Registration,  Conactme

urlpatterns = [
    path("register/", Registration.as_view(), name="register"),
    # path("profile/", Editprofile.as_view(), name="editprofile"),
    path("contact/", Conactme.as_view(), name="contact")





]
