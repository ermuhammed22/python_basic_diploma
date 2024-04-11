from telebot.types import Message
from loader import bot
import sqlite3

def get_user_history(user_id):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT command, arguments FROM history WHERE user_id=? ORDER BY id DESC LIMIT 10", (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history

@bot.message_handler(commands=["history"])
def history_command(message: Message):
    try:
        user_id = message.from_user.id
        user_history = get_user_history(user_id)

        if not user_history:
            bot.reply_to(message, "У вас пока нет истории запросов.")
            return

        history_message = "История ваших запросов:\n"
        for idx, (command, arguments) in enumerate(user_history, start=1):
            history_message += f"{idx}. Команда: {command}, Аргументы: {arguments}\n"

        bot.reply_to(message, history_message)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
