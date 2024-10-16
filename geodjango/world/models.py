from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# --- ОБЪЕКТНАЯ МОДЕЛЬ ДАННЫХ ДЛЯ БД - ТАБЛИЦА
class WeatherStation(models.Model):
    # --- КАЖДАЯ ПЕРЕМЕННАЯ СОЗДАЕТ ОДНО ПОЛЕ В БД, Т.Е. ЯВЛЯЕТСЯ ОБЪЕКТОМ, ХРАНИМЫМ В БД.
    # --- НУЖНО ВСЕГО ЛИШЬ ОБЪЯВИТЬ ЕЙ ТИП ДАННЫХ.
    name = models.CharField(max_length=100)
    location = models.PointField(default=Point(41.97, 45.04), srid=4326) # lat, lon
    objects = models.Manager()

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)
    date = models.DateField()
    rainfall = models.FloatField()  # количество осадков, 0 если не было дождя
    objects = models.Manager()
