from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands="clear",  is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear(msg: types.Message):
    await msg.answer("Qa'te buyriq berdin'iz!")

@dp.message_handler(IsAdmin(), commands="clear", is_reply=True, is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear(msg: types.Message):
    reply_user_id = msg.reply_to_message.from_id
    DBS.clear_all_user(DBS, user_id=reply_user_id)
    await msg.answer("maglumatlari tazalandi/c")

@dp.message_handler(IsAdmin(), commands="clearall", is_chat_admin=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear_all(msg: types.Message):
    DBS.clear_all_group(DBS, msg.chat.id)
    await msg.answer("Gruppa maglumatlari tazalandi")