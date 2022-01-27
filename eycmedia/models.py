from distutils.command.upload import upload
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class PhotosCenter(models.Model):
    title    = models.CharField(max_length=500)
    title_en = models.CharField(max_length=500)
    image    = models.ImageField(blank = True , null = True , upload_to='static/img/photoscenter')

class VideosCenter(models.Model):
    title    = models.CharField(max_length=500)
    title_en = models.CharField(max_length=500)
    video    = models.FileField(blank = True , null = True , upload_to='static/img/videoscenter')
