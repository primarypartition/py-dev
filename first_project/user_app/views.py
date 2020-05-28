from django.shortcuts import render
from django.http import HttpResponse

from user_app.models import User

def index(request):
    return HttpResponse("<em>My User App</em>")

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request,'user_app/help.html', context=helpdict)

def home(request):
    return render(request, 'user_app/home.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users": user_list}
    return render(request, 'user_app/users.html', context=user_dict)
