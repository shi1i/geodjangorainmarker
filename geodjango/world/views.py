from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_last_rainfall_date
from .models import WeatherData, WeatherStation
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.contrib.gis.measure import D

def last_rainfall(request, latitude, longitude):
    try:
        point = Point(float(longitude), float(latitude))
        station = WeatherStation.objects.filter(location__distance_lte=(point, D(km=10))).first()
        if not station:
            return JsonResponse({"error": "Station not found"}, status=404)

        last_rain = WeatherData.objects.filter(station=station).order_by('-date').first()
        if not last_rain:
            return JsonResponse({"error": "No weather data found for this station"}, status=404)

        return JsonResponse({
            "station": station.name,
            "location": {"latitude": latitude, "longitude": longitude},
            "last_rainfall": last_rain.rainfall,
            "date": last_rain.date,
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
from django.shortcuts import render

def home(request):
    return render(request, r"home.html")