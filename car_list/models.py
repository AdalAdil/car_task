from django.db import models


class CarList(models.Model):

    mark = models.CharField(
        verbose_name='mark', max_length=64,
    )
    car_model = models.CharField(
        verbose_name='car_model', max_length=64,
    )
    price = models.IntegerField(verbose_name='price',)
    mileage = models.IntegerField(verbose_name='mileage',)
    year_manufactured = models.IntegerField(
        verbose_name='year_manufactured',
    )

    class Meta:
        verbose_name = 'car_list'
