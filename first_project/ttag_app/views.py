from django.shortcuts import render
from django.http import HttpResponse

# ttag_app/
def index(request):
    data = {'text': "This is text from view hello world.",
            'number': 100}
            
    return render(request, 'ttag_app/index.html', context=data)

# ttag_app/home
def home(request):
    return HttpResponse("Hello World!")
    
# ttag_app/other
def other(request):
    return render(request, 'ttag_app/other.html')

# ttag_app/ttag_url
def ttag_url(request):
    return render(request, 'ttag_app/ttag_url.html')
    
# ttag_app/base
def base(request):
    return render(request, 'ttag_app/base.html')
