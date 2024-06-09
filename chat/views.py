from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request, *args, **kwargs):

    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'index.html', context)


def joinRoom(request, pk):
    room = Room.objects.get(id=pk)
    rooms = Room.objects.all()
    context = {'room': room, 'rooms': rooms}
    return render(request, 'room.html', context)


def searchRoom(request):
    rooms = Room.objects.filter(name__icontains=request.POST.get('search'))

    context = {'rooms': rooms}
    return render(request, 'index.html', context)

def createRoom(request):
    if request.method == 'POST':
        room_name=request.POST.get('roomname')
        room_img=request.POST.get('roomimg')
        room_disc=request.POST.get('roomdisc')
        room=Room.objects.create(name=room_name,room_img=room_img,disc=room_disc)   
        return redirect('index') 
    else:
        return render(request,'createroom.html')
