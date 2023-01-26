import math
import time
from aiogram import types
from loader import dp
from utils.db_api import DBS


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def new_chat_member_bot(msg: types.Message):
    DBS.group_register(DBS, msg.chat.id)
    await msg.delete()
    new_members = msg.new_chat_members
    for x in new_members:
        if x.id != msg.from_id:
            DBS.join_in_group(DBS, msg.from_id, x.id, msg.chat.id)
            
    count_data = DBS.get_member_count(DBS, msg.chat.id)
    if count_data != False:
        if DBS.my_members(DBS, user_id=msg.from_id, group_id=msg.chat.id) >= int(count_data):  
            permissions =  DBS.get_group_premissions(DBS, msg.chat.id)
            await dp.bot.restrict_chat_member(
                        chat_id=msg.chat.id,
                        user_id=msg.from_id,
                        permissions=permissions
                    )
        