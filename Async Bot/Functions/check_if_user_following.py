from aiogram import types
from create_bot import bot
from config import CHAT_ID, STATUS_FOLLOWED


async def check_if_user_following(user: types.User):
    return (await bot.get_chat_member(
        chat_id=CHAT_ID,
        user_id=user.id)).status in STATUS_FOLLOWED
