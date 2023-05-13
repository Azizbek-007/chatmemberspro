from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['addoff'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_unlimit(msg: types.Message):
    await msg.delete()
    DBS.unlimit(DBS, msg.chat.id)
    await msg.answer("Мәжбурий адам қосыў өширилди!")