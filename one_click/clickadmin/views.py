from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from customer.models import Review




# @login_required(login_url='login')
def index(request):
    try:
        reviews=Review.objects.filter(user_id=request.user)
        print(reviews)
    except:
        reviews = None
    return render(request,"clickadmin/index.html",{'reviews':reviews})

def about(request):
    return render(request,"clickadmin/about.html")
def contact(request):
    return render(request,"clickadmin/contact.html",context={})
def service(request):
    return render(request,"clickadmin/service.html",context={})
def chart(request):
    return render(request,"clickadmin/chart.html",context={})
def form(request):
    return render(request,"clickadmin/form.html",context={})
def indexadm(request):
    return render(request,"clickadmin/indexadm.html",context={})
def table(request):
    return render(request,"clickadmin/table.html",context={})
def widget(request):
    return render(request,"clickadmin/widget.html",context={})
def signin(request):
    return render(request,"clickadmin/signin.html",context={})
def signup(request):
    return render(request,"clickadmin/signup.html",context={})
def user(request):
    return render(request,"clickadmin/user.html",context={})


# def register(request):
#     return render(request,"customer\\register.html",context={})

# def user(request):
#     return render(request,'customer\\user.html')


# Create your views here.

