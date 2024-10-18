from django.shortcuts import render
from .serializators import PolygonOwnerSerializator
from rest_framework import generics
from .models import Polygon

#
# Рендерит карту по запросу
#

def mapView(request):
    return render(request, 'site_back/map_over_osm.html')


#
#### Отправляет JSON от сериализатора по запросу 
#

class UserPolygonsView(generics.ListAPIView):
    serializer_class = PolygonOwnerSerializator
    queryset = Polygon.objects.all()
