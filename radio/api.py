from .models import All_Season , Episodes 
from .serializers import SeasonSerializers , EpisodeSerializers 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def seasonapi(request):
    s_data = All_Season.objects.all()
    season_data = SeasonSerializers(s_data , many=True).data
    return Response({'season_data': season_data})


@api_view(['GET'])
def episodeapi(request):
    e_data = Episodes.objects.all()
    episode_data = EpisodeSerializers(e_data , many=True).data
    return Response({'episode_data': episode_data})

