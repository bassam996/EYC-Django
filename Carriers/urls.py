from django.urls import path
from . import api
from . import views

app_name = "Carriers"


urlpatterns = [
               #path('peace' , views.peace , name='peace'),
               path('peace/<slug:slug>', views.peace_detail , name='peacedetail'),
               #path('political' , views.political , name='political'),
               path('political/<slug:slug>', views.political_detail , name='politicaldetail'),
               #path('women' , views.women , name='women'),
               path('women/<slug:slug>', views.women_detail , name='womendetail'),
               #path('human_rights' , views.human_rights , name='human_rights'),
               path('human_rights/<slug:slug>', views.human_detail , name='humandetail'),
               #path('environment' , views.environment , name='environment'),
               path('environment/<slug:slug>', views.environment_detail , name='environmentdetail'),


               # api 

               path('api/peace' , api.peaceapi , name='peaceapi'),
               path('api/political' , api.politicalapi , name='politicalapi'),
               path('api/women' , api.womenapi , name='womenapi'),
               path('api/humanrights' , api.humanrighesapi , name='humanrighesapi'),
               path('api/environment' , api.environmentsapi , name='environmentsapi'),

]
