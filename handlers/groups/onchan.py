from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['onchan'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_onchan(msg: types.Message):
    await msg.delete()
    DBS.offchan(DBS, msg.chat.id)
    await dp.bot.send_message(msg.chat.id, "✅ Канал атынан хабар жиберилиўдин алдын алыў дизими иске түсти!")