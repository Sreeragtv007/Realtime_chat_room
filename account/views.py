from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user=User.objects.create_user(username=username,password=pass1)
        login(request,user)
        messages.info(request,"sign up sucess")
        
    return render(request, 'register.html')


def userLogin(request):
    return render(request,'login.html')
