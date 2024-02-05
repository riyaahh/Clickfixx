from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('indexadm/')
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_obj= User.objects.filter(username=username)
            if not user_obj.exists ():
                messages.info(request, request,'Account not found')
                return HttpResponseRedirect(request.META.get('META_REFERER'))
            
            user_obj = authenticate(username= username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect('indexadm')
            
            messages.info(request, 'Invalid password')
            return redirect('/')
        
        return render(request,'signin.html')
    
    except Exception as e:
        print(e)


# Create your views here.
