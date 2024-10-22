import rest_framework.permissions as rp
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import generics, status
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework.response import Response
from .models import Polygon
from .serializators import PolygonOwnerSerializator, UserRegistrationSerializator, UserLoginSerializator


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
            return render(request, "site_back/map_over_osm.html", context={'auth_check': False})
            #return Response(user.username)
        else:
            """
            Возвращаем дату из сериализатора
            """
            # // TO
            

            # DO //
            return render(request, "site_back/map_over_osm.html", context={'auth_check': True})
            #return Response(user.username)
        
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
            return redirect(reverse('map'))
        
            # return Response(template_name="site_back/map_over_osm.html")
        
        # // TO
        # Добавить перенаправление на 404, или сообщение о ошибках.
        # DO //
        return redirect(reverse('map'))
    
        # return Response(template_name="site_back/map_over_osm.html")


class LoginView(APIView):
    """
    Функция логина в аккаунт
    """ 
    permission_classes = [rp.AllowAny]

    def post(self, request):
        loginData = UserLoginSerializator(data=request.data)
        loginData.is_valid()
        username = loginData.data.get('username')
        password = loginData.data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('map'))
  
    
"""
Request запросы на JSON
"""

class UserPolygonsView(generics.ListAPIView):
    """
    Отправляет JSON от сериализатора по запросу 
    """
    serializer_class = PolygonOwnerSerializator
    queryset = Polygon.objects.all()

"""
Функции КОпатыча
"""
def logoutView(request):
    logout(request)
    return redirect(reverse('map'))

