from django.db.models import fields
from rest_framework import serializers
from .models import Media , WelcomeScreen , Cadres , Technology_Desc , Radio , Desc_Achievements



class MediaCustomSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Media
        fields = '__all__'


class WelComeSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = WelcomeScreen
        fields = '__all__'

class CadresCustomSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Cadres
        fields = '__all__'

class TechCustomSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Technology_Desc
        fields = '__all__'

class RadioCustomSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Radio
        fields = '__all__'

class AchievCustomSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Desc_Achievements
        fields = '__all__'
