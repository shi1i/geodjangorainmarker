from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_last_rainfall_date
from .models import WeatherData, WeatherStation
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import D


def last_rainfall(request, latitude, longitude):
    # point = Point(float(longitude), float(latitude)) Тут неправильные ввод переменных, они должны быть наоборот, верните мне мои 3 дня жизни))
    point = Point(float(latitude), float(longitude))
    station = get_object_or_404(WeatherStation, location__distance_lte=(point, D(km=5)))  # Найти станцию в пределах 5 км от точки
    last_rain = WeatherData.objects.filter(station=station).order_by('-date').first()

    if last_rain:
        data = {
            'station': station.name,
            'date': last_rain.date.strftime("%Y-%m-%d %H:%M:%S"),
            'rainfall': last_rain.rainfall,
        }
    else:
        data = {
            'station': station.name,
            'date': None,
            'rainfall': None,
        }
    


from django.shortcuts import render



def home(request):
    return render(request, r"home.html")