import django_filters
from .models import Episodes

class EpisodesFilter(django_filters.FilterSet):
    class Meta:
        model    = Episodes
        fields   = '__all__'
        exclude  = ['episode_image' , 'episode_url' , 'episode_name' , 'episode_name_en']

        