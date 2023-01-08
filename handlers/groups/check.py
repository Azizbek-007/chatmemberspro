from aiogram import types
from loader import dp
from utils.db_api import DBS
from lang.message import lang
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['check'], is_reply=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_chek_member(msg: types.Message):
    reply_user = msg.reply_to_message.from_user
    reply_user_count = DBS.my_members(DBS, user_id=reply_user.id, group_id=msg.chat.id)
    if reply_user_count == 0:
        await msg.answer("Gruppaga ele adam qospagan")
    else:
        text = lang.get("reply_user_count").get("uz")
        await msg.answer(text.format(reply_user.id, reply_user.first_name, reply_user_count))
    
@dp.message_handler(IsAdmin(), commands=['check'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_check_fix(msg: types.Message):
    await msg.answer("/check komandadan paydalaniw ushin reply qilip jiberin")
