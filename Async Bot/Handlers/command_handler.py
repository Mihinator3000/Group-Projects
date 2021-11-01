from aiogram import types, Dispatcher
from Keyboards.subscribe_keyboard import subscribe_keyboard
from Functions.user_name_format import user_name_format


async def command_start(message: types.Message):
    await message.answer(
        text=f"Добро пожаловать, {user_name_format(message)}",
        reply_markup=subscribe_keyboard)


def register_handlers_commands(dispatcher: Dispatcher):
    dispatcher.register_message_handler(callback=command_start, commands=["start"])
