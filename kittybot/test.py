import requests
from bs4 import BeautifulSoup
import time
import logging
from telegram import Bot

# Настройки Telegram
bot_token = '7383082964:AAHVo1EAhwKPZmYMMpyLYb9EEianZniPHow'
chat_id = '398298944'
bot = Bot(token=bot_token)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    filename='parsetest.txt'
)

# Установи свои параметры
max_price = 800  # Максимальная цена в евро
url = 'https://www.immowelt.de/classified-search?distributionTypes=Rent&estateTypes=House,Apartment&locations=AD08DE6863&priceMax=800'  # URL для поиска квартир в Landshut

def check_apartments():
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Здесь указывай правильный класс для элементов квартиры
    apartments = soup.find_all('div', class_='class-of-apartment-listing')  # Обнови этот класс
    print(apartments)
    for apartment in apartments:
        print(apartments)
        print(apartment)
        price_text = apartment.find('span', class_='class-of-price').text  # Обнови этот класс
        print(price_text)
        price = extract_price(price_text)
        print(price)
        if price <= max_price:
            send_message(apartment)

def extract_price(price_text):
    # Убрать символы и преобразовать в число
    price = int(price_text.replace('€', '').replace('.', '').strip())
    return price

def send_message(apartment):
    # Получаем название и ссылку на квартиру
    title = apartment.find('h2').text.strip()  # Обнови этот класс
    link = apartment.find('a')['href']  # Обнови этот класс
    
    message = f'Новая квартира: {title}\nСсылка: {link}'
    bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    while True:
        check_apartments()
        time.sleep(60)  # Проверять раз в час