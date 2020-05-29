from django.urls import path
from . import views

urlpatterns = [      
    path('home/', views.home, name='home'),    
    path('formpage/', views.form_name_view, name='formpage'),
    path('users/', views.users, name="users"),
    
    path('', views.index, name='index')
]
