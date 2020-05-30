from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

from . import models

# cbv_app/home  
def home(request):
    return render(request, 'cbv_app/home.html')

# cbv_app/simple                                
class SimpleView(View):
    def get(self, request):            
        return HttpResponse("Simple View Class")

# cbv_app/
class IndexView(TemplateView):
    template_name = 'cbv_app/index.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        
        return context

# cbv_app/list
class SchoolListView(ListView):
    context_object_name = 'schools' # default: school_list
    model = models.School    
        
    template_name = 'cbv_app/school/list.html' # default: cbv_app/school_list

# cbv_app/list/<int:pk>
class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = models.School
            
    template_name = 'cbv_app/school/detail.html'

# cbv_app/create
class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")    
    model = models.School
    
    template_name = 'cbv_app/school/create.html'

# cbv_app/update/<int:pk>
class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

    template_name = 'cbv_app/school/create.html'
    
# cbv_app/delete/<int:pk>
class SchoolDeleteView(DeleteView):    
    success_url = reverse_lazy("cbv_app:list")
    model = models.School
    
    template_name = 'cbv_app/school/confirm_delete.html'
