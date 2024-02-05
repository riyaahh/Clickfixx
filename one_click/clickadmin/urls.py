from django.urls import path,include
from clickadmin import views
from clickadmin.views import index,about,contact,service
from .import views
from . views import index,about,contact,service
from customer.views import signin
from django.contrib import admin
from django.urls import path








urlpatterns = [
    path('',index,name="dashboard"),


    path('about', views.about ,name="about"),
    path('contact', views.contact ,name="contact"),
    path('service', views.service,name="service"),
    # path('login', views.login ,name="login"),

    # path('about/', views.about ,name="about"),
    # path('contact/', views.contact ,name="contact"),
    # path('service/', views.service,name="service"),


    path('about/', views.about ,name="about"),
    path('contact/', views.contact ,name="contact"),
    path('service/', views.service,name="service"),
    path('login/', signin ,name="login"),

    # path('register' , views.register, name='register'),
    # path('user',views.user,name="user")
    path('chart/',views.chart , name="chart"),
    path('form/',views.form , name= "form"),
    path('indexadm/',views.indexadm , name= "indexadm"),
    path('table/',views.table , name= "table"),
    path('widget/',views.widget , name= "widget"),
    path('signin/',views.signin , name= "signin"),
    path('signup/',views.signup , name= "signup"),
    path('user/',views.user , name="user"),
    
    

]

