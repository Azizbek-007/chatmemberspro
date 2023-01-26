from aiogram import types
from loader import dp, bot_id
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['add'], is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_addlimit(msg: types.Message):
    add_count = msg.text.split(' ')
    if len(add_count) == 2:
        try: 
            add_count_number = int(add_count[1])
            group_data= await dp.bot.get_chat(msg.chat.id)
            DBS.set_group_premissions(DBS, group_id=msg.chat.id, premissions=group_data.permissions)
            DBS.add_member_count(DBS, msg.chat.id, add_count_number)
            await msg.answer("Qosildi")
        except TypeError:
            await msg.answer("/addlimit 10") 
    else: await msg.reply("/addlimit 10")