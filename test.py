import telebot
from telebot import types
import Configuration

# bot initialisation
client = telebot.TeleBot(Configuration.config['token'])


@client.message_handler(commands=['help', 'start'])

def send_welcome(message):
    msg = client.send_message(message.chat.id, """\
Hi there, I am Example bot.
What's your name?
""")
    client.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    client.send_message(message.chat.id, "Working")



client.enable_save_next_step_handlers(delay=2)
client.load_next_step_handlers()
client.infinity_polling()
