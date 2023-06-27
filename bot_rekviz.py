import telebot
from telebot import types
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_KEY')  # Replace with your Telegram Bot API token

bot = telebot.TeleBot(API_TOKEN)

start_message = """
Добрый день👋🏻

Благодарим за регистрацию! Что нужно сделать сейчас?

1) Подпишись на нашу страницу в Instagram
https://www.instagram.com/lashtrainer_marafon/

2) Оплатить регистрационный взнос:

СБЕРБАНК 5469 7700 1521 6071 (Александрова Наталия А.)

ТИНЬКОФФ 2200 7007 9399 6793

Для оплаты взноса из ЕС 🇪🇺 напишите в Direct "IBAN", вышлем реквизиты отдельно.

🇧🇾 Если вы не знаете, как оплатить участие из РБ, напишите в Direct " БЕЛАРУСЬ" вышлем информацию по способам оплаты.

СКРИН чека об оплате просьба прислать в Direct организаторам✅.

https://www.instagram.com/lashtrainer_marafon/
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='НАЧАТЬ', callback_data='begin'))
    bot.send_message(message.chat.id, "Привет! Здесь я расскажу тебе, как оплатить участие в первом международном online- проекте для LASH- тренеров.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'begin')
def begin_callback(call):
    bot.send_message(call.message.chat.id, start_message)

# The bot will keep running and listening to incoming messages
while True:
    try:
        bot.polling(none_stop=True)

    # If the bot loses connection, it will try to reconnect
    except telebot.apihelper.ApiException:
        time.sleep(15)