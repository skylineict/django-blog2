from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category
from .models import Post, Category
from .forms import Form, Edit, Addedit
from hitcount.views import HitCountDetailView
from django.contrib.auth import get_user_model
from singup.models import Registration
from comment.models import Comment
from comment.forms import Addcomment

User = get_user_model()


class Home(ListView):  # to display list of all content in a blog with there heading
    model = Post
    template_name = "home.html"
    context_object_name = "list_post"
    # ordering = ["-date"]

    # def profile(self):
    #     myuser = Registration.objects.filter(id=1)
    #     if not myuser.first:
    #         return render(self.request, 'registration/editprofile.html"')


# # this is function base view to check the function of our likes


def blogpost_likes(request, pk):
    blogpost = get_object_or_404(Post, id=request.POST.get(
        "blogpost_id"))  # get  to get the like html name value
    if blogpost.likes.filter(id=request.user.id).exists():  # to xhec
        blogpost.likes.remove(request.user)
    else:
        blogpost.likes.add(request.user)
    return HttpResponseRedirect(reverse("info", args=[str(pk)]))


class Catqegoryview(ListView):
    model = Post

    template_name = "listofcate.html"
    context_object_name = "mypost"

    def get_queryset(self,):
        post = {
            "cat": self.kwargs['cateme'],
            "postme": Post.objects.filter(category__name=self.kwargs['cateme'])


        }
        return post


# # def categoryview(request, category):
# #     category_post = Post.objects.filter(category=category)
# #     return render(request, "listofcate.html", {"category_post": category_post})


class Details(HitCountDetailView):
    model = Post
    template_name = "details.html"
    context_object_name = "view_post"
    count_hit = True
#

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        populated = Post.objects.order_by('-hit_count_generic__hits')
        data['puporlar'] = populated
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
            data['number_of_likes'] = likes_connected.numbers_of_likes()
            data['post_likes'] = liked
#
        return data
# #

#     # def get_context_data(self, **kwargs):
#         # context = super(Details, self).get_context_data(**kwargs)
#         # context.update({
#         # 'popular_posts': Post.objects.order_by('hit_count_generic__hits')
#         # })
#         # context = {'countme': Post.hit_count.hits}
#         # return context


# # class Postdetails(HitCountDetailView):
#     # model = Post
#     # count_hit = True
#     # template_name = "details.html"

#     # def get_context_data(self, **kwargs):
#         # conext = super(Postdetails, self).get_context_data(**kwargs)
#         # conext = conext.update({'popular_post': Post.objects.order_by('-hit_count_generic__hits')[:5],

#         # })
#         # return conext


class Categorylist(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "category_list"


class Addcategory(CreateView):
    model = Category
    form_class = Addedit
    template_name = "createcate.html"


class Addpost(CreateView):
    model = Post
    form_class = Form
    context_object_name = "post"
    template_name = "create.html"

    # def form_valid(self, form):
    # form.instance.author = self.request.user
    # return super().form_valid(form)
#

# add comment start from  here


class Editpost(UpdateView):
    model = Post
    form_class = Edit
    context_object_name = "post"
    template_name = 'editpost.html'
    # fields = ['title', 'body']


class Deletepost(DeleteView):
    model = Post
    context_object_name = 'mydeletepost'
    template_name = "delete.html"
    success_url = "/"

#     # def details(request, pk):
#     #     book = get_object_or_404(Post, pk=pk)
#     #     return render(request, 'details.htmldetails.html', context={'book': book})

#     # def home(request):
#     #     return render(request, 'home.html', {})


def category_list(request):
    mylistcat = Category.objects.all()

    context = {
        "mycatlist": mylistcat,


    }
    return context


def mypost(request):
    allpost = Post.objects.all()
    mycontent = {
        "allpost": allpost
    }

    return mycontent
