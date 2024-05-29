from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    chatrooms=Chatroom.objects.all()
    
    connected=False
    context={'chatrooms':chatrooms,'connected':connected}
    return render(request,'index.html',context)

def chat(request,pk):
    chatrooms=Chatroom.objects.all()
    chatroom=Chatroom.objects.get(id=pk)
    
    connected=None
    context={'chatrooms':chatrooms,'connected':connected,'chatroom':chatroom}
    return render(request,'roomchat.html',context)