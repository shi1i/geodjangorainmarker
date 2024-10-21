
# УРЛЫ ПРИЛОЖУХИ

from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.MapView.as_view()),
    path('sign-in/', views.RegistrationView.as_view(), name="sign-in")
]
