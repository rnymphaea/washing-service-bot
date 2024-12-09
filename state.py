from aiogram.fsm.state import State, StatesGroup

class RoleSelection(StatesGroup):
    choosing_role = State()
    check_admin = State()


class AdminState(StatesGroup):
    car_number = State()
    manage_price_lists = State()
    load_main_price_list = State()


class EmployeeState(StatesGroup):
    pass