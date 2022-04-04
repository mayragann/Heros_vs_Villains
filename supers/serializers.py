from rest_framework import serializers
from .models import Supers

class Supers(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ablity', 'catchprhase', 'type']
        dept = 1