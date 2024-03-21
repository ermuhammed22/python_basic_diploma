import telebot


token = "7110090587:AAHlTBPP8-4mKgKp51c-1_H11yb11Jur380"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет")


bot.infinity_polling()