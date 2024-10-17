from django.shortcuts import render


def mapView(request):
    return render(request, 'site_back/map_over_osm.html')