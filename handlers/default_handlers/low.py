from telebot.types import Message
from loader import bot
from handlers import api
import sqlite3

def save_request_to_history(user_id, command, arguments):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (user_id, command, arguments) "
                   "VALUES (?, ?, ?)", (user_id, command, arguments))
    conn.commit()
    conn.close()

@bot.message_handler(commands=["low"])
def low_command(message: Message):
    try:
        args = message.text.split()[1:]
        if len(args) != 2:
            bot.reply_to(message, "Неверное количество аргументов. Используйте команду "
                                  "/low <услуга/товар> <количество>")
            return
        service = args[0]
        quantity = int(args[1])

        lowest_values = api.get_lowest_values(service, quantity)

        bot.reply_to(message, f"Самые низкие значения для {service}: {lowest_values}")

        # Сохраняем запрос в историю
        save_request_to_history(message.from_user.id, "/low",
                                f"{service}, {quantity}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
