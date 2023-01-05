from aiogram import types
from loader import dp

@dp.message_handler(commands="toplist", chat_type=[types.ChatType.GROUP, types.ChatType.SUPER_GROUP])
async def bot_top_list(msg: types.Message):
    await msg.answer("Hello")