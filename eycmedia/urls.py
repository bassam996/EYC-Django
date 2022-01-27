from django.urls import path
from . import views
from . import api

app_name = "eycmedia"


urlpatterns = [

           path('' , views.mediacenter , name='mediacenter'),
           path('photos/' , views.photoscenter , name='photoscenter'),
           path('videos/' , views.videoscenter , name='videoscenter'),

           #api

           path('api/photos' , api.photosapi , name = 'photosapiurl'),
           path('api/videos' , api.episodeapi , name = 'videosapiurl'),
]
