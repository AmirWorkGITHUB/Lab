import telebot
from telebot import types

bot = telebot.TeleBot("Токен")

joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def start(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open('joined.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курсы")
    btn2 = types.KeyboardButton("Адрес")
    btn3 = types.KeyboardButton("Записаться на пробный урок")
    btn4 = types.KeyboardButton("Оставить свой вопрос")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Онлайн консультант IT Академии выбери о чем хочешь узнать".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, more)


@bot.message_handler(commands=['send'])
def mess(message):
    if message.chat.id == 1694197855:
        for user in joinedUsers:
            bot.send_message(user, message.text[message.text.find(' '):])
    else:
        bot.send_message(message.chat.id, text='Вы не админ !')

@bot.message_handler(content_types=['text'])
def more(message):
    if message.text == "Курсы":
        bot.send_message(message.chat.id, text='Для детей 7-12 лет\n'
                                               'Scratch\n'
                                               '-длительность 3 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы игра го и английский язык бесплатно\n'
                                               'PYTHON на Майнкрафт\n'
                                               '-длительность 3 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы игра го и английский язык бесплатно\n'
                                                )
        bot.send_message(message.chat.id, text='Для подростков 12-17 лет\n'
                                               'HTML/CSS\n'
                                               '-длительность 3 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно\n'
                                               'PYTHON\n'
                                               '-длительность 4 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно\n'
                                               'JAVA-SCRIPT\n'
                                               '-длительность 4 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно\n'
                                                )
        bot.send_message(message.chat.id, text='Для подростков 17+ лет\n'
                                               'HTML/CSS\n'
                                               '-длительность 3 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно\n'
                                               'PYTHON\n'
                                               '-длительность 4 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно\n'
                                               'JAVA-SCRIPT\n'
                                               '-длительность 4 месяца\n'
                                               '-цена за один месяц 5000 сом\n'
                                               '-бонусы английский язык бесплатно'
                                                )
        bot.send_message(message.chat.id, text='Если вы хотите получить обширную информацию о курсах пожалуйста оставьте свой вопрос')
    elif message.text == "Адрес":
        bot.send_message(message.chat.id,
                         text='Мы находимся по адресу улица Исанова 105/3 или же https://2gis.kg/bishkek/firm/70000001038163168')
    elif message.text == "Записаться на пробный урок":
        bot.send_message(message.chat.id, text='Что бы записаться отправьте команду /request')
        bot.register_next_step_handler(message, request)

    elif message.text == "Оставить свой вопрос":
        bot.send_message(message.chat.id, text='Что бы записаться отправьте команду /question')
        bot.register_next_step_handler(message, question)

    else:
        bot.send_message(message.chat.id, text='Такой команды не существует')

@bot.message_handler(commands=['request'])
def request(message):
    app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    app_keyboard = types.KeyboardButton(text="Отправить заявку")
    app_markup.add(app_keyboard)
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"{first_name} Следуй инструкциям ниже\n"
                              f"Что бы отправить заявку нажмите кнопку позже мы с вами свяжемся", reply_markup=app_markup)
    bot.register_next_step_handler(message, text_one)

@bot.message_handler(content_types=["text"])
def text_one(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Отправить заявку':
            bot.send_message(chat_id, "Пришлите ваше имя и номер :\n"
                                      "Пример : Шахамир 0706926608 урок по UX/UI дизайну")
            bot.register_next_step_handler(message, send_z)


def send_z(message):
    first_name = message.chat.first_name
    chat_id = message.chat.id
    user_name = message.chat.username
    z = message.text
    admin_id = 1694197855
    app_text = []
    app_name = []
    app_username = []
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(z)
    bot.send_message(admin_id, f"Поступила заявку от {app_name[0]} !\n"
                               f"Его username = @{app_username[0]}\n"
                               f"Его текст :\n"
                               f"{app_text[0]}")


    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, "Заявка отправлена !")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курсы")
    btn2 = types.KeyboardButton("Адрес")
    btn3 = types.KeyboardButton("Записаться на пробный урок")
    btn4 = types.KeyboardButton("Оставить свой вопрос")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Что ещё хотите узнать ?".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['question'])
def question(message):
    app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    app_keyboard = types.KeyboardButton(text="Оставить вопрос")
    app_markup.add(app_keyboard)
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"{first_name} Следуй инструкциям ниже\n"
                              f"Что бы оставить свой вопрос нажмите на кнопку позже мы с вами свяжемся", reply_markup=app_markup)
    bot.register_next_step_handler(message, text_two)

@bot.message_handler(content_types=["text"])
def text_two(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Оставить вопрос':
            bot.send_message(chat_id, "Что вы хотите спросить ? :\n"
                                      "Пример: Что делают на курсах по HTML/CSS ?")
            bot.register_next_step_handler(message, send_q)


def send_q(message):
    first_name = message.chat.first_name
    chat_id = message.chat.id
    user_name = message.chat.username
    z = message.text
    admin_id = 1694197855
    app_text = []
    app_name = []
    app_username = []
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(z)
    bot.send_message(admin_id, f"Пользователь с ником {app_name[0]}!\n"
                               f"Пользователь username = @{app_username[0]}\n"
                               f"Спросил :\n"
                               f"{app_text[0]}")


    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, "Вопрос отправлен !")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курсы")
    btn2 = types.KeyboardButton("Адрес")
    btn3 = types.KeyboardButton("Записаться на пробный урок")
    btn4 = types.KeyboardButton("Оставить свой вопрос")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Что ещё хотите узнать ?".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Наш бот поможет вам разобраться что где и как')

bot.polling(none_stop=True)