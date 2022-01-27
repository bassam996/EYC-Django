from .models import Media , WelcomeScreen , Cadres , Technology_Desc , Radio , Desc_Achievements
from .serializers import MediaCustomSerializers , WelComeSerializers , CadresCustomSerializers , TechCustomSerializers , RadioCustomSerializers , AchievCustomSerializers 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def mediaapi(request):
    m_data     = Media.objects.all()
    media_data = MediaCustomSerializers(m_data , many=True).data
    return Response({'media_data': media_data})


@api_view(['GET'])
def welcomeapi(request):
    w_data       = WelcomeScreen.objects.all()
    welcome_data = WelComeSerializers(w_data , many=True).data
    return Response({'welcome_data': welcome_data})

@api_view(['GET'])
def cadresapi(request):
    c_data      = Cadres.objects.all()
    cadres_data = CadresCustomSerializers(c_data , many=True).data
    return Response({'cadres_data': cadres_data})

@api_view(['GET'])
def techcustomapi(request):
    tc_data         = Technology_Desc.objects.all()
    techcustom_data = TechCustomSerializers(tc_data , many=True).data
    return Response({'techcustom_data': techcustom_data})

@api_view(['GET'])
def radiocustomapi(request):
    rc_data          = Radio.objects.all()
    radiocustom_data = RadioCustomSerializers(rc_data , many=True).data
    return Response({'radiocustom_data': radiocustom_data})

@api_view(['GET'])
def descachievapi(request):
    achdes_data     = Desc_Achievements.objects.all()
    achievdesc_data = AchievCustomSerializers(achdes_data , many=True).data
    return Response({'achievdesc_data': achievdesc_data})

