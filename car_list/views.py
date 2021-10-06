from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import CarList
from .serializers import CarListSerializer


class CarListFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_mileage = filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    max_mileage = filters.NumberFilter(field_name='mileage', lookup_expr='lte')
    min_year_manufactured = filters.NumberFilter(
        field_name='year_manufactured', lookup_expr='gte'
    )
    max_year_manufactured = filters.NumberFilter(
        field_name='year_manufactured', lookup_expr='lte'
    )

    class Meta:
        model = CarList
        fields = [
            'car_model', 'mark',
            'price', 'mileage', 'year_manufactured',
        ]


class CarListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = CarList.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CarListFilter
