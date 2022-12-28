from aiogram import types
from loader import dp
from utils.db_api import DBS
from lang.message import lang

@dp.message_handler(commands=['check'], is_reply=True)
async def bot_chek_member(msg: types.Message):
    reply_user = msg.reply_to_message.from_user
    reply_user_count = DBS.my_members(DBS, user_id=reply_user.id)
    text = lang.get("reply_user_count").get("uz")
    await msg.answer(text.format(reply_user.id, reply_user.first_name, reply_user_count[0]))
    
@dp.message_handler(commands=['check'])
async def bot_check_fix(msg: types.Message):
    await msg.answer("/check komandadan paydalaniw ushin reply qilip jiberin")
