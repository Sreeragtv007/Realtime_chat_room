from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request,*args, **kwargs):
    
    
    room=Room.objects.all()
    context={'rooms':room}
    return render(request,'index.html',context)

def joinRoom(request,pk):
    room=Room.objects.get(id=pk)
    rooms=Room.objects.all()
    context={'room':room,'rooms':rooms}
    return render(request,'room.html',context)

def searchRoom(request):
    rooms=Room.objects.filter(name__icontains=request.POST.get('search'))
    
    
    context={'rooms':rooms}
    return render(request,'index.html',context)
    