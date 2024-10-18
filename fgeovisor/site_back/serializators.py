from rest_framework import serializers
from .models import Polygon, Image, SessionStorage, ActivityLog
from django.contrib.auth.models import User


###### Тут храним сериализаторы данных из quaryset моделей, который в БД у нас
###### Сериализаторы делают каткаткат и выдают нам красивые гейсоны
###### Эти json мы будем использовать во вьюхах, переадресовывая все в fetch на форнте ммм сладко

# Получает queryset из модели Polygon

class PolygonSerializator(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        fields = '__all__'

# Получает queryset из модели Image

class ImageSerializator(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


# Нерабочая хуйня

class UserSerializator(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["login_username"]

#### Основной сериализатор с связми User + полигон + изображение

class PolygonOwnerSerializator(serializers.ModelSerializer):

    # 
    Images = ImageSerializator(many=True, read_only=True, source='images')
    
    # Обращается в модель Polygon к записи Login и оттуда берет через связь username
    login_username = serializers.ReadOnlyField(source="login.username")

    class Meta:
        model = Polygon
        fields = ['login', 'login_username', 'polygon_id', 'polygon_data', 'Images', 'created_at', 'updated_at']