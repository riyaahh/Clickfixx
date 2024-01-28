from django.urls import path,include

from clickadmin import views
from clickadmin.views import index,about,contact,service

from .import views
from . views import index,about,contact,service
from customer.views import signin



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
]

