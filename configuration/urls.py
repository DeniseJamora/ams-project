"""portfolio URL Configuration

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
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accreditationlist/', views.accreditationlist, name='accreditationlist'),
    path('docuoutlinelist/', views.docuoutlinelist, name='docuoutlinelist'),
    path('announcementlist/', views.announcementlist, name='announcementlist'),
    path('ongoinglist/', views.ongoinglist, name='ongoinglist'),
    path('assignuser/', views.assignuser, name='assignuser'),
    path('committeelist/', views.committeelist, name='committeelist'),
    path('createperiod/', views.createperiod, name='createperiod'),
    path('createteam/', views.createteam, name='createteam'),
    path('addcommittees/', views.addcommittees, name='addcommittees'),

]