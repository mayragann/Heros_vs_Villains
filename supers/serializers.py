from rest_framework import serializers
from .models import Super

class Super(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ablity', 'catchprhase', 'type']
        dept = 1