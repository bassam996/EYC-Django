from django.shortcuts import render
from .models import *

# Peace

def peace_detail (request , slug):
    peacedetail = Peace.objects.get(slug=slug)
    context     = {'peacedetail' : peacedetail}
    return render(request , 'peace_details.html' , context)


# Political


def political_detail (request , slug):
    politicaldetail = Political_participation.objects.get(slug=slug)
    context         = {'politicaldetail' : politicaldetail}
    return render(request , 'political_details.html' , context)

# Women

def women_detail (request , slug):
    womendetail = Women.objects.get(slug=slug)
    context     = {'womendetail' : womendetail}
    return render(request , 'women_details.html' , context)

# human_rights


def human_detail (request , slug):
    humandetail = Human_Rights.objects.get(slug=slug)
    context     = {'humandetail' : humandetail }
    return render(request , 'human_details.html' , context)

# Environment

def environment_detail (request , slug):
    environmentdetail = Environment.objects.get(slug=slug)
    context           = {'environmentdetail' : environmentdetail }
    return render(request , 'environment_details.html' , context)
