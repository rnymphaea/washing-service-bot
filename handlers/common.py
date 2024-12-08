from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards import common
from state import RoleSelection

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    kb = common.start_keyboard()
    await message.answer("Здравствуйте! Выберите роль:", reply_markup=kb)
    await state.set_state(RoleSelection.choosing_role)

@router.callback_query(F.data == "back_to_role_selection")
async def back_to_role_selection(callback: CallbackQuery, state: FSMContext):
    kb = common.start_keyboard();
    await callback.message.edit_text("Выберите свою роль:", reply_markup=kb)
    await state.set_state(RoleSelection.choosing_role)