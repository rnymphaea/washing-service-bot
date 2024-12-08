from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def start_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Работник", callback_data="role_employee")],
        [InlineKeyboardButton(text="Администратор", callback_data="role_admin")],
    ])
    return keyboard

def get_back_to_role_selection_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться к выбору роли", callback_data="back_to_role_selection")]
    ])