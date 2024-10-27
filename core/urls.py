"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import *

urlpatterns = [
    path('' , home, name='home'),
    path('create/' , create, name='create'),
    path('store/', store, name='store'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('edit/<int:student_id>/', edit, name='edit'),
    path('update/<int:student_id>/', update, name='update'), 
    path('delete/<int:student_id>/', delete, name='delete'),
    
    path('api/students/', StudentListCreate.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),
    
    path('admin/', admin.site.urls),
]
