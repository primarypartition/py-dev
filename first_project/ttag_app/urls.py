from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'ttag_app'

urlpatterns = [      
    path('home', views.home, name='home'),
    path('other', views.other, name='other'),
    path('base', views.base, name='base'),
    path('ttag_url', views.ttag_url, name='ttag_url'),
    
    path('', views.index, name='index')
]
