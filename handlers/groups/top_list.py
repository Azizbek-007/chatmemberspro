from aiogram import types
from loader import dp

@dp.message_handler(commands="toplist")
async def bot_top_list(msg: types.Message):
    await msg.answer("Hello")