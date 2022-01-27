from .models import Research , Media , Youth , Technology
from .serializers import ResearchSerializers , MediaUnitsSerializers , YouthSerializers , TechnologyUnitsSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def researcheapi(request):
    res_data = Research.objects.all()
    research_data = ResearchSerializers(res_data , many=True).data
    return Response({'research_data': research_data})


@api_view(['GET'])
def mediaunitsapi(request):
    mu_data = Media.objects.all()
    media_units_data = MediaUnitsSerializers(mu_data , many=True).data
    return Response({'media_units_data': media_units_data})

@api_view(['GET'])
def youthapi(request):
    yth_data = Youth.objects.all()
    youth_data = YouthSerializers(yth_data , many=True).data
    return Response({'youth_data': youth_data})

@api_view(['GET'])
def techunitsapi(request):
    tcu_data = Technology.objects.all()
    technology_units_data = TechnologyUnitsSerializers(tcu_data , many=True).data
    return Response({'technology_units_data': technology_units_data})
