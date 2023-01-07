"""vindingmachine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
     path('reset', views.reset, name='reset'),
     path('', views.home, name='home'),
     
     path('get_property/',views.get_property, name="get_property"),
     path('manage_patient', views.manage_patient, name='manage_patient'),
     path('manage_doctor', views.manage_doctor, name='manage_doctor'),
     path('manage_department', views.manage_department, name='manage_department')
]
