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
def bot_start(message):
    msg = client.send_message(message.chat.id, "Начало работы")
    client.register_next_step_handler(msg, application)

def application(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание клавиатуры
    rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("No"))  # Создание двух кнопок
    msg = client.reply_to(message, "Желаете подать заявку на модератора?", reply_markup=rmk)  # Добавление клавиатуры
    client.register_next_step_handler(msg, user_answer)  # Переводчик на следующий шаг в функцию user_answer


def user_answer(message):
    if message.text == "Да":
        msg = client.reply_to(message, "Впишите ваши данные: ")
        client.register_next_step_handler(msg, user_reg)
    elif message.text == "Нет":
        client.message_handler(message.chat.id, "Ну и пока!")
    else:
        client.message_handler(message.chat.id, "Прочитай, что ты ввел")


def user_reg(message):
    client.send_message(message.chat.id, f"Your date: {message.text}")


# Telegram Bot works void
client.enable_save_next_step_handlers(delay=2)
client.infinity_polling()
