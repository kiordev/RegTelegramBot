# Testing Regestration Bot by Python Telebot
# Creator: kiordev@gmail.com | with youtuber "Фсоки"
# Date: 17 APRIL 2022

# imports:
import telebot
from telebot import types
import Configuration

# bot initialisation
client = telebot.TeleBot(Configuration.config['token'])


# Main Code:
@client.message_handler(commands=['start'])
def start_message(message):
    client.send_message(message.chat.id, "Menu: /info - информация про вас")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Info"))
    msg = client.send_message(message.chat.id, "Выберите пункт", reply_markup=keyboard)
    client.register_next_step_handler(msg, main_work)

def main_work (message):
    if message.text == "Info":
        client.send_message(message.chat.id, "<b>Информация про вас:</b> ", parse_mode='html')
        client.send_message(message.chat.id, f" Имя: {message.from_user.first_name}, Фамилия: {message.from_user.last_name}")
    else:
        client.send_message(message.chat.id, "Иди нахуй")


client.enable_save_next_step_handlers(delay=2)
client.load_next_step_handlers()
client.infinity_polling()