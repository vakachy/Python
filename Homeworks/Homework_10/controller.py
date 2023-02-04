
import model
import view

def get_weather():
    s_city = "Brest,BY"
    appid = "bca5f66e12f45632cf19400f0281222a" # токен (бесплатный)
    latitude, longitude = model.coordinates_OWM(s_city, appid)
    params_1 = model.current_weather_yandex(latitude, longitude)
    params_2 = model.current_weather_OWM(s_city, appid)
    return view.show_weather('OpenWeatherMap', *params_2),view.show_weather('Yandex', *params_1)
