from django.shortcuts import render

def accreditationlist(request):
	return render(request, 'configuration/accreditationlist.html')

def docuoutlinelist(request):
	return render(request, 'configuration/docuoutlinelist.html')

def ongoinglist(request):
	return render(request, 'configuration/ongoinglist.html')

def announcementlist(request):
	return render(request, 'configuration/announcementlist.html')

def assignuser(request):
	return render(request, 'configuration/assignuser.html')

def committeelist(request):
	return render(request, 'configuration/committeelist.html')

def createperiod(request):
	return render(request, 'configuration/createperiod.html')

def createteam(request):
	return render(request, 'configuration/createteam.html')

def addcommittees(request):
	return render(request, 'configuration/addcommittees.html')

# Create your views here.
