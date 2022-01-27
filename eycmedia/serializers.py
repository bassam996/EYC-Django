from django.db.models import fields
from rest_framework import serializers
from .models import PhotosCenter , VideosCenter 



class PhotosSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = PhotosCenter
        fields = '__all__'


class VideosSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = VideosCenter
        fields = '__all__'
