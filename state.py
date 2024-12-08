from aiogram.fsm.state import State, StatesGroup

class RoleSelection(StatesGroup):
    choosing_role = State()
    check_admin = State()

class AdminState(StatesGroup):
    pass

class EmployeeState(StatesGroup):
    pass