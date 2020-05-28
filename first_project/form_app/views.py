from django.shortcuts import render
from django.http import HttpResponse

from . import forms
from .formsModel import NewUserForm

# form_app/home
def home(request):
    return HttpResponse("Hello World!")

# form_app/
def index(request):
    return render(request, 'form_app/index.html')

# form_app/formpage
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request, 'form_app/form.html', {'form': form})

# form_app/users
def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)            
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'form_app/users.html', {'form': form})
