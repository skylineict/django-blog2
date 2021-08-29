from django.contrib.auth import get_user_model
from django.forms import fields
from singup.form import UserChangeForm, UserCreationForm
# from django.db import models
# from django.db.models import fields
# from django.db.models.base import Model
# from django.forms import widgets
# from django.forms.fields import DateTimeField
from .models import Contactus
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
# from django.core import validators
# from django.core import exceptions
# from django.core.checks.messages import Error
# from django.core.exceptions import ObjectDoesNotExist
from.validiator import blacklist


User = get_user_model()


def username_datacheck(value):
    if len(value) < 4:
        raise forms.ValidationError("value most be 6 charatesr")


def comment(value):
    if len(value) < 70:
        raise forms.ValidationError("value most be 70 charatesr")
# def emailvalue(value, self):
    # data = super(Signup, self)
    # email = self.cleaned_data.get('email')
    # comfirm_email = self.cleaned_data.get('comfirm_email')
    # if email.value(self) != email.value(self):
        # raise forms.ValidationError("value most be 6 charatesr")
# def clean_username(self):
    # userexit = User.objects.filter(
        # username__iexist=self.cleaned_data["username "])
    # if userexit.exists():
        # raise forms.ValidationError("this username is not allowed")
#


class Contactusform(forms.ModelForm):
    full_name = forms.CharField(validators=[username_datacheck], widget=forms.TextInput(
        attrs={'type': "text", 'name': "name", "placeholder": "first name", "class": "input100"}))
    email = forms.CharField(validators=[username_datacheck], widget=forms.EmailInput(
        attrs={'class': "input100", "type": "email", "placeholder": "email"}))
    # phone = forms.RegexField(regex=r'^\+?1?\d{2,12}$', error_messages={"required": 'you mos entera valid number'},
    #  widget=forms.NumberInput(attrs={'type': "text", "placeholder": "phone number", "class": "input100"}))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={'type': "text", "placeholder": "phone number", "class": "input100"}))
    comment = forms.CharField(validators=[comment], widget=forms.Textarea(
        attrs={"class": "input100", "name": "message"}))
    widgets = {"purpose": forms.Select(attrs={"class": "input100 form-control", 'type': "text", "placeholder": "select"
                                              })}

    class Meta:
        model = Contactus
        fields = ('full_name', 'email', 'purpose', 'phone', 'comment')

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        full_name = cleaned_data.get('full_name')
        email = cleaned_data.get('email')
        purpose = cleaned_data.get('purpose')
        comment = cleaned_data.get('purpose')

    # def save(self, commit=True):
        # user = super(Contactusform, self).save(commit=False)
        # if commit:
        # print('yes ooo')
        # user.save()
        # return user

    # user.self.cleaned_data['email']
    # user.self.cleaned_data['firstname']
    # user.self.cleaned_data['lastname']

    # def clean_email(self):
        # cleaned_data = super().clean()
        # phone = cleaned_data.get('phone')
        # if len(phone) < 10:
        # raise forms.ValidationError("number most be 11")
        # return cleaned_data


class Signup(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['email', 'username', 'phone','password1', 'password2', ]


# class Signup(UserCreationForm):
#     ####

#     email = forms.CharField(  # validators=[emailvalue],
#         help_text="Enter a valid email", widget=forms.EmailInput(attrs={'class': "input-field", "type": "email", "placeholder": "email"}))

#     comfirm_email = forms.CharField(  # validators=[emailvalue],
#         help_text="Enter a valid email",  widget=forms.EmailInput(
#             attrs={'class': "input-field", "type": "email", "placeholder": "comfirm Email"}))

#     # Comfirm_email = forms.EmailField(help_text="Enter a valid email",  widget=forms.EmailInput(
#     # attrs={'class': "input-sign email", "type": "email", "placeholder": "comfirm email"}))

#     firstname = forms.CharField(validators=[username_datacheck], widget=forms.TextInput(
#         attrs={'type': "text", "placeholder": "first name", "class": "input-field"}))

#     lastname = forms.CharField(validators=[username_datacheck], widget=forms.TextInput(
#         attrs={'type': "text", "placeholder": "Lastname", "class": "input-field"}))

#     state = forms.CharField(widget=forms.TextInput(
#         attrs={'type': "text", "placeholder": "Rivers", "class": "input-field"}))

#     city = forms.CharField(widget=forms.TextInput(
#         attrs={'type': "text", "placeholder": "Provinc", "class": "input-field"}))

#     office_address = forms.CharField(widget=forms.TextInput(
#         attrs={"type": "text", "placeholder": "Office address", "class": "input-field"}))

#     phone = forms.CharField(label="phone", widget=forms.NumberInput(attrs={
#         'type': "number", "placeholder": "phone number", "class": "input-field"}))

#     username = forms.CharField(validators=[username_datacheck], help_text="Enter a valid username",
#                                label="username ", widget=forms.TextInput(attrs={'class': 'input username', "type": "text", "placeholder": "username", "class": "input-field"}))

#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'input password', "type": "password", "placeholder": "password", "class": "input-field"}))
#     password2 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'input password', "type": "password", "placeholder": 'comfrim password', "class": "input-field"}))

#     class Meta:

#         model = User
#         fields = ('username', 'firstname', "lastname", "phone", 'password1',
#                   'password2', "email", "comfirm_email", "office_address", 'city',  'state')

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("email in use, try again")
#         return email
    # def clean_email(self):
        # email = self.cleaned_data.get('email')
        # comfirm_email = self.cleaned_data.get("comfirm_email")
        # if email and comfirm_email and email != comfirm_email:
        # raise forms.ValidationError("email not match")
        # return email

    # def emailvalue(value, self):
        # data = super(Signup, self)
        # email = self.cleaned_data.get('email')
        # comfirm_email = self.cleaned_data.get('comfirm_email')
        # if email.value != email.value:
        # raise forms.ValidationError("value most be 6 charatesr")

    # def clean_email(self):
        # super().clean()
        # email = self.cleaned_data.get('email')
        # comfirm_email = self.cleaned_data.get('comfirm_email')
        # if email and comfirm_email and email != comfirm_email:
        # errors = {'email': ValidationError(
        # 'email didnt match', code='email_mismatch')}
        # raise ValidationError(errors)

        # return email

    # def save(self, commit=True):
    #     user = super(Signup, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     # user.self.cleaned_data['email']
    #     # user.self.cleaned_data['firstname']
    #     # user.self.cleaned_data['lastname']
    #     if commit:

    #         print('yes ooo')
    #         user.save()
    #     return user


#  = form.cleaned_data.get('username')
# password1 = form.cleaned_data.get('password1')
# password2 = form.cleaned_data.get('password2')
#  firstname = form.cleaned_data.get('firstname')
# email = form.cleaned_data.get('email')
# ciy = form.cleaned_data.get('city')
# user = form.save()
        #
        # def clean(self):

        # cleaned_data = super(Signup, self).clean()
        # email = cleaned_data.get('email')
        # comfirmemail = cleaned_data.get('comfirm_email')
        # if email and comfirmemail:
        # if email != comfirmemail:
        # raise forms.ValidationError('Email doenot match')
        # return cleaned_data


#  def clean_email(self):
    #  email = self.cleaned_data.get('email')
    #  try:
        #  emailmatch = User.objects.get(email=email)
    #  except User.DoesNotExist:
        #  return email
    #  raise forms.ValidationError("email already exist")
        #


# "date": forms.DateInput(attrs={"class": "form-control"})
# def clean_password(self):
    # password = self.cleaned_data['password1']
    # if len(password) > 5:
        # forms.ValidationError("passsword is too short")
    # return password
#

# def usernameexit(self):
    # username = self.cleaned_data['username']
    # if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
    # raise forms.ValidationError(
    # _('username in the database', code="username_exists"))
    # exceptions: User.DoesNotExist
    # return username
#
