from django.urls import path
from . import views

urlpatterns = [  
    path('users/', views.users, name="users"),
    path('help/', views.help, name='help'),
    path('home', views.home, name='home'), 
    path('', views.index, name='index')    
]
