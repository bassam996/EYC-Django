from django.db.models import fields
from rest_framework import serializers
from .models import Branches , Partnerships



class BranchesSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Branches
        fields = '__all__'


class PartnerShipsSerializers(serializers.ModelSerializer):
    class Meta : 
        model  = Partnerships
        fields = '__all__'
