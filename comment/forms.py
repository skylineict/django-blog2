from django.db import models
from django.forms import widgets
from .models import Comment
from django import forms
from tinymce.widgets import TinyMCE


class Addcomment(forms.ModelForm):
    your_comment = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    widgets = {
        "name": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"}),
        # "post": forms.Select(attrs={"class": "form-control"}),


        #             # "date": forms.DateInput(attrs={"class": "form-control"})
    }

    class Meta:
        model = Comment
        fields = ('name', 'your_comment')
