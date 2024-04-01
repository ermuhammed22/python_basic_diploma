import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("7110090587:AAHlTBPP8-4mKgKp51c-1_H11yb11Jur380")
RAPID_API_KEY = os.getenv("dict.1.1.20240321T090041Z.519173ee60c3f4cf.b43ee96f7a8f34a004a676af50a9f778ceb1f1e8")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("hello world", "Привет, я-бот. Чем могу помочь?")
)
