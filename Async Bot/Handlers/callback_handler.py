from aiogram import types, Dispatcher
from Functions.check_if_user_following import check_if_user_following


async def process_callback_if_user_is_following(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_reply_markup()
    await call.message.answer(await check_if_user_following(call.from_user))


def register_callback_handlers(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(
        process_callback_if_user_is_following,
        lambda call: call.data == "check_if_user_is_following"
    )
