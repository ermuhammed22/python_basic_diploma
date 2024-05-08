import sqlite3

from telebot.types import Message
from loader import bot
from api.api import api   # Импортируем модуль api, где определена функция get_highest_values

# Состояния для запроса аргументов
ARGUMENT_SERVICE, ARGUMENT_QUANTITY = range(2)

@bot.message_handler(commands=["high"])
def high_command(message: Message):
    msg = bot.reply_to(message, "Введите услугу/товар, по которым будет проводиться поиск:")
    bot.register_next_step_handler(msg, process_service_step)

def process_service_step(message: Message):
    try:
        chat_id = message.chat.id
        service = message.text

        msg = bot.reply_to(message, "Введите количество:")
        bot.register_next_step_handler(msg, process_quantity_step, service)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

def process_quantity_step(message: Message, service):
    try:
        chat_id = message.chat.id
        quantity = int(message.text)

        # Вызываем функцию API с передачей пользовательских данных
        data = api.get_highest_values(service, quantity)
        conn = sqlite3.connect('history.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (user_id, command, arguments) VALUES (?, ?, ?)",
                       (message.from_user.id, "/high", f"{service}, {quantity}"))
        conn.commit()
        conn.close()

        bot.reply_to(message, str(data))

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
