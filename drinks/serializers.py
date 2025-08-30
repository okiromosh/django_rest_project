from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    # the metadata describing the json
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']

