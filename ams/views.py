from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'ams/login.html')

def register(request):
    return render(request, 'ams/register.html')

def addfaculty(request):
    return render(request, 'ams/addfaculty.html')

def programlist(request):
    return render(request, 'ams/programlist.html')

def viewprogram(request):
    return render(request, 'ams/viewprogram.html')

def dash(request):
    return render(request, 'ams/dashboard.html')

  