"""
URL configuration for visor_bend_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# ГЛАВНЫЙ

from django.contrib import admin
from django.urls import path, include
import site_back.views as views


urlpatterns = [
    path('secretadmin/', admin.site.urls, name="admin"),
    path('', include('site_back.urls'), name="api"),
    path('api/users/', views.UserPolygonsView.as_view(), name="users")
]
