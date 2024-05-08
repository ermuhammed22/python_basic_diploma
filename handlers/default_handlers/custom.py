import sqlite3

from telebot.types import Message
from loader import bot
from api.api import api   # Импортируем модуль api, где определена функция get_custom_values

# Состояния для запроса аргументов
ARGUMENT_SERVICE, ARGUMENT_RANGE, ARGUMENT_QUANTITY = range(3)

@bot.message_handler(commands=["custom"])
def custom_command(message: Message):
    msg = bot.reply_to(message, "Введите услугу/товар, по которым будет проводиться поиск:")
    bot.register_next_step_handler(msg, process_service_step)

def process_service_step(message: Message):
    try:
        chat_id = message.chat.id
        service = message.text

        msg = bot.reply_to(message, "Введите диапазон значений:")
        bot.register_next_step_handler(msg, process_range_step, service)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

def process_range_step(message: Message, service):
    try:
        chat_id = message.chat.id
        range_values = message.text

        msg = bot.reply_to(message, "Введите количество:")
        bot.register_next_step_handler(msg, process_quantity_step, service, range_values)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

def process_quantity_step(message: Message, service, range_values):
    try:
        chat_id = message.chat.id
        quantity = int(message.text)

        # Вызываем функцию API с передачей пользовательских данных
        data = api.get_custom_values(service, range_values, quantity)
        conn = sqlite3.connect('history.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (user_id, command, arguments) VALUES (?, ?, ?)",
                       (message.from_user.id, "/custom", f"{service}, {quantity}"))
        conn.commit()
        conn.close()

        bot.reply_to(message, str(data))

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")