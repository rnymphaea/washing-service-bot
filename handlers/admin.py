from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot import ADMIN_SECRET, bot
from state import RoleSelection
from storage import user_roles
from keyboards import common

router = Router()

@router.callback_query(RoleSelection.choosing_role, F.data == "role_admin")
async def admin_role_selected(callback: CallbackQuery, state: FSMContext):
    kb = common.get_back_to_role_selection_keyboard()
    message = await callback.message.edit_text("Введите секретную фразу для подтверждения роли администратора:", reply_markup=kb)
    await state.set_state(RoleSelection.check_admin)
    await state.update_data(secret_message_id=message.message_id)


@router.message(RoleSelection.check_admin)
async def check_admin_secret(message: Message, state: FSMContext):
    kb = common.get_back_to_role_selection_keyboard()
    state_data = await state.get_data()
    secret_message_id = state_data.get("secret_message_id")
    if message.text == ADMIN_SECRET:
        user_roles[message.from_user.id] = "admin"  # Назначаем роль "админ"
        if secret_message_id:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=secret_message_id)
            except Exception as e:
                print(f"Не удалось удалить сообщение: {e}")
        await message.answer("Поздравляем! Вы подтвердили роль администратора.")
        await state.clear()  # Сбрасываем состояние
    else:
        await message.answer("Неверная секретная фраза. Попробуйте снова.", reply_markup=kb)

