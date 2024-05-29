from django.db import models

# Create your models here.
class Chatroom(models.Model):
    room_name=models.TextField()
    room_discription=models.TextField()
    room_img=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None, default='avatar4.png')
    