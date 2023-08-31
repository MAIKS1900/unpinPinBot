import os

import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])


def unpin_message(message: telebot.types.Message):
    bot.unpin_chat_message(message.chat.id, message.id)


@bot.message_handler(func=lambda message: True, content_types=telebot.util.content_type_media)
def message_all_type(message: telebot.types.Message):
    if message.from_user.id == 777000:
        unpin_message(message)


if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except KeyboardInterrupt:
            break
