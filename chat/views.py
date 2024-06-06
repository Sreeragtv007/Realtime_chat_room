from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    room=Room.objects.all()
    context={'room':room}
    return render(request,'index.html',context)

def joinRoom(request,pk):
    room=Room.objects.get(id=pk)
    rooms=Room.objects.all()
    context={'room':room,'rooms':rooms}
    return render(request,'room.html',context)