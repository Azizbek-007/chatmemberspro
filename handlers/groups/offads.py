from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['offads'], is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_offads(msg: types.Message):
    DBS.offads(DBS, msg.chat.id)
    await msg.answer("ok")