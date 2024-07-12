appid = "2da675754b21b4495b04716c4ca5319f"

import requests

# def get_wind_direction(deg):
#     l = ['С ','СВ',' В','ЮВ','Ю ','ЮЗ',' З','СЗ']
#     for i in range(0,8):
#         step = 45.
#         min = i*step - 45/2.
#         max = i*step + 45/2.
#         if i == 0 and deg > 360-45/2.:
#             deg = deg - 360
#         if deg >= min and deg <= max:
#             res = l[i]
#             break
#     return res

# # Проверка наличия в базе информации о нужном населенном пункте
# def get_city_id(s_city_name):
#     try:
#         res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                      params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#         data = res.json()
#         cities = ["{} ({})".format(d['name'], d['sys']['country'])
#                   for d in data['list']]
#         print("city:", cities)
#         city_id = data['list'][0]['id']
#         print('city_id=', city_id)
#     except Exception as e:
#         print("Exception (find):", e)
#         pass
#     assert isinstance(city_id, int)
#     return city_id

# # Запрос текущей погоды по координатам
# #https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# def request_current_weather_c(lat,lon):
#     try:
#         res = requests.get("http://api.openweathermap.org/data/2.5/weather",
#                      params={'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#         data = res.json()
#         print("conditions:", data['weather'][0]['description'])
#         print("temp:", data['main']['temp'])
#         print("temp_min:", data['main']['temp_min'])
#         print("temp_max:", data['main']['temp_max'])
#         print("data:", data)  
#     except Exception as e:
#         print("Exception (weather):", e)
#         pass


# # Запрос текущей погоды
# def request_current_weather(city_id):
#     try:
#         res = requests.get("http://api.openweathermap.org/data/2.5/weather",
#                      params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#         data = res.json()
#         print("conditions:", data['weather'][0]['description'])
#         print("temp:", data['main']['temp'])
#         print("temp_min:", data['main']['temp_min'])
#         print("temp_max:", data['main']['temp_max'])
#         print("data:", data)
#     except Exception as e:
#         print("Exception (weather):", e)
#         pass

# # Прогноз
# def request_forecast(city_id):
#     try:
#         res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
#                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#         data = res.json()
#         print('city:', data['city']['name'], data['city']['country'])
#         for i in data['list']:
#             print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
#                    '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
#                    get_wind_direction(i['wind']['deg']),
#                    i['weather'][0]['description'] )
#     except Exception as e:
#         print("Exception (forecast):", e)
#         pass

# #city_id for SPb
# city_id = 519690

# import sys
# if len(sys.argv) == 2:
#     s_city_name = sys.argv[1]
#     print("city:", s_city_name)
#     city_id = get_city_id(s_city_name)
# elif len(sys.argv) > 2:
#     print('Enter name of city as one argument. For example: Petersburg,RU')
#     sys.exit()

# #request_forecast(city_id)
# #request_current_weather(city_id)
# lat = 45.298012
# lon = 41.490128
# request_current_weather_c(lat, lon)

from datetime import datetime, timedelta

def get_last_rain_date(lat, lon):
    try:
        # Получаем текущую дату
        current_date = datetime.now().date()

        # Устанавливаем временной интервал для получения данных (например, 7 дней назад)
        start_date = current_date - timedelta(days=7)
        
        last_rain_date = None

        # Проверяем погоду за каждый день в указанном диапазоне
        for days_ago in range(7):
            date_to_check = start_date + timedelta(days=days_ago)
            date_str = date_to_check.strftime('%Y-%m-%d')

            url = f"https://api.openweathermap.org/data/3.0/day_summary?"
            params = {
                'lat': lat,
                'lon': lon,
                'date': date_str,
                'appid': appid
            }

            response = requests.get(url, params=params)
            response.raise_for_status()  # Проверка успешности запроса

            data = response.json()

            if "precipitation" in data and data["precipitation"]["total"] > 0:
                last_rain_date = date_to_check

        if last_rain_date:
            days_since_rain = (current_date - last_rain_date).days
            print(f"Прошло {days_since_rain} дней с последнего дождя, который был {last_rain_date}")
        else:
            print("Дождя не было в течение последней недели.")

    except requests.exceptions.RequestException as e:
        print("Exception (last rain request):", e)
    except Exception as e:
        print("Exception:", e)
    
# Пример использования функции
lat = 45.03098439438117  # Широта Ставрополя
lon = 41.93773269653321  # Долгота Ставрополя

get_last_rain_date(lat, lon)

# Это функция не работает, потому что оказывается база данных из сервиса стоит денег) Поэтому придется вручную наспамить данных чут-чут