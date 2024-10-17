# test_last_rainfall.py
import os
import django
import json
from django.test import RequestFactory


# Установите переменную окружения для файла настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango.settings')

# Инициализируйте Django
django.setup()

# Теперь можно импортировать функцию last_rainfall
from world.views import last_rainfall

# Инициализируем RequestFactory и создаем тестовый запрос
factory = RequestFactory()
request = factory.get('/api/last_rainfall/')

# Примерные координаты
latitude = 41.917648315429695
longitude = 45.04356967657023

# Вызов функции
response = last_rainfall(request, latitude, longitude)

# Печать ответа
print(json.loads(response.content))