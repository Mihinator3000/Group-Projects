from aiogram import types


def user_name_format(message: types.Message) -> str:
    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name

    if user_name is None:
        return user_surname
    elif user_surname is None:
        return user_name
    return f"{user_name} {user_surname}!"
