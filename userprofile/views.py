# from blog.members.form import User
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from singup.form import UserCreationForm, UserChangeForm
from .form import Profile
from singup.models import Registration
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.models import Post
from django.contrib.messages import constants as messages

# Create your views here.


class Editprofile(UpdateView):
    model = ''
    form_class = Profile
    context_object_name = 'forms'
    template_name = "registration/editprofile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
 


        
   


class Profilepage(DetailView, LoginRequiredMixin):
    model = Registration
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profilepage, self).get_context_data(**kwargs)
        show_profilepage = get_object_or_404(
            Registration, id=self.kwargs['pk'])
        # gettting the id of a post
        mypost = get_object_or_404(Post, id=self.kwargs['pk'])
        context['showprofile'] = show_profilepage
        context['post'] = mypost
        return context
