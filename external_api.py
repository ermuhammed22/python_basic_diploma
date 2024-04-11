import requests
from config_data.config import RAPID_API_KEY

class ExternalAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_lowest_values(self, service, quantity):
        # Пример запроса к API для получения самых низких значений
        url = "https://yandex.ru/dev/dictionary"
        params = {
            "service": service,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_highest_values(self, service, quantity):
        # Пример запроса к API для получения самых высоких значений
        url = "https://yandex.ru/dev/dictionary"
        params = {
            "service": service,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_custom_values(self, service, range_values, quantity):
        # Пример запроса к API для получения значений по пользовательскому диапазону
        url = "https://yandex.ru/dev/dictionary"
        params = {
            "service": service,
            "range_values": range_values,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    # Другие методы для работы с API

# Создание экземпляра класса для работы с API с использованием ключа API
api = ExternalAPI(RAPID_API_KEY)
