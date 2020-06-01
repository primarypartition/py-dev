from django.urls import path
from . import views

app_name = 'social_app'

urlpatterns = [             
    path('keeper/', views.KeeperPage.as_view(), name="keeper"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    
    path('', views.HomePage.as_view(), name="home"),
]
