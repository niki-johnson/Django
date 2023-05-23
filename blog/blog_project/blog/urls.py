from unicodedata import name
from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView

urlpatterns = [
    
    path('', BlogListView.as_view(), name='home'),
    #All blog post entries will start with post
    #pk é uma id gerada automaticamente pela base de dados models e é um inteiro
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    #
    #
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
]
