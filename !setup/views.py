from django.shortcuts import render

def addagency(request):
	return render(request, 'setup/addagency.html')

def viewprogram(request):
	return render(request, 'setup/viewprogram.html')

def programlist(request):
	return render(request, 'setup/programlist.html')

def createdocuoutline(request):
	return render(request, 'setup/createdocuoutline.html')

def addprogram(request):
	return render(request, 'setup/addprogram.html')

# Create your views here.
