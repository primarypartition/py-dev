from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is response</h1>")

def help(request):
    my_dict = {'insert_me': "Hello I am from help views.py!"}
    return render(request, 'second_app/help.html', context=my_dict)
  