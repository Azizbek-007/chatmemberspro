from aiogram import types
from loader import dp, bot_id
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['limit'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_limit(msg: types.Message):
    _count = DBS.get_member_count(DBS, msg.chat.id)
    if _count !=False:
        await msg.answer(f"{_count} limit")
    else: await msg.answer("0")