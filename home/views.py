from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import *
from rest_framework import generics
from .serializers import StudentSerializer

def home(request):
    students = Student.objects.all()
    
    return render(request, 'home/index.html', {'students': students})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def create(request):
    return render(request, 'home/create.html')

def store(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print("Form errors:", form.errors) 
        form = StudentForm()
    return render(request, 'home/create.html')

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'home/edit.html', {'form': form, 'student': student})

def update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=student)

    return render(request, 'home/edit.html', {'form': form, 'student': student})

def delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)  
    if request.method == 'POST':
        student.delete() 
        return redirect('home')  
    return redirect('home')  

def success(request):
    return render(request, 'success.html')



class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer