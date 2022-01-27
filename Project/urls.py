"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('' , include('home.urls' , namespace='home')),
    path('news_events/' , include('news_events.urls' , namespace='news')),
    path('carriers/' , include('Carriers.urls' , namespace='carriers')),
    path('units/' , include('units.urls' , namespace='units')),
    path('' , include('about.urls' , namespace='contact')),
    path('mediacenter/' , include('eycmedia.urls' , namespace='media')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('radio/' , include('radio.urls' , namespace='radio')),
    path('' , include('about.urls' , namespace='about')),
    path('' , include('custom.urls' , namespace='custom')),



    #api path

    path('api-auth/', include('rest_framework.urls')),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)