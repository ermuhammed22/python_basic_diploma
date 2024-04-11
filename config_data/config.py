import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ('start', 'Начать работу с ботом'),
    ('help', 'Получить помощь'),
    ('low', 'Получить минимальные значения'),
    ('high', 'Получить максимальные значения'),
    ('custom', 'Получить значения по пользовательскому диапазону'),
    ('history', 'Получить историю запросов'),
)
