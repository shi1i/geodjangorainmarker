from django.shortcuts import render

# Create your views here.
def mapView(request):
    return render(request, 'openlayers-osm.html')