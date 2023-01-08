from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['unlimit'], is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_unlimit(msg: types.Message):
    DBS.unlimit(DBS, msg.chat.id)
    await msg.answer("majburiy adam qosiw o'shirildi")