import requests
from config_data.config import RAPID_API_KEY

class ExternalAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city_name):
        url = "http://api.openweathermap.org/data/2.5/weather"
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "api.openweathermap.org"
        }
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data

# Использование вашего ключа OpenWeatherMap API
api = ExternalAPI(RAPID_API_KEY)
