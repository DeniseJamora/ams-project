from django.shortcuts import render

def criteria(request):
	return render(request, 'committee/criteria.html')

def viewcriteria(request):
	return render(request, 'committee/viewcriteria.html')

def addevidence(request):
	return render(request, 'committee/addevidence.html')
	
def assignuser(request):
	return render(request, 'committee/assignuser.html')

def dashboard(request):
	return render(request, 'committee/dashboard.html')

def docurepo(request):
	return render(request, 'committee/docurepo.html')

def viewchecklist(request):
	return render(request, 'committee/viewchecklist.html')

def evidencelist(request):
	return render(request, 'committee/evidencelist.html')



# Create your views here.
