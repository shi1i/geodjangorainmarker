from django.shortcuts import render
from rest_framework import generics
from .models import Polygon
from .serializators import PolygonOwnerSerializator


def mapView(request):
    """
    Рендерит карту по запросу
    """
    return render(request, 'site_back/map_over_osm.html')

def loginView(request):
    return render(request, 'site_back/login.html')

def regView(request):
    return render(request, 'site_back/registration.html')


class UserPolygonsView(generics.ListAPIView):
    """
    Отправляет JSON от сериализатора по запросу 
    """
    serializer_class = PolygonOwnerSerializator
    queryset = Polygon.objects.all()
