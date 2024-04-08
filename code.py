import requests
import os
import time
print('Enter city:')
city = input('>>>')
os.system('cls')
print('Finding your city...')
time.sleep(2)
os.system('cls')
print('Finding temperature...')
time.sleep(2)
os.system('cls')
url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url).json()
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
print('Now in city', city, str(temperature), '°C')
print('Feel in city', str(temperature_feels), '°C')
delay = input()
