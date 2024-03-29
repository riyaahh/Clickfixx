
from django.urls import path,include
from .import views

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('register' , views.register, name='register'),
    path('UserData',views.UserData,name="user"),
    path('reviews',views.reviews,name="reviews"),
    path('bookings',views.bookings,name="bookings"),
    path('bookform',views.bookform,name="bookform"),
    path('adduser',views.adduser,name="adduser"),
    path('adminindex',views.adminindex,name="adminindex"),



    path('reset_form',views.reset_form,name="reset_form"),
    # path('reset_done',views.reset_done,name="reset_done"),
    path('reset_confirm',views.reset_confirm,name="reset_confirm"),
    # path('reset_complete',views.reset_complete,name="reset_complete"),


    path('deleteappointment/<str:ID>',views.deleteappointment,name="deleteappointment")
   

    # path('addappointments',views.addappointments,name="addappointments"),

]