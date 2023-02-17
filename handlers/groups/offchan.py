from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['offchan'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_offchan(msg: types.Message):
    await msg.delete()
    DBS.onchan(DBS, msg.chat.id)
    await msg.answer("🛑 Канал атынан хабар жибериў дизим өширилди")