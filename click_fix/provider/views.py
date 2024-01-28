from django.shortcuts import render
from django.http import HttpResponse
# from provider.models import 


def prof(request):
    return render(request,"provider/prof.html",context={})
def profform(request):
    return render(request,"provider/profform.html",context={})
def history(request):
    return render (request,"provider/history.html",context={})
    
def appointments(request):
    if request.method=="POST":
        appid=request.POST.get('firstName')
        Lastn=request.POST.get('secondName')
        phoneno=request.POST.get('phoneNo')
        Email=request.POST.get('email')
        Gender=request.POST.get('Gender')
        
        newuser=userDetails(firstname=Firstname,lastname=Lastname,phone_number=phoneno,mail=Email,gender=Gender)
        newuser.save()
        return redirect('adduser')