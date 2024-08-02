from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def std_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Получить цитату сейчас')],
        [KeyboardButton(text='Изменить интересы')]
    ], resize_keyboard=True, one_time_keyboard=False)