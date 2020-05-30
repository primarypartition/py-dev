from django.urls import path
from . import views

app_name = "cbv_app"

urlpatterns = [        
    path('list/', views.SchoolListView.as_view(), name='list'),    
    path('list/<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    
    path('simple/', views.SimpleView.as_view(), name='simple'),
    path('home/', views.home, name='home'),
    path('', views.IndexView.as_view(), name='index')    
]
