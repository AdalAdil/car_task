# Generated by Django 3.2.8 on 2021-10-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=64, verbose_name='mark')),
                ('car_model', models.CharField(max_length=64, verbose_name='car_model')),
                ('price', models.IntegerField(verbose_name='price')),
                ('mileage', models.IntegerField(verbose_name='mileage')),
                ('year_manufactured', models.IntegerField(verbose_name='year_manufactured')),
            ],
            options={
                'verbose_name': 'car_list',
            },
        ),
    ]
