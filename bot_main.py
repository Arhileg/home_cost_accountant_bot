import sqlite3
import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def write_id(id):
    conn = sqlite3.Connection('')

bot.polling(none_stop=True, interval=0)