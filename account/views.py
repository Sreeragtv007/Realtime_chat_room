from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.create_user(username=username, password=pass1)
        login(request, user)
        messages.info(request, "sign up sucess")

    return render(request, 'register.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user= authenticate(username=username,password=pass1)
        if user is not None :
            login(request,user)
            return redirect ('index')
        else:
            messages.info(request,'user name or password is incorrect')
            
    
    
    return render(request, 'login.html')
def userLogout(request):
    logout(request)
    
    return redirect ('login')