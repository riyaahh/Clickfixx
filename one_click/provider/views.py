from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from customer.models import userDetails,appointmentdetails
from provider.models import provider

def prof(request):
    pro=provider.objects.all()
    return render(request,"provider/prof.html",context={'pro':pro})
def profform(request,id):
    object=provider.objects.get(pid=id)
    if request.POST:
                newname=request.POST['name']
                newmailid=request.POST['email']
                newphone=request.POST['phone']
                newexperience=request.POST['experience']
                neweducation=request.POST['education']
                newdob=request.POST['dob']
                newimage=request.FILES.get('image')
                object.pname=newname
                object.pemail=newmailid
                object.exp=newexperience
                object.peducation=neweducation
                object.pDOB=newdob
                object.pimage=newimage
                object.pcontactno=newphone
                object.save()
                return redirect('prof')
    return render(request,"provider/profform.html")
               
    #  if request.method=="POST":
    #       name = request.POST['name'].strip()
    #       mailid=request.POST['email'].strip()
    #       service=request.POST['service'].strip()
    #       phone=request.POST['phone'].strip()
    #       experience=request.POST['experience'].strip()
    #       education=request.POST['education'].strip()
    #       dob=request.POST['dob'].strip()
    #       image=request.FILES.get('image')

    #       newprov=editprovider(name=name,mailid=mailid,service=service,phone=phone,experience=experience,education=education,image=image,dob=dob)
    #       newprov.save()

          

def history(request):
    newapp=appointmentdetails.objects.filter(user_id=request.user)
    return render (request,"provider/history.html",context={'newapp':newapp})
def pappointments(request):
    pid=request.user
    print(pid)
    newapp=appointmentdetails.objects.filter()
    return render(request,"provider/pappointments.html",context={'newapp':newapp})
    
# def addproviders(request):
#     if request.method=="POST":
#         firstname = request.POST['firstName'].strip()
#         lastname = request.POST['secondName'].strip()
#         email = request.POST['email'].strip()
#         gender = request.POST['Gender'].strip()
#         password = request.POST['password'].strip()
#         phonenumber=request.POST['phoneNo'].strip()
        
        
        

#         new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=email,password=password,is_active=True)
#         new_user.save()
#         ud=userDetails.objects.create(user=new_user,phone_number=phonenumber,gender=gender,)
#         ud
#         return redirect('login')
#         return redirect('addproviders')


   
