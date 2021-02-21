"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    path('dash/', views.dash, name="dash"),
    path('setup/', include('setup.urls')),
    path('config/', include('configuration.urls')),
    path('committee/', include('committee.urls')),views.accreditationlist, name='accreditationlist'),

"""
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('dash/', views.dash, name='dash'),
    path('addagency/', views.addagency, name='addagency'),
    path('createdocuoutline/', views.createdocuoutline, name='createdocuoutline'),
    path('agencylist/', views.agencylist, name='agencylist'),
    path('finalizedocument/', views.finalizedocument, name='finalizedocument'),
    path('setcriteria/', views.setcriteria, name='setcriteria'),
    path('docuoutlinelist/', views.docuoutlinelist, name='docuoutlinelist'),
    path('viewdocuoutline/', views.viewdocuoutline, name='viewdocuoutline'),
    path('setdeadlines/', views.setdeadlines, name='setdeadlines'),
    path('deadlinelist/', views.deadlinelist, name='deadlinelist'),
    path('completeddoculist/', views.completeddoculist, name='completeddoculist'),
    path('addprogram/', views.addprogram, name='addprogram'),
    path('programlist/', views.programlist, name="programlist"),  
    path('viewprogram/<int:pk>/', views.viewprogram, name="viewprogram"), 
    path('createperiod/', views.createperiod, name='createperiod'),
    path('createteam/', views.createteam, name='createteam'), 
    path('evidencelist/', views.evidencelist, name='evidencelist'), 
    path('assigncriteria/', views.assigncriteria, name='assigncriteria'),
    path('accreditationbase/', views.accreditationbase, name='accreditationbase'),
    path('accreditationlist/', views.accreditationlist, name='accreditationlist'),
    path('viewaccreditation/', views.viewaccreditation, name='viewaccreditation'),
    path('teamlist/', views.teamlist, name='teamlist'),
    path('ongoinglist/', views.ongoinglist, name='ongoinglist'),
    path('viewongoing/', views.viewongoing, name='viewongoing'),
    path('ansdocu/', views.ansdocu, name='ansdocu'),
    path('uploadevidence/', views.uploadevidence, name='uploadevidence'),
    path('approveevidence/', views.approveevidence, name='approveevidence'),
    path('deadlines/', views.deadlines, name='deadlines'),
    path('filerepo/', views.filerepo, name='filerepo'),
    path('userlist/', views.userlist, name='userlist'),
    path('viewcompletedreport/', views.viewcompletedreport, name='viewcompletedreport'),
    path('selectevidence/', views.selectevidence, name='selectevidence'),
]