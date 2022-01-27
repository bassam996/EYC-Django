from .models import Peace , Political_participation , Women , Human_Rights , Environment
from .serializers import PeaceSerializers , Political_participationSerializers , WomenSerializers , Human_RightsSerializers , EnvironmentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def peaceapi(request):
    pc_data    = Peace.objects.all()
    peace_data = PeaceSerializers(pc_data , many=True).data
    return Response({'peace_data': peace_data})


@api_view(['GET'])
def politicalapi(request):
    political_data               = Political_participation.objects.all()
    political_participation_data = Political_participationSerializers(political_data , many=True).data
    return Response({'political_participation_data': political_participation_data})



@api_view(['GET'])
def womenapi(request):
    wm_data    = Women.objects.all()
    women_data = WomenSerializers(wm_data , many=True).data
    return Response({'women_data': women_data})



@api_view(['GET'])
def humanrighesapi(request):
    hr_data           = Human_Rights.objects.all()
    human_rights_data = Human_RightsSerializers(hr_data , many=True).data
    return Response({'human_rights_data': human_rights_data})



@api_view(['GET'])
def environmentsapi(request):
    environ_data     = Environment.objects.all()
    environment_data = EnvironmentSerializers(environ_data , many=True).data
    return Response({'environment_data': environment_data})
