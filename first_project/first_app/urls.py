from django.urls import path
from . import views

urlpatterns = [
    path('webpages', views.webpages, name='webpages'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),    
    path('', views.index, name='index')    
]
