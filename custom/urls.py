from django.urls import path
from . import views
from . import api

app_name = "custom"


urlpatterns = [

        path('api/media' , api.mediaapi , name = 'mediacustomapi'),
        path('api/welcome' , api.welcomeapi , name = 'welcomeapi'),
        path('api/cadres' , api.cadresapi , name = 'cadresapi'),
        path('api/customtech' , api.techcustomapi , name = 'customtechapi'),
        path('api/customradio' , api.radiocustomapi , name = 'customradioapi'),
        path('api/achievment_desc' , api.descachievapi , name = 'achievdescapi'),
                                        
]
