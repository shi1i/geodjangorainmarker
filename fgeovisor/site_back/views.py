import rest_framework.permissions as rp
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Polygon
from .serializators import PolygonOwnerSerializator, UserRegistrationSerializator


"""
Request запросы на вывод HTML файлов
"""

class MapView(APIView):
    """
    Рендерит карту по запросу и проверяет авторизован пользователь или нет
    """
    permission_classes = [rp.IsAuthenticatedOrReadOnly]

    # ТУТА ПРОВЕРКА ГУТ ГУТ
    def get(self, request):
        user = self.request.user
        if user.username == AnonymousUser.username:
            """
            Просто возвращаем карту 
            """
            return render(request, "site_back/map_over_osm.html")
        else:
            """
            Возвращаем дату из сериализатора
            """
            # // TO
            # DO //
            return render(request, "site_back/map_over_osm.html")
        
class RegistrationView(APIView):
    """
    Функция регистрации аккаунта с простейшей валидацией на стороне сервера
    """
    permission_classes = [rp.AllowAny]

    def post(self, request):
        # Распакоука данных из сериализатора POST сессии
        registrationData = UserRegistrationSerializator(data=request.data)
        if registrationData.is_valid():
            # Сохранение в БД
            registrationData.save()
            # Перенаправление на основную страницу
            return redirect("/api/map/")
        
            # return Response(template_name="site_back/map_over_osm.html")
        
        # // TO
        # Добавить перенаправление на 404, или сообщение о ошибках.
        # DO //
        return redirect("/api/map/")
    
        # return Response(template_name="site_back/map_over_osm.html")


"""
Request запросы на JSON
"""

class UserPolygonsView(generics.ListAPIView):
    """
    Отправляет JSON от сериализатора по запросу 
    """
    serializer_class = PolygonOwnerSerializator
    queryset = Polygon.objects.all()


