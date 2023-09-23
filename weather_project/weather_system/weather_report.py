import autocorrect
from requests import get
import time as Time

class weather_report:
    
    def weather_by_city(city: str):
        spell = autocorrect.Speller()
        city = spell(city)
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = get(url).json()
        if weather_data['cod'] == 200:
            return [city, weather_data]
        elif weather_data['cod'] == 404:
            print('city not found!')
            return False
    
    def weather_output(user):
        city = input("Enter your city:\n")
        report = weather_report.weather_by_city(city)
        if report:
            time = list(Time.gmtime())
            time = f'{time[3]}:{time[4]}:{time[5]}'
            city = report[0]
            weather = report[1]['weather'][0]['main']
            temperature = round(report[1]['main']['temp'], 1)
            delta = round(abs((report[1]['main']['temp_max'] + report[1]['main']['temp_min'] - 2 * temperature) / 2), 1)
            feels_like = round(report[1]['main']['feels_like'], 1)
            pressure = report[1]['main']['pressure']
            wind = round(report[1]['wind']['speed'], 1)
            print(f'''
                    time: {time}
                    city: {city}
                    weather: {weather}
                    temperature: {temperature} °C
                    delta: +-{delta} °C
                    feels like: {feels_like} °C
                    pressure: {pressure} 
                    wind: {wind} m/s
                    ''')
            with open(f'{user.login} history.txt', 'a') as file:
                file.write(f'''{time}
{city}
{weather}
{temperature}
{delta}
{feels_like}
{pressure}
{wind}\n
''')