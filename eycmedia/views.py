from django.shortcuts import render
from .models import *

# Create your views here.

def mediacenter(request):
    return render(request , 'mediacenter.html')


def photoscenter(request):
    all_photos = PhotosCenter.objects.all()
    context    = {'photos' : all_photos}
    return render(request , 'photos.html' , context)

def videoscenter(request):
    all_videos = VideosCenter.objects.all()
    context    = {'videos' : all_videos}
    return render(request , 'videos.html' , context)