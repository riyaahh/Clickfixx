from django.urls import path
from . import views



urlpatterns = [

 path('indexadm/',views.indexadm , name= "indexadm"),
 path('signup/',views.signup , name= "signup"),
 path('signin/',views.signin , name="signin"),
 path('signout/',views.signout, name"signout"),



]