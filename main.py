import telebot
from telebot import types

bot = telebot.TeleBot('6506562881:AAFs4Bku_Fmakmwwk6_U80ghbw5tJ5x9t60')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📜Карты корпусов📜")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, {0.first_name}! Я помогу тебе ориентироваться внутри корпусов МАОУ СОШ №48.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '📜Карты корпусов📜':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('¹Первый корпус¹')
        btn2 = types.KeyboardButton('²Второй корпус²')
        back = types.KeyboardButton('❌Вернуться в главное меню❌')
        markup.add(btn1, btn2, back)
        bot.send_message(message.from_user.id, 'Какой корпус вам нужен?', reply_markup=markup) #ответ бота

    # Карты корпусов: 1 корпус

    elif message.text == '¹Первый корпус¹':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnbuild11 = types.KeyboardButton('₁Первый этаж₁')
        btnbuild12 = types.KeyboardButton('₂Второй этаж₂')
        btnbuild13 = types.KeyboardButton('₃Третий этаж₃')
        back = types.KeyboardButton('❌Вернуться в главное меню❌')
        markup.add(btnbuild11, btnbuild12, btnbuild13, back)
        bot.send_message(message.chat.id, text='Какой этаж вам нужен?', reply_markup=markup)

    elif message.text == '₁Первый этаж₁':
        bot.send_message(message.chat.id, text='Карта данного этажа ещё в разработке')

    elif message.text == '₂Второй этаж₂':
        bot.send_message(message.chat.id, text='Карта данного этажа ещё в разработке')

    elif message.text == '₃Третий этаж₃':
        bot.send_message(message.chat.id, text='Карта данного этажа ещё в разработке')

    # карты корпусов: 2 корпус

    elif message.text == '²Второй корпус²':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnbuild21 = types.KeyboardButton('₁Первый этaж₁')
        btnbuild22 = types.KeyboardButton('₂Второй этaж₂')
        btnbuild23 = types.KeyboardButton('₃Третий этaж₃')
        back = types.KeyboardButton('❌Вернуться в главное меню❌')
        markup.add(btnbuild21, btnbuild22, btnbuild23, back)
        bot.send_message(message.chat.id, text='Какой этаж вам нужен?', reply_markup=markup)

    elif message.text == '₁Первый этaж₁':
            bot.send_message(message.chat.id, text='Карта данного этажа ещё в разработке')

    elif message.text == '₂Второй этaж₂':
        bot.send_photo(message.chat.id, photo=open('Second floor.jpg', 'rb'))

    elif message.text == '₃Третий этaж₃':
        bot.send_photo(message.chat.id, photo=open('Third floor.jpg', 'rb'))

    elif message.text == '❌Вернуться в главное меню❌':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📜Карты корпусов📜')
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

bot.polling(none_stop=True, interval=0)

"""новая ветка разработки"""