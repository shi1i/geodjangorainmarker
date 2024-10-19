
# УРЛЫ ПРИЛОЖУХИ

from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.mapView),
    path('map/login/',views.loginView),
    path('map/registration/',views.regView)
]
