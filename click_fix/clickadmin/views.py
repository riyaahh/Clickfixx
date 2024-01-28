from django.shortcuts import render
from django.http import HttpResponse






def index(request):
    return render(request,"clickadmin/index.html")
def about(request):
    return render(request,"clickadmin/about.html")
def contact(request):
    return render(request,"clickadmin/contact.html",context={})
def service(request):
    return render(request,"clickadmin/service.html",context={})

# def register(request):
#     return render(request,"customer\\register.html",context={})

# def user(request):
#     return render(request,'customer\\user.html')


# Create your views here.

