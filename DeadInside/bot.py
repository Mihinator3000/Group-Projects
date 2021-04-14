import telebot
import random
import config

bot = telebot.TeleBot(config.API_TOKEN)

ID = []


@bot.message_handler(commands=["start"])
def welcome_user(message):
    markup_inline = telebot.types.InlineKeyboardMarkup(row_width=1)
    #  todo replace link to user's channel
    subscribe = telebot.types.InlineKeyboardButton(text="Подписаться на канал",
                                                   url="youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")
    markup_inline.add(subscribe)
    cont_watching = telebot.types.InlineKeyboardButton(text="Продолжить просмотр", callback_data="followed")
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
    print(message.from_user.id)


@bot.callback_query_handler(func=lambda call: True)
def work(call):
    if call.data == "followed":
        #  todo check if subscribe
        if random.randint(1, 2) == 1:
            bot.delete_message(call.message.chat.id, call.message.id)
            markup_reply = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            search_button = telebot.types.KeyboardButton("Поиск")
            list_button = telebot.types.KeyboardButton("Список сериалов")
            markup_reply.add(search_button, list_button)
            bot.send_message(call.message.chat.id, text="Вы успешно подписались на канал, приятного просмотра!\n"
                                                        "Напишите название сериала, который вы ищете, "
                                                        "или воспользуйтесь кнопками ниже!",
                             reply_markup=markup_reply)
        else:
            bot.answer_callback_query(callback_query_id=call.id,
                                      text='Вы не подписаны на канал! Сделайте это немедленно!')


@bot.message_handler(content_types=["text"])
def reply_to_request(message):
    #  todo normal search
    if message.text == "Поиск":
        bot.send_message(message.chat.id, text="🔎 Просто отправьте боту название сериала.")
    #  todo fkn list of series by deleting message
    elif message.text == "Список сериалов":
        bot.send_message(message.chat.id, text="🔎Ниже представлен список сериалов отсортированных по названию ("
                                               "алфавиту).\n\nКакой хотите посмотреть сериал?")
    elif message.text == "чебурашка":
        video = open("D:/ITMO/cheburashka.mp4", "rb")
        bot.send_video(message.chat.id, video, timeout=1000, supports_streaming=True)

    elif message.text == "cum":
        bot.send_video(message.chat.id, ID[-1], timeout=1000, supports_streaming=True)

    else:
        bot.send_message(message.chat.id, text="Я не смог найти такой сериал. Пожалуйста, повторите попытку!")


@bot.message_handler(content_types=["video"])
def upload_video(message):
    #  todo check if person is admin or not
    ID.append(message.video.file_id)
    print(ID[-1])


if __name__ == "__main__":
    bot.polling()
