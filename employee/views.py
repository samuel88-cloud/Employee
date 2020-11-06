from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .form import EmployeeForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

class EmployeeListView(ListView):
    model=Employee

class EmployeeDetailView(DetailView):
    model=Employee

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model=Employee
    fields=['name','email','age','salary','position','address']

    def form_valid(self, form):
        if len(form.cleaned_data['name'])<=2:
            print('inside if')
            messages.error(self.request,'Name too small')


            return HttpResponseRedirect(self.request.path_info,form)
        else:
           
            return super().form_valid(form)

class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model=Employee
    fields=['name','email','age','salary','position','address']

    def form_valid(self, form):
        print(form.cleaned_data)
        print(form.cleaned_data['name'])
        name=form.cleaned_data['name']
        age=form.cleaned_data['age']
        position=form.cleaned_data['position']
        salary=form.cleaned_data['salary']
        address=form.cleaned_data['address']
        email=form.cleaned_data['email']
        
        if len(form.cleaned_data['name'])<=2:
            print('inside if')
            messages.error(self.request,'Name too small')
            return render(self.request,'formemployeeview.html',
            {'name':name,'age':age,'position':position,'salary':salary,'address':address,'email':email})


            #return HttpResponseRedirect(self.request.path_info,form)
        else:
           
            return super().form_valid(form)

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model=Employee

    
class FormEmployeeView(FormView):
    template_name='formemployeeview.html'
    form_class=EmployeeForm
    success_url='/employee/'

    def form_valid(self, form):
        print(form.cleaned_data)
        print(form.cleaned_data['name'])
        try:
            if form.cleaned_data['name']=='Muthu':
                print('inside if')
                messages.error(self.request,'Do not enter Muthu')
        except:
            print('exce')
            messages.error(self.request,'Enter Name')
        return super().form_valid(form)

