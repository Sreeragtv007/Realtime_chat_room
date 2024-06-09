from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.TextField()
    room_img=models.ImageField(upload_to='images/',blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    