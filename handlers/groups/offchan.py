from aiogram import types
from loader import dp
from utils.db_api import DBS

@dp.message_handler(commands=['offchan'], is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_offchan(msg: types.Message):
    DBS.offchan(DBS, msg.chat.id)
    await msg.answer("ok")