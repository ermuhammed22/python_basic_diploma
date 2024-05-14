from telebot.types import Message
from loader import bot
from database.database import get_user_history, log_command, create_history_table  # Импортируем функцию log_command

# Запускаем функцию создания таблицы перед использованием
create_history_table()

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

    # Ответил на команду, добавляем запись в историю
    log_command(user_id, "history")
