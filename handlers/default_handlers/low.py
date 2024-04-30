from telebot.types import Message
from loader import bot

# Состояния для запроса аргументов
ARGUMENT_SERVICE, ARGUMENT_QUANTITY = range(2)

@bot.message_handler(commands=["low"])
def low_command(message: Message):
    msg = bot.reply_to(message, "Введите услугу/товар:")
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

        # Дальнейшая обработка: запрос к API, отправка сообщения с результатом и т.д.

        bot.reply_to(message, f"Вы запросили {quantity} минимальных значений для {service}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
