from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['onads'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_onchan(msg: types.Message):
    await msg.delete()
    DBS.onads(DBS, msg.chat.id)
    await msg.answer("✅ Рекламаға қарсы дизим тохтатылды!")