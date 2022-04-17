# TelegramBotAPI Summary File
# Creator: kiordev@gmail.com
# Date: 16 APRIL

# TelegramBot API for Python "https://pypi.org/project/pyTelegramBotAPI/#methods"

# === Bot Globals ===
# bot.polling(none_stop=True)  - для постоянной работы бота, писать в конец кода

# === Message Methods ===
# bot.send_message(message.chat.id, *сообщение*, parse_mode='html') - метод для вывода сообщения после команды
# bot.send_message(message.chat.id, message, parse_mode='html') - вывод всех параметров для обращения

# ...Фотография...
# photo = open('Блокнот.png', 'rb') - открытие файла в проекте перед работой (rb - формат)
# bot.send_photo(message.chat.id, photo) - отправка этого файла

# ...Декораторы...
# @bot.message_handler(commands=['*команда*']) - декоратор перед методом, который работает с командой
# @bot.message_handler (ничего) - просто декоратор для обработки текста пользователя

# === Button work ===
# ...Кнопки внутри сообщения...
# markup_inline = types.InlineKeyboardMarkup() - Создание "панели с кнопкам"
# item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') - Создание самой кнопки, text - текст на кнопке
# markup_inline.add(item_yes) - добавление кнопки на клавиатуру
# bot.send_message(message.chat.id, "Информация", reply_markup=markup_inline) - прикрепение клавиатуры к сообщению
# bot.callback_query_handler(func=lambda call: True) - декоратор при работы с использованием кнопок

# ...Кнопки за сообщением
# Специфика кнопок заключается в том, что они вводят прописанные им текст  - МОЙ ИД, МОЙ НИК - как текст пользователя
# markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True) Создание "панели с кнопкам" (под инпутом)
# item_id = types.KeyboardButton('МОЙ ID') - создание самой кнопки
# markup_reply.add(item_id)

# === Work With User ===
# message.from_user.first_name - обращение к имени
# message.from_user.last_name - обращение к фамилии
# список параметров можно найти через bot.send_message(message.chat.id, message, parse_mode='html')
# @bot.message_handler(content_types=["photo"]) - декоратор для работы с файлами приёма пользователем