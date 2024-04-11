from telebot.types import Message

from handlers.default_handlers.low import save_request_to_history
from loader import bot
from handlers import api
import sqlite3

@bot.message_handler(commands=["custom"])
def custom_command(message: Message):
    try:
        args = message.text.split()[1:]
        if len(args) != 4:
            bot.reply_to(message, "Неверное количество аргументов. Используйте команду "
                                  "/custom <услуга/товар> <диапазон> <количество>")
            return
        service = args[0]
        range_values = args[1]
        quantity = int(args[2])

        custom_values = api.get_custom_values(service, range_values, quantity)

        bot.reply_to(message, f"Пользовательские значения для {service} "
                              f"в диапазоне {range_values}: {custom_values}")

        # Сохраняем запрос в историю
        save_request_to_history(message.from_user.id, "/custom",
                                f"{service}, {range_values}, {quantity}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
