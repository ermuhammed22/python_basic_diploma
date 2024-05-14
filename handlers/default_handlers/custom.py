import sqlite3
from telebot.types import Message
from loader import bot
from api.api import api  # Импортируем модуль api, где определена функция get_weather


@bot.message_handler(commands=["custom"])
def custom_command(message: Message):
    msg = bot.reply_to(message, "Введите название города для получения полной информации о погоде:")
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message: Message):
    try:
        city_name = message.text

        # Вызываем функцию API для получения данных о погоде
        data = api.get_weather(city_name)
        conn = sqlite3.connect('history.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (user_id, command, arguments) VALUES (?, ?, ?)",
                       (message.from_user.id, "/custom", city_name))
        conn.commit()
        conn.close()

        if data.get("cod") != 200:
            bot.reply_to(message, f"Произошла ошибка: {data.get('message', 'Неизвестная ошибка')}")
            return

        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        response_message = (f"Погода в городе {city_name} сегодня:\n"
                            f"Описание: {weather_description}\n"
                            f"Температура сейчас: {temp}°C (Ощущается как {feels_like}°C)\n"
                            f"Минимальная температура: {temp_min}°C\n"
                            f"Максимальная температура: {temp_max}°C\n"
                            f"Влажность: {humidity}%\n"
                            f"Скорость ветра: {wind_speed} м/с")

        bot.reply_to(message, response_message)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
