from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.TextField(blank=True, null=True)
    room_img=models.ImageField(upload_to='images/',blank=True, null=True,default='defaults/avengers.jpg')
    disc=models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Roommessage(models.Model):
    message=models.TextField(blank=True, null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
        
    