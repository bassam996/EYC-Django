from .models import PhotosCenter , VideosCenter 
from .serializers import PhotosSerializers , VideosSerializers 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def photosapi(request):
    p_data      = PhotosCenter.objects.all()
    photos_data = PhotosSerializers(p_data , many=True).data
    return Response({'photos_data': photos_data})


@api_view(['GET'])
def episodeapi(request):
    v_data     = VideosCenter.objects.all()
    video_data = VideosSerializers(v_data , many=True).data
    return Response({'video_data': video_data})

