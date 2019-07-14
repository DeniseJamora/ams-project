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

def generateform(request):
	return render(request, 'setup/generateform.html')

def addqa(request):
	return render(request, 'setup/addqa.html')

def addschedules(request):
	return render(request, 'setup/addschedules.html')

def addteams(request):
	return render(request, 'setup/addteams.html')

def createchecklist(request):
	return render(request, 'setup/createchecklist.html')

def createinstrument(request):
	return render(request, 'setup/createinstrument.html')

def facultyandstaff(request):
	return render(request, 'setup/facultyandstaff.html')

# Create your views here.
