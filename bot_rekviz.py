import telebot
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

🇧🇾 Если вы не знаете, как оплатить участие из РБ, напишите в Direct "БЕЛАРУСЬ", вышлем информацию по способам оплаты.

СКРИН чека об оплате просьба прислать в Direct организаторам✅.

https://www.instagram.com/lashtrainer_marafon/
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == 'Показать IBAN':
        bot.send_message(message.chat.id, "🇪🇺 Для оплаты в евро:\n\nIBAN: LT12 3250 0640 8072 8643\nБанк: REVOLUT\nПолучатель: Anna Zorina")
    elif message.text == 'Беларусь':
        bot.send_message(message.chat.id, "🇧🇾 Для оплаты из Республики Беларусь:\n\nТерминалы \"Qiwi\" ➡️ выбираете \"Переводы\" ➡️ \"Перевод на карту\"\nтам же будут перечислены банки РФ.\nВыбираете нужный банк➡️ оплачиваете.")

# The bot will keep running and listening to incoming messages
while True:
    try:
        bot.polling(none_stop=True)
    except telebot.apihelper.ApiException:
        time.sleep(15)