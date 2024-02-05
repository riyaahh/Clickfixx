from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('indexadm')

    return render(request, 'signin.html')

def indexadm(request):
    return render(request, 'indexadm.html')



# Create your views here.
