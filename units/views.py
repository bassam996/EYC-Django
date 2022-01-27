from django.shortcuts import render
from .models import *

# Research

def research_detail (request , slug):
    research_detail = Research.objects.get(slug=slug)
    context = {'research_detail' : research_detail}
    return render(request , 'research_details.html' , context)

# MediaModel



def media_detail (request , slug):
    mediadetail = Media.objects.get(slug=slug)
    context = {'mediadetail' : mediadetail}
    return render(request , 'media_details.html' , context)

# Youth

def youth_detail (request , slug):
    youthdetail = Youth.objects.get(slug=slug)
    context = {'youthdetail' : youthdetail}
    return render(request , 'youth_details.html' , context)

# Technology



def tech_detail (request , slug):
    techdetail = Technology.objects.get(slug=slug)
    context = {'techdetail' : techdetail}
    return render(request , 'technology_details.html' , context)
