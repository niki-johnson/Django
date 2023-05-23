from msilib.schema import ListView
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
# Create your views here.

class BlogListView(ListView):
    
    model = Post

    template_name = 'home.html'
    
class BlogDetailView(DetailView):

    model = Post

    template_name = 'post_detail.html'

class BlogCreateView(CreateView):

    model = Post

    template_name = 'post_new.html'

    fields = ['title', 'author', 'body']

    