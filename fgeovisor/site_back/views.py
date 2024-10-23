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
            #context={'auth_check': True,
                     #'is_staff': user.is_staff}
            
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
        else: 
            # // TO
            # Добавить перенаправление на 404, или сообщение о ошибках.
            # DO //
            return Response({"Ошибка": "Неверные данные или пользователь уже существует"})
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)   
        return redirect(reverse('map'))

class LoginView(APIView):
    """
    Функция логина в аккаунт
    """ 
    permission_classes = [rp.AllowAny]

    def post(self, request):
        # Распакоука данных из сериализатора POST сессии
        loginData = UserLoginSerializator(data=request.data)
        loginData.is_valid()

        username = loginData.data.get('username')
        password = loginData.data.get('password')
        user = authenticate(username=username, password=password)
        try: 
            login(request, user)
            return redirect(reverse('map'))
        except AttributeError:
            return Response({'AttributeError': "неверный логин или пароль"})
  
    
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
