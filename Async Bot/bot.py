from aiogram import executor
from Handlers.command_handler import register_handlers_commands
from Handlers.callback_handler import register_callback_handlers
from create_bot import dispatcher

register_handlers_commands(dispatcher)
register_callback_handlers(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
