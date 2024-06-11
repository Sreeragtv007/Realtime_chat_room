from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage
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
        name = request.POST['name']
        uploaded_file = request.FILES['image']
        
        # Save the file to the media directory
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        # Save the file and name to the model
        my_model_instance = Room(name=name, room_img=filename)
        my_model_instance.save()
        return redirect('index') 
    else:
        return render(request,'createroom.html')
