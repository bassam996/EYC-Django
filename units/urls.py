from django.urls import path
from . import api
from . import views

app_name = "units"


urlpatterns = [

           # path('research' , views.research , name='research'),
            path('research/<slug:slug>' , views.research_detail , name='researchdetail'),
           # path('media' , views.media , name='media'),
            path('media/<slug:slug>' , views.media_detail , name='mediadetail'),
           # path('youth' , views.youth , name='youth'),
            path('youth/<slug:slug>' , views.youth_detail , name='youthdetail'),
           # path('technology' , views.technology , name='technology'),
            path('technology/<slug:slug>' , views.tech_detail , name='techdetail'),
            #api

            path('api/research' , api.researcheapi , name='researcheapi'),
            path('api/media_units' , api.mediaunitsapi , name='mediaunitsapi'),
            path('api/youth' , api.youthapi , name='youthapi'),
            path('api/tech_units' , api.techunitsapi , name='techunitsapi'),

]
