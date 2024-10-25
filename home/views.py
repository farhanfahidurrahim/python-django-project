from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Bob', 'age': 35},
    ]
    
    return render(request, 'home/index.html', {'peoples': peoples})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def create(request):
    return render(request, 'home/create.html')