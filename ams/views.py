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
	return render(request, 'ams/accreditationlist.html')

def docuoutlinelist(request):
	return render(request, 'ams/docuoutlinelist.html')

def ongoinglist(request):
	return render(request, 'ams/ongoinglist.html')

def announcementlist(request):
	return render(request, 'ams/announcementlist.html')

def committeelist(request):
	return render(request, 'ams/committeelist.html')

def createperiod(request):
	return render(request, 'ams/createperiod.html')

def createteam(request):
	return render(request, 'ams/createteam.html')


def docurepo(request):
	return render(request, 'ams/docurepo.html')


def addagency(request):
	return render(request, 'ams/addagency.html')

def viewprogram(request):
	return render(request, 'ams/viewprogram.html')

def programlist(request):
	return render(request, 'ams/programlist.html')

def createdocuoutline(request):
	return render(request, 'ams/createdocuoutline.html')

def addprogram(request):
	return render(request, 'ams/addprogram.html')



def viewaccreditation(request):
	return render(request, 'ams/viewaccreditation.html')

def viewdocuoutline(request):
	return render(request, 'ams/viewdocuoutline.html')

def viewongoing(request):
	return render(request, 'ams/viewongoing.html')

def userlist(request):
	return render(request, 'ams/userlist.html')

def teamlist(request):
	return render(request, 'ams/teamlist.html')

def ansdocu(request):
	return render(request, 'ams/ansdocu.html')

  