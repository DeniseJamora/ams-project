from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'ams/base.html')

def login(request):
    return render(request, 'ams/login.html')

def register(request):
    return render(request, 'ams/register.html')

def dash(request):
    return render(request, 'ams/dash.html')

def addagency(request):
	return render(request, 'ams/addagency.html')

def createdocuoutline(request):
	return render(request, 'ams/createdocuoutline.html')

def docuoutlinelist(request):
	return render(request, 'ams/docuoutlinelist.html')

def viewdocuoutline(request):
	return render(request, 'ams/viewdocuoutline.html')

def addprogram(request):
	return render(request, 'ams/addprogram.html')

def programlist(request):
    return render(request, 'ams/programlist.html')

def viewprogram(request):
    return render(request, 'ams/viewprogram.html')

def createperiod(request):
	return render(request, 'ams/createperiod.html')

def createteam(request):
	return render(request, 'ams/createteam.html')

def accreditationlist(request):
	return render(request, 'ams/accreditationlist.html')

def viewaccreditation(request):
	return render(request, 'ams/viewaccreditation.html')

def teamlist(request):
	return render(request, 'ams/teamlist.html')

def ongoinglist(request):
	return render(request, 'ams/ongoinglist.html') 

def viewongoing(request):
	return render(request, 'ams/viewongoing.html')

def ansdocu(request):
	return render(request, 'ams/ansdocu.html')

def docurepo(request):
	return render(request, 'ams/filerepo.html')

def filerepo(request):
	return render(request, 'ams/filerepo.html')

def userlist(request):
	return render(request, 'ams/userlist.html')