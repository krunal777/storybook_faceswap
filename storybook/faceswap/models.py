from django.db import models


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    face_Main_Img = models.ImageField(upload_to='images/')
    cartoon_Main_Img = models.ImageField(upload_to='images/')
    # swap_Main_Img = models.ImageField(upload_to='images/')

    