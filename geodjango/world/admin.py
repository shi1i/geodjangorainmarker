from django.contrib import admin

# Register your models here.
from .models import WeatherData, WeatherStation

admin.site.register(WeatherData)
admin.site.register(WeatherStation)