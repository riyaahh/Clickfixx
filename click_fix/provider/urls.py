from django.urls import path,include
from .import views



urlpatterns = [
      
      path('prof',views.prof,name="prof"),
      path('profform',views.profform,name="profform"),
      path('history',views.history,name="history")
]