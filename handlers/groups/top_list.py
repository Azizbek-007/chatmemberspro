from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin
from lang.message import lang
from keyboards.inline import share_btn

@dp.message_handler(IsAdmin(), commands="top", is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_top_list(msg: types.Message):
    await msg.delete()
    users = DBS.top_users(DBS, msg.chat.id)
    bot_info = await dp.bot.get_me()
    if len(users) == 0: 
        text = lang.get("toplist").get("uz")[0]
        return await msg.answer(text, reply_markup=share_btn(bot_info.username))
         
    text = "TOP 50\n\n"
    for x, i in zip(users, range(1, len(users)+1)):
        get_user = await dp.bot.get_chat(x[0])
        text  +=f"{i}. <a href='tg://user?id={x[0]}'>{get_user.full_name}</a> - {x[2]}\n"
    await msg.answer(text=text, reply_markup=share_btn(bot_info.username))

@dp.message_handler(IsAdmin(), commands="top", chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_top_list_mem(msg: types.Message):
    await msg.delete()