from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from api.api import api  # Импортируем api из пакета api

if __name__ == "__main__":
    set_default_commands(bot)
    handlers.api = api
    bot.infinity_polling()
