import os

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.fsm.context import FSMContext

from bot import ADMIN_SECRET, bot
from state import RoleSelection, AdminState
# from storage import user_roles
from keyboards import common, admin
from storage import vehicle as vehicle_table
from storage import pricelist as pricelist_table

from utils import car

router = Router()

UPLOAD_DIR = "uploads"

@router.callback_query(RoleSelection.choosing_role, F.data == "role_admin")
async def admin_role_selected(callback: CallbackQuery, state: FSMContext):
    kb = common.get_back_to_role_selection_keyboard()
    message = await callback.message.edit_text("Введите секретную фразу для подтверждения роли администратора:", reply_markup=kb)
    await state.set_state(RoleSelection.check_admin)
    await state.update_data(secret_message_id=message.message_id)


@router.message(RoleSelection.check_admin)
async def check_admin_secret(message: Message, state: FSMContext):
    back_kb = common.get_back_to_role_selection_keyboard()
    state_data = await state.get_data()
    secret_message_id = state_data.get("secret_message_id")
    if message.text == ADMIN_SECRET:
        admin_kb = admin.admin_main_keyboard()
        if secret_message_id:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=secret_message_id)
            except Exception as e:
                print(f"Не удалось удалить сообщение: {e}")
        await message.answer("Поздравляем! Вы подтвердили роль администратора.", reply_markup=admin_kb)
        await state.clear()
    else:
        await message.answer("Неверная секретная фраза. Попробуйте снова.", reply_markup=back_kb)


@router.callback_query(F.data == "enter_car_number")
async def enter_car_number(callback: CallbackQuery, state: FSMContext):
    back_kb = admin.back_to_main_keyboard()
    await callback.message.edit_text("Пожалуйста, введите номер машины.", reply_markup=back_kb)
    await state.set_state(AdminState.car_number)


@router.message(AdminState.car_number)
async def handle_car_number_input(message: Message, state: FSMContext):
    car_number = message.text
    back_kb = admin.back_to_main_keyboard()
    formalized_car_number = car.formalize_car_number(car_number)
    if len(formalized_car_number) == 0:
        await message.answer("Неверный номер машины!", reply_markup=back_kb)
    else:
        # await message.answer(f"Формализованный номер: {formalized_car_number}")
        agent_id = 1  # Например, agent_id может быть извлечен из состояния или контекста
        vehicle = await vehicle_table.get_vehicle_by_number(formalized_car_number)
        if vehicle is None:
            await message.answer("Машины нет в базе данных!")
        else:
            await message.answer(f"{vehicle.id} - {vehicle.created_at}")


@router.callback_query(F.data == "manage_price_lists")
async def enter_car_number(callback: CallbackQuery, state: FSMContext):
    kb = admin.manage_price_lists_keyboard()
    await callback.message.edit_text("Выберите прайслист", reply_markup=kb)
    await state.set_state(AdminState.manage_price_lists)


@router.callback_query(F.data == "main_price_list")
async def enter_car_number(callback: CallbackQuery, state: FSMContext):
    kb = admin.main_price_list_keyboard()
    await callback.message.edit_text("Выберите действие", reply_markup=kb)
    # await state.set_state(AdminState.manage_price_lists)



@router.callback_query(F.data == "load_main_price_list")
async def enter_car_number(callback: CallbackQuery, state: FSMContext):
    kb = admin.back_to_main_keyboard()
    await callback.message.edit_text("Загрузите файл .xls или .xlsx", reply_markup=kb)
    await state.set_state(AdminState.load_main_price_list)


@router.message(AdminState.load_main_price_list, F.content_type.in_({'document'}))
async def load_price_list(message: Message, state: FSMContext):
    document = message.document
   
    if not document.file_name.endswith((".xlsx", ".xls")):
        await message.reply("Пожалуйста, загрузите файл формата .xlsx или .xls.")
        return
    
    # os.path.join(UPLOAD_DIR, document.file_name)
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, document.file_name)
    await bot.download(document, destination=file_path)
    await pricelist_table.import_price_list(file_path)
    await message.answer("Прайслист загружен!")


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    kb = admin.admin_main_keyboard()
    await state.clear()
    await callback.message.edit_text("Вы вернулись в главное меню.", reply_markup=kb)

