from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from customer.models import userDetails,appointmentdetails

def prof(request):
    return render(request,"provider/prof.html",context={})
def profform(request):
    return render(request,"provider/profform.html",context={})
def history(request):
    newapp=appointmentdetails.objects.filter(user_id=request.user)
    
    return render (request,"provider/history.html",context={'newapp':newapp})
    
def addproviders(request):
    if request.method=="POST":
        firstname = request.POST['firstName'].strip()
        lastname = request.POST['secondName'].strip()
        email = request.POST['email'].strip()
        gender = request.POST['Gender'].strip()
        password = request.POST['password'].strip()
        phonenumber=request.POST['phoneNo'].strip()
        
        
        

        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=email,password=password,is_active=True)
        new_user.save()
        ud=userDetails.objects.create(user=new_user,phone_number=phonenumber,gender=gender,)
        ud
        return redirect('login')
        return redirect('addproviders')