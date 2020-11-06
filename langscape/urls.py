"""langscape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import EmployeeListView,EmployeeDetailView,EmployeeCreateView,EmployeeUpdateView,EmployeeDeleteView,FormEmployeeView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EmployeeListView.as_view(),name='employee-list'),
    path('employee/', EmployeeListView.as_view(),name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(),name='employee-detail'),
    path('employee/new/', EmployeeCreateView.as_view(),name='employee-create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(),name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(success_url="/employee/"),name='employee-delete'),


    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('register/',user_views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

]
