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


def accreditationlist(request):
	return render(request, 'configuration/accreditationlist.html')

def docuoutlinelist(request):
	return render(request, 'configuration/docuoutlinelist.html')

def ongoinglist(request):
	return render(request, 'configuration/ongoinglist.html')

def announcementlist(request):
	return render(request, 'configuration/announcementlist.html')

def committeelist(request):
	return render(request, 'configuration/committeelist.html')

def createperiod(request):
	return render(request, 'configuration/createperiod.html')

def createteam(request):
	return render(request, 'configuration/createteam.html')


def dashboard(request):
	return render(request, 'committee/dashboard.html')

def docurepo(request):
	return render(request, 'committee/docurepo.html')


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



def viewaccreditation(request):
	return render(request, 'configuration/viewaccreditation.html')

def viewdocuoutline(request):
	return render(request, 'configuration/viewdocuoutline.html')

def viewongoing(request):
	return render(request, 'configuration/viewongoing.html')

def userlist(request):
	return render(request, 'configuration/userlist.html')

def teamlist(request):
	return render(request, 'configuration/teamlist.html')

def ansdocu(request):
	return render(request, 'configuration/ansdocu.html')

  