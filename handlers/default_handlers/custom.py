from telebot.types import Message
from loader import bot

# Состояния для запроса аргументов
ARGUMENT_SERVICE, ARGUMENT_RANGE, ARGUMENT_QUANTITY = range(3)

@bot.message_handler(commands=["custom"])
def custom_command(message: Message):
    msg = bot.reply_to(message, "Введите услугу/товар:")
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

        # Дальнейшая обработка: запрос к API, отправка сообщения с результатом и т.д.

        bot.reply_to(message, f"Вы запросили {quantity} значений в диапазоне {range_values} для {service}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
