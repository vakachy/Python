
import time
import requests

# ---------------------------------------------------------------------------
# получение данных о ГОРОДе запросом с OWM

def coordinates_OWM(s_city, appid):
    res = requests.get("https://api.openweathermap.org/geo/1.0/direct?",
                    params={'q': s_city, 'APPID': appid})

    data = res.json() # декодер json модуля requests (исп.,если ответ приходит в виде json)
    latitude = data[0]['lat']
    longitude = data[0]['lon']
    return latitude, longitude
# ---------------------------------------------------------------------------
# получение погоды НА ТЕКУЩИЙ МОМЕНТ запросом с OpenWeatherMap
# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}


def current_weather_OWM(s_city, appid):
    res = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    
    data = res.json()
    time_stamp = time.ctime(data['dt'])
    city_name = data['name']
    temperature = data['main']['temp']
    temperature_feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    return time_stamp, city_name, temperature, \
        temperature_feels_like, humidity, \
            weather_description, wind_speed
# ---------------------------------------------------------------------------
# получение  погоды НА ТЕКУЩИЙ МОМЕНТ запросом с Яндекс


# GET https://api.weather.yandex.ru/v2/forecast?lat=55.75396&lon=37.620393
# X-Yandex-API-Key: 3fc...7

def current_weather_yandex(latitude, longitude):
    url = "https://api.weather.yandex.ru/v2/forecast?"
    params = {'lat': latitude, 'lon': longitude, 'lang': 'ru_RU'}
    headers = {'X-Yandex-API-Key': '2f83147c-cbff-4832-b3ad-e262c3cabbd1'}
    r = requests.get(url, params=params, headers=headers)

    answer = r.json()

    seconds = answer['fact']['obs_time']
    time_stamp = time.ctime(seconds)
    city_name = answer['geo_object']['locality']['name']
    temperature = answer['fact']['temp']
    temperature_feels_like = answer['fact']['feels_like']
    humidity = answer['fact']['humidity']
    weather_description = answer['fact']['condition']
    wind_speed = answer['fact']['wind_speed']
    return time_stamp, city_name, temperature, \
        temperature_feels_like, humidity, \
            weather_description, wind_speed 