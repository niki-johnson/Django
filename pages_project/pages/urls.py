from django.urls import path
from .views import AboutPageView, HomePageView

urlpatterns = [
    #quando usamos class, sempre add as_view()
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]