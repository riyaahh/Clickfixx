from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
    path('clickadmin/', admin.site.urls),
    path('clickadmin', include('clickadmin.urls')),

]

