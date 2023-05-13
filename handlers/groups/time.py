from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin
from aiogram.utils.exceptions import Throttled
from datetime import datetime
import pytz

@dp.message_handler(IsAdmin(), commands=['time'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_timee(msg: types.Message):
    await msg.delete()
    try:
        await dp.throttle(key='*', rate=5)
        time_ = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%Y-%m-%d %H:%M:%S")
        await msg.answer(time_)
    except Throttled: pass