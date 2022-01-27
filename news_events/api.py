from .models import News 
from .serializers import NewsSerializers 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def newsapi(request):
    n_data    = News.objects.all()
    news_data = NewsSerializers(n_data , many=True).data
    return Response({'news_data': news_data})

