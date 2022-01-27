from django.shortcuts import redirect, render
from .models import Counters

# Create your views here.

def home (request):
    counters = Counters.objects.all()
    context  = {'counters' : counters }
    return render(request , 'index.html', context)
