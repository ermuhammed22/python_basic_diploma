from telebot.types import Message

from handlers.default_handlers.low import save_request_to_history
from loader import bot
from handlers import api
import sqlite3

@bot.message_handler(commands=["high"])
def high_command(message: Message):
    try:
        args = message.text.split()[1:]
        if len(args) != 2:
            bot.reply_to(message, "Неверное количество аргументов. Используйте команду "
                                  "/high <услуга/товар> <количество>")
            return
        service = args[0]
        quantity = int(args[1])

        highest_values = api.get_highest_values(service, quantity)

        bot.reply_to(message, f"Самые высокие значения для {service}: {highest_values}")

        # Сохраняем запрос в историю
        save_request_to_history(message.from_user.id, "/high", f"{service}, {quantity}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
