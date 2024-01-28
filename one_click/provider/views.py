from django.shortcuts import render,redirect
from django.http import HttpResponse
# from provider.models import 
from .models import provider

def prof(request):
    return render(request,"provider/prof.html",context={})
def profform(request):
    return render(request,"provider/profform.html",context={})
def history(request):
    return render (request,"provider/history.html",context={})
    
def addproviders(request):
    if request.method=="POST":
        pname=request.POST.get('name')
        email=request.POST.get('email')
        service=request.POST.get('service')
        experience=request.POST.get('experience')
        phoneno=request.POST.get('phone')
        education=request.POST.get('education')
        dob=request.POST.get('dob')
        image=request.POST.get('image')
        
        newprovider=provider(pname=pname,pcontactno=phoneno,pemail=email,pservicetype=service,exp=experience,pDOB=dob,peducation=education,pimage=image)
        newprovider.save()
        return redirect('addprovider')