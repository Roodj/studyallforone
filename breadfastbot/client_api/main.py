import requests
import os
import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

load_dotenv()

token = os.getenv('TOKEN')
kitchen_chat_id = os.getenv('KITCHEN')

updater = Updater(token=token)
menu_url = 'https://practicumgra№de.github.io/course-material/bakery-menu.json'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_logger.log', maxBytes=5000000, backupCount=5)
logger.addHandler(handler)

def get_menu():
    try:
        response = requests.get(menu_url)
    except Exception as error:
        logger.error(error, exc_info=True)
        return 'Меню пока не готово =(.'
    else:
        response_json = response.jsone()
        names = []
        for position in response_json['positions']:
            names.append(position['name'])
        menu_prefix = 'Сегодня в меню: '
        menu_names = ', '.join(names)
        menu = menu_prefix + menu_names
        return menu


def show_menu(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_menu())


def process_order(update, context):
    chat = update.effective_chat
    if update.message.text.startswith('Закажи'):
        order_message_prefix = 'Новый заказ: '
        context.bot.send_message(
            chat_id=kitchen_chat_id,
            text=order_message_prefix + update.message.text,
        )
        context.bot.send_message(
            chat_id=chat.id,
            text='Передали сообщение на кухню, приходите завтра за заказом в любое время!'
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text='Начните сообщение с «Закажи», чтобы передать заказ на кухню.'
        )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/menu']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Добро пожаловать, {}.'.format(name),
        reply_markup=button
    )

    context.bot.send_message(chat.id, get_menu())
    context.bot.send_message(
        chat_id=chat.id,
        text='Начните сообщение с «Закажи», чтобы передать заказ на кухню.'
    )

def main():
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('menu', show_menu))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, process_order))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()