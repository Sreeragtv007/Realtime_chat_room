
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('room/<str:pk>/',joinRoom,name='room')
]
