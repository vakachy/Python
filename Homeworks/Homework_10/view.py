
def show_weather(provider, time, city_name, temperature, \
        temperature_feels_like, humidity, \
            weather_description, wind_speed):

    return f"{'='*30}\nПо данным {provider}\n{'='*30}\nПо состоянию на: {time}\n\
Город: {city_name}\nТемпература: {round(temperature,0)} гр. Цельсия\n\
Ощущается как: {round(temperature_feels_like,0)} гр. Цельсия\n\
Влажность: {humidity}%\nСейчас: {weather_description}\nВетер: {wind_speed} м/с\n"
