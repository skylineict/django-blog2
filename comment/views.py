
from django.shortcuts import render
from .models import Comment
from .forms import Addcomment
from django.urls.base import is_valid_path, reverse, reverse_lazy
from django.views.generic import CreateView
from blogapp.models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.


class Commentview(CreateView):
    model = Comment
    form_class = Addcomment
    template_name = 'addcomment.html'
    success_url = reverse_lazy("home")

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     post = get_object_or_404(Post, id=self.kwargs['pk'])
    #     data['list'] = post
    #     return data

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
