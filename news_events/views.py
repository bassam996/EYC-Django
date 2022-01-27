from django.shortcuts import render
from .models import News

# Create your views here.



def news (request):
    news     = News.objects.all()
    context  = {'news' : news}
    return render(request , 'news.html' , context)


def news_detail (request , id):
    newsdetail   = News.objects.get(id=id)
    context      = {'nd' : newsdetail}
    return render(request , 'singlenews_event.html' , context)

