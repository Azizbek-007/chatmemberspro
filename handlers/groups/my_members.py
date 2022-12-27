from aiogram import types
from loader import dp
from utils.db_api import DBS

@dp.message_handler(commands=['mymembers'])
async def bo_my_members(msg: types.Message):
    _count = DBS.my_members(DBS, msg.from_id)[0]
    await msg.answer(f"Siz {_count} adam qosin'iz")