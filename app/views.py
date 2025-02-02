from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

class home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    queryset=School.objects.filter().all()
    template_name='app/school_list.html'


class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobject'
    success_url=reverse_lazy('SchoolList')
