from aiogram import types
from loader import dp

@dp.message_handler(commands="set")
async def bot_set(msg: types.Message):
    await 