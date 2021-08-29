from django import forms
from django.contrib.auth import get_user_model
from singup.form import UserCreationForm, UserChangeForm
User = get_user_model()


class Profile(UserChangeForm):
    password = None

    class Meta:

        model = User
        exclude = []
        fields = ('email', 'image', 'username', 'surname', 'firstname', 'lastname', 'phone',
                  'Occupation', 'Qualification', 'marital_status', 'location',  'about', 'facebook', "twitter", "instagram", "youtube",
                  )
