from django.shortcuts import render
from .models import *
from .filters import EpisodesFilter

# Create your views here.


def episodes(request):
    episodeview      = Episodes.objects.all()
    my_filter        = EpisodesFilter(request.GET , queryset=episodeview )
    episodeview      = my_filter.qs
    context          = {'v_episode' : episodeview  , 'filter' : my_filter }
    return render(request , 'all_episodes.html' , context)