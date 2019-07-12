from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'ams/login.html')

def register(request):
    return render(request, 'ams/register.html')

def dash(request):
    return render(request, 'ams/dashboard.html')

  