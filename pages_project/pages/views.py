from pipes import Template
from re import template
from django.shortcuts import render
# importando a built in TemplateView, facilita o uso e aumenta a cobertura de casos comuns do views
from django.views.generic import TemplateView

# Create your views here.
#criando uma class-based generic views
#TemplateView already contains all the logic needed to display our template
class HomePageView(TemplateView):
    #é preciso apenas especificar o nome do template
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    