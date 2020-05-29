from django.urls import path
from . import views

app_name = 'user_auth_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),    
    
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),   
    
    path('special/', views.special, name='special'),
    path('', views.index, name='index')    
]
