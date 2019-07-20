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
    path('base/', views.base, name="base"),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('dash/', views.dash, name='dash'),
    path('addagency/', views.addagency, name='addagency'),
    path('createdocuoutline/', views.createdocuoutline, name='createdocuoutline'),
    path('docuoutlinelist/', views.docuoutlinelist, name='docuoutlinelist'),
    path('viewdocuoutline/', views.viewdocuoutline, name='viewdocuoutline'),
    path('addprogram/', views.addprogram, name='addprogram'),
    path('programlist/', views.programlist, name="programlist"),  
    path('viewprogram/', views.viewprogram, name="viewprogram"), 
    path('createperiod/', views.createperiod, name='createperiod'),
    path('createteam/', views.createteam, name='createteam'), 
    path('accreditationlist/', views.accreditationlist, name='accreditationlist'),
    path('viewaccreditation/', views.viewaccreditation, name='viewaccreditation'),
    path('teamlist/', views.teamlist, name='teamlist'),
    path('ongoinglist/', views.ongoinglist, name='ongoinglist'),
    path('viewongoing/', views.viewongoing, name='viewongoing'),
    path('ansdocu/', views.ansdocu, name='ansdocu'),
    path('filerepo/', views.filerepo, name='filerepo'),
    path('userlist/', views.userlist, name='userlist'),
]
