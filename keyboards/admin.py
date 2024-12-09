from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def admin_main_keyboard():
    button1 = InlineKeyboardButton(text="Ввести номер машины", callback_data="enter_car_number")
    button2 = InlineKeyboardButton(text="Управление прайслистами", callback_data="manage_price_lists")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2]])
    return keyboard


def manage_price_lists_keyboard():
    back_button = InlineKeyboardButton(text="Назад", callback_data="back_to_menu")
    button1 = InlineKeyboardButton(text="Основной прайслист", callback_data="main_price_list")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1], [back_button]])
    return keyboard


def main_price_list_keyboard():
    load_button = InlineKeyboardButton(text="Загрузить", callback_data="load_main_price_list")
    show_button = InlineKeyboardButton(text="Показать", callback_data="show_main_price_list")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[load_button], [show_button]])
    return keyboard
    



def back_to_main_keyboard():
    back_button = InlineKeyboardButton(text="Назад", callback_data="back_to_menu")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[back_button]])
    return keyboard
