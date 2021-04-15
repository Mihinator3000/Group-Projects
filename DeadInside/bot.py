import telebot
import config
import user_table
import film_table


bot = telebot.AsyncTeleBot(config.API_TOKEN)
#  todo admin panel


@bot.message_handler(commands=["start"])
def welcome_user(message):
    user_data = user_table.UserTable('database.db')
    markup_inline = telebot.types.InlineKeyboardMarkup(row_width=1)
    #  todo replace with employer chat id
    subscribe = telebot.types.InlineKeyboardButton(text="Подписаться на канал",
                                                   url="t.me/joinchat/zEmgN-Vc3sMwN2Iy")
    markup_inline.add(subscribe)
    cont_watching = telebot.types.InlineKeyboardButton(text="Продолжить просмотр", callback_data="check_followed")
    markup_inline.add(cont_watching)
    if message.from_user.first_name is None:
        bot.send_message(message.chat.id, "Добро пожаловать, {0.last_name}!".
                         format(message.from_user), reply_markup=markup_inline)
    elif message.from_user.last_name is None:
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!".
                         format(message.from_user), reply_markup=markup_inline)
    else:
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name} {0.last_name}!".
                         format(message.from_user, message.from_user), reply_markup=markup_inline)

    user_data.add_person(message.from_user.id)
    user_data.close()


@bot.callback_query_handler(func=lambda call: True)
def work(call):
    if call.data == "check_followed":
        if bot.get_chat_member(config.CHAT_ID, call.message.chat.id).wait().status in config.STATUS_FOLLOWED:
            bot.delete_message(call.message.chat.id, call.message.id)
            markup_reply = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            search_button = telebot.types.KeyboardButton("Поиск")
            list_button = telebot.types.KeyboardButton("Список сериалов")
            user_data = user_table.UserTable('database.db')
            markup_reply.add(search_button, list_button)
            if user_data.get_admin(call.message.chat.id):
                adm_panel = telebot.types.KeyboardButton("Включить панель администратора")
                markup_reply.add(adm_panel)
            bot.send_message(call.message.chat.id, text="Вы успешно подписались на канал, приятного просмотра!\n"
                                                        "Напишите название сериала, который вы ищете, "
                                                        "или воспользуйтесь кнопками ниже!",
                             reply_markup=markup_reply)
        else:
            bot.answer_callback_query(callback_query_id=call.id,
                                      text='Вы не подписаны на канал! Сделайте это немедленно!')


@bot.message_handler(content_types=["text"])
def reply_to_request(message):
    if message.text == "Поиск":
        bot.send_message(message.chat.id, text="🔎 Просто отправьте боту название сериала.")
    #  todo fkn list of series by deleting message
    elif message.text == "Список сериалов":
        bot.send_message(message.chat.id, text="🔎Ниже представлен список сериалов отсортированных по названию ("
                                               "алфавиту).\n\nКакой хотите посмотреть сериал?")
    else:
        film_data = film_table.FilmTable('film_database.db')
        try:
            film_id = film_data.find_film(message.text)[3]
            bot.send_video(message.chat.id, film_id, timeout=1000, supports_streaming=True)
        except IndexError:
            bot.send_message(message.chat.id, text="Нет такого фильма!")


@bot.message_handler(content_types=["video"])
def upload_video(message):
    #  todo add description, name etc.
    user_data = user_table.UserTable('database.db')
    if user_data.get_admin(message.from_user.id):
        film_data = film_table.FilmTable('film_database.db')
        film_data.add_film("Пустой", message.video.file_id)
        #  todo print id of added film
        answ = bot.send_message(message.chat.id, text="Добавьте имя фильма:")
        bot.register_next_step_handler(answ, name_of_video)
        film_data.close()
    else:
        bot.send_message(message.chat.id, text="У вас не прав на добавление материалов в данного бота.")
    user_data.close()


def name_of_video(message):
    #  todo check if input message is wrong and alert user
    #  todo other options year, genre etc.
    num, name = message.text.split(maxsplit=1)
    film_data = film_table.FilmTable('film_database.db')
    film_data.change_name_rus(num, name)
    bot.send_message(message.chat.id, text="Название успешно изменено!")
    film_data.close()
    return


if __name__ == "__main__":
    bot.polling()