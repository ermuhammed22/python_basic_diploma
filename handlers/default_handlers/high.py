from telebot.types import Message
from loader import bot
from api.api import api  # Импортируем модуль api, где определена функция get_weather
from database.database import log_command  # Импортируем функцию log_command

@bot.message_handler(commands=["high"])
def high_command(message: Message):
    msg = bot.reply_to(message, "Введите название города для получения максимальной температуры:")
    bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message: Message):
    try:
        city_name = message.text

        # Вызываем функцию API для получения данных о погоде
        data = api.get_weather(city_name)
        log_command(message.from_user.id, "/high", city_name)

        if data.get("cod") != 200:
            bot.reply_to(message, f"Произошла ошибка: {data.get('message', 'Неизвестная ошибка')}")
            return

        temp_max = data['main']['temp_max']

        response_message = f"Максимальная температура в городе {city_name} сегодня: {temp_max}°C"

        bot.reply_to(message, response_message)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
