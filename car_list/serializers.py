from rest_framework import serializers
from .models import CarList


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = (
            'id', 'car_model', 'mark',
            'price', 'mileage', 'year_manufactured',
        )
