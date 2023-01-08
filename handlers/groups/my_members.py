from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin
from aiogram.utils.exceptions import Throttled

@dp.message_handler(IsAdmin(), commands=['mymembers'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bo_my_members(msg: types.Message):
    try:
        await dp.throttle(key='*', rate=5)
        _count = DBS.my_members(DBS, msg.from_id, msg.chat.id)
        if _count == 0: 
            await msg.answer("siz adam qospagansiz")
        else:
            await msg.answer(f"Siz {_count} adam qosin'iz")
    except Throttled: pass