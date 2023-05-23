from django.shortcuts import render
#importando um class-based generico que sera usado para listar os conteudos da basede dados do modelo
from django.views.generic import ListView

from.models import Post

# Create your views here.
#atente-se que listview é uma subclasse
#listview retorna um contexto chamado object_list, que nós podemos fz um loop pelo template
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    #explicitando o nome da lista
    context_object_name = 'all_posts_list'
    