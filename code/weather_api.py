import requests
import os

api_key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': api_key}
url = 'https://api.openweathermap.org/data/2.5/weather' 
data = requests.get(url, params=query).json()
weather_descr = data['weather'][0]['description']
temp_f = data['main']['temp']

print(f'The weather is: {weather_descr}, and the temp is: {temp_f}F')