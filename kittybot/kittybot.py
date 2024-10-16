import os
import logging
from logging.handlers import RotatingFileHandler

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_logger.log', maxBytes=5000000, backupCount=5)
logger.addHandler(handler)

URL = 'https://api.thecatapi.com/v1/images/search'  

def random_kitty_pic():
    try:
        response = requests.get(URL).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = "https://api.thedogapi.com/v1/images/search"
        response = requests.get(new_url).json()

    pic_url = response[0].get("url")
    return pic_url

def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(
        chat.id,
        random_kitty_pic()
    )

def wake_up(update, context):
    chat = update.effective_chat
    name = chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']],resize_keyboard=True)
    
    context.bot.send_message(
        chat_id=chat.id, 
        text=f'Спасибо, что включили меня {name}',
        reply_markup=button
        )
    
    context.bot.send_photo(chat.id,random_kitty_pic())

def main():
    updater = Updater(token=token)
# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
    updater.start_polling()
    updater.idle() 

if __name__ == '__main__':
    main()