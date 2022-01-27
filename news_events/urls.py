from django.urls import path
from . import views
from . import api

app_name = "news_events"


urlpatterns = [

           path('' , views.news , name='allnews'),
           path('<int:id>', views.news_detail , name='newsdetail'),

           #api

           path('api/news' , api.newsapi , name = 'newsapiurl')
]
