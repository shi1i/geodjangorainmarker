from django.contrib.gis import admin
from django.contrib.gis.forms.widgets import OSMWidget

# Register your models here.
from .models import WeatherData, WeatherStation

# ---ИЗМЕНИЛ РЕГ НА ДЕКОРАТОРЫ + УБРАЛ LEAFLET ИЗ АДМИНКИ

@admin.register(WeatherData)
class WeatherDataAdmin(admin.GISModelAdmin):
    pass

@admin.register(WeatherStation)
class WeatherStationAdmin(admin.GISModelAdmin):
    gis_widget=OSMWidget
    # ИЗМЕНЕНИЯ ФОКУСА ЧЕРЕЗ СТАНДАРТНЫЕ ПАРАМЕТРЫ ТИПА ДАННЫХ В МОДЕЛИ
