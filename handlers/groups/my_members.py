from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin
from aiogram.utils.exceptions import Throttled
from lang.message import lang
from keyboards.inline import share_btn

@dp.message_handler(IsAdmin(), commands=['mymembers'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bo_my_members(msg: types.Message):
    await msg.delete()
    try:
        await dp.throttle(key='*', rate=3)
        _count = DBS.my_members(DBS, msg.from_id, msg.chat.id)
        bot_info = await dp.bot.get_me()
        if _count == 0: 
            text = lang.get("my_member").get("uz")[1].format(msg.from_id, msg.from_user.first_name)
            await msg.answer(text, reply_markup=share_btn(bot_info.username))
        else:
            text = lang.get("my_member").get("uz")[0].format(msg.from_id, msg.from_user.first_name, _count)
            await msg.answer(text, reply_markup=share_btn(bot_info.username))
    except Throttled: pass