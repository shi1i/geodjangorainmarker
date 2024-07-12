from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import WeatherData, WeatherStation


class WeatherDataAdmin(LeafletGeoAdmin):
    pass

class WeatherStationAdmin(LeafletGeoAdmin):
    pass

admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(WeatherStation, WeatherStationAdmin)