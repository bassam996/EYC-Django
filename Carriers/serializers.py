from django.db.models import fields
from rest_framework import serializers
from .models import Peace , Political_participation , Women , Human_Rights , Environment



class PeaceSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Peace
        fields = '__all__'


class Political_participationSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Political_participation
        fields = '__all__'


class WomenSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Women
        fields = '__all__'

class Human_RightsSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Human_Rights
        fields = '__all__'


class EnvironmentSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Environment
        fields = '__all__'



