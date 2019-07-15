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
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('addfaculty/', views.addfaculty, name="addfaculty"),
    path('viewprogram/', views.viewprogram, name="viewprogram"),
    path('programlist/', views.programlist, name="programlist"),    


    path('accreditationlist/', views.accreditationlist, name='accreditationlist'),
    path('docuoutlinelist/', views.docuoutlinelist, name='docuoutlinelist'),
    path('announcementlist/', views.announcementlist, name='announcementlist'),
    path('ongoinglist/', views.ongoinglist, name='ongoinglist'),
    path('assignuser/', views.assignuser, name='assignuser'),
    path('committeelist/', views.committeelist, name='committeelist'),
    path('createperiod/', views.createperiod, name='createperiod'),
    path('createteam/', views.createteam, name='createteam'),
    path('addcommittees/', views.addcommittees, name='addcommittees'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('docurepo/', views.docurepo, name='docurepo'),


    path('addagency/', views.addagency, name='addagency'),
    path('createdocuoutline/', views.createdocuoutline, name='createdocuoutline'),
    path('viewprogram/', views.viewprogram, name='viewprogram'),
    path('programlist/', views.programlist, name='programlist'),
    path('addprogram/', views.addprogram, name='addprogram'),


    path('viewaccreditation/', views.viewaccreditation, name='viewaccreditation'),
    path('viewdocuoutline/', views.viewdocuoutline, name='viewdocuoutline'),
    path('viewongoing/', views.viewongoing, name='viewongoing'),
    path('userlist/', views.userlist, name='userlist'),
    path('teamlist/', views.teamlist, name='teamlist'),
    path('ansdocu/', views.ansdocu, name='ansdocu'),
]
