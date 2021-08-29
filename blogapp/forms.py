from blogapp.models import Post, Category
from django import forms
from tinymce.widgets import TinyMCE
# cate = Category.objects.filter(name='name')


class Form(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'image', 'author', )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control", "value": "", }),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "full name here", 'id': "username", "value": "", "type": "hidden"}),
            "image": forms.FileInput(attrs={"class": "form-control form-control-file "}),

            #             # "date": forms.DateInput(attrs={"class": "form-control"})
        }


class Addedit(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"}),
            "slug": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"})}
        #     # "body": forms.Textarea(attrs={"class": "form-control form-control-sm"})
        #     # # "author": forms.Select(attrs={"class": "form-control"}),
        #     # # "date": forms.DateInput(attrs={"class": "form-control"})
        #


class Edit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"}),
            "body": forms.Textarea(attrs={"class": "form-control form-control-sm"})
            # "author": forms.Select(attrs={"class": "form-control"}),
            # "date": forms.DateInput(attrs={"class": "form-control"})
        }


# # add category in django
#         # title = forms.TextInput(
#         #     attrs= {'size': 10, "place holder": "articles title", "class": "form-control"})
#         # body = forms.Textarea(attrs={"class": "form-control"})
#         # author = forms.Textar(attrs={"class": "form-control"})
