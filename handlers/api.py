import requests
from config_data.config import RAPID_API_KEY

class ExternalAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_lowest_values(self, service, quantity):
        url = "https://www.wildberries.ru"
        params = {
            "service": service,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_highest_values(self, service, quantity):
        url = "https://www.wildberries.ru"
        params = {
            "service": service,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_custom_values(self, service, range_values, quantity):
        url = "https://www.wildberries.ru"
        params = {
            "service": service,
            "range_values": range_values,
            "quantity": quantity,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data

api = ExternalAPI(RAPID_API_KEY)
