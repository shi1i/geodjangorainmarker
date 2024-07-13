from django.urls import path
from . import views

# Основная проблема была в том, что параметрам нельзя присваивать свойство float, т.к оно вообще отсутствует, я пробовал int
# Но оказывается ему без разницы, принимая что то там.021504921051 он преобразует его в int ввиде ЧТОТОТАМ.0150250151 (ДА С ТОЧКОЙ!!!)
urlpatterns = [
    path('last_rainfall/<latitude>/<longitude>/', views.last_rainfall, name='last_rainfall'),
    path('home/', views.home, name='home'),
]
