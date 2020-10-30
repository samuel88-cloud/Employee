from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class EmployeeListView(ListView):
    model=Employee

class EmployeeDetailView(DetailView):
    model=Employee

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model=Employee
    fields=['name','email','age','salary','position','address']

class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model=Employee
    fields=['name','email','age','salary','position','address']

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model=Employee

    