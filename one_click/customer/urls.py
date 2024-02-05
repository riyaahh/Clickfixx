
from django.urls import path,include
from .import views

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('register' , views.register, name='register'),
    path('UserData',views.UserData,name="user"),
    # path('adduser',views.adduser,name="adduser"),
    path('bookings',views.bookings,name="bookings"),
    path('bookform',views.bookform,name="bookform"),
    path('adduser',views.adduser,name="adduser"),
    path('deleteappointment/<str:ID>',views.deleteappointment,name="deleteappointment")
   
    # path('addappointments',views.addappointments,name="addappointments"),
]