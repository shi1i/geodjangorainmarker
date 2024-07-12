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
request = factory.get('/api/last_rainfall/41.50461563024414/44.9626747549759/')

# Примерные координаты
latitude = 41.50461563024414
longitude = 44.9626747549759

# Вызов функции
response = last_rainfall(request, latitude, longitude)

# Печать ответа
print(json.loads(response.content))