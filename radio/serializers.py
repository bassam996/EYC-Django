from django.db.models import fields
from rest_framework import serializers
from .models import All_Season , Episodes 



class SeasonSerializers(serializers.ModelSerializer):
    class Meta : 
        model = All_Season
        fields = '__all__'


class EpisodeSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Episodes
        fields = '__all__'
