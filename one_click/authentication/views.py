from django.shortcuts import render
from django.http import HttpResponse

def indexadm(request):
    return render(request,"clickadmin/indexadm.html")

def signin(request):
    return render(request,"clickadmin/signin.html")


def signup(request):
    return render(request,"clickadmin/signup.html")

def signout(request):
    pass


# Create your views here.
