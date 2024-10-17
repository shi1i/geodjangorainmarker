from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import WeatherStation, WeatherData

def get_last_rainfall_date(lat, lon):
    user_location = Point(lon, lat, srid=4326)
    nearest_station = WeatherStation.objects.annotate(distance=Distance('location', user_location)).order_by('distance').first()
    
    if nearest_station:
        last_rain_date = WeatherData.objects.filter(station=nearest_station, rainfall__gt=0).order_by('-date').first()
        if last_rain_date:
            return last_rain_date.date
    return None
