from django.shortcuts import render
from rest_framework import generics
from .models import Polygon
from .serializators import PolygonOwnerSerializator

"""
Request запросы на вывод HTML файлов
"""

def mapView(request):
    """
    Рендерит карту по запросу
    """
    return render(request, 'site_back/map_over_osm.html')

def loginView(request):
    """
    Рендерит виджет логина по запросу
    """
    return render(request, 'site_back/login.html')

def regView(request):
    """
    Рендерит виджет регистрации по запросу
    """
    return render(request, 'site_back/registration.html')

"""
Request запросы на JSON
"""

class UserPolygonsView(generics.ListAPIView):
    """
    Отправляет JSON от сериализатора по запросу 
    """
    serializer_class = PolygonOwnerSerializator
    queryset = Polygon.objects.all()
