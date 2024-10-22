
# УРЛЫ ПРИЛОЖУХИ

from django.urls import path
from . import views

urlpatterns = [
    path('', views.MapView.as_view(), name="map"),
    path('sign-in/', views.RegistrationView.as_view(), name="sign-in"),
    path('log-in/', views.LoginView.as_view(), name='log-in'),
    path('log-out/', views.logoutView, name='log-out'),
    #path('save_polygon/',views.save_polygon,name='save_polygon'),
]
