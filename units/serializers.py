from django.db.models import fields
from rest_framework import serializers
from .models import Research , Media , Youth , Technology 



class ResearchSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Research
        fields = '__all__'


class MediaUnitsSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Media
        fields = '__all__'



class YouthSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Youth
        fields = '__all__'

        
class TechnologyUnitsSerializers(serializers.ModelSerializer):
    class Meta : 
        model = Technology
        fields = '__all__'
