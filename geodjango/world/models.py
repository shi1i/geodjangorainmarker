from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(default=Point(0, 0), srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)
    date = models.DateField()
    rainfall = models.FloatField()  # количество осадков, 0 если не было дождя
    objects = models.Manager()
