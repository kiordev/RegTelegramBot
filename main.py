# Testing Regestration Bot by Python Telebot
# Creator: kiordev@gmail.com | with youtuber "Фсоки"
# Date: 17 APRIL 2022

# imports:
import telebot
import Configuration

# bot initialisation
client = telebot.TeleBot(Configuration.config['token'])


# Main Code:
# command start message:
@client.message_handler(commands=['start'])
def bot_start (message):
    client.send_message(message.chat.id, "<b>Начало работы</b>", parse_mode='html')





# Telegram Bot works void
client.polling(none_stop=True, interval=1)