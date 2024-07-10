from django.urls import path
from . import views

urlpatterns = [
    path('last_rainfall/<int:latitude>/<int:longitude>/', views.last_rainfall, name='last_rainfall'),
    path('home/', views.home, name='home'),
]
