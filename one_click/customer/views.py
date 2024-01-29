from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import userDetails


def UserData(request):
    return render(request,"customer/UserData.html",context={})
def bookings(request):
    return render(request,"customer/bookings.html",context={})
def bookform(request):
    return render(request,"customer/bookform.html",context={})


# def login(request):

def signin(request):

    if request.method == "POST":
        email=request.POST.get('email')
        pasword=request.POST.get('password')

        user=authenticate(request, username=email,password=pasword)
        if user is not None:
            
            if user.is_superuser:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("Admin User")
            elif user.is_staff:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("prof")
            else:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("user")
        else:
            msg='invalid details'
            return render(request,'customer\login.html',{'msg':msg})
    else:
            return render(request,'customer\login.html')
        


def register(request):
    errors = {}
    if request.method == 'POST':

        firstname = request.POST['firstName'].strip()
        lastname = request.POST['secondName'].strip()
        email = request.POST['email'].strip()
        gender = request.POST['Gender'].strip()
        password = request.POST['password'].strip()
        phonenumber=request.POST['phoneNo'].strip()
        image=request.FILES.get('image')
      
        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=email,password=password,is_active=True)
        new_user.save()
        ud = userDetails.objects.create(user=new_user,phone_number=phonenumber,gender=gender,images=image)
        ud.save()
        return redirect('login')
    else:
        return render(request, 'customer\Register.html')





def adduser(request):       
    return render(request,'customer\\UserData.html')

        

