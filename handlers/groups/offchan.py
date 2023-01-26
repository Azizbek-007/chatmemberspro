from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['offchan'], is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_offchan(msg: types.Message):
    DBS.onchan(DBS, msg.chat.id)
    await msg.answer("oshirildi")