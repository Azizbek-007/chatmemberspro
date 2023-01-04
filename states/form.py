from aiogram.dispatcher.filters.state import State, StatesGroup

class PromisSendMessage(StatesGroup):
    promis = State()
    group_promis = State()