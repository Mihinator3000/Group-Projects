from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import JOIN_URL

button_subscribe = InlineKeyboardButton(
    text="Подписаться на канал.", url=JOIN_URL)

button_continue_watching = InlineKeyboardButton(
    text="Продолжить просмотр.", callback_data="check_if_user_is_following")

subscribe_keyboard = InlineKeyboardMarkup(row_width=1).add(
    button_subscribe, button_continue_watching)
