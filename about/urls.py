from django.urls import path
from . import views
from . import api

app_name = "about"


urlpatterns = [
           path('volunteering/' , views.volunteering),
           path('contact-us/' , views.contact),
           path('ourParteners/' , views.ourParteners),
           path('board/' , views.board),
           path('branches/' , views.branches),

           #api

           path('api/branches' , api.branchapi , name='branchapi'),
           path('api/partnerships' , api.partnershipsapi , name = 'partnershipsapi')
]
