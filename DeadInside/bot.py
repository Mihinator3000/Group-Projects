import telebot
import config
import user_table
import film_table

bot = telebot.AsyncTeleBot(config.API_TOKEN)
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()


#  todo finish admin panel


@bot.message_handler(commands=["start"])
def welcome_user(message):
    if message.chat.type == 'private':
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
            markup_reply.add(search_button, list_button)

            user_data = user_table.UserTable('database.db')
            if user_data.get_admin(call.message.chat.id):
                adm_panel = telebot.types.KeyboardButton("Включить панель администратора")
                markup_reply.add(adm_panel)
            bot.send_message(call.message.chat.id, text="Вы успешно подписались на канал, приятного "
                                                        "просмотра!\n "
                                                        "Напишите название сериала, который вы ищете, "
                                                        "или воспользуйтесь кнопками ниже!",
                             reply_markup=markup_reply)
        else:
            bot.answer_callback_query(callback_query_id=call.id,
                                      text='Вы не подписаны на канал! Сделайте это немедленно!')


@bot.message_handler(content_types=["text"])
def reply_to_request(message):
    if message.chat.type == 'private':
        user_data = user_table.UserTable('database.db')
        if message.text == "Поиск":
            bot.send_message(message.chat.id, text="🔎 Просто отправьте боту название сериала.")
        #  todo fkn list of series by deleting message
        elif message.text == "Список сериалов":
            bot.send_message(message.chat.id,
                             text="🔎Ниже представлен список сериалов отсортированных по названию ("
                                  "алфавиту).\n\nКакой хотите посмотреть сериал?")

        elif user_data.get_admin(message.from_user.id):
            if message.text == "Включить панель администратора":
                keyboard = telebot.types.ReplyKeyboardRemove()
                delete_keyboard = bot.send_message(message.chat.id, text="Панель администратора включена:",
                                                   reply_markup=keyboard)
                bot.delete_message(message.chat.id, delete_keyboard.wait().message_id)

                admin_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                add_film_button = telebot.types.KeyboardButton("Добавить фильм")
                num_of_film_button = telebot.types.KeyboardButton("Количество фильмов")
                num_of_users_button = telebot.types.KeyboardButton("Количество пользователей")
                list_films_button = telebot.types.KeyboardButton("Список фильмов")
                change_genre_by_id_button = telebot.types.KeyboardButton("Изменить жанр по ID")
                change_name_by_id_button = telebot.types.KeyboardButton("Изменить название по ID")
                delete_by_id_button = telebot.types.KeyboardButton("Удалить по ID")
                find_id_by_name_button = telebot.types.KeyboardButton("Найти ID по названию")
                change_year_by_id_button = telebot.types.KeyboardButton("Изменить год по ID")
                exit_button = telebot.types.KeyboardButton("Выход")

                admin_markup.add(add_film_button, num_of_film_button, num_of_users_button, list_films_button
                                 , change_genre_by_id_button, change_name_by_id_button,
                                 delete_by_id_button, find_id_by_name_button, change_year_by_id_button, exit_button)

                bot.send_message(chat_id=delete_keyboard.wait().chat.id, text="Панель администратора включена",
                                 reply_markup=admin_markup)

            elif message.text == "Выход":
                markup_reply = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                search_button = telebot.types.KeyboardButton("Поиск")
                list_button = telebot.types.KeyboardButton("Список сериалов")
                markup_reply.add(search_button, list_button)
                adm_panel = telebot.types.KeyboardButton("Включить панель администратора")
                markup_reply.add(adm_panel)
                bot.send_message(message.chat.id, text="Панель администратора выключена", reply_markup=markup_reply)

            elif message.text == "Добавить фильм":
                config.INPUT_FLAG = True
                bot.send_message(message.chat.id, text="Напишите название фильма:")

            elif message.text == "Количество фильмов":
                film_data = film_table.FilmTable('film_database.db')
                bot.send_message(message.chat.id, text=film_data.film_count())
                film_data.close()

            elif message.text == "Количество пользователей":
                bot.send_message(message.chat.id, text=user_data.user_count())

            elif message.text == "Список фильмов":
                #  todo film list ctrl+c ctrl+v
                pass

            elif message.text == "Изменить жанр по ID":
                film_data = film_table.FilmTable('film_database.db')
                answer = bot.send_message(message.chat.id, text="Впишите ID фильма, для которого хотите изменить "
                                                                "жанр в формате: ID фильма новые жанры")

                bot.register_next_step_handler(answer.wait(), change_genre_by_id)
                film_data.close()

            elif message.text == "Изменить название по ID":
                film_data = film_table.FilmTable('film_database.db')
                answer = bot.send_message(message.chat.id, text="Впишите ID фильма, для которого хотите изменить "
                                                                "название в формате: ID фильма новое название")
                bot.register_next_step_handler(answer.wait(), change_name_by_id)
                film_data.close()

            elif message.text == "Удалить по ID":
                film_data = film_table.FilmTable('film_database.db')
                answer = bot.send_message(message.chat.id, text="Впишите ID фильма, который хотите удалить")
                bot.register_next_step_handler(answer.wait(), delete_film)
                film_data.close()

            elif message.text == "Найти ID по названию":
                film_data = film_table.FilmTable('film_database.db')
                answer = bot.send_message(message.chat.id, text="Впишите название фильма, ID которого вы хотите узнать")
                bot.register_next_step_handler(answer.wait(), get_id)
                film_data.close()

            elif message.text == "Изменить год по ID":
                film_data = film_table.FilmTable('film_database.db')
                answer = bot.send_message(message.chat.id, text="Впишите ID фильма, для которого хотите изменить "
                                                                "год в формате: ID фильма новый год")
                bot.register_next_step_handler(answer.wait(), change_year_by_id)
                film_data.close()

            elif config.INPUT_FLAG:
                config.INPUT_NAME = message.text
                bot.send_message(message.chat.id, text="Залейте фильмец:")

            else:
                film_data = film_table.FilmTable('film_database.db')
                try:
                    film_id = film_data.find_film(message.text)[3]
                    bot.send_video(message.chat.id, film_id, timeout=1000, supports_streaming=True)
                except IndexError:
                    bot.send_message(message.chat.id, text="Нет такого фильма!")

        else:
            film_data = film_table.FilmTable('film_database.db')
            try:
                film_id = film_data.find_film(message.text)[3]
                bot.send_video(message.chat.id, film_id, timeout=1000, supports_streaming=True)
            except IndexError:
                bot.send_message(message.chat.id, text="Нет такого фильма!")
    user_data.close()


@bot.message_handler(content_types=["video"])
def add_video(message):
    if config.INPUT_FLAG:
        user_data = user_table.UserTable('database.db')
        if user_data.get_admin(message.from_user.id):
            film_data = film_table.FilmTable('film_database.db')
            film_data.add_film(config.INPUT_NAME, message.video.file_id)
            film_data.close()
            bot.send_message(message.chat.id, text="Фильм <{0}> успешно добавлен".format(config.INPUT_NAME))
            config.INPUT_FLAG = False
            config.INPUT_NAME = ""
        else:
            bot.send_message(message.chat.id, text="У вас не прав на добавление материалов в данного бота.")
        user_data.close()
    else:
        bot.send_message(message.chat.id, text="Неверный формат запроса")


#  todo add option if didn`t find anything
def change_genre_by_id(message):
    num, genre = message.text.split(maxsplit=1)
    film_data = film_table.FilmTable('film_database.db')
    film_data.change_genre(num, genre)
    bot.send_message(message.chat.id, text="Жанр успешно изменён!")
    film_data.close()
    return


def change_name_by_id(message):
    num, name = message.text.split(maxsplit=1)
    film_data = film_table.FilmTable('film_database.db')
    film_data.change_name_rus(num, name)
    bot.send_message(message.chat.id, text="Имя успешно изменено!")
    film_data.close()
    return


def change_year_by_id(message):
    num, year = message.text.split(maxsplit=1)
    film_data = film_table.FilmTable('film_database.db')
    film_data.change_year(num, year)
    bot.send_message(message.chat.id, text="Год успешно изменен!")
    film_data.close()
    return


def delete_film(message):
    num = int(message.text)
    film_data = film_table.FilmTable('film_database.db')
    film_data.delete_by_id(num)
    bot.send_message(message.chat.id, text="Фильм успешно удалён")
    film_data.close()
    return


def get_id(message):
    name = message.text
    film_data = film_table.FilmTable('film_database.db')
    result = film_data.get_film_id(name)
    if result is None:
        bot.send_message(message.chat.id, text="Мне не удалось найти такой фильм :(")
    else:
        bot.send_message(message.chat.id, text="ID фильма {0[1]} : {0[0]}".format(result, result))
    film_data.close()
    return


if __name__ == "__main__":
    bot.polling()
