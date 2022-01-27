from django.urls import path
from . import views
from . import api

app_name = "radio"


urlpatterns = [

           path('' , views.episodes , name='eposideshowurl'),

           #api

           path('api/seasons' , api.seasonapi , name='seasonapiurl'),
           path('api/episodes' , api.episodeapi , name='episodeapiurl'),

           
]
