from aiogram import types
from loader import dp
from utils.db_api import DBS
from lang.message import lang
from filters import IsAdmin
from lang.message import lang
from keyboards.inline import share_btn

@dp.message_handler(IsAdmin(), commands=['check'], is_reply=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_chek_member(msg: types.Message):
    await msg.delete()
    try:
        await dp.throttle(key='*', rate=2)
        reply_user = msg.reply_to_message.from_user
        reply_user_count = DBS.my_members(DBS, user_id=reply_user.id, group_id=msg.chat.id)
        bot_info = await dp.bot.get_me()
        if reply_user_count == 0:
            text = lang.get("check").get("uz")[1].format(reply_user.id, reply_user.first_name)
            await msg.answer(text, reply_markup=share_btn(bot_info.username))
        else:
            text = lang.get("check").get("uz")[0].format(reply_user.id, reply_user.first_name, reply_user_count)
            await msg.answer()
    except: pass
    
@dp.message_handler(IsAdmin(), commands=['check'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_check_fix(msg: types.Message):
    await msg.delete()
    try:
        await dp.throttle(key='*', rate=2)
        text = lang.get("check").get("uz")[2]
        await msg.answer(text)
    except: pass
